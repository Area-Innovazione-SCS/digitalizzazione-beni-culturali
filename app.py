"""
Portale dei Cantieri - Flask Application
Server di sviluppo locale per il portale dei cantieri

NOTA: I dati dei cantieri sono ora su MongoDB.
      Connessione gestita da db/connection.py
      Query gestite da db/cantieri_repository.py
"""

from flask import Flask, render_template, send_from_directory, jsonify, request, abort, session, redirect, url_for
from flask_babel import Babel, gettext as _
import os
from datetime import datetime

# ========================================
# IMPORTAZIONE REPOSITORY DATABASE
# ========================================
try:
    from db.cantieri_repository import Cantieri
    from db.connection import get_db
    _db_ok = True
    print("✓ Modulo database importato correttamente")
except ImportError as e:
    print(f"❌ ERRORE: Impossibile importare il modulo database!")
    print(f"   Assicurati che la cartella db/ sia presente accanto ad app.py")
    print(f"   Errore: {e}")
    _db_ok = False

# Configurazione Flask con le nuove cartelle
app = Flask(__name__, 
    template_folder='templates',
    static_folder='static',
    static_url_path='/static')

# Configurazione
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'portale-cantieri-secret-key-2025')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', '0') == '1'

# ========================================
# HEADER DI SICUREZZA HTTP
# ========================================

@app.after_request
def set_security_headers(response):
    """Aggiunge header di sicurezza HTTP a ogni risposta."""
    # Impedisce che il sito venga inserito in iframe da altri siti (clickjacking)
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # Impedisce al browser di indovinare il tipo MIME dei file
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # Limita le informazioni di provenienza passate ai siti esterni
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    # Disabilita funzionalità browser non utilizzate dal portale
    response.headers['Permissions-Policy'] = 'camera=(), microphone=(), geolocation=(), payment=()'
    return response

# ========================================
# CONFIGURAZIONE BABEL (Traduzioni)
# ========================================
app.config['BABEL_DEFAULT_LOCALE'] = 'it'
app.config['BABEL_SUPPORTED_LOCALES'] = ['it', 'en']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

def get_locale():
    """Determina la lingua da usare, controllando prima la sessione"""
    lang = session.get('lang')
    if lang and lang in ['it', 'en']:
        return lang
    return 'it'

babel = Babel(app, locale_selector=get_locale)

# ========================================
# UTILITÀ - Localizzazione cantiere
# ========================================

# Campi testuali che hanno una variante _en in cantieri_data.py
_CANTIERE_TRANSLATABLE_FIELDS = [
    'titolo',
    'descrizione_breve',
    'descrizione_completa',
    'categorie_labels',
    'orari_apertura',
    'costo_biglietto',
    'accessibilita',
    'stato_label',
]

def localize_cantiere(cantiere, lang):
    """
    Restituisce una copia del dizionario cantiere con i campi testuali
    sostituiti dalla versione inglese (_en) quando lang == 'en'.
    Se il campo _en è vuoto o assente, viene mantenuto il testo italiano.
    """
    if lang != 'en':
        return cantiere  # nessuna modifica in italiano

    c = dict(cantiere)  # copia superficiale

    for field in _CANTIERE_TRANSLATABLE_FIELDS:
        en_key = f'{field}_en'
        en_val = c.get(en_key)
        # Sostituisce solo se il campo _en è definito e non vuoto
        if en_val:
            c[field] = en_val

    # Traduce anche i nomi dei beni nella composizione
    if c.get('composizione_beni'):
        beni_localizzati = []
        for bene in c['composizione_beni']:
            b = dict(bene)
            if b.get('nome_en'):
                b['nome'] = b['nome_en']
            beni_localizzati.append(b)
        c['composizione_beni'] = beni_localizzati

    return c

# ========================================
# ROUTE - Cambio lingua
# ========================================

@app.route('/set_language/<lang>')
def set_language(lang):
    """Imposta la lingua nella sessione e reindirizza alla pagina precedente"""
    if lang in ['it', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

# ========================================
# ROUTES - Pagine HTML
# ========================================

@app.route('/')
def index():
    """Homepage del sito"""
    return render_template('index.html')

@app.route('/progetto.html')
@app.route('/progetto')
def progetto():
    """Pagina del progetto"""
    return render_template('progetto.html')

@app.route('/cantieri.html')
@app.route('/cantieri')
def cantieri():
    """Pagina elenco cantieri"""
    return render_template('cantieri.html')

@app.route('/cantieri/<int:cantiere_id>')
def dettaglio_cantiere(cantiere_id):
    """Pagina dettaglio cantiere con ID dinamico"""
    cantiere = Cantieri.get_by_id(cantiere_id)

    if not cantiere:
        abort(404)

    lang = session.get('lang', 'it')
    cantiere_locale = localize_cantiere(cantiere, lang)

    return render_template('dettaglio-cantiere.html',
                           cantiere=cantiere_locale)

@app.route('/statistiche.html')
@app.route('/statistiche')
def statistiche():
    """Pagina statistiche"""
    return render_template('statistiche.html')

@app.route('/mappa.html')
@app.route('/mappa')
def mappa():
    """Pagina mappa"""
    return render_template('mappa.html')

@app.route('/contatti.html')
@app.route('/contatti')
def contatti():
    """Pagina contatti"""
    return render_template('contatti.html')

@app.route('/amministrazione-trasparente')
def amministrazione_trasparente():
    """Pagina Amministrazione Trasparente"""
    return render_template('amministrazione-trasparente.html')

@app.route('/privacy-policy')
def privacy_policy():
    """Pagina Privacy Policy"""
    return render_template('privacy-policy.html')

@app.route('/note-legali')
def note_legali():
    """Pagina Note Legali"""
    return render_template('note-legali.html')

@app.route('/cookie-policy')
def cookie_policy():
    """Pagina Cookie Policy"""
    return render_template('cookie-policy.html')

@app.route('/api/cookie-consent', methods=['POST'])
def log_consent():
    data = request.get_json()
    # Salvi solo: timestamp, versione policy, categorie — NO IP, NO dati personali
    app.logger.info(f"CONSENT | {data['timestamp']} | v{data['version']} | {data['categories']}")
    return jsonify({'ok': True})

# ========================================
# ROUTES - File Statici (CSS, JS, Immagini)
# ========================================

@app.route('/style.css')
def style_css_compat():
    """Compatibilità: redirect a /static/css/style.css"""
    return send_from_directory('static/css', 'style.css', mimetype='text/css')

@app.route('/script.js')
def script_js_compat():
    """Compatibilità: redirect a /static/js/script.js"""
    return send_from_directory('static/js', 'script.js', mimetype='application/javascript')

# ========================================
# ROUTES - Documentazione
# ========================================

@app.route('/docs/<path:filename>')
def docs(filename):
    """Serve file di documentazione"""
    docs_dir = os.path.join(app.static_folder, 'docs')
    return send_from_directory(docs_dir, filename)

# ========================================
# API ENDPOINTS
# ========================================

@app.route('/api/cantieri')
def api_cantieri():
    """
    API: Restituisce l'elenco dei cantieri
    Query params:
    - categoria: filtra per categoria (cerca nell'array categorie)
    - provincia: filtra per provincia (sigla 2 lettere maiuscole)
    - stato: filtra per stato
    - search: ricerca testuale (titolo e località)
    - page: numero pagina (default: 1)
    - per_page: risultati per pagina (default: 9)
    """
    # Recupera tutti i cantieri dal database
    cantieri = Cantieri.get_all()

    # Filtro per categoria
    categoria_filter = request.args.get('categoria', '').lower()
    if categoria_filter:
        cantieri = [
            c for c in cantieri
            if any(cat.lower() == categoria_filter for cat in c.get('categorie', []))
        ]

    # Filtro per provincia
    provincia_filter = request.args.get('provincia', '').upper()
    if provincia_filter:
        cantieri = [
            c for c in cantieri
            if c.get('provincia', '') == provincia_filter
        ]

    # Filtro per stato
    stato = request.args.get('stato', '').lower()
    if stato:
        cantieri = [c for c in cantieri if stato in c.get('stato', '').lower()]

    # Ricerca testuale
    search = request.args.get('search', '').lower()
    if search:
        cantieri = [
            c for c in cantieri if
            search in c.get('titolo', '').lower() or
            search in c.get('localita', '').lower()
        ]

    # Paginazione
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 9))

    total = len(cantieri)
    start = (page - 1) * per_page
    end = start + per_page

    cantieri_page = cantieri[start:end]

    return jsonify({
        'success': True,
        'cantieri': cantieri_page,
        'total': total,
        'page': page,
        'per_page': per_page,
        'total_pages': (total + per_page - 1) // per_page
    })


@app.route('/api/cantieri/<int:cantiere_id>')
def api_cantiere_dettaglio(cantiere_id):
    """API: Restituisce i dettagli di un cantiere specifico"""
    cantiere = Cantieri.get_by_id(cantiere_id)

    if cantiere:
        return jsonify({
            'success': True,
            'cantiere': cantiere
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Cantiere non trovato'
        }), 404


@app.route('/api/cantieri/<int:cantiere_id>/follow', methods=['POST'])
def api_cantiere_follow(cantiere_id):
    """API: Segui un cantiere per ricevere aggiornamenti"""
    cantiere = Cantieri.get_by_id(cantiere_id)

    if not cantiere:
        return jsonify({
            'success': False,
            'error': 'Cantiere non trovato'
        }), 404

    return jsonify({
        'success': True,
        'message': f'Ora segui il cantiere "{cantiere["titolo"]}"'
    })


@app.route('/api/stats')
def api_stats():
    """API: Restituisce le statistiche generali"""
    tutti = Cantieri.get_all()

    totale = len(tutti)
    in_corso = len([c for c in tutti if c['stato'] == 'in-corso'])
    completati = len([c for c in tutti if c['stato'] == 'completato'])
    pianificati = len([c for c in tutti if c['stato'] == 'pianificato'])

    budget_totale = sum(
        c.get('importo', 0) for c in tutti
        if isinstance(c.get('importo'), (int, float))
    )

    return jsonify({
        'success': True,
        'stats': {
            'totale_cantieri': totale,
            'in_corso': in_corso,
            'completati': completati,
            'pianificati': pianificati,
            'budget_totale': budget_totale,
            'budget_totale_formatted': f'€{budget_totale/1000000:.1f}M' if budget_totale > 0 else 'N/A'
        }
    })

# ========================================
# ERROR HANDLERS
# ========================================

@app.errorhandler(404)
def page_not_found(error):
    """Gestione errore 404"""
    return '''
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>404 - Pagina non trovata</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #0048ad 0%, #00a8ff 100%);
                color: white;
            }
            .container {
                text-align: center;
                padding: 2rem;
            }
            h1 {
                font-size: 6rem;
                margin: 0;
            }
            p {
                font-size: 1.5rem;
                margin: 1rem 0;
            }
            a {
                display: inline-block;
                margin-top: 2rem;
                padding: 1rem 2rem;
                background: white;
                color: #0048ad;
                text-decoration: none;
                border-radius: 8px;
                font-weight: 600;
                transition: transform 0.3s;
            }
            a:hover {
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>404</h1>
            <p>Ops! Pagina non trovata</p>
            <a href="/">← Torna alla Homepage</a>
        </div>
    </body>
    </html>
    ''', 404

@app.errorhandler(500)
def internal_error(error):
    """Gestione errore 500"""
    return '''
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>500 - Errore del server</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
                background: linear-gradient(135deg, #cc0000 0%, #ff6b6b 100%);
                color: white;
            }
            .container {
                text-align: center;
                padding: 2rem;
            }
            h1 {
                font-size: 6rem;
                margin: 0;
            }
            p {
                font-size: 1.5rem;
                margin: 1rem 0;
            }
            a {
                display: inline-block;
                margin-top: 2rem;
                padding: 1rem 2rem;
                background: white;
                color: #cc0000;
                text-decoration: none;
                border-radius: 8px;
                font-weight: 600;
                transition: transform 0.3s;
            }
            a:hover {
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>500</h1>
            <p>Errore interno del server</p>
            <a href="/">← Torna alla Homepage</a>
        </div>
    </body>
    </html>
    ''', 500



# ========================================
# MAIN
# ========================================

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug,
        use_reloader=debug
    )