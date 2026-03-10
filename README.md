# Portale della Digitalizzazione del Patrimonio Culturale Siciliano

Portale web istituzionale sviluppato per la **Regione Siciliana** nell'ambito del progetto PNRR di digitalizzazione del patrimonio culturale. Il portale documenta e rende accessibili al pubblico i **40 cantieri di digitalizzazione** distribuiti nelle nove province siciliane, coinvolgendo soprintendenze, musei, siti archeologici e istituti culturali.

---

## Indice

- [Tecnologie utilizzate](#tecnologie-utilizzate)
- [Struttura del progetto](#struttura-del-progetto)
- [Installazione e avvio](#installazione-e-avvio)
- [Pagine e template](#pagine-e-template)
- [Dati dei cantieri](#dati-dei-cantieri)
- [Internazionalizzazione (IT/EN)](#internazionalizzazione-iten)
- [Design system](#design-system)
- [Conformità legale e privacy](#conformità-legale-e-privacy)
- [Note per i collaboratori](#note-per-i-collaboratori)

---

## Tecnologie utilizzate

| Componente | Tecnologia |
|---|---|
| Backend | Flask 3.0 + Jinja2 |
| Internazionalizzazione | Flask-Babel (`.po` / `.mo`) |
| Frontend | HTML5, CSS3 (variabili CSS), Vanilla JS |
| Font | Titillium Web (Google Fonts) |
| Icone | Font Awesome 6.4 |
| Mappe | ArcGIS Story Maps (iframe embed) |
| Modelli 3D | Google `<model-viewer>` web component (formato GLB) |
| Gestione cookie | Implementazione custom (Garante Privacy-compliant) |

---

## Struttura del progetto

```
progetto/
│
├── app.py                                  # Entry point Flask; routing e logica applicativa
├── cantieri_data.py                        # Dati di tutti i 40 cantieri (separato da app.py)
├── requirements.txt                        # Dipendenze Python
│
├── templates/                              # Template Jinja2
│   ├── base.html                           # Layout base (header, footer, nav, cookie banner)
│   ├── index.html                          # Homepage
│   ├── cantieri.html                       # Griglia dei cantieri con filtri e paginazione
│   ├── dettaglio-cantiere.html             # Scheda dettaglio singolo cantiere
│   ├── mappa.html                          # Visualizzazione ArcGIS Story Maps
│   ├── progetto.html                       # Descrizione del progetto PNRR
│   ├── statistiche.html                    # Dashboard statistiche aggregate
│   ├── contatti.html                       # Pagina contatti
│   ├── amministrazione-trasparente.html    # Sezione amministrazione trasparente
│   ├── note-legali.html                    # Note legali
│   ├── privacy-policy.html                 # Informativa privacy (GDPR)
│   └── cookie-policy.html                  # Cookie policy (Garante Privacy)
│
├── static/
│   ├── css/
│   │   ├── style.css               # Foglio di stile principale
│   │   └── cookie-consent.css      # Stili aggiuntivi per cookie banner
│   ├── js/
│   │   |── script.js               # Logica frontend (filtri, paginazione, menu mobile, cookie)
|   |   └── cookie-consent.css      # Stili aggiuntivi per cookie banner
|   |
│   └── img/                        # Immagini dei cantieri e asset grafici
│       ├── logo-regione-sicilia.png
│       └── [immagini cantieri].jpg
│
└── translations/                   # File di traduzione Flask-Babel
    ├── it/LC_MESSAGES/
    │   ├── messages.po
    │   └── messages.mo
    └── en/LC_MESSAGES/
        ├── messages.po
        └── messages.mo
```


## Installazione e avvio

### Prerequisiti

- Python 3.10+
- pip

### Setup

```bash
# 1. Clona il repository
git clone https://github.com/Area-Innovazione-SCS/digitalizzazione-beni-culturali.git
cd digitalizzazione-beni-culturali

# 2. Crea e attiva un ambiente virtuale
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Installa le dipendenze
pip install -r requirements.txt

# 4. Compila i file di traduzione (se necessario)
flask translate compile

# 5. Avvia il server di sviluppo
flask run
```

Il portale sarà disponibile su `http://localhost:5000`.

## Dati dei cantieri

Tutti i dati sono centralizzati in `cantieri_data.py` e importati in `app.py`. La struttura di ogni cantiere è un dizionario Python con i seguenti campi principali:

*Progetto finanziato nell'ambito del Piano Nazionale di Ripresa e Resilienza (PNRR) — Regione Siciliana, Assessorato dei Beni Culturali e dell'Identità Siciliana.*
