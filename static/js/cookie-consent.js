/**
 * ============================================================
 * COOKIE NOTICE - Barra informativa passiva
 * Portale Digitalizzazione Patrimonio Culturale - Regione Siciliana
 *
 * Questo sito utilizza ESCLUSIVAMENTE cookie tecnici necessari:
 *   - session   → gestione sessione Flask (lingua IT/EN)
 *   - csrf_token → protezione CSRF
 *
 * I cookie tecnici NON richiedono consenso preventivo ai sensi
 * dell'art. 122 D.Lgs. 196/2003 e del Provvedimento Garante
 * Privacy 10 giugno 2021 (Linee guida cookie).
 *
 * Non viene richiesto alcun consenso. La barra informativa
 * è una notifica passiva, non un banner bloccante.
 * ============================================================
 */

;(function () {
    'use strict';

    var STORAGE_KEY = 'cookie_notice_dismissed';

    /* ── Controlla se l'utente ha già chiuso la barra ── */
    function isDismissed() {
        // localStorage come storage primario (persistente tra pagine)
        try {
            if (localStorage.getItem(STORAGE_KEY) === '1') return true;
        } catch (e) { /* localStorage non disponibile */ }

        // Fallback: cookie (per browser con localStorage disabilitato)
        try {
            if (document.cookie.indexOf(STORAGE_KEY + '=1') !== -1) return true;
        } catch (e) { /* */ }

        return false;
    }

    /* ── Salva la dismissione ── */
    function saveDismissed() {
        // localStorage (primario)
        try {
            localStorage.setItem(STORAGE_KEY, '1');
        } catch (e) { /* */ }

        // Cookie fallback: 12 mesi
        try {
            var expires = new Date();
            expires.setFullYear(expires.getFullYear() + 1);
            document.cookie = STORAGE_KEY + '=1; expires=' + expires.toUTCString() +
                              '; path=/; SameSite=Lax';
        } catch (e) { /* */ }
    }

    /* ── Costruisce e mostra la barra ── */
    function showNotice() {
        var bar = document.createElement('div');
        bar.id = 'cookie-notice-bar';
        bar.setAttribute('role', 'note');
        bar.setAttribute('aria-label', 'Informativa cookie');
        bar.innerHTML =
            '<div class="cookie-notice-inner">' +
                '<i class="fas fa-shield-alt" aria-hidden="true"></i>' +
                '<p>' +
                    'Questo sito utilizza esclusivamente <strong>cookie tecnici necessari</strong> ' +
                    'al funzionamento del portale. Non vengono utilizzati cookie di profilazione ' +
                    'o di tracciamento. ' +
                    '<a href="/cookie-policy">Informativa cookie</a>' +
                '</p>' +
                '<button id="cookie-notice-close" type="button" aria-label="Chiudi informativa cookie">' +
                    '<i class="fas fa-times" aria-hidden="true"></i>' +
                    '<span>Ho capito</span>' +
                '</button>' +
            '</div>';

        /* Stili inline: nessuna dipendenza da cookie-consent.css */
        bar.style.cssText = [
            'position: fixed',
            'bottom: 0',
            'left: 0',
            'right: 0',
            'background: #1a2b4a',
            'color: #ffffff',
            'z-index: 9999',
            'box-shadow: 0 -2px 12px rgba(0,0,0,0.25)',
            'font-family: "Titillium Web", sans-serif',
            'font-size: 0.9rem',
            'transition: transform 0.3s ease',
        ].join(';');

        var inner = bar.querySelector('.cookie-notice-inner');
        inner.style.cssText = [
            'display: flex',
            'align-items: center',
            'gap: 1rem',
            'max-width: 1200px',
            'margin: 0 auto',
            'padding: 0.85rem 1.5rem',
            'flex-wrap: wrap',
        ].join(';');

        var icon = bar.querySelector('i.fa-shield-alt');
        icon.style.cssText = 'font-size: 1.25rem; color: #ca8114; flex-shrink: 0;';

        var p = bar.querySelector('p');
        p.style.cssText = 'margin: 0; line-height: 1.5; flex: 1; color: #e0e6f0;';

        var link = bar.querySelector('a');
        link.style.cssText = 'color: #ca8114; font-weight: 600; white-space: nowrap;';

        var btn = bar.querySelector('#cookie-notice-close');
        btn.style.cssText = [
            'display: flex',
            'align-items: center',
            'gap: 0.4rem',
            'background: #ca8114',
            'color: white',
            'border: none',
            'padding: 0.5rem 1.1rem',
            'border-radius: 4px',
            'font-size: 0.875rem',
            'font-weight: 600',
            'cursor: pointer',
            'white-space: nowrap',
            'font-family: inherit',
            'flex-shrink: 0',
        ].join(';');

        document.body.appendChild(bar);

        /* Chiusura */
        btn.addEventListener('click', function () {
            saveDismissed();
            bar.style.transform = 'translateY(100%)';
            setTimeout(function () {
                if (bar.parentNode) bar.parentNode.removeChild(bar);
            }, 320);
        });
    }

    /* ── Avvio ── */
    function init() {
        if (isDismissed()) return;
        showNotice();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    /* ── API pubblica minimale (compatibilità con eventuali riferimenti esistenti) ── */
    window.CookieConsent = {
        openPanel: function () {
            window.location.href = '/cookie-policy';
        },
        getConsent: function () { return null; },
        hasConsent: function () { return true; },
        reset: function () {
            try { localStorage.removeItem(STORAGE_KEY); } catch (e) { }
            try {
                document.cookie = STORAGE_KEY + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            } catch (e) { }
            location.reload();
        },
    };

}());
