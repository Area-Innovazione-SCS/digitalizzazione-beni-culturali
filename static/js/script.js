// ========================================
// PORTALE DEI CANTIERI - Main JavaScript
// ========================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ========================================
    // MOBILE MENU TOGGLE
    // ========================================
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    if (mobileMenuToggle && mainNav) {
        mobileMenuToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            this.classList.toggle('active');
            
            // Update aria-expanded
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
            
            // Animate menu icon
            const spans = this.querySelectorAll('span');
            if (this.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translateY(10px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translateY(-10px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!mainNav.contains(e.target) && !mobileMenuToggle.contains(e.target)) {
                mainNav.classList.remove('active');
                mobileMenuToggle.classList.remove('active');
                mobileMenuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }
    
    // ========================================
    // CANTIERI FILTERS - VERSIONE AGGIORNATA
    // ========================================
    const filterCategory = document.getElementById('filter-category');
    const filterProvincia = document.getElementById('filter-provincia');
    const filterStatus = document.getElementById('filter-status');
    const searchInput = document.getElementById('search-cantieri');
    const cantieriCards = document.querySelectorAll('.cantiere-card');
    
    function filterCantieri() {
        const categoryValue = filterCategory ? filterCategory.value.toLowerCase() : '';
        const provinciaValue = filterProvincia ? filterProvincia.value.toUpperCase() : '';
        const statusValue = filterStatus ? filterStatus.value.toLowerCase() : '';
        const searchValue = searchInput ? searchInput.value.toLowerCase() : '';
        
        cantieriCards.forEach(card => {
            // ✅ NUOVA LOGICA: Legge categorie dall'attributo data-categorie (array)
            const categorieAttr = card.getAttribute('data-categorie');
            let categorie = [];
            try {
                categorie = categorieAttr ? JSON.parse(categorieAttr) : [];
            } catch (e) {
                console.error('Errore nel parsing delle categorie:', e);
                categorie = [];
            }
            
            // ✅ NUOVA LOGICA: Legge provincia dall'attributo data-provincia
            const provincia = card.getAttribute('data-provincia') || '';
            
            // ✅ NUOVA LOGICA: Legge titolo e località dagli attributi data
            const titolo = card.getAttribute('data-titolo') || '';
            const localita = card.getAttribute('data-localita') || '';
            
            // Filtro stato (rimane invariato)
            const status = card.querySelector('.cantiere-status span:last-child')?.textContent.toLowerCase() || '';
            
            // ✅ FILTRO CATEGORIA: Controlla se la categoria selezionata è nell'array
            const matchesCategory = !categoryValue || categorie.some(cat => cat.toLowerCase() === categoryValue);
            
            // ✅ FILTRO PROVINCIA: Confronta con l'attributo data-provincia
            const matchesProvincia = !provinciaValue || provincia === provinciaValue;
            
            // Filtro stato (rimane invariato)
            const matchesStatus = !statusValue || status.includes(statusValue);
            
            // ✅ FILTRO RICERCA: Cerca in titolo e località dagli attributi data
            const matchesSearch = !searchValue || 
                                titolo.includes(searchValue) || 
                                localita.includes(searchValue);
            
            // Mostra/nascondi card in base ai filtri
            if (matchesCategory && matchesProvincia && matchesStatus && matchesSearch) {
                card.style.display = 'flex';
                card.style.animation = 'fadeIn 0.5s ease';
            } else {
                card.style.display = 'none';
            }
        });
        
        // Show message if no results
        const visibleCards = Array.from(cantieriCards).filter(card => card.style.display !== 'none');
        const grid = document.querySelector('.cantieri-grid');
        let noResultsMsg = document.querySelector('.no-results-message');
        
        if (visibleCards.length === 0 && grid) {
            if (!noResultsMsg) {
                noResultsMsg = document.createElement('div');
                noResultsMsg.className = 'no-results-message';
                noResultsMsg.style.gridColumn = '1 / -1';
                noResultsMsg.style.textAlign = 'center';
                noResultsMsg.style.padding = '3rem';
                noResultsMsg.innerHTML = `
                    <i class="fas fa-search" style="font-size: 3rem; color: var(--text-muted); margin-bottom: 1rem;"></i>
                    <h3 style="color: var(--text-primary); margin-bottom: 0.5rem;">Nessun cantiere trovato</h3>
                    <p style="color: var(--text-secondary);">Prova a modificare i filtri di ricerca</p>
                `;
                grid.appendChild(noResultsMsg);
            }
        } else if (noResultsMsg) {
            noResultsMsg.remove();
        }
    }
    
    // Add event listeners for filters
    if (filterCategory) filterCategory.addEventListener('change', filterCantieri);
    if (filterProvincia) filterProvincia.addEventListener('change', filterCantieri);
    if (filterStatus) filterStatus.addEventListener('change', filterCantieri);
    if (searchInput) {
        searchInput.addEventListener('input', debounce(filterCantieri, 300));
    }
    
    // ========================================
    // DEBOUNCE FUNCTION
    // ========================================
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // ========================================
    // SMOOTH SCROLL
    // ========================================
    const smoothScrollLinks = document.querySelectorAll('a[href^="#"]');
    
    smoothScrollLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // ========================================
    // INTERSECTION OBSERVER FOR ANIMATIONS
    // ========================================
    const animateOnScroll = document.querySelectorAll('.cantiere-card, .stat-card, .feature-card');
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'all 0.6s ease';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    animateOnScroll.forEach(element => {
        observer.observe(element);
    });
    
    // ========================================
    // PROGRESS BAR ANIMATION
    // ========================================
    const progressBars = document.querySelectorAll('.progress-fill');
    
    const progressObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const targetWidth = entry.target.style.width;
                entry.target.style.width = '0%';
                
                setTimeout(() => {
                    entry.target.style.width = targetWidth;
                }, 200);
                
                progressObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    progressBars.forEach(bar => {
        progressObserver.observe(bar);
    });
    
    // ========================================
    // LOAD MORE BUTTON
    // ========================================
    const loadMoreBtn = document.getElementById('load-more');
    
    if (loadMoreBtn) {
        loadMoreBtn.addEventListener('click', function() {
            // Simulate loading more cantieri
            this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Caricamento...';
            this.disabled = true;
            
            setTimeout(() => {
                this.innerHTML = '<i class="fas fa-check"></i> Tutti i cantieri caricati';
                setTimeout(() => {
                    this.style.display = 'none';
                }, 2000);
            }, 1500);
        });
    }
    
    // ========================================
    // FORM VALIDATION
    // ========================================
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const inputs = this.querySelectorAll('input[required], textarea[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = 'var(--danger-color)';
                    
                    // Remove error styling after user starts typing
                    input.addEventListener('input', function() {
                        this.style.borderColor = '';
                    }, { once: true });
                }
            });
            
            if (isValid) {
                // Show success message
                const successMsg = document.createElement('div');
                successMsg.style.cssText = `
                    position: fixed;
                    top: 20px;
                    right: 20px;
                    background: var(--success-color);
                    color: white;
                    padding: 1rem 2rem;
                    border-radius: 8px;
                    box-shadow: var(--shadow-lg);
                    z-index: 9999;
                    animation: slideInFromRight 0.5s ease;
                `;
                successMsg.innerHTML = '<i class="fas fa-check-circle"></i> Richiesta inviata con successo!';
                document.body.appendChild(successMsg);
                
                setTimeout(() => {
                    successMsg.style.animation = 'fadeOut 0.5s ease';
                    setTimeout(() => successMsg.remove(), 500);
                }, 3000);
                
                this.reset();
            }
        });
    });
    
    // ========================================
    // CANTIERE CARD HOVER EFFECTS
    // ========================================
    const cantiereLinks = document.querySelectorAll('.cantiere-link');
    
    cantiereLinks.forEach(link => {
        link.addEventListener('mouseenter', function() {
            const card = this.closest('.cantiere-card');
            if (card) card.style.transform = 'translateY(-8px)';
        });
        
        link.addEventListener('mouseleave', function() {
            const card = this.closest('.cantiere-card');
            if (card) card.style.transform = '';
        });
    });
    
    // ========================================
    // SEARCH MODAL (if implemented)
    // ========================================
    const searchToggle = document.querySelector('[data-toggle="search"]');
    
    if (searchToggle) {
        searchToggle.addEventListener('click', function() {
            // Toggle search modal or expand search bar
            const searchBar = document.querySelector('.search-input');
            if (searchBar) {
                searchBar.focus();
                searchBar.style.minWidth = '300px';
            }
        });
    }
    
    // ========================================
    // BACK TO TOP BUTTON
    // ========================================
    const backToTopBtn = document.createElement('button');
    backToTopBtn.className = 'back-to-top';
    backToTopBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTopBtn.setAttribute('aria-label', 'Torna su');
    backToTopBtn.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 50px;
        height: 50px;
        background: var(--primary-color);
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        display: none;
        align-items: center;
        justify-content: center;
        box-shadow: var(--shadow-lg);
        z-index: 1000;
        transition: all 0.3s ease;
    `;
    
    document.body.appendChild(backToTopBtn);
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopBtn.style.display = 'flex';
        } else {
            backToTopBtn.style.display = 'none';
        }
    });
    
    backToTopBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
    
    backToTopBtn.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px)';
        this.style.background = 'var(--secondary-color)';
    });
    
    backToTopBtn.addEventListener('mouseleave', function() {
        this.style.transform = 'none';
        this.style.background = 'var(--primary-color)';
    });
    
    // ========================================
    // ACCESSIBILITY ENHANCEMENTS
    // ========================================
    
    // Focus trap for mobile menu
    const focusableElements = mainNav ? mainNav.querySelectorAll('a, button') : [];
    
    if (focusableElements.length > 0) {
        const firstFocusable = focusableElements[0];
        const lastFocusable = focusableElements[focusableElements.length - 1];
        
        document.addEventListener('keydown', function(e) {
            if (mainNav && mainNav.classList.contains('active')) {
                if (e.key === 'Tab') {
                    if (e.shiftKey) {
                        if (document.activeElement === firstFocusable) {
                            e.preventDefault();
                            lastFocusable.focus();
                        }
                    } else {
                        if (document.activeElement === lastFocusable) {
                            e.preventDefault();
                            firstFocusable.focus();
                        }
                    }
                }
                
                if (e.key === 'Escape') {
                    mainNav.classList.remove('active');
                    mobileMenuToggle.classList.remove('active');
                    mobileMenuToggle.focus();
                }
            }
        });
    }
    
    // ========================================
    // CONSOLE MESSAGE
    // ========================================
    console.log('%c🏗️ Portale dei Cantieri', 'font-size: 24px; font-weight: bold; color: #0048ad;');
    console.log('%cSito sviluppato con HTML5, CSS3 e JavaScript moderno', 'color: #666;');
    console.log('%c✓ Accessibile ✓ Responsive ✓ Performante', 'color: #00cc66; font-weight: bold;');
});

// ========================================
// UTILITY FUNCTIONS
// ========================================

// Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('it-IT', {
        style: 'currency',
        currency: 'EUR',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(amount);
}

// Format date
function formatDate(date) {
    return new Intl.DateTimeFormat('it-IT', {
        day: '2-digit',
        month: 'long',
        year: 'numeric'
    }).format(new Date(date));
}

// Calculate percentage
function calculatePercentage(current, total) {
    return Math.round((current / total) * 100);
}

// ========================================
// EXPORT FUNCTIONS (if needed)
// ========================================
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        formatCurrency,
        formatDate,
        calculatePercentage
    };
}