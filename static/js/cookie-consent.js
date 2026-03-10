/**
 * ============================================================
 * COOKIE CONSENT MANAGER
 * Portale Digitalizzazione Patrimonio Culturale - Regione Siciliana
 * 
 * Conforme a:
 *  - GDPR (Reg. UE 2016/679)
 *  - D.Lgs. 196/2003 (Codice Privacy)
 *  - Provvedimento Garante Privacy 10 giugno 2021 (Linee guida cookie)
 * 
 * File: static/js/cookie-consent.js
 * ============================================================
 *
 * CATEGORIE GESTITE:
 *  - tecnici    → necessari, sempre attivi, nessun consenso richiesto
 *  - funzionali → preferenze utente (lingua, ecc.), opzionali
 *
 * COME AGGIUNGERE UNA NUOVA CATEGORIA IN FUTURO (es. analytics):
 *  1. Aggiungere la definizione in COOKIE_CATEGORIES
 *  2. Aggiungere i cookie specifici nell'array cookies[]
 *  3. Creare la funzione enableAnalytics() e aggiungerla in applyConsent()
 *  4. Aggiornare la cookie-policy.html
 * ============================================================
 */

;(function() {
    'use strict';

    /* ============================================================
       CONFIGURAZIONE
       ============================================================ */

    const CONFIG = {
        // Nome del cookie che salva il consenso
        CONSENT_COOKIE_NAME: 'cookie_consent_v1',

        // Durata del consenso in giorni (12 mesi come da Garante)
        CONSENT_DURATION_DAYS: 365,

        // Versione della policy: incrementare se cambiano le categorie
        // o i cookie usati → l'utente dovrà esprimere nuovamente il consenso
        POLICY_VERSION: '1.0',

        // Path del sito
        COOKIE_PATH: '/',

        // Produzione = HTTPS → SameSite=Lax; Secure
        SECURE: true,
    };


    /* ============================================================
       DEFINIZIONE CATEGORIE E COOKIE
       ============================================================ */

    const COOKIE_CATEGORIES = {

        tecnici: {
            id: 'tecnici',
            label: 'Cookie Tecnici e Necessari',
            description: 'Indispensabili per il corretto funzionamento del sito. ' +
                         'Senza questi cookie il portale non funzionerebbe correttamente. ' +
                         'Non richiedono il tuo consenso.',
            icon: 'fas fa-cog',
            iconClass: 'green',
            required: true,   // ← sempre attivo, toggle disabilitato
            defaultEnabled: true,
            cookies: [
                {
                    name: 'session',
                    purpose: 'Gestione della sessione utente (Flask)',
                    duration: 'Sessione',
                    provider: 'Proprio',
                },
                {
                    name: CONFIG.CONSENT_COOKIE_NAME,
                    purpose: 'Memorizza le preferenze espresse sui cookie',
                    duration: '12 mesi',
                    provider: 'Proprio',
                },
                {
                    name: 'csrf_token',
                    purpose: 'Protezione da attacchi Cross-Site Request Forgery',
                    duration: 'Sessione',
                    provider: 'Proprio',
                },
            ],
        },

        funzionali: {
            id: 'funzionali',
            label: 'Cookie Funzionali',
            description: 'Permettono di ricordare le tue preferenze di navigazione, ' +
                         'come la lingua selezionata (italiano/inglese). ' +
                         'Non profilano l\'utente e non tracciano la navigazione.',
            icon: 'fas fa-sliders-h',
            iconClass: 'blue',
            required: false,
            defaultEnabled: false,
            cookies: [
                {
                    name: 'lang',
                    purpose: 'Ricorda la lingua preferita dell\'utente (it/en)',
                    duration: '6 mesi',
                    provider: 'Proprio',
                },
            ],
        },

        /*
         * TEMPLATE PER CATEGORIE FUTURE
         * (decommentare e compilare quando necessario)
         *
        analitici: {
            id: 'analitici',
            label: 'Cookie Analitici',
            description: '...',
            icon: 'fas fa-chart-line',
            iconClass: 'orange',
            required: false,
            defaultEnabled: false,
            cookies: [
                { name: '_ga', purpose: '...', duration: '24 mesi', provider: 'google.com' },
            ],
        },
        */
    };


    /* ============================================================
       STATO INTERNO
       ============================================================ */

    let currentConsent = null;  // null = non ancora espresso
    let panelOpen = false;


    /* ============================================================
       UTILITY: COOKIE CRUD
       ============================================================ */

    function setCookie(name, value, days) {
        const expires = new Date();
        expires.setDate(expires.getDate() + days);

        let cookieStr = `${encodeURIComponent(name)}=${encodeURIComponent(value)}` +
                        `; expires=${expires.toUTCString()}` +
                        `; path=${CONFIG.COOKIE_PATH}` +
                        `; SameSite=Lax`;

        if (CONFIG.SECURE) {
            cookieStr += '; Secure';
        }

        document.cookie = cookieStr;
    }

    function getCookie(name) {
        const key = encodeURIComponent(name) + '=';
        const cookies = document.cookie.split(';');
        for (let c of cookies) {
            c = c.trim();
            if (c.startsWith(key)) {
                return decodeURIComponent(c.substring(key.length));
            }
        }
        return null;
    }

    function deleteCookie(name) {
        document.cookie = `${encodeURIComponent(name)}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=${CONFIG.COOKIE_PATH}; SameSite=Lax`;
    }


    /* ============================================================
       UTILITY: SALVATAGGIO / LETTURA CONSENSO
       ============================================================ */

    function saveConsent(preferences) {
        const payload = {
            version:    CONFIG.POLICY_VERSION,
            timestamp:  new Date().toISOString(),
            sid:        getOrCreateAnonymousId(),
            categories: preferences,
        };

        setCookie(
            CONFIG.CONSENT_COOKIE_NAME,
            JSON.stringify(payload),
            CONFIG.CONSENT_DURATION_DAYS
        );

        currentConsent = payload;

        // Invia il log al server (nessun dato personale)
        fetch('/api/cookie-consent', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        }).catch(function(err) {
            // Errore silenzioso: il consenso è già salvato nel browser
            // Il logging server-side è accessorio, non bloccante
            console.warn('[CookieConsent] Log server non raggiunto:', err);
        });

        return payload;
    }

    function loadConsent() {
        const raw = getCookie(CONFIG.CONSENT_COOKIE_NAME);
        if (!raw) return null;

        try {
            const parsed = JSON.parse(raw);

            // Se la versione della policy è cambiata → consenso da rinnovare
            if (parsed.version !== CONFIG.POLICY_VERSION) {
                console.info('[CookieConsent] Versione policy aggiornata — richiedo nuovo consenso');
                deleteCookie(CONFIG.CONSENT_COOKIE_NAME);
                return null;
            }

            return parsed;
        } catch (e) {
            console.warn('[CookieConsent] Cookie consenso corrotto — reset');
            deleteCookie(CONFIG.CONSENT_COOKIE_NAME);
            return null;
        }
    }

    function getOrCreateAnonymousId() {
        // Usa sessionStorage per l'ID anonimo di sessione (non persiste tra sessioni)
        // Non è un dato personale identificativo
        let sid = sessionStorage.getItem('_csid');
        if (!sid) {
            sid = 'cs_' + Math.random().toString(36).substring(2, 11);
            sessionStorage.setItem('_csid', sid);
        }
        return sid;
    }


    /* ============================================================
       LOGICA DI APPLICAZIONE DEL CONSENSO
       ============================================================ */

    function applyConsent(categories) {
        // Cookie tecnici → sempre attivi, nessuna azione necessaria

        // Cookie funzionali
        if (categories.funzionali) {
            enableFunctional();
        } else {
            disableFunctional();
        }

        /*
         * TEMPLATE PER CATEGORIE FUTURE:
         *
         * if (categories.analitici) {
         *     enableAnalytics();
         * } else {
         *     disableAnalytics();
         * }
         */
    }

    function enableFunctional() {
        // Il cookie 'lang' viene già gestito da Flask-Babel.
        // Qui puoi aggiungere logica JS per preferenze salvabili lato client.
        console.info('[CookieConsent] Cookie funzionali: ABILITATI');
    }

    function disableFunctional() {
        // Rimuovi eventuali cookie funzionali già impostati
        deleteCookie('lang');
        console.info('[CookieConsent] Cookie funzionali: DISABILITATI');
    }

    /* TEMPLATE per analytics future:
    function enableAnalytics() {
        if (window._analyticsLoaded) return;
        window._analyticsLoaded = true;
        // Carica GA4, Matomo, ecc. SOLO dopo il consenso
        const s = document.createElement('script');
        s.src = 'https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX';
        s.async = true;
        document.head.appendChild(s);
    }
    function disableAnalytics() {
        deleteCookie('_ga');
        deleteCookie('_gid');
        deleteCookie('_gat');
    }
    */


    /* ============================================================
       COSTRUZIONE DELL'HTML (generato dinamicamente)
       ============================================================ */

    function buildHTML() {
        // --- OVERLAY ---
        const overlay = document.createElement('div');
        overlay.className = 'cookie-overlay';
        overlay.id = 'cookie-overlay';
        overlay.setAttribute('aria-hidden', 'true');

        // --- BANNER ---
        const banner = document.createElement('div');
        banner.id = 'cookie-banner';
        banner.setAttribute('role', 'dialog');
        banner.setAttribute('aria-modal', 'true');
        banner.setAttribute('aria-labelledby', 'cookie-banner-title');
        banner.setAttribute('aria-describedby', 'cookie-banner-desc');

        banner.innerHTML = `
            <div class="cookie-banner-inner">
                <div class="cookie-banner-icon" aria-hidden="true">
                    <i class="fas fa-cookie-bite"></i>
                </div>
                <div class="cookie-banner-text">
                    <h2 id="cookie-banner-title">Questo sito utilizza cookie</h2>
                    <p id="cookie-banner-desc">
                        Utilizziamo cookie tecnici necessari al funzionamento del sito e, 
                        con il tuo consenso, cookie funzionali per ricordare le tue preferenze.
                        Puoi accettare, rifiutare o personalizzare le tue scelte.
                        Leggi la nostra <a href="/cookie-policy">Cookie Policy</a>.
                    </p>
                </div>
                <div class="cookie-banner-actions">
                    <button class="cookie-btn cookie-btn-reject" id="cookie-btn-reject-all-banner" type="button">
                        <i class="fas fa-times" aria-hidden="true"></i>
                        Rifiuta tutto
                    </button>
                    <button class="cookie-btn cookie-btn-settings" id="cookie-btn-settings" type="button">
                        <i class="fas fa-sliders-h" aria-hidden="true"></i>
                        Personalizza
                    </button>
                    <button class="cookie-btn cookie-btn-accept" id="cookie-btn-accept-all-banner" type="button">
                        <i class="fas fa-check" aria-hidden="true"></i>
                        Accetta tutto
                    </button>
                </div>
            </div>
        `;

        // --- PANNELLO ---
        const panel = document.createElement('div');
        panel.id = 'cookie-panel';
        panel.setAttribute('role', 'dialog');
        panel.setAttribute('aria-modal', 'true');
        panel.setAttribute('aria-labelledby', 'cookie-panel-title');
        panel.setAttribute('tabindex', '-1');

        // Costruiamo le righe per ogni categoria
        let categoriesHTML = '';
        for (const [key, cat] of Object.entries(COOKIE_CATEGORIES)) {
            const isChecked  = cat.required ? 'checked' : (currentConsent?.categories?.[key] ? 'checked' : '');
            const isDisabled = cat.required ? 'disabled' : '';
            const badgeClass = cat.required ? 'cookie-badge-required' : 'cookie-badge-optional';
            const badgeText  = cat.required ? 'Sempre attivo' : 'Opzionale';

            // Tabella cookie per questa categoria
            let cookieRows = '';
            for (const ck of cat.cookies) {
                cookieRows += `
                    <tr>
                        <td><code>${ck.name}</code></td>
                        <td>${ck.purpose}</td>
                        <td>${ck.duration}</td>
                        <td>${ck.provider}</td>
                    </tr>
                `;
            }

            categoriesHTML += `
                <div class="cookie-category" data-category="${key}">
                    <div class="cookie-category-header">
                        <div class="cookie-category-icon ${cat.iconClass}" aria-hidden="true">
                            <i class="${cat.icon}"></i>
                        </div>
                        <div class="cookie-category-info">
                            <div class="cookie-category-name">
                                ${cat.label}
                                <span class="cookie-badge ${badgeClass}">${badgeText}</span>
                            </div>
                            <div class="cookie-category-desc">${cat.description}</div>
                        </div>
                        <div class="cookie-category-toggle">
                            <label class="cookie-toggle" aria-label="Abilita ${cat.label}">
                                <input 
                                    type="checkbox" 
                                    data-cat="${key}" 
                                    ${isChecked} 
                                    ${isDisabled}
                                    ${cat.required ? 'aria-disabled="true"' : ''}
                                >
                                <span class="cookie-toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    <div class="cookie-category-detail" id="detail-${key}">
                        <button class="cookie-detail-expand" type="button" data-detail="${key}" aria-expanded="false">
                            <i class="fas fa-chevron-down" aria-hidden="true"></i>
                            Visualizza cookie utilizzati (${cat.cookies.length})
                        </button>
                        <table class="cookie-table" aria-label="Cookie categoria ${cat.label}">
                            <thead>
                                <tr>
                                    <th>Nome</th>
                                    <th>Finalità</th>
                                    <th>Durata</th>
                                    <th>Fornitore</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${cookieRows}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }

        panel.innerHTML = `
            <div class="cookie-panel-header">
                <h3 id="cookie-panel-title">
                    <i class="fas fa-shield-alt" aria-hidden="true"></i>
                    Gestione preferenze cookie
                </h3>
                <button class="cookie-panel-close" id="cookie-panel-close" type="button" aria-label="Chiudi pannello">
                    <i class="fas fa-times" aria-hidden="true"></i>
                </button>
            </div>
            <div class="cookie-panel-body">
                <p class="cookie-panel-intro">
                    <i class="fas fa-info-circle" aria-hidden="true" style="margin-right:0.3rem; color:var(--secondary-color);"></i>
                    Puoi abilitare o disabilitare le singole categorie. I cookie tecnici non possono essere disattivati 
                    perché necessari al funzionamento del sito. Puoi modificare le tue preferenze in qualsiasi momento.
                </p>
                ${categoriesHTML}
            </div>
            <div class="cookie-panel-footer">
                <button class="cookie-btn cookie-btn-reject-all" id="cookie-btn-reject-all-panel" type="button">
                    Rifiuta tutto
                </button>
                <button class="cookie-btn cookie-btn-accept-all" id="cookie-btn-accept-all-panel" type="button">
                    Accetta tutto
                </button>
                <button class="cookie-btn cookie-btn-save" id="cookie-btn-save" type="button">
                    <i class="fas fa-save" aria-hidden="true"></i>
                    Salva preferenze
                </button>
            </div>
        `;

        // --- FLOATING BUTTON ---
        const floatBtn = document.createElement('button');
        floatBtn.id = 'cookie-float-btn';
        floatBtn.type = 'button';
        floatBtn.setAttribute('aria-label', 'Gestisci preferenze cookie');
        floatBtn.innerHTML = '<i class="fas fa-cookie-bite" aria-hidden="true"></i> Cookie';

        // --- TOAST ---
        const toast = document.createElement('div');
        toast.className = 'cookie-toast';
        toast.id = 'cookie-toast';
        toast.setAttribute('role', 'status');
        toast.setAttribute('aria-live', 'polite');
        toast.innerHTML = '<i class="fas fa-check-circle" aria-hidden="true"></i> <span id="cookie-toast-msg"></span>';

        // Appendiamo tutto al body
        document.body.appendChild(overlay);
        document.body.appendChild(banner);
        document.body.appendChild(panel);
        document.body.appendChild(floatBtn);
        document.body.appendChild(toast);
    }


    /* ============================================================
       SHOW / HIDE BANNER E PANNELLO
       ============================================================ */

    function showBanner() {
        const banner = document.getElementById('cookie-banner');
        if (banner) {
            banner.classList.add('active');
            // Focus sul primo pulsante per accessibilità
            setTimeout(() => {
                const firstBtn = banner.querySelector('.cookie-btn');
                if (firstBtn) firstBtn.focus();
            }, 350);
        }
    }

    function hideBanner() {
        const banner = document.getElementById('cookie-banner');
        if (banner) banner.classList.remove('active');
    }

    function showPanel() {
        const overlay = document.getElementById('cookie-overlay');
        const panel   = document.getElementById('cookie-panel');
        if (!overlay || !panel) return;

        // Aggiorna i toggle in base all'eventuale consenso già salvato
        syncTogglesWithConsent();

        overlay.classList.add('active');
        panel.classList.add('active');
        panel.focus();
        panelOpen = true;

        // Blocca scroll del body
        document.body.style.overflow = 'hidden';
    }

    function hidePanel() {
        const overlay = document.getElementById('cookie-overlay');
        const panel   = document.getElementById('cookie-panel');
        if (!overlay || !panel) return;

        overlay.classList.remove('active');
        panel.classList.remove('active');
        panelOpen = false;

        document.body.style.overflow = '';
    }

    function showFloatButton() {
        const btn = document.getElementById('cookie-float-btn');
        if (btn) btn.classList.add('visible');
    }

    function showToast(message) {
        const toast = document.getElementById('cookie-toast');
        const msg   = document.getElementById('cookie-toast-msg');
        if (!toast || !msg) return;

        msg.textContent = message;
        toast.classList.add('show');
        setTimeout(() => toast.classList.remove('show'), 3000);
    }

    function syncTogglesWithConsent() {
        const checkboxes = document.querySelectorAll('#cookie-panel input[type="checkbox"][data-cat]');
        checkboxes.forEach(cb => {
            const catKey = cb.dataset.cat;
            const cat = COOKIE_CATEGORIES[catKey];
            if (cat && !cat.required) {
                cb.checked = currentConsent?.categories?.[catKey] || false;
            }
        });
    }


    /* ============================================================
       AZIONI DEL CONSENSO
       ============================================================ */

    function acceptAll() {
        const allCategories = {};
        for (const key of Object.keys(COOKIE_CATEGORIES)) {
            allCategories[key] = true;
        }
        saveConsent(allCategories);
        applyConsent(allCategories);
        hideBanner();
        hidePanel();
        showFloatButton();
        showToast('Preferenze salvate — tutti i cookie accettati');
    }

    function rejectAll() {
        const minCategories = {};
        for (const [key, cat] of Object.entries(COOKIE_CATEGORIES)) {
            // Tecnici sempre true, tutto il resto false
            minCategories[key] = cat.required ? true : false;
        }
        saveConsent(minCategories);
        applyConsent(minCategories);
        hideBanner();
        hidePanel();
        showFloatButton();
        showToast('Preferenze salvate — solo cookie necessari');
    }

    function saveCustom() {
        const categories = {};
        for (const [key, cat] of Object.entries(COOKIE_CATEGORIES)) {
            if (cat.required) {
                categories[key] = true;
            } else {
                const cb = document.querySelector(`#cookie-panel input[data-cat="${key}"]`);
                categories[key] = cb ? cb.checked : false;
            }
        }
        saveConsent(categories);
        applyConsent(categories);
        hidePanel();
        showFloatButton();
        showToast('Preferenze personalizzate salvate');
    }


    /* ============================================================
       REGISTRAZIONE DEGLI EVENT LISTENERS
       ============================================================ */

    function bindEvents() {
        // Banner → Rifiuta
        document.getElementById('cookie-btn-reject-all-banner')
            ?.addEventListener('click', rejectAll);

        // Banner → Personalizza
        document.getElementById('cookie-btn-settings')
            ?.addEventListener('click', function() {
                hideBanner();
                showPanel();
            });

        // Banner → Accetta
        document.getElementById('cookie-btn-accept-all-banner')
            ?.addEventListener('click', acceptAll);

        // Pannello → Chiudi (X)
        document.getElementById('cookie-panel-close')
            ?.addEventListener('click', function() {
                hidePanel();
                // Se il consenso non era ancora stato espresso, rimostra il banner
                if (!currentConsent) showBanner();
            });

        // Pannello → Rifiuta tutto
        document.getElementById('cookie-btn-reject-all-panel')
            ?.addEventListener('click', rejectAll);

        // Pannello → Accetta tutto
        document.getElementById('cookie-btn-accept-all-panel')
            ?.addEventListener('click', acceptAll);

        // Pannello → Salva preferenze
        document.getElementById('cookie-btn-save')
            ?.addEventListener('click', saveCustom);

        // Overlay → click fuori dal pannello
        document.getElementById('cookie-overlay')
            ?.addEventListener('click', function() {
                if (panelOpen) {
                    hidePanel();
                    if (!currentConsent) showBanner();
                }
            });

        // Floating button → riapri pannello
        document.getElementById('cookie-float-btn')
            ?.addEventListener('click', showPanel);

        // Keyboard: ESC chiude il pannello
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && panelOpen) {
                hidePanel();
                if (!currentConsent) showBanner();
            }
        });

        // Dettagli espandibili per ogni categoria
        document.querySelectorAll('.cookie-detail-expand').forEach(btn => {
            btn.addEventListener('click', function() {
                const key = this.dataset.detail;
                const detail = document.getElementById(`detail-${key}`);
                if (!detail) return;

                const isOpen = detail.classList.contains('open');
                detail.classList.toggle('open', !isOpen);
                this.setAttribute('aria-expanded', String(!isOpen));

                const icon = this.querySelector('i');
                if (icon) {
                    icon.classList.toggle('fa-chevron-down', isOpen);
                    icon.classList.toggle('fa-chevron-up', !isOpen);
                }
                this.childNodes[1].textContent = !isOpen
                    ? ` Nascondi cookie (${COOKIE_CATEGORIES[key]?.cookies.length})`
                    : ` Visualizza cookie utilizzati (${COOKIE_CATEGORIES[key]?.cookies.length})`;
            });
        });

        // Focus trap nel pannello (accessibilità)
        const panelEl = document.getElementById('cookie-panel');
        if (panelEl) {
            panelEl.addEventListener('keydown', function(e) {
                if (e.key !== 'Tab') return;
                const focusable = panelEl.querySelectorAll(
                    'button:not([disabled]), input:not([disabled]), a[href], [tabindex]:not([tabindex="-1"])'
                );
                if (!focusable.length) return;
                const first = focusable[0];
                const last  = focusable[focusable.length - 1];

                if (e.shiftKey && document.activeElement === first) {
                    e.preventDefault();
                    last.focus();
                } else if (!e.shiftKey && document.activeElement === last) {
                    e.preventDefault();
                    first.focus();
                }
            });
        }
    }


    /* ============================================================
       INIZIALIZZAZIONE
       ============================================================ */

    function init() {
        // Leggi eventuale consenso già salvato
        currentConsent = loadConsent();

        // Costruisci e inietta l'HTML nel DOM
        buildHTML();

        // Registra tutti gli event listeners
        bindEvents();

        if (currentConsent) {
            // Consenso già espresso: applica le preferenze silenziosamente
            applyConsent(currentConsent.categories);
            showFloatButton();
        } else {
            // Prima visita o policy aggiornata: mostra il banner
            showBanner();
        }
    }

    /* Avvio dopo il caricamento del DOM */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }


    /* ============================================================
       API PUBBLICA
       Espone funzioni utili per altri script del sito
       ============================================================ */

    window.CookieConsent = {
        /** Apre il pannello di gestione cookie (utile per link nel footer) */
        openPanel: showPanel,

        /** Restituisce le categorie attualmente accettate, o null se non espresso */
        getConsent: function() {
            return currentConsent ? { ...currentConsent } : null;
        },

        /** Controlla se una specifica categoria è stata accettata */
        hasConsent: function(category) {
            return currentConsent?.categories?.[category] === true;
        },

        /** Resetta il consenso (utile per test/debug) */
        reset: function() {
            deleteCookie(CONFIG.CONSENT_COOKIE_NAME);
            currentConsent = null;
            location.reload();
        },
    };

}());
