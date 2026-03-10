"""
Dati dei Cantieri di Digitalizzazione del Patrimonio Culturale
File di dati aggiornato - SUPPORTO MULTILINGUA IT/EN

CAMPI TRADUCIBILI:
  Per ogni campo testuale esiste la variante _en (es. titolo_en).
  Inserisci la traduzione inglese nei campi _en; se vuoto viene usato il campo IT.

COMPOSIZIONE BENI:
  Ogni elemento ha anche "nome_en" per tradurre il nome del tipo di bene.
"""

# ========================================
# LISTA COMPLETA DEI CANTIERI
# ========================================

CANTIERI_DATA = [
{
    'id': 1,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Agrigento',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Agrigento',
    'categorie': [
        'negativi-pellicola',
        'negativi-lastre',
        'diapositive',
        'stampe-fotografiche'
    ],
    'categorie_labels': [
        'Negativi su pellicola',
        'Negativi su lastre di vetro',
        'Diapositive',
        'Stampe fotografiche'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Film negatives',
        'Glass plate negatives',
        'Slides',
        'Photographic prints'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus su Valle dei Templi e siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the Valley of the Temples and the archaeological sites of the province.',
    'descrizione_completa': '''
        <p style="margin-bottom: 1rem;">
            La <strong>Soprintendenza per i Beni Culturali e Ambientali di Agrigento</strong> conserva uno dei più importanti archivi fotografici 
            della Sicilia dedicato alla documentazione archeologica e monumentale della provincia. L'archivio copre un arco temporale 
            che va dalla fine dell'Ottocento fino ai giorni nostri.
        </p>
        <p style="margin-bottom: 1rem;">
            La collezione include immagini storiche della <strong>Valle dei Templi</strong>, degli scavi di Eraclea Minoa, 
            di Selinunte e di numerosissimi altri siti archeologici e monumentali della provincia. Di particolare rilevanza 
            sono le lastre fotografiche dei primi del Novecento che documentano lo stato dei monumenti prima dei restauri moderni.
        </p>
        <p style="margin-bottom: 1rem;">
            Il fondo fotografico comprende negativi su pellicola, diapositive a colori, stampe fotografiche storiche 
            e negativi su lastra di vetro. Molti di questi materiali sono opera di fotografi professionisti dell'epoca 
            e rappresentano testimonianze uniche del patrimonio culturale siciliano.
        </p>
        <p>
            Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
            di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
        </p>
    ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
        <p style="margin-bottom: 1rem;">
            The <strong>Superintendency for Cultural and Environmental Heritage of Agrigento</strong> holds one of the most important photographic archives
            in Sicily, dedicated to the archaeological and monumental documentation of the province. The archive spans a timeframe
            ranging from the late nineteenth century to the present day.
        </p>
        <p style="margin-bottom: 1rem;">
            The collection includes historical images of the <strong>Valley of the Temples</strong>, the excavations of Heraclea Minoa,
            Selinunte, and numerous other archaeological and monumental sites across the province. Of particular significance
            are the glass plate photographs from the early twentieth century, documenting the state of the monuments before modern restoration works.
        </p>
        <p style="margin-bottom: 1rem;">
            The photographic holdings include film negatives, colour slides, historical photographic prints,
            and glass plate negatives. Many of these materials are the work of professional photographers of the era
            and represent unique testimonies of Sicilian cultural heritage.
        </p>
        <p>
            The digitization project will preserve this invaluable documentary heritage and
            make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
        </p>
    ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Agrigento',
    'provincia': 'AG',
    'indirizzo': 'Via Ugo La Malfa, Villa Genuardi - 92100 Agrigento (AG)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 367400,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 180400,
        },
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 132000,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 50000,
        },
        {
            'nome': 'Negativi su lastra di vetro',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Glass plate negatives',
            'quantita': 5000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-agrigento.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': 'https://storymaps.arcgis.com/stories/fc49d5192b02446b8f361d47d7a45aff',

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Ven: 9:00-13:00<br>Mer: 15:00-18:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Fri: 9:00-13:00<br>Wed: 15:00-18:00',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-agrigento',
    'telefono': '+39 0922 552611',
    'email': 'sopriag@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/ricerca?istituto=sbca-agrigento',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',

    # ========================================
    # MODELLO 3D
    # ========================================
    'modello_3d_url': '/static/models/bugatti.glb',
    'modello_3d_poster': '/static/images/preview-3d.jpg',
    'modello_3d_sketchfab': 'https://sketchfab.com/...',
},

{
    'id': 2,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Caltanissetta',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Caltanissetta',
    'categorie': [
        'stampe-fotografiche',
        'negativi-lastre',
        'diapositive',
        'negativi-pellicola'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Negativi su lastre di vetro',
        'Diapositive',
        'Negativi su pellicola'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Glass plate negatives',
        'Slides',
        'Film negatives'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus su siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of the province.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di Caltanissetta</strong> conserva vari tipi di beni culturali nella provincia, tra cui beni archittetonici e storico-artistici, siti paesaggistici ed ambientali, patrimonio archeologico, beni bibliografici e archivi e patrimoni demoetnoantropologici.
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche dell' <strong>Antiquarium iconografico e Mura Timoleontee di Capo Soprano</strong> e dell'area archeologica e Antiquarium di Sabucina. 
            </p>
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende negativi su pellicola, diapositive a colori, stampe fotografiche storiche 
                e negativi su lastra di vetro. Molti di questi materiali sono opera di fotografi professionisti dell'epoca 
                e rappresentano testimonianze uniche del patrimonio culturale siciliano.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Caltanissetta</strong> preserves various types of cultural assets across the province, including architectural and historical-artistic heritage, landscape and environmental sites, archaeological patrimony, bibliographic assets, archives, and ethno-anthropological heritage.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the <strong>Iconographic Antiquarium and Timoleontean Walls of Capo Soprano</strong> and the archaeological area and Antiquarium of Sabucina.
            </p>
            <p style="margin-bottom: 1rem;">
                The photographic holdings include film negatives, colour slides, historical photographic prints,
                and glass plate negatives. Many of these materials are the work of professional photographers of the era
                and represent unique testimonies of Sicilian cultural heritage.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Caltanissetta',
    'provincia': 'CL',
    'indirizzo': 'Via Francesco Crispi 25 - 93100 Caltanissetta (CL)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 40200,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 15000,
        },
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 5000,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 20000,
        },
        {
            'nome': 'Negativi su lastra di vetro',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Glass plate negatives',
            'quantita': 200,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-caltanissetta.png',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': 'https://storymaps.arcgis.com/stories/e18bf0d7188d424ea453512acdc51480',

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun e Mer: 9:00-13:00 / Mer: 16:00-18:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon and Wed: 9:00-13:00 / Wed: 16:00-18:00<br>',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-caltanissetta',
    'telefono': '+39 0934 554965',
    'email': 'sopricl@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': '-',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 3,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Enna',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Enna',
    'categorie': [
        'stampe-fotografiche',
        'diapositive',
        'negativi-pellicola'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Diapositive',
        'Negativi su pellicola'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Slides',
        'Film negatives'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus sui siti archeologici di Aidone, Centuripe e Piazza Armerina.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of Aidone, Centuripe and Piazza Armerina.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di Enna</strong> conserva il patrimonio della provincia ennese, con l'obiettivo di salvaguardare e valorizzare la storia e l'identità culturale del territorio. 
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche dell' <strong>Area archeologica di Morgantina</strong>, del museo archeologico di Centuripe,, del Museo Regionale di Aidone e del Museo interdisciplinare di Enna.
            </p>
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende negativi su pellicola, diapositive a colori e stampe fotografiche storiche.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Enna</strong> preserves the heritage of the Enna province, with the aim of safeguarding and enhancing the history and cultural identity of the territory.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the <strong>Archaeological Area of Morgantina</strong>, the archaeological museum of Centuripe, the Regional Museum of Aidone, and the Interdisciplinary Museum of Enna.
            </p>
            <p style="margin-bottom: 1rem;">
                The photographic holdings include film negatives, colour slides, and historical photographic prints.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Enna',
    'provincia': 'EN',
    'indirizzo': 'Via Orfanotrofio 15 - 94100 Enna (EN)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 367400,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 3000,
        },
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 1000,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 7000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-enna.png',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': '-',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': '',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-enna',
    'telefono': '+39 0935 507611',
    'email': 'sopreng@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/detail/PhotographicHeritage/1900382255',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 4,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Messina',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Messina',
    'categorie': [
        'stampe-fotografiche',
        'diapositive',
        'negativi-pellicola',
        'disegni-grafici-mappe'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Diapositive',
        'Negativi su pellicola',
        'Disegni, grafici, mappe'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Slides',
        'Film negatives',
        'Drawings, graphics, maps'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus sui siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of the province.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di 	Messina</strong> conserva un ricco patrimonio culturale che include beni architettonici e storico-artistici, siti archeologici, beni bibliografici, archi storici, fondi librari e collezioni documentarie.
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche dei principali siti archeologici della provincia, tra cui quello di Capo d'Orlando, di Naxos, di Grotta San Teodoro e del Teatro Greco Romano di Taormina.
            </p>
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende negativi su pellicola, diapositive a colori, stampe fotografiche storiche 
                e disegni, grafici e mappe. Molti di questi materiali sono opera di fotografi professionisti dell'epoca 
                e rappresentano testimonianze uniche del patrimonio culturale siciliano.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Messina</strong> preserves a rich cultural patrimony that includes architectural and historical-artistic assets, archaeological sites, bibliographic heritage, historical archives, library collections, and documentary collections.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the main archaeological sites of the province, among them Capo d'Orlando, Naxos, Grotta San Teodoro, and the Greco-Roman Theatre of Taormina.
            </p>
            <p style="margin-bottom: 1rem;">
                The photographic holdings include film negatives, colour slides, historical photographic prints,
                and drawings, graphics, and maps. Many of these materials are the work of professional photographers of the era
                and represent unique testimonies of Sicilian cultural heritage.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Messina',
    'provincia': 'ME',
    'indirizzo': 'Viale Boccetta 83 - 98122 Messina (ME)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 92000,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 19000,
        },
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 17000,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 41000,
        },
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 15000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-messina.png',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': 'https://storymaps.arcgis.com/stories/1d4848bae9c146da8694dde1849b08a3',

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': '-',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': '',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-messina',
    'telefono': '+39 0903 6746498',
    'email': 'soprime@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/ricerca?istituto=sbca-agrigento',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 5,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Palermo',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Palermo',
    'categorie': [
        'stampe-fotografiche',
        'negativi-pellicola'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Negativi su pellicola'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Film negatives'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus sui siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of the province.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di Palermo</strong> conserva e valorizza la storia, l'arte, l'archeologia, il paesaggio e la documentazione scritta della città di Palermo e dei suoi dintorni.
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche delle aree archeologiche di Himera, Solunto, Monte Jato, Castello a Mare, Villa Bonanno, oltre che di numerosi musei regionali e castelli. 
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende negativi su pellicola e stampe fotografiche storiche.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Palermo</strong> preserves and promotes the history, art, archaeology, landscape, and written documentation of the city of Palermo and its surroundings.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the archaeological areas of Himera, Solunto, Monte Jato, Castello a Mare, and Villa Bonanno, as well as numerous regional museums and castles.
            <p style="margin-bottom: 1rem;">
                The photographic holdings include film negatives and historical photographic prints.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Palermo',
    'provincia': 'PA',
    'indirizzo': 'Via Giuseppe Garibaldi 41, Palazzo Ajiutamicristo - 90133 Palermo (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 204400,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 90000,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 114400,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-palermo.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': 'https://storymaps.arcgis.com/stories/9408a47ecd8b4c29bbef45d4a686e6c6',

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': '-',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': '',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-palermo',
    'telefono': '+39 0917 234011',
    'email': 'sopripa@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/ricerca?istituto=sbca-agrigento',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 6,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Trapani',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Trapani',
    'categorie': [
        'stampe-fotografiche',
        'diapositive',
        'negativi-pellicola',
        'negativi-lastre'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Diapositive',
        'Negativi su pellicola',
        'Negativi su lastre di vetro'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Slides',
        'Film negatives',
        'Glass plate negatives'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus sui siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of the province.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di Trapani</strong> include la catalogazione e tutela dei beni architettonici, storico-artistici, demoetnoantropologici e paesaggistici, nonchÃ¨ numerosi siti archeologici. 
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche delle aree archeologiche di Segesta, Selinunte, delle Cave di Cusa, del Museo archeologico di Baglio Anselmi e del Museo del Satiro.
            </p>
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende negativi su pellicola, diapositive a colori, stampe fotografiche storiche 
                e negativi su lastra di vetro.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Trapani</strong> oversees the cataloguing and protection of architectural, historical-artistic, ethno-anthropological, and landscape heritage, as well as numerous archaeological sites.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the archaeological areas of Segesta, Selinunte, the Cave di Cusa quarries, the Archaeological Museum of Baglio Anselmi, and the Museum of the Satyr.
            </p>
            <p style="margin-bottom: 1rem;">
                The photographic holdings include film negatives, colour slides, historical photographic prints,
                and glass plate negatives.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Trapani',
    'provincia': 'TP',
    'indirizzo': 'Via Giuseppe Garibaldi 85 - 91100 Trapani (TP)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 35580,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 500,
        },
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 30,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 50,
        },
        {
            'nome': 'Negativi su lastra di vetro',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Glass plate negatives',
            'quantita': 35000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-trapani.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar: 10:00-13:00 / Mer: 15:30-17:30<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue: 10:00-13:00 / Wed: 15:30-17:30<br>',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www2.regione.sicilia.it/beniculturali/SoprinTP/sito%20sbca%20trapani/home/sbca_trapani_home.html',
    'telefono': '+39 0923 808241',
    'email': 'sopritp@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': '-',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 7,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Catania',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Catania',
    'categorie': [
        'stampe-fotografiche',
        'diapositive',
        'negativi-pellicola',
        'negativi-lastre',
        'disegni-grafici-mappe'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Diapositive',
        'Negativi su pellicola',
        'Negativi su lastre di vetro',
        'Disegni, grafici, mappe'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Slides',
        'Film negatives',
        'Glass plate negatives',
        'Drawings, graphics, maps'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus sui siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of the province.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di Catania</strong> protegge e valorizza il ricco patrimonio culturale della provincia di Catania, tra cui beni architettonici, elementi paesaggistici, siti archeologici e un vasto patrimonio bibliografico e archivistico.
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche delle aree archeologiche di PalikÃ¨ e Santa Venera al Pozzo, musei regionali, teatri, anfiteatri e terme.
            </p>
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende negativi su pellicola, diapositive a colori, stampe fotografiche storiche, 
                negativi su lastra di vetro e disegni, grafici e mappe.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Catania</strong> protects and promotes the rich cultural patrimony of the province of Catania, including architectural assets, landscape features, archaeological sites, and an extensive bibliographic and archival heritage.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the archaeological areas of Palikè and Santa Venera al Pozzo, regional museums, theatres, amphitheatres, and thermal baths.
            </p>
            <p style="margin-bottom: 1rem;">
                The photographic holdings include film negatives, colour slides, historical photographic prints,
                glass plate negatives, and drawings, graphics, and maps.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Catania',
    'provincia': 'CT',
    'indirizzo': 'Via Luigi Sturzo 80 - 95131 Catania (CT)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 173560,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 142560,
        },
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 1000,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 25000,
        },
        {
            'nome': 'Negativi su lastra di vetro',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Glass plate negatives',
            'quantita': 2000,
        },
        {
            'nome': 'Unicum e disegni fotografici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Unique items and photographic drawings',
            'quantita': 3000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-catania.jpeg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': 'https://storymaps.arcgis.com/stories/6fd463e56c8e46fa888fdec848d5198f',

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': '-',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': '',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-catania',
    'telefono': '+39 0957 472111',
    'email': 'soprict@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': '-',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 8,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Ragusa',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Ragusa',
    'categorie': [
        'stampe-fotografiche',
        'diapositive'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Diapositive'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Slides'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus sui siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of the province.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di Ragusa</strong> tutela la memoria materiale e immateriale del territorio ragusano, dalle testimonianze antiche alle tradizioni locali, passando per le risorse librarie e documentarie.
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche aree archeologiche di Agorà, di Caucana, di Cava d'Ispica, di Parco Forza, nonchÃ¨ di diversi musei regionali.
            </p>
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende diapositive a colori e stampe fotografiche storiche.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Ragusa</strong> safeguards the tangible and intangible memory of the Ragusa territory, from ancient testimonies to local traditions, including library and documentary resources.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the archaeological areas of the Agorà, Caucana, Cava d'Ispica, and Parco Forza, as well as several regional museums.
            </p>
            <p style="margin-bottom: 1rem;">
                The photographic holdings include colour slides and historical photographic prints.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Ragusa',
    'provincia': 'RG',
    'indirizzo': 'Via Libertà 2 - 97100 Ragusa (RG)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 32250,
    'composizione_beni': [
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 12500,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 19750,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-ragusa.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Ven: 9:00-15:00 / Mar-Gio: 15:00-18:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Fri: 9:00-15:00 / Tue-Thu: 15:00-18:00<br>',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-ragusa',
    'telefono': '+39 0932 623044',
    'email': 'sopriag@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/detail/PhotographicHeritage/1900382255',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 9,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza per i Beni Culturali e Ambientali di Siracusa',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Cultural and Environmental Heritage of Siracusa',
    'categorie': [
        'stampe-fotografiche',
        'diapositive',
        'negativi-pellicola',
        'negativi-lastre'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Diapositive',
        'Negativi su pellicola',
        'Negativi su lastre di vetro'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Slides',
        'Film negatives',
        'Glass plate negatives'
    ],
    'descrizione_breve': 'Digitalizzazione dell\'archivio fotografico storico della Soprintendenza con focus sui siti archeologici della provincia.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Digitization of the Superintendency\'s historical photographic archive, with a focus on the archaeological sites of the province.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
                La <strong>Soprintendenza per i Beni Culturali e Ambientali di Siracusa</strong> conserva un patrimonio culturale estremamente ricco e variegato, che comprende beni archeologici, tra cui resti greci, romani e medievali, beni architettonici e storico-artistici, beni paesaggistici, raccolte storiche e documentarie custodite dalla sezione apposita.
            </p>
            <p style="margin-bottom: 1rem;">
                La collezione include immagini storiche delle aree archeologiche di Castello Eurialo, della Neapolis, di Akrai, di Leontinoi, di Megara Hyblaea, di Eloro, oltre che di gallerie, musei e templi.
            </p>
            <p style="margin-bottom: 1rem;">
                Il fondo fotografico comprende negativi su pellicola, diapositive a colori, stampe fotografiche storiche 
                e negativi su lastra di vetro.
            </p>
            <p>
                Il progetto di digitalizzazione permetterà di preservare questo prezioso patrimonio documentale e 
                di renderlo accessibile a studiosi, ricercatori e al grande pubblico attraverso piattaforme digitali interoperabili.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
                The <strong>Superintendency for Cultural and Environmental Heritage of Siracusa</strong> preserves an exceptionally rich and varied cultural patrimony, encompassing archaeological assets including Greek, Roman, and medieval remains, architectural and historical-artistic heritage, landscape assets, and historical and documentary collections held in a dedicated section.
            </p>
            <p style="margin-bottom: 1rem;">
                The collection includes historical images of the archaeological areas of Castello Eurialo, the Neapolis, Akrai, Leontinoi, Megara Hyblaea, and Eloro, as well as galleries, museums, and temples.
            </p>
            <p style="margin-bottom: 1rem;">
                The photographic holdings include film negatives, colour slides, historical photographic prints,
                and glass plate negatives.
            </p>
            <p>
                The digitization project will preserve this invaluable documentary heritage and
                make it accessible to scholars, researchers, and the general public through interoperable digital platforms.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Siracusa',
    'provincia': 'SR',
    'indirizzo': 'Piazza Duomo 14 - 96100 Siracusa (SR)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 806700,
    'composizione_beni': [
        {
            'nome': 'Negativi su pellicola',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Film negatives',
            'quantita': 180400,
        },
        {
            'nome': 'Diapositive',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Slides',
            'quantita': 127600,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 440000,
        },
        {
            'nome': 'Negativi su lastra di vetro',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Glass plate negatives',
            'quantita': 58700,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-siracusa.jpeg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': 'https://storymaps.arcgis.com/stories/12853e595e6e405288777605a399ed24',

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': '-',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': '',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/soprintendenza-beni-culturali-ambientali-siracusa',
    'telefono': '+39 0931 21205',
    'email': 'soprisr@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': '-',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 10,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Regionale "Pietro Griffo"',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Archaeological Museum "Pietro Griffo"',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti Archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico Regionale "Pietro Griffo" di Agrigento raccoglie le collezioni di materiali archeologici statali, civiche e diocesane.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Archaeological Museum "Pietro Griffo" of Agrigento brings together state, civic, and diocesan collections of archaeological materials.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale "Pietro Griffo" di Agrigento è uno dei più importanti scrigni della memoria storica della Sicilia antica. Nato dall'unione delle collezioni statali, civiche e diocesane, il museo offre una lettura organica e profonda dell'evoluzione di Agrigento e del suo vasto territorio, dall'età preistorica fino al mondo romano. L'edificio, progettato dall'architetto Franco Minissi, coniuga rigore moderno e rispetto per il contesto storico, dando vita a un percorso espositivo chiaro, essenziale e fortemente didattico.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo si articola in un doppio itinerario di visita. Il primo accompagna il visitatore attraverso la storia di Akrágas, una delle più potenti colonie greche del Mediterraneo, seguendone lo sviluppo urbano, religioso e funerario. Qui emergono testimonianze straordinarie: dalle prime tracce delle culture indigene e protostoriche fino ai capolavori dell'arte greca classica, come il celebre Efebo di Agrigento, il torso di guerriero in stile severo e preziosi vasi figurati che raccontano miti e rituali del mondo ellenico.
            </p>
            <p style="margin-bottom: 1rem;">
            Un ruolo centrale è occupato dai materiali provenienti dai santuari cittadini, che restituiscono l'intensità della vita religiosa agrigentina: statuette votive, busti fittili di divinità ctonie, kernoi e bracieri decorati testimoniano una devozione diffusa e profondamente radicata. Tra le opere più spettacolari spicca il colossale Telamone dell'Olympeion, ricomposto in museo, che restituisce la grandiosità di uno dei templi più imponenti della Magna Grecia.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso si arricchisce poi di sezioni dedicate alla vita quotidiana e al mondo dei morti: quartieri ellenistico-romani con affreschi e mosaici, collezioni numismatiche, epigrafi e monumentali sarcofagi greci e romani raccontano una città viva, complessa e in continua trasformazione.
            </p>
            <p style="margin-bottom: 1rem;">
            Il secondo itinerario amplia lo sguardo al territorio, seguendo un ideale viaggio archeologico attraverso le province di Agrigento, Enna e Caltanissetta. Dai villaggi preistorici alle città greche e indigene, dai santuari costieri ai centri dell'entroterra, il museo documenta il lento e affascinante processo di ellenizzazione della Sicilia, arricchito da reperti di eccezionale valore come il cratere attico con Amazzonomachia e i corredi funerari di guerrieri.
            </p>
            <p style="margin-bottom: 1rem;">
            Il Museo "Pietro Griffo" non è soltanto un luogo di conservazione, ma uno spazio di racconto e comprensione: un viaggio nel tempo che permette di cogliere l'identità profonda di Agrigento e della Sicilia antica, attraverso oggetti che continuano a parlare di uomini, dei, riti e civiltà che hanno segnato la storia del Mediterraneo.
            </p>            
    ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Archaeological Museum "Pietro Griffo" of Agrigento is one of the most important repositories of the historical memory of ancient Sicily. Born from the union of state, civic, and diocesan collections, the museum offers a comprehensive and in-depth reading of the evolution of Agrigento and its vast territory, from prehistoric times through to the Roman world. The building, designed by architect Franco Minissi, combines modern rigour with respect for the historical context, resulting in a clear, essential, and highly educational exhibition route.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum is structured around two visiting itineraries. The first guides visitors through the history of Akrágas, one of the most powerful Greek colonies in the Mediterranean, tracing its urban, religious, and funerary development. Extraordinary testimonies emerge here: from the earliest traces of indigenous and proto-historic cultures to the masterpieces of classical Greek art, such as the celebrated Ephebe of Agrigento, the warrior torso in severe style, and precious figured vases recounting the myths and rituals of the Hellenic world.
            </p>
            <p style="margin-bottom: 1rem;">
            A central role is played by materials from the city's sanctuaries, which convey the intensity of Agrigento's religious life: votive statuettes, terracotta busts of chthonic deities, kernoi, and decorated braziers bear witness to a widespread and deeply rooted devotion. Among the most spectacular works stands the colossal Telamon of the Olympeion, reassembled in the museum, which conveys the grandeur of one of the most imposing temples of Magna Graecia.
            </p>
            <p style="margin-bottom: 1rem;">
            The route is further enriched by sections dedicated to daily life and the world of the dead: Hellenistic-Roman quarters with frescoes and mosaics, numismatic collections, inscriptions, and monumental Greek and Roman sarcophagi tell the story of a vibrant, complex, and ever-changing city.
            </p>
            <p style="margin-bottom: 1rem;">
            The second itinerary broadens the perspective to the surrounding territory, following an ideal archaeological journey through the provinces of Agrigento, Enna, and Caltanissetta. From prehistoric villages to Greek and indigenous cities, from coastal sanctuaries to inland centres, the museum documents the slow and fascinating process of Hellenisation of Sicily, enriched by finds of exceptional value such as the Attic crater with Amazonomachy and the funerary assemblages of warriors.
            </p>
            <p style="margin-bottom: 1rem;">
            The "Pietro Griffo" Museum is not merely a place of conservation, but a space for storytelling and understanding: a journey through time that allows visitors to grasp the deep identity of Agrigento and ancient Sicily, through objects that continue to speak of men, gods, rituals, and civilisations that have shaped the history of the Mediterranean.
            </p>            
    ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Agrigento',
    'provincia': 'AG',
    'indirizzo': 'Contrada San Nicola - 92100 Agrigento (AG)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 2000,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 2000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-griffo.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-19:30<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-19:30<br>',
    'costo_biglietto': 'Intero: € 10.00, ridotto: € 5.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 10.00, reduced: € 5.00',
    'sito_web': 'https://www.museogriffo.it/it',
    'telefono': '+39 0922621611',
    'email': 'parcodeitempli@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 11,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Regionale di Gela',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Archaeological Museum of Gela',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti Archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico Regionale di Gela illustra la storia della città attraverso reperti ceramici, bronzei e numismatici. Il nucleo più antico è costituito dalle collezioni Navarra e Nocera.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Archaeological Museum of Gela illustrates the history of the city through ceramic, bronze, and numismatic finds. The oldest core consists of the Navarra and Nocera collections.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale di Gela rappresenta il cuore della memoria storica della città e uno dei più significativi punti di riferimento per la conoscenza della Sicilia greca. Nato per custodire e valorizzare i reperti rinvenuti nel territorio gelese e nella provincia di Caltanissetta, il museo conserva oltre quattromila testimonianze archeologiche che raccontano, in modo continuo e articolato, la lunga vicenda di Gela dall'età preistorica fino al Medioevo.
            </p>
            <p style="margin-bottom: 1rem;">
            Il complesso museale sorge in posizione strategica, accanto all'antica acropoli, quasi a stabilire un dialogo diretto tra il paesaggio archeologico e le collezioni esposte. Realizzato negli anni Cinquanta su progetto di Luigi Pasquarelli e successivamente ampliato e rinnovato da Franco Minissi, il museo è stato concepito come uno spazio moderno e funzionale, capace di accogliere le importanti scoperte emerse nel corso delle campagne di scavo e di offrire al pubblico un percorso espositivo chiaro e didatticamente efficace.
            </p>
            <p style="margin-bottom: 1rem;">
            La visita si sviluppa su due piani e segue un rigoroso ordine cronologico, accompagnando il visitatore dalle prime tracce di insediamento umano fino alla fase romana e medievale. Ampio spazio è dedicato alla Gela greca, una delle più floride colonie del Mediterraneo, documentata attraverso materiali provenienti dall'acropoli, dalla città bassa, dall'emporio di Bosco Littorio, da Capo Soprano e dalle vaste necropoli. Ceramiche, bronzi, monete e oggetti di uso quotidiano restituiscono l'immagine di una città dinamica, crocevia di scambi commerciali e culturali
            </p>
            <p style="margin-bottom: 1rem;">
            Tra i reperti di maggiore rilievo spiccano un pregevole elmo calcidese, le ricchissime collezioni di ceramica attica e corinzia a figure nere e a figure rosse, e i resti del celebre "relitto di Gela", una nave mercantile greca affondata davanti al porto cittadino, testimonianza straordinaria delle rotte e dei traffici marittimi antichi. Di grande interesse sono anche gli elementi architettonici dei templi, le arule votive dell'emporio e l'ampia collezione numismatica, che documenta i rapporti di Gela con le altre colonie greche.
            </p>
            <p style="margin-bottom: 1rem;">
            Un ruolo fondamentale è svolto dalle collezioni storiche Navarra e Nocera, nucleo originario del museo, che conservano vasi di eccezionale qualità, attribuiti ad alcuni dei più importanti ceramografi attici del V secolo a.C., tra cui il Pittore di Berlino, il Pittore di Brygos e il Pittore di Boreas. Questi manufatti elevano il museo a centro di riferimento per lo studio della ceramica greca in Sicilia.
            </p>
            <p style="margin-bottom: 1rem;">
            All'esterno, la statua del tragediografo Eschilo, che la tradizione vuole legato a Gela, accoglie il visitatore, suggellando il legame tra la città, la cultura greca e il suo patrimonio. Il Museo Archeologico Regionale di Gela non è soltanto un luogo di conservazione, ma un racconto vivo e continuo della storia di una comunità che, attraverso i secoli, ha lasciato un segno profondo nella civiltà del Mediterraneo.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Archaeological Museum of Gela stands as the heart of the city's historical memory and one of the most significant reference points for the study of Greek Sicily. Founded to preserve and promote the finds unearthed in the Gela territory and the province of Caltanissetta, the museum holds over four thousand archaeological testimonies that recount, in a continuous and articulate manner, the long history of Gela from prehistoric times through to the Middle Ages.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum complex occupies a strategic position beside the ancient acropolis, almost establishing a direct dialogue between the archaeological landscape and the displayed collections. Built in the 1950s to a design by Luigi Pasquarelli and later extended and renovated by Franco Minissi, the museum was conceived as a modern and functional space, capable of housing the important discoveries emerging from excavation campaigns and offering the public a clear and educationally effective exhibition route.
            </p>
            <p style="margin-bottom: 1rem;">
            The visit unfolds over two floors in strict chronological order, guiding the visitor from the earliest traces of human settlement through to the Roman and medieval phases. Considerable space is devoted to Greek Gela, one of the most prosperous colonies in the Mediterranean, documented through materials from the acropolis, the lower city, the emporium of Bosco Littorio, Capo Soprano, and the vast necropolises. Ceramics, bronzes, coins, and everyday objects conjure the image of a dynamic city, a crossroads of commercial and cultural exchange.
            </p>
            <p style="margin-bottom: 1rem;">
            Among the most noteworthy finds are a fine Chalcidian helmet, the extraordinarily rich collections of Attic and Corinthian black-figure and red-figure pottery, and the remains of the celebrated "Gela Wreck", a Greek merchant vessel that sank off the city's harbour — an extraordinary testament to ancient maritime routes and trade. Also of great interest are the architectural elements of the temples, the votive altars of the emporium, and the extensive numismatic collection documenting Gela's relations with other Greek colonies.
            </p>
            <p style="margin-bottom: 1rem;">
            A fundamental role is played by the historic Navarra and Nocera collections, the museum's original core, which preserve vases of exceptional quality attributed to some of the most important Attic vase-painters of the 5th century BC, including the Berlin Painter, the Brygos Painter, and the Boreas Painter. These artefacts elevate the museum to a key centre for the study of Greek ceramics in Sicily.
            </p>
            <p style="margin-bottom: 1rem;">
            Outside, a statue of the tragedian Aeschylus — whom tradition associates with Gela — welcomes the visitor, sealing the bond between the city, Greek culture, and its heritage. The Regional Archaeological Museum of Gela is not merely a place of conservation, but a living and continuous account of the history of a community that, across the centuries, has left a profound mark on Mediterranean civilisation.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Gela',
    'provincia': 'CL',
    'indirizzo': 'Corso Vittorio Emanuele 1 - 93012 Gela (CL)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 5540,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 5540,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-gela.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Sab: 9:00-19:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sat: 9:00-19:00<br>',
    'costo_biglietto': 'Intero: € 4.00, ridotto: € 2.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 4.00, reduced: € 2.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/gela/siti-archeologici/museo-archeologico-regionale-gela/',
    'telefono': '+39 0933912626',
    'email': 'parco.archeo.gela@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 12,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo di Palazzo Trigona',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Palazzo Trigona Museum',
    'categorie': [
        'dipinti',
        'beni-demoetno'
    ],
    'categorie_labels': [
        'Dipinti',
        'Beni demoetnoantropologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Paintings',
        'Ethno-anthropological heritage'
    ],
    'descrizione_breve': 'll Palazzo dei Marchesi di Trigona della Floresta e Baroni di San Cono, comunemente detto Palazzo Trigona, sorge nella piazza Cattedrale, qualificando scenograficamente lo spazio urbano della piazza che li accoglie. ',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Palace of the Marquises of Trigona della Floresta and Barons of San Cono, commonly known as Palazzo Trigona, stands on Cathedral Square, providing a scenic backdrop to the urban space it overlooks.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo di Palazzo Trigona, ospitato nello storico Palazzo dei Marchesi di Trigona della Floresta e Baroni di San Cono, rappresenta uno dei luoghi simbolo di Piazza Armerina e un punto di riferimento per la conoscenza della sua storia e del suo territorio. Affacciato su Piazza Cattedrale, il palazzo contribuisce in modo scenografico alla definizione dello spazio urbano, imponendosi come uno dei più autorevoli esempi di architettura civile del tardo barocco siciliano.
            </p>
            <p style="margin-bottom: 1rem;">
            Edificato tra la fine del XVII e la prima metà del XVIII secolo, il palazzo fu oggetto di continui interventi decorativi e ristrutturazioni protrattisi fino ai primi decenni del Novecento, segno della sua centralità nella vita sociale e politica della città. Acquisito nel 1959 dall'Amministrazione regionale dei beni culturali, l'edificio è stato destinato a sede del Museo della Città e del Territorio, trasformandosi da residenza nobiliare in spazio di narrazione e valorizzazione del patrimonio storico locale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso museale si articola sui quattro livelli del palazzo, sfruttandone pienamente la ricchezza architettonica. Al piano terra, l'ampio androne e il monumentale scalone introducono il visitatore in un ambiente che unisce rappresentanza e accoglienza, affiancato da una sala conferenze multimediale e da spazi dedicati a laboratori e attività culturali. Il piano ammezzato ospita, accanto agli uffici e alla direzione, la sezione archeologica del museo, dedicata alle testimonianze più antiche del territorio.
            </p>
            <p style="margin-bottom: 1rem;">
            Il cuore dell'esposizione si trova al primo piano, il piano nobile, dove le sale raccontano la storia di Piazza Armerina dal Medioevo fino al XX secolo. Qui, ambienti storici e contenuti museali dialogano con tecnologie innovative: tavoli interattivi touch-screen e installazioni multimediali accompagnano il visitatore in una lettura dinamica dei diversi periodi storici, mentre una suggestiva sala immersiva offre un'esperienza coinvolgente e contemporanea.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo si distingue inoltre per l'attenzione al rapporto tra città e territorio. Attraverso strumenti digitali e un'applicazione dedicata per smartphone, il visitatore può esplorare percorsi tematici che approfondiscono la storia, i protagonisti e le tradizioni culturali di Piazza Armerina, con particolare riferimento alla Villa Romana del Casale, sito UNESCO e simbolo assoluto del patrimonio archeologico locale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il Museo di Palazzo Trigona si configura così come un luogo in cui architettura, storia e innovazione si intrecciano, offrendo un racconto unitario e coinvolgente dell'identità di Piazza Armerina e del suo straordinario patrimonio culturale.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Palazzo Trigona Museum, housed in the historic Palace of the Marquises of Trigona della Floresta and Barons of San Cono, is one of the landmark venues of Piazza Armerina and a key point of reference for understanding its history and territory. Overlooking Cathedral Square, the palace makes a dramatic contribution to the urban landscape, standing as one of the most authoritative examples of late Baroque civic architecture in Sicily.
            </p>
            <p style="margin-bottom: 1rem;">
            Built between the late 17th and the first half of the 18th century, the palace underwent continuous decorative interventions and renovations well into the early decades of the twentieth century, reflecting its central role in the social and political life of the city. Acquired in 1959 by the Regional Cultural Heritage Administration, the building was designated as the seat of the Museum of the City and Territory, transforming from a noble residence into a space for the narration and promotion of local historical heritage.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum route unfolds across the palace's four levels, making full use of its architectural richness. On the ground floor, the wide entrance hall and monumental staircase welcome visitors into a space that combines formal grandeur with hospitality, flanked by a multimedia conference room and spaces dedicated to workshops and cultural activities. The mezzanine floor houses, alongside the offices and management, the museum's archaeological section, dedicated to the earliest testimonies of the territory.
            </p>
            <p style="margin-bottom: 1rem;">
            The heart of the exhibition is found on the first floor, the piano nobile, where the rooms recount the history of Piazza Armerina from the Middle Ages to the twentieth century. Here, historic interiors and museum content engage in dialogue with innovative technologies: interactive touch-screen tables and multimedia installations guide the visitor through a dynamic reading of the various historical periods, while an evocative immersive room offers an engaging and contemporary experience.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum also stands out for its attention to the relationship between the city and its surrounding territory. Through digital tools and a dedicated smartphone application, visitors can explore thematic routes that delve into the history, key figures, and cultural traditions of Piazza Armerina, with particular reference to the Villa Romana del Casale, a UNESCO World Heritage Site and the foremost symbol of the local archaeological heritage.
            </p>
            <p style="margin-bottom: 1rem;">
            The Palazzo Trigona Museum thus emerges as a place where architecture, history, and innovation intertwine, offering a unified and engaging account of the identity of Piazza Armerina and its extraordinary cultural heritage.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Piazza Armerina',
    'provincia': 'EN',
    'indirizzo': 'Piazza Cattedrale 20 - 94015 Piazza Armerine (EN)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 114,
    'composizione_beni': [
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 4,
        },
        {
            'nome': 'Beni demoetnoantropologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Ethno-anthropological heritage',
            'quantita': 110,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-trigona.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-18:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-18:00<br>',
    'costo_biglietto': 'Intero: € 7.00, ridotto: € 3.50',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 7.00, reduced: € 3.50',
    'sito_web': 'https://www.villaromanadelcasale.it/museo-della-citta-e-del-territorio-di-piazza-armerina-palazzo-trigona/',
    'telefono': '+39 0935 687667',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 13,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Regionale di Centuripe',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Archaeological Museum of Centuripe',
    'categorie': [
        'sculture',
        'reperti-archeologici',
        'beni-demoetnoantropologici'
    ],
    'categorie_labels': [
        'Sculture',
        'Reperti Archeologici',
        'Beni demoetnoantropologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Sculptures',
        'Archaeological finds',
        'Ethno-anthropological heritage'
    ],
    'descrizione_breve': 'Il Museo Archeologico Regionale di Centuripe  espone la maggior collezione di reperti archeologici della romanità della Sicilia ',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Archaeological Museum of Centuripe houses the largest collection of Roman-era archaeological finds in Sicily.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale di Centuripe è uno dei luoghi più significativi per la conoscenza della romanità nella Sicilia interna e racconta, in modo intenso e articolato, la storia millenaria di una città che fu crocevia di culture, potere e sperimentazione artistica. Situato in posizione panoramica, nei pressi del tempio degli Augustali e delle principali aree archeologiche, il museo dialoga costantemente con il paesaggio e con i resti monumentali dell'antica Centuripe, affacciandosi sulla valle del Simeto e sull'Etna.
            </p>
            <p style="margin-bottom: 1rem;">
            La nascita del museo è legata alle scoperte archeologiche dei primi decenni del Novecento, quando il Comune iniziò a raccogliere i reperti provenienti dagli scavi e dalle collezioni locali, dando vita a un primo museo civico. Dopo un lungo e complesso percorso progettuale, culminato nell'intervento dell'architetto Franco Minissi, la sede attuale è stata inaugurata nel 2000 e, dopo una fase di chiusura, ha riaperto nel 2024 con un allestimento completamente rinnovato, più ampio e contemporaneo, capace di valorizzare un patrimonio di circa 3.000 reperti
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo ripercorre la storia di Centuripe dalle frequentazioni preistoriche fino alla distruzione della città in età tardoantica. Le prime sezioni raccontano un territorio abitato ininterrottamente fin dal V millennio a.C., favorito dalla presenza di corsi d'acqua e da una posizione strategica. Le pitture rupestri del Riparo Cassataro, con figure umane e animali legate a rituali arcaici, costituiscono una testimonianza rara e suggestiva delle fasi più antiche dell'insediamento.
            </p>
            <p style="margin-bottom: 1rem;">
            Ampio spazio è dedicato alla fase sicula e al processo di ellenizzazione, documentato da ceramiche, iscrizioni e produzioni locali. Tra queste spiccano le celebri terrecotte centuripine, che per qualità e raffinatezza hanno valso alla città l'appellativo di "Tanagra di Sicilia": statuette femminili dai panneggi eleganti, maschere teatrali enigmatiche e figure ispirate al mito e alla vita quotidiana restituiscono l'immagine di una produzione artistica originale e di altissimo livello. Accanto ad esse, i vasi centuripini, decorati con rilievi e pitture policrome post-cottura, raccontano rituali dionisiaci, il mondo femminile e il legame con la sfera funeraria.
            </p>
            <p style="margin-bottom: 1rem;">
            Il momento di massimo splendore di Centuripe coincide con l'età romana, ampiamente rappresentata nel museo. Dopo l'alleanza con Roma, la città conobbe una straordinaria crescita urbanistica e demografica, testimoniata da sculture monumentali, iscrizioni e architetture pubbliche. Il fulcro dell'esposizione è il complesso legato all'Augusteum, con ritratti della famiglia imperiale, una raffinata statua di Musa, una colossale testa di Adriano e il celebre torso loricato attribuibile ad Augusto. Particolarmente significativa è la presenza dei columbaria, rara tipologia funeraria in Sicilia, qui documentata in modo eccezionale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo non elude i temi più complessi della tutela del patrimonio: una sezione è dedicata agli scavi clandestini, ai falsi archeologici e alla dispersione dei reperti, fenomeni che hanno segnato profondamente la storia di Centuripe. In questo contesto si inseriscono anche racconti emblematici, come quello dell'epigrafe usata per schiacciare le olive, oggi preziosa testimonianza di un antico legame diplomatico con Roma e Lanuvio.
            </p>
            <p style="margin-bottom: 1rem;">
            Articolato su più livelli, il Museo Archeologico Regionale di Centuripe unisce rigore scientifico e capacità narrativa, offrendo al visitatore un viaggio immersivo nella storia di una città che seppe trasformarsi, reinventarsi e lasciare un'impronta duratura nella cultura della Sicilia antica.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Archaeological Museum of Centuripe is one of the most significant places for understanding Roman-era Sicily, recounting in vivid and articulate terms the millennial history of a city that was a crossroads of cultures, power, and artistic experimentation. Set in a panoramic position near the temple of the Augustales and the main archaeological areas, the museum engages in constant dialogue with the landscape and the monumental remains of ancient Centuripe, overlooking the Simeto valley and Mount Etna.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum's origins are linked to the archaeological discoveries of the early twentieth century, when the municipality began collecting finds from excavations and local collections, establishing a first civic museum. After a long and complex design process, culminating in the involvement of architect Franco Minissi, the current premises were inaugurated in 2000 and, following a period of closure, reopened in 2024 with a completely renewed, larger, and more contemporary layout, capable of showcasing a heritage of approximately 3,000 finds.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition route traces the history of Centuripe from its prehistoric occupation through to the city's destruction in late antiquity. The opening sections recount a territory inhabited continuously since the 5th millennium BC, favoured by the presence of waterways and a strategic position. The rock paintings of the Riparo Cassataro shelter, featuring human and animal figures connected to archaic rituals, constitute a rare and evocative testimony of the earliest phases of settlement.
            </p>
            <p style="margin-bottom: 1rem;">
            Considerable space is devoted to the Sicel phase and the process of Hellenisation, documented through ceramics, inscriptions, and local productions. Among these stand out the celebrated Centuripan terracottas, which by virtue of their quality and refinement earned the city the epithet "Tanagra of Sicily": female statuettes with elegant drapery, enigmatic theatrical masks, and figures inspired by myth and everyday life convey the image of an original and exceptionally high-level artistic production. Alongside them, the Centuripan vases, decorated with reliefs and polychrome post-firing paintings, recount Dionysian rituals, the feminine world, and the bond with the funerary sphere.
            </p>
            <p style="margin-bottom: 1rem;">
            Centuripe's period of greatest splendour coincides with the Roman era, extensively represented in the museum. Following its alliance with Rome, the city experienced extraordinary urban and demographic growth, attested by monumental sculptures, inscriptions, and public architecture. The focal point of the exhibition is the complex associated with the Augusteum, featuring portraits of the imperial family, a refined statue of a Muse, a colossal head of Hadrian, and the celebrated cuirassed torso attributable to Augustus. Particularly significant is the presence of the columbaria, a rare funerary typology in Sicily, exceptionally documented here.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum does not shy away from the more complex issues of heritage protection: one section is dedicated to clandestine excavations, archaeological forgeries, and the dispersal of finds — phenomena that have profoundly marked the history of Centuripe. In this context, emblematic stories also emerge, such as that of the inscription used to press olives, today a precious testimony of an ancient diplomatic bond with Rome and Lanuvium.
            </p>
            <p style="margin-bottom: 1rem;">
            Arranged across multiple levels, the Regional Archaeological Museum of Centuripe combines scientific rigour with narrative skill, offering the visitor an immersive journey through the history of a city that knew how to transform itself, reinvent itself, and leave a lasting mark on the culture of ancient Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Centuripe',
    'provincia': 'EN',
    'indirizzo': 'Via Giulio Cesare 1 - 94014 Centuripe (EN)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 3030,
    'composizione_beni': [
        {
            'nome': 'Reperti Archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 2000,
        },
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 30,
        },
        {
            'nome': 'Beni demoetnoantropologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Ethno-anthropological heritage',
            'quantita': 1000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-centuripe.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Ven: 9:00-13:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Fri: 9:00-13:00<br>',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/catania-valle-aci/biglietti/museo-regionale-di-centuripe/',
    'telefono': '+39 093573079',
    'email': 'parco.archeo.catania@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 14,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico di Aidone',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Archaeological Museum of Aidone',
    'categorie': [
        'beni-demoetno'
    ],
    'categorie_labels': [
        'Beni demoetnoantropologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Ethno-anthropological heritage'
    ],
    'descrizione_breve': 'Il Museo Archeologico di Aidone è ospitato nel convento dei Cappuccini annesso all\'omonima chiesa; è stato inaugurato nell\'estate del 1984 e custodisce i reperti di oltre trent\'anni di scavi a Morgantina.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Archaeological Museum of Aidone is housed in the Capuchin convent adjoining the church of the same name; inaugurated in the summer of 1984, it preserves the finds from over thirty years of excavations at Morgantina.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico di Aidone è uno dei luoghi più suggestivi e simbolici della Sicilia interna, custode della memoria dell'antica Morgantina e delle sue straordinarie vicende storiche, religiose e artistiche. Ospitato nel convento dei Cappuccini, annesso alla chiesa omonima, il museo unisce il fascino dell'architettura monastica alla forza evocativa dei reperti archeologici, offrendo un percorso di visita intimo e al tempo stesso di grande valore scientifico.
            </p>
            <p style="margin-bottom: 1rem;">
            Inaugurato nel 1984, il museo raccoglie e valorizza oltre trent'anni di scavi condotti nel sito di Morgantina, uno dei più importanti centri dell'antica Sicilia. L'allestimento segue un criterio cronologico e tematico che accompagna il visitatore dalle fasi più antiche dell'insediamento umano fino alla distruzione della città nel 211 a.C., restituendo un'immagine completa e stratificata della vita nel cuore dell'isola.
            </p>
            <p style="margin-bottom: 1rem;">
            Le prime sale documentano la preistoria e la protostoria, con materiali provenienti dal villaggio castellucciano: strumenti in pietra levigata, fuseruoli, ceramiche modellate a mano con decorazioni essenziali raccontano una comunità legata ai ritmi della natura e alle attività domestiche. Alla fase sicula della prima età del ferro appartengono invece le ceramiche acrome carenate, che testimoniano contatti culturali con altre realtà mediterranee, come Lipari.
            </p>
            <p style="margin-bottom: 1rem;">
            Il periodo compreso tra il IX e la metà del V secolo a.C. rivela la convivenza e l'incontro tra mondo siculo e greco. Antefisse architettoniche, pithoi decorati, arule domestiche, kernoi e il monumentale cratere di Eutimide, con scene di simposio e amazzonomachia, raccontano una società in trasformazione, in cui ritualità, banchetto e identità civica assumono un ruolo centrale.
            </p>
            <p style="margin-bottom: 1rem;">
            Le sezioni dedicate all'età classica ed ellenistica sono fortemente legate al culto di Demetra e Kore, divinità profondamente venerate a Morgantina. Terrecotte votive, busti di Persefone, lucerne e vasellame raffinato provenienti dai santuari urbani e dalle necropoli restituiscono la dimensione religiosa e simbolica della città. Particolarmente significativa è la statua acefala in pietra calcarea rinvenuta nel santuario centrale, che ha contribuito a dimostrare l'origine morgantina della celebre Dea di Morgantina.
            </p>
            <p style="margin-bottom: 1rem;">
            Uno spazio specifico è riservato ai reperti delle Terme Nord di contrada Agnese, attribuite alla sfera cultuale di Afrodite o Cibele, note per l'ingegnosa struttura architettonica con volte realizzate tramite tubuli fittili, tradizionalmente collegata alla figura di Archimede.
            </p>
            <p style="margin-bottom: 1rem;">
            Nell'ex sacrestia del convento, gli oggetti della vita quotidiana come utensili domestici, stoviglie, attrezzi agricoli, giochi e ornamenti personali, offrono uno spaccato vivido dell'esistenza degli abitanti di Morgantina, avvicinando il visitatore alla dimensione più umana e concreta del passato.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo è diventato negli ultimi decenni anche un potente simbolo di giustizia culturale e tutela del patrimonio. Il rientro degli acroliti di Demetra e Kore, del prezioso tesoro argenteo di Eupolemo e, soprattutto, della celebre Dea di Morgantina, restituita dal Paul Getty Museum nel 2011, ha segnato una pagina storica nella lotta contro il traffico illecito di beni archeologici. Oggi la Dea, alta oltre due metri e realizzata con raffinata tecnica acrolitica, domina il percorso museale come emblema dell'identità sacra e artistica della città antica.
            </p>
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico di Aidone non è soltanto un luogo di esposizione, ma uno spazio di memoria, restituzione e consapevolezza, dove la storia di Morgantina torna a essere patrimonio condiviso e vivo della comunità e dei visitatori.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Archaeological Museum of Aidone is one of the most evocative and symbolic places in inland Sicily, guardian of the memory of ancient Morgantina and its extraordinary historical, religious, and artistic legacy. Housed in the Capuchin convent adjoining the church of the same name, the museum combines the charm of monastic architecture with the evocative power of archaeological finds, offering a visit that is both intimate and of great scientific significance.
            </p>
            <p style="margin-bottom: 1rem;">
            Inaugurated in 1984, the museum collects and showcases over thirty years of excavations conducted at the site of Morgantina, one of the most important centres of ancient Sicily. The layout follows a chronological and thematic approach, guiding the visitor from the earliest phases of human settlement through to the destruction of the city in 211 BC, presenting a complete and layered picture of life at the heart of the island.
            </p>
            <p style="margin-bottom: 1rem;">
            The opening rooms document prehistory and protohistory, with materials from the Castelluccian village: polished stone tools, spindle whorls, and hand-modelled ceramics with simple decorations speak of a community attuned to the rhythms of nature and domestic activities. Belonging to the Sicel phase of the early Iron Age are the undecorated carinated ceramics, attesting to cultural contacts with other Mediterranean realities such as Lipari.
            </p>
            <p style="margin-bottom: 1rem;">
            The period between the 9th and the mid-5th century BC reveals the coexistence and encounter between the Sicel and Greek worlds. Architectural antefixes, decorated pithoi, domestic altars, kernoi, and the monumental crater by Euthymides — depicting scenes of symposium and Amazonomachy — recount a society in transformation, in which ritual, banqueting, and civic identity assumed a central role.
            </p>
            <p style="margin-bottom: 1rem;">
            The sections dedicated to the Classical and Hellenistic periods are closely linked to the cult of Demeter and Kore, deities deeply venerated at Morgantina. Votive terracottas, busts of Persephone, oil lamps, and refined tableware from the urban sanctuaries and necropolises convey the religious and symbolic dimension of the city. Particularly significant is the headless limestone statue found in the central sanctuary, which helped to establish the Morgantina origin of the celebrated Goddess of Morgantina.
            </p>
            <p style="margin-bottom: 1rem;">
            A dedicated space is reserved for finds from the North Baths of contrada Agnese, attributed to the cultic sphere of Aphrodite or Cybele, and renowned for their ingenious architectural structure featuring vaults built using clay tubes — a technique traditionally linked to the figure of Archimedes.
            </p>
            <p style="margin-bottom: 1rem;">
            In the former sacristy of the convent, everyday objects such as domestic utensils, tableware, agricultural tools, games, and personal ornaments offer a vivid glimpse into the daily existence of Morgantina's inhabitants, bringing the visitor closer to the most human and tangible dimension of the past.
            </p>
            <p style="margin-bottom: 1rem;">
            In recent decades the museum has also become a powerful symbol of cultural justice and heritage protection. The return of the acrolithic statues of Demeter and Kore, the precious silver treasure of Eupolemos, and above all the celebrated Goddess of Morgantina — repatriated from the J. Paul Getty Museum in 2011 — marked a historic moment in the fight against the illicit trafficking of archaeological objects. Today the Goddess, standing over two metres tall and crafted using refined acrolithic technique, dominates the museum route as an emblem of the sacred and artistic identity of the ancient city.
            </p>
            <p style="margin-bottom: 1rem;">
            The Archaeological Museum of Aidone is not merely a place of exhibition, but a space of memory, restitution, and awareness, where the history of Morgantina once again becomes the shared and living heritage of the community and its visitors.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Aidone',
    'provincia': 'EN',
    'indirizzo': 'Largo Torres Truppia 1 - 94010 Aidone (EN)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 2518,
    'composizione_beni': [
        {
            'nome': 'Beni demoetnoantropologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Ethno-anthropological heritage',
            'quantita': 2518,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-aidone.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-18:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-18:00<br>',
    'costo_biglietto': 'Intero: € 8.00 ridotto: € 4.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 8.00, reduced: € 4.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/morgantina-villa-romana-casale/biglietti/museo-archeologico-di-aidone/',
    'telefono': '+39 0935687667',
    'email': ' parco.archeo.villacasale@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 15,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico di Palazzo Varisano',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Archaeological Museum of Palazzo Varisano',
    'categorie': [
        'beni-demoetno'
    ],
    'categorie_labels': [
        'Beni demoetnoantropologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Ethno-anthropological heritage'
    ],
    'descrizione_breve': 'Il Museo Archeologico di Palazzo Varisano illustra le fasi di età preistorica, classica e medievale dei siti archeologici nella provincia di Enna, ad esclusione dei territori di Centuripe, Aidone e Piazza Armerina.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Archaeological Museum of Palazzo Varisano illustrates the prehistoric, classical, and medieval phases of the archaeological sites in the province of Enna, excluding the territories of Centuripe, Aidone, and Piazza Armerina.',
    'descrizione_completa': ''' 
            <p style="margin-bottom: 1rem;">
            Il Museo di Palazzo Varisano, sede del Museo Archeologico Regionale di Enna, rappresenta il principale punto di riferimento per la conoscenza della storia antica del territorio ennese. Istituito dalla Regione Siciliana negli ultimi decenni del Novecento, il museo nasce con l'obiettivo di raccogliere ed esporre i materiali provenienti dalle importanti campagne di scavo condotte dalla Soprintendenza ai Beni Culturali di Enna, in particolare a partire dal 1979, che hanno profondamente arricchito il quadro archeologico della Sicilia centrale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo è ospitato nello storico Palazzo Varisano, elegante edificio di impianto barocco che si affaccia direttamente sul Duomo di Enna, nel cuore del centro storico. La facciata scenografica e la posizione dominante rendono il palazzo un luogo simbolico, in cui l'architettura storica dialoga con i reperti esposti, creando un legame diretto tra la città attuale e il suo passato più remoto.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo è concepito come un viaggio attraverso gli insediamenti umani che, nel corso dei millenni, hanno occupato le alture dell'ennese. Particolare attenzione è rivolta ai siti dell'Età del Bronzo e dell'Età del Ferro, documentati soprattutto attraverso le necropoli, che permettono di ricostruire le strutture sociali, le credenze e i rituali delle comunità antiche. Emblematica è la sezione dedicata a Calascibetta, dove i corredi funerari restituiscono l'immagine di centri abitati fortificati, dei quali le sepolture rappresentano spesso l'unica testimonianza archeologica.
            </p>
            <p style="margin-bottom: 1rem;">
            Un ruolo centrale nel museo è occupato dal culto di Demetra e Kore, profondamente radicato nella storia di Enna. Iscrizioni, terrecotte votive e materiali provenienti anche da collezioni private attestano la continuità e l'importanza di questa tradizione religiosa dall'età classica all'ellenismo e fino all'epoca imperiale romana, come dimostra l'iscrizione funeraria di una sacerdotessa di Cerere, che sottolinea il prestigio e la sacralità del culto cittadino.
            </p>
            <p style="margin-bottom: 1rem;">
            L'allestimento si estende poi ai numerosi siti del territorio provinciale, offrendo una visione d'insieme dei processi di trasformazione avvenuti in età greca, quando le comunità indigene dell'entroterra entrarono progressivamente in contatto con le colonie della costa. L'insediamento siculo ellenizzato di Cozzo Matrice, nei pressi del lago di Pergusa, con le sue aree sacre arcaiche, rappresenta un esempio significativo di questo incontro culturale. I ricchi corredi funerari di Rossomanno, Agira, Assoro, Cerami e Pietraperzia, con monili metallici di tradizione locale, ceramiche greche e oggetti di provenienza orientale, raccontano una società complessa e stratificata, aperta a influenze esterne e a nuove forme di identità.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso si conclude con materiali di età medievale provenienti dall'area del castello e da altri contesti cittadini, che documentano la continuità dell'insediamento e l'evoluzione storica di Enna nel tempo. Il Museo di Palazzo Varisano si configura così come uno spazio di sintesi e approfondimento, capace di restituire la storia profonda della Sicilia centrale attraverso un racconto coerente e fortemente legato al territorio.
            </p> 
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Palazzo Varisano Museum, home of the Regional Archaeological Museum of Enna, is the principal point of reference for understanding the ancient history of the Enna territory. Established by the Sicilian Region in the final decades of the twentieth century, the museum was created with the aim of collecting and displaying materials from the important excavation campaigns conducted by the Superintendency for Cultural Heritage of Enna — particularly from 1979 onwards — which have profoundly enriched the archaeological picture of central Sicily.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum is housed in the historic Palazzo Varisano, an elegant Baroque building that looks directly onto the Cathedral of Enna, in the heart of the historic centre. The dramatic façade and commanding position make the palace a symbolic venue, in which historic architecture engages in dialogue with the exhibited finds, forging a direct link between the city of today and its most distant past.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition route is conceived as a journey through the human settlements that, over the millennia, occupied the heights of the Enna area. Particular attention is devoted to the Bronze Age and Iron Age sites, documented primarily through the necropolises, which allow the social structures, beliefs, and rituals of ancient communities to be reconstructed. Emblematic is the section dedicated to Calascibetta, where the funerary assemblages evoke the image of fortified inhabited centres, of which the burials are often the only surviving archaeological evidence.
            </p>
            <p style="margin-bottom: 1rem;">
            A central role in the museum is played by the cult of Demeter and Kore, deeply rooted in the history of Enna. Inscriptions, votive terracottas, and materials from private collections alike attest to the continuity and importance of this religious tradition from the Classical period through Hellenism and into the Roman Imperial era, as demonstrated by the funerary inscription of a priestess of Ceres, which underscores the prestige and sanctity of the civic cult.
            </p>
            <p style="margin-bottom: 1rem;">
            The layout extends to the numerous sites of the provincial territory, offering an overview of the processes of transformation that took place in the Greek period, when indigenous inland communities progressively came into contact with the coastal colonies. The Hellenised Sicel settlement of Cozzo Matrice, near Lake Pergusa, with its archaic sacred areas, represents a significant example of this cultural encounter. The rich funerary assemblages from Rossomanno, Agira, Assoro, Cerami, and Pietraperzia — featuring metal ornaments of local tradition, Greek ceramics, and objects of eastern origin — speak of a complex and stratified society, open to external influences and new forms of identity.
            </p>
            <p style="margin-bottom: 1rem;">
            The route concludes with medieval materials from the castle area and other urban contexts, documenting the continuity of settlement and the historical evolution of Enna over time. The Palazzo Varisano Museum thus emerges as a space of synthesis and in-depth study, capable of conveying the deep history of central Sicily through a coherent narrative strongly rooted in the territory.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Enna',
    'provincia': 'EN',
    'indirizzo': 'Piazza G. Mazzini - 94100 Enna (EN)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 1688,
    'composizione_beni': [
        {
            'nome': 'Beni demoetnoantropologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Ethno-anthropological heritage',
            'quantita': 1688,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/palazzo-varisano.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-19:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-19:00<br>',
    'costo_biglietto': 'Intero: € 4.00 ridotto: € 2.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 4.00, reduced: € 2.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/morgantina-villa-romana-casale/biglietti/museo-interdisciplinare-di-enna/',
    'telefono': '+39 09355076319',
    'email': 'parco.archeo.villacasale@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 16,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Eoliano "Luigi Bernabò Brea"',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Aeolian Archaeological Museum "Luigi Bernabò Brea"',
    'categorie': [
        'disegni-grafici-mappe',
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Disegni, grafici, mappe',
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Drawings, graphics, maps',
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico Eoliano "Luigi Bernabò Brea" è ubicato nel complesso del Castello che domina l\'isola di Lipari ed è intitolato a Luigi Bernabò Brea, grande archeologo e Soprintendente della Sicilia Orientale.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Aeolian Archaeological Museum "Luigi Bernabò Brea" is located within the Castle complex that dominates the island of Lipari, and is named after Luigi Bernabò Brea, distinguished archaeologist and Superintendent of Eastern Sicily.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale Eoliano "Luigi Bernabò Brea" è uno dei complessi museali più importanti del Mediterraneo per la conoscenza della preistoria e della storia antica delle isole Eolie. Sorge all'interno del maestoso Castello di Lipari, che domina l'isola dall'alto e racchiude, in un unico straordinario contesto, archeologia, architettura religiosa e paesaggio. Intitolato a Luigi Bernabò Brea, archeologo e soprintendente della Sicilia orientale per oltre trent'anni, il museo rappresenta il risultato scientifico e culturale delle sistematiche campagne di scavo condotte, a partire dal secondo dopoguerra, dallo stesso Bernabò Brea e da Madeleine Cavalier.
            </p>
            <p style="margin-bottom: 1rem;">
            Inaugurato nel 1954, il museo si articola in oltre quaranta sale distribuite nei diversi edifici del complesso fortificato, offrendo un percorso espositivo ampio e articolato che accompagna il visitatore dalla preistoria fino all'età medievale, con aperture tematiche sulla geologia, la vulcanologia e la paleontologia delle isole. L'allestimento è concepito in stretta relazione con il territorio, rendendo immediatamente comprensibile il legame tra i reperti, i luoghi di rinvenimento e l'evoluzione dell'ambiente naturale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il cuore del museo è la sezione preistorica, una delle più complete d'Europa, che documenta in modo continuo la storia degli insediamenti umani nelle Eolie dal Neolitico all'età del Ferro. Attraverso ceramiche, strumenti in ossidiana, manufatti e strutture ricostruite, si ripercorrono le principali culture che si sono succedute sull'isola: da Stentinello a Diana, da Capo Graziano alla cultura del Milazzese e alle fasi ausonie. Tra i reperti più celebri spicca la Tazza di Filo Braccio, straordinaria testimonianza dell'età del Bronzo, considerata uno dei più antichi esempi di rappresentazione figurata della preistoria italiana, carica di significati simbolici e ancora oggetto di interpretazioni.
            </p>
            <p style="margin-bottom: 1rem;">
            La sezione di archeologia classica racconta invece la storia della polis di Lipari in età greca e romana attraverso corredi funerari, ceramiche dipinte, sculture, monete e testimonianze della vita quotidiana. Di particolare rilievo sono le sale dedicate alle necropoli, con sarcofagi, cippi, steli e vasi cinerari, che illustrano l'evoluzione dei rituali funerari e del culto dei defunti. Accanto a queste, la sezione di archeologia subacquea espone materiali provenienti da relitti e naufragi, restituendo l'immagine di un arcipelago profondamente legato alla navigazione e ai traffici marittimi.
            </p>
            <p style="margin-bottom: 1rem;">
            Completano il percorso la sezione epigrafica, con un'eccezionale raccolta di iscrizioni greche e romane, quella dedicata alle isole minori, Panarea, Filicudi, Salina, che amplia lo sguardo all'intero arcipelago, e le sezioni vulcanologica e paleontologica, fondamentali per comprendere l'origine geologica delle Eolie e il loro continuo mutamento nel tempo.
            </p>
            <p style="margin-bottom: 1rem;">
            Il Museo "Luigi Bernabò Brea" non è soltanto un luogo di conservazione, ma un vero centro di studio e divulgazione, arricchito da una biblioteca specialistica, spazi per mostre e convegni, sezioni didattiche e sedi distaccate sulle altre isole. È un museo in cui la storia dell'uomo e quella della natura si intrecciano profondamente, offrendo al visitatore un'esperienza unica, capace di raccontare le Eolie come un laboratorio privilegiato della civiltà mediterranea.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Aeolian Archaeological Museum "Luigi Bernabò Brea" is one of the most important museum complexes in the Mediterranean for the study of the prehistory and ancient history of the Aeolian Islands. It stands within the majestic Castle of Lipari, which dominates the island from above and brings together, in a single extraordinary setting, archaeology, religious architecture, and landscape. Named after Luigi Bernabò Brea, archaeologist and superintendent of eastern Sicily for over thirty years, the museum embodies the scientific and cultural outcome of the systematic excavation campaigns conducted from the post-war period onwards by Bernabò Brea himself and by Madeleine Cavalier.
            </p>
            <p style="margin-bottom: 1rem;">
            Inaugurated in 1954, the museum spans over forty rooms distributed across the various buildings of the fortified complex, offering a broad and articulate exhibition route that guides the visitor from prehistory through to the medieval period, with thematic digressions into the geology, volcanology, and palaeontology of the islands. The layout is conceived in close relation to the territory, making immediately comprehensible the link between the finds, their places of discovery, and the evolution of the natural environment.
            </p>
            <p style="margin-bottom: 1rem;">
            The heart of the museum is the prehistoric section — one of the most complete in Europe — which documents in continuous fashion the history of human settlements in the Aeolian Islands from the Neolithic to the Iron Age. Through ceramics, obsidian tools, artefacts, and reconstructed structures, the principal cultures that succeeded one another on the island are traced: from Stentinello to Diana, from Capo Graziano to the Milazzese culture and the Ausonian phases. Among the most celebrated finds stands the Cup of Filo Braccio, an extraordinary Bronze Age testimony considered one of the earliest examples of figurative representation in Italian prehistory, laden with symbolic meanings and still the subject of scholarly debate.
            </p>
            <p style="margin-bottom: 1rem;">
            The classical archaeology section recounts the history of the polis of Lipari in the Greek and Roman periods through funerary assemblages, painted ceramics, sculptures, coins, and testimonies of daily life. Of particular significance are the rooms dedicated to the necropolises, featuring sarcophagi, boundary stones, stelae, and cinerary urns, which illustrate the evolution of funerary rituals and the cult of the dead. Alongside these, the underwater archaeology section displays materials from shipwrecks and sunken vessels, evoking the image of an archipelago profoundly connected to navigation and maritime trade.
            </p>
            <p style="margin-bottom: 1rem;">
            Completing the route are the epigraphic section, with an exceptional collection of Greek and Roman inscriptions; the section dedicated to the minor islands — Panarea, Filicudi, Salina — which broadens the perspective to the entire archipelago; and the volcanological and palaeontological sections, essential for understanding the geological origins of the Aeolian Islands and their continuous transformation over time.
            </p>
            <p style="margin-bottom: 1rem;">
            The "Luigi Bernabò Brea" Museum is not merely a place of conservation, but a true centre of study and dissemination, enriched by a specialist library, spaces for exhibitions and conferences, educational sections, and branch locations on the other islands. It is a museum in which the history of mankind and that of nature are profoundly intertwined, offering the visitor a unique experience, capable of presenting the Aeolian Islands as a privileged laboratory of Mediterranean civilisation.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Lipari',
    'provincia': 'ME',
    'indirizzo': 'Via Castello 2 - 98050 Lipari (ME)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 8000,
    'composizione_beni': [
        {
            'nome': 'Disegni, grafici, mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics, maps',
            'quantita': 3000,
        },
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 5000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-brea.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Sab: 9:00-19:30<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sat: 9:00-19:30<br>',
    'costo_biglietto': 'Intero: € 8.00, ridotto: € 4.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 8.00, reduced: € 4.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/isole-eolie/biglietti/museo-luigi-bernabo-brea-lipari/',
    'telefono': '+39 0909880174',
    'email': ' parco.archeo.eolie@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 17,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Regionale di Messina',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Museum of Messina',
    'categorie': [
        'disegni-grafici-mappe',
        'reperti-archeologici',
        'dipinti',
        'sculture',
        'beni-demoetno'
    ],
    'categorie_labels': [
        'Disegni, grafici, mappe',
        'Reperti archeologici',
        'Dipinti',
        'Sculture',
        'Beni demoetnoantropologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Drawings, graphics, maps',
        'Archaeological finds',
        'Paintings',
        'Sculptures',
        'Ethno-anthropological heritage'
    ],
    'descrizione_breve': 'Ubicato in una ex filanda di fine ottocento adeguata a fini espositivi, il Museo Regionale di Messina illustra l\'arte figurativa messinese dal XII al XVIII secolo.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Housed in a late nineteenth-century former silk mill adapted for exhibition purposes, the Regional Museum of Messina illustrates the figurative art of Messina from the 12th to the 18th century.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Regionale Interdisciplinare di Messina, intitolato a Maria Accascina, è molto più di un contenitore di opere d'arte: è il luogo in cui la memoria della città, segnata da distruzioni, rinascite e continui mutamenti, trova una forma unitaria e leggibile. Situato oggi in un moderno complesso museale inaugurato definitivamente nel 2017, il museo sorge nell'area di San Salvatore dei Greci, uno spazio simbolico che raccoglie le tracce materiali della Messina scomparsa dopo il terremoto del 1908.
            </p>
            <p style="margin-bottom: 1rem;">
            Le sue origini risalgono al Museo Civico Peloritano, fondato nel 1806 con un intento fortemente conservativo: sottrarre il patrimonio artistico locale alla dispersione e alle spoliazioni. Fin dall'inizio, il museo si caratterizza per una vocazione enciclopedica e documentaria, alimentata da collezioni private, donazioni pubbliche e dall'incameramento dei beni ecclesiastici successivo alle soppressioni ottocentesche. Questa natura stratificata, anziché essere un limite, diventa nel tempo il tratto distintivo dell'istituzione: il museo non racconta solo i capolavori, ma restituisce l'intero tessuto culturale della città e del suo territorio.
            </p>
            <p style="margin-bottom: 1rem;">
            La storia del Museo Regionale di Messina è indissolubilmente legata alle tragedie che hanno colpito la città. Il sisma del 1908 distrusse la sede storica e provocò la perdita irreparabile di molte opere; quelle salvate divennero frammenti di una città non più esistente. Da quel momento, il museo assume anche il ruolo di luogo della ricostruzione simbolica, accogliendo portali, sculture, tarsie marmoree e decorazioni architettoniche recuperate dalle macerie, trasformandole in testimonianza viva di una Messina monumentale ormai scomparsa.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo, articolato in ampie sale luminose, accompagna il visitatore attraverso l'arte figurativa messinese dal XII al XVIII secolo, secondo un criterio cronologico che privilegia il dialogo tra pittura, scultura e arti decorative. Qui convivono grandi nomi della storia dell'arte e produzioni locali, opere eccellenti e manufatti cosiddetti "minori", restituiti a pari dignità storica. Questa scelta museografica riflette una visione moderna: l'arte non come selezione di capolavori isolati, ma come espressione complessa di una cultura, di un gusto e di una società.
            </p>
            <p style="margin-bottom: 1rem;">
            Tra le opere più celebri spiccano i capolavori di Antonello da Messina, figura centrale del Rinascimento mediterraneo, le intense tele di Michelangelo Merisi da Caravaggio, la Resurrezione di Lazzaro e l'Adorazione dei pastori e le opere di Mattia Preti, Mario Minniti e dei protagonisti della scuola messinese tra Cinque e Seicento. Accanto a questi, la scultura rinascimentale e manierista, con Montorsoli e Laurana, dialoga con una straordinaria raccolta di marmi, intarsi policromi e tarsie "a mischio", che raccontano l'originalità decorativa delle chiese cittadine prima del terremoto.
            </p>
            <p style="margin-bottom: 1rem;">
            Un ruolo fondamentale è svolto anche dalle collezioni di arti applicate: oreficerie sacre, tessuti ricamati, argenti, maioliche e arredi lignei, che testimoniano l'eccellenza delle maestranze locali e il ruolo di Messina come crocevia culturale del Mediterraneo. In questo senso, il museo si configura come una narrazione continua tra arte, artigianato e architettura, capace di restituire la complessità della storia urbana.
            </p>
            <p style="margin-bottom: 1rem;">
            Oggi il Museo Regionale di Messina non è soltanto uno spazio espositivo, ma un centro di ricerca, conservazione e divulgazione, aperto al dialogo con la città e alle attività educative.
            </p>        
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Interdisciplinary Museum of Messina, dedicated to Maria Accascina, is far more than a container of artworks: it is the place where the memory of the city — marked by destruction, rebirth, and continuous change — finds a unified and legible form. Housed today in a modern museum complex definitively inaugurated in 2017, the museum stands in the area of San Salvatore dei Greci, a symbolic space that gathers the material traces of the Messina that disappeared after the earthquake of 1908.
            </p>
            <p style="margin-bottom: 1rem;">
            Its origins date back to the Museo Civico Peloritano, founded in 1806 with a strongly conservational intent: to rescue the local artistic heritage from dispersal and spoliation. From the outset, the museum was characterised by an encyclopaedic and documentary vocation, nourished by private collections, public donations, and the absorption of ecclesiastical assets following the nineteenth-century suppressions. This layered nature, rather than being a limitation, became over time the defining trait of the institution: the museum does not merely recount masterpieces, but restores the entire cultural fabric of the city and its territory.
            </p>
            <p style="margin-bottom: 1rem;">
            The history of the Regional Museum of Messina is inextricably linked to the tragedies that have struck the city. The 1908 earthquake destroyed the historic premises and caused the irreparable loss of many works; those that were saved became fragments of a city that no longer existed. From that moment, the museum also assumed the role of a place of symbolic reconstruction, welcoming portals, sculptures, marble inlays, and architectural decorations recovered from the rubble, transforming them into living testimony of a monumental Messina now lost.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition route, arranged across spacious, light-filled rooms, guides the visitor through the figurative art of Messina from the 12th to the 18th century, following a chronological approach that favours dialogue between painting, sculpture, and the decorative arts. Here, great names of art history coexist with local productions, outstanding works alongside so-called "minor" artefacts, all restored to equal historical standing. This museographic choice reflects a modern vision: art not as a selection of isolated masterpieces, but as the complex expression of a culture, a taste, and a society.
            </p>
            <p style="margin-bottom: 1rem;">
            Among the most celebrated works stand the masterpieces of Antonello da Messina, a central figure of the Mediterranean Renaissance; the intense canvases of Michelangelo Merisi da Caravaggio, the Raising of Lazarus and the Adoration of the Shepherds; and works by Mattia Preti, Mario Minniti, and the leading figures of the Messina school between the sixteenth and seventeenth centuries. Alongside these, Renaissance and Mannerist sculpture — with Montorsoli and Laurana — engages in dialogue with an extraordinary collection of marbles, polychrome inlays, and mixed-stone inlay work, which speak of the decorative originality of the city's churches before the earthquake.
            </p>
            <p style="margin-bottom: 1rem;">
            A fundamental role is also played by the applied arts collections: sacred goldwork, embroidered textiles, silverware, majolica, and wooden furnishings, which attest to the excellence of local craftsmen and Messina's role as a cultural crossroads of the Mediterranean. In this sense, the museum emerges as a continuous narrative between art, craft, and architecture, capable of conveying the complexity of the city's urban history.
            </p>
            <p style="margin-bottom: 1rem;">
            Today the Regional Museum of Messina is not merely an exhibition space, but a centre of research, conservation, and dissemination, open to dialogue with the city and to educational activities.
            </p>        
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Messina',
    'provincia': 'ME',
    'indirizzo': 'Viale della Libertà 465 - 98121 Messina (ME)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 7263,
    'composizione_beni': [
        {
            'nome': 'Disegni, grafici, mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics, maps',
            'quantita': 496,
        },
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 500,
        },
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 5123,
        },
        {
            'nome': 'Beni demoetnoantropologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Ethno-anthropological heritage',
            'quantita': 284,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 860,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-messina.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Sab: 9:00-19:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sat: 9:00-19:00<br>',
    'costo_biglietto': 'Intero: € 9,00, ridotto: € 4,50',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 9.00, reduced: € 4.50',
    'sito_web': 'https://www2.regione.sicilia.it/beniculturali/MuMe/index2.html',
    'telefono': '+39 090361292',
    'email': 'museo.messina@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 18,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico di Naxos',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Archaeological Museum of Naxos',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti Archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico di Naxos illustra la storia della colonia greca di Naxos, prendendo al contempo in esame le evidenze preistoriche attestanti l\'ininterrotta continuità di vita nel sito.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Archaeological Museum of Naxos illustrates the history of the Greek colony of Naxos, while also examining the prehistoric evidence attesting to the uninterrupted continuity of life on the site.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico di Naxos sorge sul suggestivo Capo Schisò, in un rapporto diretto e inscindibile con l'area dell'antica città: non è solo un luogo di esposizione, ma la vera porta d'ingresso al primo insediamento greco di Sicilia. Un tratto dell'antico muro di cinta attraversa il giardino del museo, mentre proprio da qui prende avvio il percorso di visita all'area archeologica, che segue l'antica viabilità urbana lungo la platea B, restituendo al visitatore la percezione concreta dello spazio della polis.
            </p>
            <p style="margin-bottom: 1rem;">
            Le collezioni del museo sono costituite quasi interamente dai materiali provenienti da oltre mezzo secolo di scavi sistematici nel sito di Naxos. A questi si affianca un nucleo selezionato di reperti legati all'attività di Paolo Orsi, tra cui i celebri corredi delle sepolture di Cocolonazzo di Mola, databili alla seconda metà dell'VIII secolo a.C.: testimonianze fondamentali dell'incontro e della convivenza tra coloni greci e popolazioni sicule. Di grande rilievo è anche l'Arula con sfingi affrontate, ricomposta grazie a un paziente lavoro di ricerca che ha riunito frammenti conservati in sedi diverse, restituendo un raro esempio di coroplastica naxiota della fine del VI secolo a.C.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo segue un criterio cronologico e topografico, con particolare attenzione a specifiche classi di materiali che raccontano l'identità culturale della città. Spiccano le lastre di rivestimento architettonico e le antefisse con maschera silenica, tra le produzioni più caratteristiche di Naxos: una serie continua che, dagli ultimi decenni del VI fino a tutto il V secolo a.C., documenta la centralità del culto di Dioniso, divinità simbolo della città, presente anche nella sua monetazione più antica.
            </p>
            <p style="margin-bottom: 1rem;">
            Le sale introduttive sono dedicate alla preistoria del sito e alle fasi iniziali della colonia greca. La coppa di Stentinello, rinvenuta nelle immediate vicinanze, testimonia la presenza umana sul Capo Schisò già in età neolitica. Seguono i materiali della fondazione e dello sviluppo arcaico, con un'ampia documentazione di ceramiche di importazione corinzia ed euboica e delle loro imitazioni locali, che illustrano i primi intensi scambi commerciali e culturali del Mediterraneo orientale.
            </p>
            <p style="margin-bottom: 1rem;">
            Al piano superiore, le collezioni si articolano tra i reperti provenienti dalle aree sacre e quelli della città arcaica e classica, inclusi i materiali delle necropoli del V e III secolo a.C. Un monetiere, in corso di allestimento, raccoglie preziosi esemplari di monete d'argento di diverse zecche siciliane e di Reggio, rinvenuti nel quartiere settentrionale della città.
            </p>
            <p style="margin-bottom: 1rem;">
            Una sezione a sé è dedicata ai ritrovamenti subacquei, ospitati nel vicino torrione cinquecentesco: qui è esposto un ricco repertorio di ancore in pietra e ceppi d'ancora in piombo, recuperati prevalentemente nelle acque della baia di Naxos e Taormina, che raccontano la vocazione marittima e commerciale della città.
            </p>
            <p style="margin-bottom: 1rem;">
            Nel suo insieme, il Museo Archeologico di Naxos offre una narrazione coerente e profonda delle origini, dello sviluppo e del ruolo della prima colonia greca di Sicilia, fondendo in un unico racconto il dato archeologico, il paesaggio e la memoria storica del luogo.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Archaeological Museum of Naxos stands on the evocative Capo Schisò, in a direct and inseparable relationship with the area of the ancient city: it is not merely a place of exhibition, but the true gateway to the first Greek settlement in Sicily. A stretch of the ancient city wall crosses the museum garden, while the visit to the archaeological area begins here, following the ancient urban road network along platea B, giving the visitor a concrete sense of the space of the polis.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum's collections consist almost entirely of materials from over half a century of systematic excavations at the site of Naxos. These are complemented by a selected group of finds connected to the work of Paolo Orsi, including the celebrated funerary assemblages from the burials of Cocolonazzo di Mola, datable to the second half of the 8th century BC: fundamental testimonies of the encounter and coexistence between Greek colonists and Sicel populations. Of great significance is also the Arula with confronted sphinxes, reassembled through painstaking research that reunited fragments held in different institutions, restoring a rare example of Naxian coroplastic art from the late 6th century BC.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition route follows a chronological and topographical approach, with particular attention to specific classes of materials that speak of the city's cultural identity. Outstanding among these are the architectural revetment plaques and antefixes with silenic masks, among the most characteristic productions of Naxos: a continuous series spanning from the final decades of the 6th through the entire 5th century BC, documenting the centrality of the cult of Dionysus — the city's symbolic deity — also present in its earliest coinage.
            </p>
            <p style="margin-bottom: 1rem;">
            The introductory rooms are dedicated to the prehistory of the site and the initial phases of the Greek colony. The Stentinello bowl, found in the immediate vicinity, attests to human presence on Capo Schisò as early as the Neolithic period. These are followed by materials from the foundation and archaic development of the colony, with extensive documentation of Corinthian and Euboean imported ceramics and their local imitations, illustrating the earliest intense commercial and cultural exchanges of the eastern Mediterranean.
            </p>
            <p style="margin-bottom: 1rem;">
            On the upper floor, the collections span finds from the sacred areas alongside those from the archaic and classical city, including materials from the necropolises of the 5th and 3rd centuries BC. A coin cabinet, currently being arranged, brings together precious silver coin specimens from various Sicilian mints and from Reggio, found in the northern quarter of the city.
            </p>
            <p style="margin-bottom: 1rem;">
            A separate section is dedicated to underwater finds, housed in the nearby sixteenth-century tower: here a rich repertoire of stone anchors and lead anchor stocks is displayed, recovered primarily from the waters of the bay of Naxos and Taormina, speaking of the maritime and commercial vocation of the city.
            </p>
            <p style="margin-bottom: 1rem;">
            Taken as a whole, the Archaeological Museum of Naxos offers a coherent and in-depth account of the origins, development, and role of the first Greek colony in Sicily, fusing in a single narrative the archaeological evidence, the landscape, and the historical memory of the place.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Giardini Naxos',
    'provincia': 'ME',
    'indirizzo': 'Via Schisò - 98034 Giardini Naxos (ME)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 1091,
    'composizione_beni': [
        {
            'nome': 'Reperti Archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 1091,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-archeologico-naxos.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-19:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-19:00<br>',
    'costo_biglietto': 'Intero € 6.00, ridotto € 3.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 6.00, reduced: € 3.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/naxos-taormina/siti-archeologici/museo-archeologico-di-naxos/',
    'telefono': '+39 094251001',
    'email': 'parco.archeo.naxos@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 19,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Antiquarium di Tindari',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Antiquarium of Tindari',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti Archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'L\'Antiquarium del parco archeologico di Tindari è articolato in cinque sale, raccoglie una selezione di reperti frutto delle innumerevoli campagne di scavo condotte, databili dall\'età preistorica a quella romana.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Antiquarium of the Tindari archaeological park is arranged across five rooms and houses a selection of finds from the countless excavation campaigns conducted at the site, ranging in date from the prehistoric to the Roman period.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            L'Antiquarium di Tindari è il luogo in cui la lunga e complessa storia dell'antica Tyndaris prende forma attraverso reperti, immagini e testimonianze materiali, offrendo al visitatore una chiave di lettura essenziale per comprendere l'area archeologica che lo circonda. Inserito all'interno del parco archeologico, l'edificio funge da naturale introduzione alla visita del sito, raccogliendo e ordinando le evidenze emerse dagli scavi condotti nel corso del tempo.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo si sviluppa in cinque sale e accompagna il visitatore dalle fasi più antiche di frequentazione del promontorio fino all'età romana imperiale. I materiali della prima Età del Bronzo raccontano un insediamento preistorico vitale, legato alla facies culturale di Rodì-Tindari-Vallelunga, con ceramiche d'uso quotidiano, impasti modellati a mano e reperti che testimoniano i contatti con le popolazioni delle Eolie. Questi oggetti restituiscono uno spaccato della vita domestica e delle relazioni culturali di una comunità che abitava il territorio molti secoli prima della fondazione greca.
            </p>
            <p style="margin-bottom: 1rem;">
            Le sale successive illustrano lo sviluppo della città in età ellenistica e romana, quando Tindari divenne un importante centro urbano e strategico della costa tirrenica siciliana. Iscrizioni greche e latine, cippi funerari, epigrafi onorarie e materiali architettonici documentano l'organizzazione civica, religiosa e sociale della città. Tra i reperti più significativi spiccano statue frammentarie, teste imperiali, elementi decorativi e una monumentale maschera teatrale in marmo, che richiamano il ruolo centrale degli edifici pubblici, del teatro e del ginnasio nella vita cittadina.
            </p>
            <p style="margin-bottom: 1rem;">
            Un'attenzione particolare è riservata alla dimensione quotidiana: ceramiche, suppellettili, terrecotte figurate, monete e frammenti di intonaci dipinti permettono di ricostruire aspetti della vita domestica, del culto e delle attività economiche. Il plastico del teatro ellenistico, insieme ai pannelli esplicativi, aiuta a visualizzare l'aspetto originario dei monumenti oggi visibili nell'area archeologica.
            </p>
            <p style="margin-bottom: 1rem;">
            Nel suo insieme, l'Antiquarium di Tindari non è solo una raccolta di reperti, ma un racconto coerente che intreccia preistoria, mondo greco e civiltà romana, restituendo l'immagine di una città definita "nobilissima" già in antico. È uno spazio di sintesi e approfondimento che consente di cogliere il valore storico e culturale di Tindari prima di immergersi tra le sue rovine affacciate sul mare.
            </p>   
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Antiquarium of Tindari is the place where the long and complex history of ancient Tyndaris takes shape through finds, images, and material testimonies, offering the visitor an essential key to understanding the surrounding archaeological area. Set within the archaeological park, the building serves as a natural introduction to the visit of the site, collecting and ordering the evidence that has emerged from excavations carried out over time.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition route unfolds across five rooms and guides the visitor from the earliest phases of occupation of the promontory through to the Roman Imperial period. Materials from the Early Bronze Age speak of a thriving prehistoric settlement linked to the cultural facies of Rodì-Tindari-Vallelunga, with everyday ceramics, hand-modelled wares, and finds attesting to contacts with the populations of the Aeolian Islands. These objects provide a glimpse of the domestic life and cultural relations of a community that inhabited the territory many centuries before the Greek foundation.
            </p>
            <p style="margin-bottom: 1rem;">
            The following rooms illustrate the development of the city in the Hellenistic and Roman periods, when Tindari became an important urban and strategic centre on the Tyrrhenian coast of Sicily. Greek and Latin inscriptions, funerary boundary stones, honorary epigraphs, and architectural materials document the civic, religious, and social organisation of the city. Among the most significant finds stand fragmentary statues, imperial heads, decorative elements, and a monumental marble theatrical mask, all recalling the central role of public buildings, the theatre, and the gymnasium in city life.
            </p>
            <p style="margin-bottom: 1rem;">
            Particular attention is devoted to the everyday dimension: ceramics, household objects, figured terracottas, coins, and fragments of painted plaster allow aspects of domestic life, religious practice, and economic activity to be reconstructed. The scale model of the Hellenistic theatre, together with explanatory panels, helps to visualise the original appearance of the monuments still visible in the archaeological area today.
            </p>
            <p style="margin-bottom: 1rem;">
            Taken as a whole, the Antiquarium of Tindari is not merely a collection of finds, but a coherent narrative that interweaves prehistory, the Greek world, and Roman civilisation, restoring the image of a city described as "nobilissima" even in antiquity. It is a space of synthesis and in-depth study that allows the visitor to grasp the historical and cultural value of Tindari before venturing among its ruins overlooking the sea.
            </p>   
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Patti',
    'provincia': 'ME',
    'indirizzo': 'Via Monsignor Pullano 54 - 98066 Patti Marina (ME)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 2500,
    'composizione_beni': [
        {
            'nome': 'Reperti Archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 2500,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/antiquarium-di-tindari.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lunedì e Festivi: 9:00-13:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Monday and Public Holidays: 9:00-13:00<br>',
    'costo_biglietto': 'Intero € 7.00, ridotto € 3.50',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 7.00, reduced: € 3.50',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/parco-archeologico-di-tindari/',
    'telefono': '+39 3315771469',
    'email': 'parco.archeo.tindari@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 20,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Galleria Regionale di Palazzo Abatellis',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Gallery of Palazzo Abatellis',
    'categorie': [
        'disegni-grafici-mappe',
        'sculture'
    ],
    'categorie_labels': [
        'Disegni, grafici, mappe',
        'Sculture'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Drawings, graphics, maps',
        'Sculptures'
    ],
    'descrizione_breve': 'Palazzo Abatellis è sede dal 1954 della Galleria Regionale della Sicilia che espone una delle maggiori raccolte d\'arte d\'Italia e testimonia lo sviluppo della cultura figurativa in Sicilia dal XII al XVII.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'Palazzo Abatellis has been home to the Regional Gallery of Sicily since 1954, displaying one of the most important art collections in Italy and documenting the development of figurative culture in Sicily from the 12th to the 17th century.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Palazzo Abatellis è uno dei luoghi più emblematici di Palermo, dove architettura, storia e arte si fondono in un racconto di straordinaria intensità. Situato in via Alloro, nel cuore dell'antico quartiere della Kalsa, il palazzo rappresenta uno degli esempi meglio conservati di architettura gotico-catalana in Sicilia ed è oggi sede della Galleria Regionale della Sicilia, una delle più importanti raccolte d'arte del Paese.
            </p>
            <p style="margin-bottom: 1rem;">
            Edificato nel 1495 per volontà di Francesco Abatellis, maestro portolano del Regno, il palazzo fu progettato dall'architetto Matteo Carnilivari e concepito come residenza nobiliare di grande prestigio. Dopo la morte del suo fondatore, l'edificio attraversò una lunga fase di trasformazione: secondo le disposizioni testamentarie, divenne monastero femminile, subendo adattamenti strutturali che ne modificarono parzialmente l'aspetto originario. Questa stratificazione di funzioni e usi è parte integrante del suo fascino, poiché riflette le complesse vicende storiche della città.
            </p>
            <p style="margin-bottom: 1rem;">
            Gravemente danneggiato dai bombardamenti del 1943, Palazzo Abatellis fu restaurato nel secondo dopoguerra e destinato a museo. Nel 1954 aprì al pubblico la Galleria Regionale della Sicilia, con un allestimento affidato a Carlo Scarpa, considerato uno dei massimi capolavori della museografia del Novecento. Il dialogo raffinato tra architettura storica e soluzioni moderne rende ancora oggi l'esperienza di visita unica e profondamente suggestiva.
            </p>
            <p style="margin-bottom: 1rem;">
            L'edificio si articola attorno a un cortile interno con un elegante loggiato a due ordini, torri angolari merlate e un solenne portale d'ingresso decorato con gli stemmi della famiglia Abatellis. Le sale espositive accolgono un percorso cronologico che documenta lo sviluppo dell'arte in Sicilia dal XII al XVII secolo, attraverso sculture, dipinti, affreschi e opere decorative di altissimo livello.
            </p>
            <p style="margin-bottom: 1rem;">
            Tra i capolavori più celebri custoditi nel palazzo spiccano l'"Annunciata" di Antonello da Messina, autentica icona del Rinascimento italiano, e il monumentale affresco del "Trionfo della Morte", esposto in uno spazio di forte impatto emotivo. Accanto a questi, opere di Francesco Laurana, Antonello e Domenico Gagini, Pietro Novelli, Antoon van Dyck, Mattia Preti e Luca Giordano testimoniano la ricchezza e la complessità della cultura figurativa siciliana, aperta al dialogo con le grandi correnti artistiche europee.
            </p>
            <p style="margin-bottom: 1rem;">
            Palazzo Abatellis non è soltanto un museo, ma un luogo simbolo in cui si intrecciano la memoria storica di Palermo, l'eccellenza dell'arte e una concezione moderna dell'allestimento museale. È uno spazio in cui il passato continua a parlare con forza al presente, offrendo al visitatore un'esperienza culturale di altissimo valore.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            Palazzo Abatellis is one of the most emblematic places in Palermo, where architecture, history, and art merge into a narrative of extraordinary intensity. Located in Via Alloro, in the heart of the ancient Kalsa quarter, the palace represents one of the best-preserved examples of Gothic-Catalan architecture in Sicily and is today home to the Regional Gallery of Sicily, one of the most important art collections in the country.
            </p>
            <p style="margin-bottom: 1rem;">
            Built in 1495 at the behest of Francesco Abatellis, master portulanus of the Kingdom, the palace was designed by architect Matteo Carnilivari and conceived as a prestigious noble residence. After the death of its founder, the building underwent a long phase of transformation: in accordance with his testamentary wishes, it became a female monastery, undergoing structural adaptations that partially altered its original appearance. This layering of functions and uses is an integral part of its charm, as it reflects the complex historical vicissitudes of the city.
            </p>
            <p style="margin-bottom: 1rem;">
            Severely damaged by the bombings of 1943, Palazzo Abatellis was restored in the post-war period and designated as a museum. In 1954 the Regional Gallery of Sicily opened to the public, with an installation entrusted to Carlo Scarpa, considered one of the greatest masterpieces of twentieth-century museography. The refined dialogue between historic architecture and modern solutions continues to make the visiting experience unique and deeply evocative.
            </p>
            <p style="margin-bottom: 1rem;">
            The building is arranged around an internal courtyard featuring an elegant two-tiered loggia, crenellated corner towers, and a solemn entrance portal decorated with the Abatellis family coat of arms. The exhibition rooms house a chronological route documenting the development of art in Sicily from the 12th to the 17th century, through sculptures, paintings, frescoes, and decorative works of the highest quality.
            </p>
            <p style="margin-bottom: 1rem;">
            Among the most celebrated masterpieces housed in the palace stand the "Annunciata" by Antonello da Messina, a true icon of the Italian Renaissance, and the monumental fresco of the "Triumph of Death", displayed in a space of powerful emotional impact. Alongside these, works by Francesco Laurana, Antonello and Domenico Gagini, Pietro Novelli, Antoon van Dyck, Mattia Preti, and Luca Giordano attest to the richness and complexity of Sicilian figurative culture, open to dialogue with the great European artistic currents.
            </p>
            <p style="margin-bottom: 1rem;">
            Palazzo Abatellis is not merely a museum, but a symbolic place in which the historical memory of Palermo, artistic excellence, and a modern conception of museum display are interwoven. It is a space where the past continues to speak powerfully to the present, offering the visitor a cultural experience of the highest order.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Palermo',
    'provincia': 'PA',
    'indirizzo': 'Via Alloro 4 - 90135 Palermo (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 15740,
    'composizione_beni': [
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 10655,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 5085,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/abatellis.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-19:00<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-19:00<br>',
    'costo_biglietto': 'Intero: € 8.00, ridotto: € 4.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 8.00, reduced: € 4.00',
    'sito_web': 'https://www2.regione.sicilia.it/beniculturali/palazzoabatellis/home.htm',
    'telefono': '+39 091 6230011',
    'email': 'urp.gall.abatellis@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 21,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Castello Beccadelli Bologna',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Beccadelli Bologna Castle',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti Archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Castello Beccadelli Bologna, costruito nella metà del XVI secolo, si erge accanto ad una gola scoscesa a Marineo.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Beccadelli Bologna Castle, built in the mid-16th century, rises beside a steep gorge in Marineo.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Castello Beccadelli Bologna domina il centro storico di Marineo come simbolo del potere feudale e della lunga continuità storica della Valle dell'Eleuterio. Edificato nella seconda metà del XVI secolo dalla famiglia Bologna, il castello nacque come residenza signorile, in un momento cruciale per la formazione dell'attuale abitato. Fu infatti Francesco Beccadelli Bologna, investito del feudo di Marineo dall'imperatore Carlo V, a promuovere nel 1552 la fondazione del nuovo centro urbano, dando impulso alla costruzione delle prime abitazioni e dotando il territorio di un'imponente dimora nobiliare.
            </p>
            <p style="margin-bottom: 1rem;">
            La struttura del castello si sviluppa su più livelli, adattandosi con equilibrio alla morfologia del terreno. Il piano terra era destinato alle attività produttive e di servizio, con magazzini e ambienti per la conservazione e la lavorazione dei prodotti agricoli, mentre il piano nobile accoglieva ampie sale di rappresentanza, alcune delle quali conservano ancora tracce delle originarie decorazioni. Sul prospetto rivolto verso la piazza spicca lo stemma dei Beccadelli, emblema della famiglia che segnò profondamente la storia politica ed economica del territorio.
            </p>
            <p style="margin-bottom: 1rem;">
            Dal 2003 il castello ha assunto una nuova funzione culturale, diventando sede del Museo Regionale della Valle dell'Eleuterio. Gli ambienti storici ospitano oggi materiali provenienti da recenti indagini archeologiche, offrendo una lettura approfondita delle fasi più antiche di popolamento dell'area. Tra i reperti più significativi si distinguono due elmi arcaici di tipo calcidese del VI secolo a.C., testimonianze rare e di grande valore del mondo guerriero antico.
            </p>
            <p style="margin-bottom: 1rem;">
            Particolarmente eccezionale è il deposito votivo rinvenuto nei pressi della cortina muraria sul versante sud-orientale dell'abitato, databile alla fine del VI secolo a.C. Il complesso comprende schinieri ed elmi in bronzo, oggetti in ferro interpretati come finimenti per cavalli o supporti rituali, un piccolo scudo votivo e una brocca con coperchio contenente resti di ovicaprini, oltre a un pendente in bronzo a forma di accetta e a una raffinata placchetta d'avorio raffigurante un ariete accovacciato. L'insieme restituisce un quadro vivido delle pratiche cultuali e delle credenze delle comunità indigene in età arcaica.
            </p>
            <p style="margin-bottom: 1rem;">
            Dopo una fase meno documentata in età classica, il territorio conosce una forte ripresa a partire dalla metà del IV secolo a.C., durante il processo di ellenizzazione che interessò gran parte della Sicilia interna. A questo periodo risale un importante fase edilizia, caratterizzata da un complesso architettonico monumentale con un edificio pubblico di funzione non ancora definita e una grande cisterna. Gli ambienti si articolano su terrazze digradanti lungo il pendio naturale della collina, collegate da due scalinate parallele che conferiscono all'insieme un forte impatto scenografico.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Beccadelli Bologna Castle dominates the historic centre of Marineo as a symbol of feudal power and the long historical continuity of the Eleuterio Valley. Built in the second half of the 16th century by the Bologna family, the castle was conceived as a noble residence at a crucial moment in the formation of the present-day settlement. It was Francesco Beccadelli Bologna, invested with the fief of Marineo by Emperor Charles V, who in 1552 promoted the foundation of the new urban centre, driving the construction of the first dwellings and endowing the territory with an imposing noble residence.
            </p>
            <p style="margin-bottom: 1rem;">
            The castle's structure develops across multiple levels, adapting harmoniously to the morphology of the terrain. The ground floor was devoted to productive and service activities, with storerooms and spaces for the preservation and processing of agricultural produce, while the piano nobile housed large reception halls, some of which still retain traces of their original decorations. On the façade facing the square, the Beccadelli coat of arms stands out, emblem of the family that profoundly marked the political and economic history of the territory.
            </p>
            <p style="margin-bottom: 1rem;">
            Since 2003 the castle has taken on a new cultural function, becoming the seat of the Regional Museum of the Eleuterio Valley. The historic rooms now house materials from recent archaeological investigations, offering an in-depth reading of the earliest phases of settlement in the area. Among the most significant finds are two archaic Chalcidian-type helmets from the 6th century BC, rare and highly valuable testimonies of the ancient warrior world.
            </p>
            <p style="margin-bottom: 1rem;">
            Particularly exceptional is the votive deposit discovered near the curtain wall on the south-eastern slope of the settlement, datable to the late 6th century BC. The assemblage includes bronze greaves and helmets, iron objects interpreted as horse trappings or ritual supports, a small votive shield, and a covered jug containing the remains of ovicaprines, alongside a bronze axe-shaped pendant and a refined ivory plaque depicting a crouching ram. Taken together, these objects provide a vivid picture of the cultic practices and beliefs of the indigenous communities in the archaic period.
            </p>
            <p style="margin-bottom: 1rem;">
            After a less well-documented phase in the classical period, the territory experiences a strong revival from the mid-4th century BC onwards, during the process of Hellenisation that affected much of inland Sicily. To this period belongs an important building phase, characterised by a monumental architectural complex including a public building of as yet undefined function and a large cistern. The spaces are arranged on terraces descending along the natural slope of the hill, connected by two parallel stairways that give the whole a striking scenic impact.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Marineo',
    'provincia': 'PA',
    'indirizzo': 'Piazza Castello - 90035 Marineo (Pa)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 150,
    'composizione_beni': [
        {
            'nome': 'Reperti Archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 150,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/castello-beccadelli.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Gio-Ven-Dom: 9:30-13:30<br>Mer-Sab: 9:30-18:30<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Thu-Fri-Sun: 9:30-13:30<br>Wed-Sat: 9:30-18:30<br>',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.regione.sicilia.it/',
    'telefono': '+39 0916116807',
    'email': 'poloarcheologico.pa@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 22,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Area archeologica e Antiquarium di Himera',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Archaeological Area and Antiquarium of Himera',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti Archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'L\'area archeologica di Himera conserva i resti dell\'antica colonia greca, con resti di santuari, necropoli e strutture urbane che raccontano la storia della città. Accanto agli scavi si trova l\'Antiquarium Pirro Marconi, dove sono esposti i principali reperti rinvenuti durante le campagne di scavo, offrendo un quadro sintetico della vita e della cultura degli antichi abitanti del sito.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The archaeological area of Himera preserves the remains of the ancient Greek colony, including sanctuaries, necropolises, and urban structures that recount the city\'s history. Adjacent to the excavations stands the Antiquarium Pirro Marconi, where the principal finds from the excavation campaigns are displayed, offering a concise picture of the life and culture of the site\'s ancient inhabitants.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            L'area archeologica di Himera rappresenta una delle testimonianze più significative della presenza greca sulla costa settentrionale della Sicilia e racconta la storia intensa e drammatica di una polis che, pur avendo avuto una vita relativamente breve, svolse un ruolo di primo piano nel Mediterraneo antico. Fondata nel 648 a.C. da coloni di origine mista calcidese e dorica provenienti da Zankle, dalla Grecia e da un gruppo di esuli siracusani noti come Myletiadi, Himera nacque come crocevia culturale e politico, guidata dai fondatori Euclide, Simo e Sacone.
            </p>
            <p style="margin-bottom: 1rem;">
            Grazie a una posizione strategica tra mare ed entroterra, la città conobbe un rapido sviluppo urbano e demografico già dalla prima metà del VI secolo a.C., come attestano i vasti impianti urbanistici e le architetture monumentali. Le fonti ricordano rapporti complessi con le popolazioni indigene sicane dell'interno, conflitti che portarono gli Imeresi a cercare l'appoggio di Falaride, tiranno di Agrigento. La storia della città raggiunse uno dei suoi momenti più celebri nel 480 a.C., quando sotto le sue mura si combatté una delle battaglie più decisive della storia siciliana: la vittoria della coalizione greca sui Cartaginesi consacrò Himera come simbolo dell'identità ellenica dell'isola.
            </p>
            <p style="margin-bottom: 1rem;">
            Negli anni successivi la città entrò nell'orbita politica di Terone di Agrigento, che ne promosse il ripopolamento con genti di stirpe dorica. Tornata presto indipendente, Himera visse un periodo di relativa stabilità fino al tragico epilogo del 409 a.C., quando fu conquistata e distrutta dai Cartaginesi in un atto di violenza che pose definitivamente fine alla sua esistenza. I sopravvissuti contribuirono poco dopo alla fondazione di Thermai Himeraiai, l'odierna Termini Imerese, nei pressi delle sorgenti termali non lontane dall'antico sito. Tra i personaggi più illustri legati alla città spiccano il poeta lirico Stesicoro e numerosi atleti vincitori ai giochi olimpici, a testimonianza del prestigio culturale di Himera.
            </p>
            <p style="margin-bottom: 1rem;">
            L'interesse archeologico per il sito si sviluppò a partire dal XVI secolo, ma le prime indagini sistematiche risalgono agli anni tra il 1926 e il 1930, con gli scavi della necropoli orientale e del monumentale Tempio della Vittoria, condotti da Pirro Marconi. Dal 1963 le ricerche si sono intensificate soprattutto nell'area della città alta, comprendente l'abitato e il santuario di Athena. Oggi queste zone, insieme al Tempio della Vittoria, sono visitabili e permettono di cogliere in modo diretto l'organizzazione urbanistica, le architetture sacre e la vita quotidiana di una colonia greca di età arcaica e classica.
            </p>
            <p style="margin-bottom: 1rem;">
            Le indagini più recenti hanno ampliato la conoscenza del sito con la scoperta, nel Piano del Tamburino, di nuove aree sacre e spazi dedicati al culto, confermando la complessità del paesaggio religioso imerese. Particolare rilievo hanno inoltre gli scavi delle necropoli, in particolare quella occidentale, dove sono state riportate alla luce oltre 13.000 sepolture, comprese alcune fosse comuni destinate ai caduti delle battaglie del 480 e del 409 a.C. L'area archeologica di Himera si presenta oggi come un luogo di memoria potente, in cui il visitatore può ripercorrere le fasi di nascita, splendore e distruzione di una delle città più emblematiche della Sicilia greca.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The archaeological area of Himera represents one of the most significant testimonies of the Greek presence on the northern coast of Sicily, recounting the intense and dramatic history of a polis that, despite its relatively brief existence, played a leading role in the ancient Mediterranean. Founded in 648 BC by colonists of mixed Chalcidian and Doric origin from Zankle, from Greece, and from a group of Syracusan exiles known as the Myletidai, Himera was born as a cultural and political crossroads, led by the founders Euclid, Simos, and Sacon.
            </p>
            <p style="margin-bottom: 1rem;">
            Thanks to a strategic position between the sea and the hinterland, the city experienced rapid urban and demographic growth as early as the first half of the 6th century BC, as attested by its extensive urban planning and monumental architecture. The sources record complex relations with the indigenous Sican populations of the interior, conflicts that led the people of Himera to seek the support of Phalaris, tyrant of Agrigento. The city's history reached one of its most celebrated moments in 480 BC, when one of the most decisive battles in Sicilian history was fought beneath its walls: the victory of the Greek coalition over the Carthaginians consecrated Himera as a symbol of the Hellenic identity of the island.
            </p>
            <p style="margin-bottom: 1rem;">
            In the years that followed, the city entered the political orbit of Theron of Agrigento, who promoted its repopulation with people of Doric stock. Soon regaining its independence, Himera experienced a period of relative stability until the tragic epilogue of 409 BC, when it was conquered and destroyed by the Carthaginians in an act of violence that permanently ended its existence. The survivors contributed shortly afterwards to the foundation of Thermai Himeraiai, present-day Termini Imerese, near the thermal springs not far from the ancient site. Among the most illustrious figures associated with the city stand the lyric poet Stesichorus and numerous athletes who won victories at the Olympic Games, testament to the cultural prestige of Himera.
            </p>
            <p style="margin-bottom: 1rem;">
            Archaeological interest in the site developed from the 16th century onwards, but the first systematic investigations date to the years between 1926 and 1930, with excavations of the eastern necropolis and the monumental Temple of Victory, conducted by Pirro Marconi. From 1963 research intensified especially in the area of the upper city, comprising the settlement and the sanctuary of Athena. Today these areas, together with the Temple of Victory, are open to visitors and allow a direct appreciation of the urban organisation, sacred architecture, and daily life of a Greek colony of the archaic and classical periods.
            </p>
            <p style="margin-bottom: 1rem;">
            More recent investigations have broadened knowledge of the site through the discovery, at Piano del Tamburino, of new sacred areas and spaces dedicated to worship, confirming the complexity of the religious landscape of Himera. Of particular significance are also the excavations of the necropolises, especially the western one, where over 13,000 burials have been brought to light, including mass graves for the fallen of the battles of 480 and 409 BC. The archaeological area of Himera presents itself today as a powerful place of memory, where visitors can retrace the phases of birth, splendour, and destruction of one of the most emblematic cities of Greek Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Termini Imerese',
    'provincia': 'PA',
    'indirizzo': 'Contrada Buonfornello SS 113 - 90018 Termini Imerese (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 900,
    'composizione_beni': [
        {
            'nome': 'Reperti Archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 900,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/himera.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Sab: 9:00-17:30<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sat: 9:00-17:30<br>',
    'costo_biglietto': 'Intero: € 4.00,  Ridotto € 2.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 4.00, reduced: € 2.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/himera-solunto-iato/siti-archeologici/area-archeologica-di-himera-buonfornello/',
    'telefono': '+39 0918140128',
    'email': 'poloarcheologico.pa.uo5@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 23,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Antiquarium di Monte Iato',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Antiquarium of Monte Iato',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti Archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'L\'Antiquarium di Monte Iato, allestito all\'interno delle Case D\'Alia, appositamente acquisite e restaurate per accogliere la struttura museale, espone una selezione significativa delle testimonianze rinvenute nel sito. ',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Antiquarium of Monte Iato, housed within the Case D\'Alia — specifically acquired and restored to accommodate the museum — displays a significant selection of finds uncovered at the site.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            L'Antiquarium di Monte Iato rappresenta il naturale completamento della visita al grande sito archeologico dell'antica Iaitas e offre al pubblico una lettura chiara e suggestiva delle sue principali testimonianze materiali. Ospitato nelle Case D'Alia, appositamente acquisite e restaurate per accogliere la struttura museale, l'Antiquarium raccoglie una selezione significativa dei reperti rinvenuti nel corso delle indagini archeologiche, illustrando le diverse fasi di vita della città.
            </p>
            <p style="margin-bottom: 1rem;">
            Tra le opere di maggiore impatto spiccano le monumentali sculture in pietra raffiguranti Menadi e Satiri, alte circa due metri, che decoravano la scena del teatro e restituiscono con forza l'atmosfera del mondo dionisiaco legato agli spettacoli. Di straordinario interesse è anche una parete affrescata quasi integra in "primo stile pompeiano", esposta al pubblico nel 2018 al termine di un complesso intervento di restauro, che testimonia l'alto livello artistico e decorativo raggiunto dall'abitato in età ellenistica e romana.
            </p>
            <p style="margin-bottom: 1rem;">
            L'allestimento consente di cogliere il rapporto diretto tra i reperti e i monumenti del sito. In fondo alla sala è infatti ricostruita una porzione del tetto dell'edificio scenico del teatro, grazie all'esposizione dei grandi tegoloni, lunghi quasi un metro e di notevole peso, recanti la dicitura "TEATPOY". Questa iscrizione, impressa prima della cottura, documenta una pratica diffusa nella città greca di Iaitas: tutti gli edifici pubblici, come il tempio di Afrodite, l'edificio teatrale e i portici dell'agorà, erano coperti da tegole marchiate per scoraggiarne il furto e tutelare i beni collettivi.
            </p>
            <p style="margin-bottom: 1rem;">
            Nel suo insieme, l'Antiquarium di Monte Iato si configura come uno spazio essenziale per comprendere l'identità storica e culturale della città antica, integrando la visita all'area archeologica con un percorso che valorizza opere monumentali, elementi architettonici e testimonianze della vita pubblica e privata di Iaitas.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Antiquarium of Monte Iato represents the natural complement to a visit to the great archaeological site of ancient Iaitas, offering the public a clear and evocative reading of its principal material testimonies. Housed in the Case D'Alia, specifically acquired and restored to accommodate the museum, the Antiquarium brings together a significant selection of finds uncovered during archaeological investigations, illustrating the various phases of the city's life.
            </p>
            <p style="margin-bottom: 1rem;">
            Among the most striking works are the monumental stone sculptures depicting Maenads and Satyrs, standing approximately two metres tall, which decorated the stage building of the theatre and powerfully evoke the Dionysian world associated with theatrical performances. Of extraordinary interest is also a nearly intact frescoed wall in the "First Pompeian Style", opened to the public in 2018 following a complex restoration intervention, which attests to the high artistic and decorative level achieved by the settlement in the Hellenistic and Roman periods.
            </p>
            <p style="margin-bottom: 1rem;">
            The layout allows visitors to grasp the direct relationship between the finds and the monuments of the site. At the far end of the room, a section of the roof of the theatre's stage building has been reconstructed, through the display of large roof tiles nearly a metre in length and of considerable weight, bearing the inscription "TEATPOY". This inscription, stamped before firing, documents a widespread practice in the Greek city of Iaitas: all public buildings — including the temple of Aphrodite, the theatre building, and the porticoes of the agora — were covered with marked tiles to discourage theft and safeguard communal property.
            </p>
            <p style="margin-bottom: 1rem;">
            Taken as a whole, the Antiquarium of Monte Iato emerges as an essential space for understanding the historical and cultural identity of the ancient city, integrating the visit to the archaeological area with a route that showcases monumental works, architectural elements, and testimonies of the public and private life of Iaitas.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'San Cipirello',
    'provincia': 'PA',
    'indirizzo': 'Contrada Perciana - 90040 San Cipirello (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 0,
    'composizione_beni': [
        {
            'nome': 'Reperti Archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 250,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/antiquarium-di-monte-iato.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Sab: 9:00-17:30<br>',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sat: 9:00-17:30<br>',
    'costo_biglietto': 'Intero: € 4.00, ridotto: € 2.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 4.00, reduced: € 2.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/himera-solunto-iato/siti-archeologici/antiquarium-di-monte-iato/',
    'telefono': '+39 091 8577943',
    'email': 'parco.archeo.himera@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 24,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Riso - Museo Regionale d\'Arte Moderna e Contemporanea di Palermo',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Museo Riso - Regional Museum of Modern and Contemporary Art of Palermo',
    'categorie': [
        'disegni-grafici-mappe',
        'dipinti',
        'sculture'
    ],
    'categorie_labels': [
        'Disegni, grafici, mappe',
        'Dipinti',
        'Sculture'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Drawings, graphics, maps',
        'Paintings',
        'Sculptures'
    ],
    'descrizione_breve': 'Il Museo Riso di Palermo è un\'istituzione museale ospitata nell\'omonimo palazzo settecentesco, nello storico corso Vittorio Emanuele.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Museo Riso in Palermo is a museum institution housed in the eighteenth-century palace of the same name, on the historic Corso Vittorio Emanuele.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Regionale d'Arte Moderna e Contemporanea di Palermo (GAM Palermo) è uno dei principali poli espositivi della Sicilia dedicati all'arte del XIX, XX e XXI secolo. Situato nel cuore della città, il museo nasce per conservare, valorizzare e promuovere le collezioni di arte moderna e contemporanea della regione, offrendo un percorso espositivo che copre oltre due secoli di produzione artistica.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo ospita una vasta gamma di opere, tra dipinti, sculture, disegni, incisioni e installazioni, che documentano l'evoluzione della scena artistica siciliana, italiana e internazionale. Tra i punti di forza della collezione vi sono opere di artisti italiani del Novecento, tra cui Filippo de Pisis, Renato Guttuso e Carla Accardi, insieme a importanti acquisizioni di artisti contemporanei che hanno contribuito a rinnovare il panorama artistico locale. Particolare attenzione è riservata alla promozione di giovani talenti e alla realizzazione di mostre temporanee, eventi culturali e laboratori didattici.
            </p>
            <p style="margin-bottom: 1rem;">
            La GAM Palermo si distingue non solo per la ricchezza delle sue collezioni, ma anche per la qualità delle esposizioni e degli spazi espositivi, concepiti per garantire un'esperienza immersiva e coinvolgente per il visitatore. Grazie alla sua attività culturale e scientifica, il museo rappresenta oggi un punto di riferimento per la conoscenza e la valorizzazione dell'arte moderna e contemporanea in Sicilia.
            </p>            
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Museum of Modern and Contemporary Art of Palermo (GAM Palermo) is one of Sicily's principal exhibition venues dedicated to art of the 19th, 20th, and 21st centuries. Located in the heart of the city, the museum was created to preserve, promote, and enhance the region's modern and contemporary art collections, offering an exhibition route spanning over two centuries of artistic production.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum houses a wide range of works — including paintings, sculptures, drawings, prints, and installations — that document the evolution of the Sicilian, Italian, and international art scene. Among the highlights of the collection are works by twentieth-century Italian artists including Filippo de Pisis, Renato Guttuso, and Carla Accardi, alongside significant acquisitions of contemporary artists who have contributed to renewing the local artistic landscape. Particular attention is devoted to the promotion of young talent and to the organisation of temporary exhibitions, cultural events, and educational workshops.
            </p>
            <p style="margin-bottom: 1rem;">
            GAM Palermo stands out not only for the richness of its collections, but also for the quality of its exhibitions and exhibition spaces, conceived to provide an immersive and engaging experience for the visitor. Through its cultural and scientific activities, the museum today represents a key point of reference for the study and promotion of modern and contemporary art in Sicily.
            </p>            
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Palermo',
    'provincia': 'PA',
    'indirizzo': 'Via Vittorio Emanuele 365 - 90134 Palermo (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 65,
    'composizione_beni': [
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 30,
        },
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 30,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 5,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-riso.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-18:30<br>Domenica e Festivi: 9:00-13:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-18:30<br>Sunday and Public Holidays: 9:00-13:00',
    'costo_biglietto': 'Ingresso gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www.museoartecontemporanea.it/museo_Riso/',
    'telefono': '+39  091587717',
    'email': ' museo.arte.riso@regione.sicilia.it',
    'accessibilita': 'Accesso facilitato per persone con disabilità motoria',
    # EN: traduzione di 'accessibilita' — lasciare vuoto '' per usare il testo italiano
    'accessibilita_en': 'Facilitated access for people with motor disabilities',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/...',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 25,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo d\'Aumale - Museo Regionale di Terrasini',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Museo d\'Aumale - Regional Museum of Terrasini',
    'categorie': [
        'beni-naturalistici',
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Beni naturalistici',
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Natural heritage',
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Regionale di Terrasini – Museo d\'Aumale è ospitato nell\'elegante Palazzo d\'Aumale sul lungomare di Terrasini e raccoglie collezioni diverse: archeologica, etno-antropologica e naturalistica. L\'allestimento racconta la storia, la natura e le tradizioni del territorio siciliano occidentale in un percorso espositivo multidisciplinare.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Museum of Terrasini – Museo d\'Aumale is housed in the elegant Palazzo d\'Aumale on the seafront of Terrasini and brings together diverse collections: archaeological, ethno-anthropological, and naturalistic. The layout recounts the history, nature, and traditions of western Sicily through a multidisciplinary exhibition route.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Regionale di Terrasini si trova nei pressi della spiaggia di Praiola, ed ha sede nello storico Palazzo d'Aumale, edificio ottocentesco affacciato sul mare. Il museo occupa stabilmente i locali del palazzo, oggi di proprietà comunale, grazie a una convenzione tra il Comune di Terrasini e la Regione Siciliana.
            </p>
            <p style="margin-bottom: 1rem;">
            Il palazzo fu costruito intorno al 1835 per volontà di Don Vincenzo Grifeo, principe di Partanna, come struttura destinata allo stoccaggio dei prodotti agricoli, in particolare del vino. Nel 1860 venne acquistato da Enrico d'Orléans, duca d'Aumale, che ne ampliò la struttura rendendolo funzionale alla grande produzione vinicola della tenuta dello Zucco. Dopo la morte del duca, l'edificio conobbe un lungo periodo di abbandono e diversi progetti di riutilizzo mai realizzati, fino al recupero promosso dal Comune di Terrasini e dalla Regione Siciliana tra gli anni Ottanta e Novanta del Novecento.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo conserva una delle più importanti collezioni naturalistiche d'Italia, composta da oltre 500.000 reperti tra paleontologia, malacologia, entomologia, ornitologia, mineralogia e geologia. Accanto a questa, è presente una significativa sezione etnoantropologica, dedicata alla cultura materiale siciliana, con carretti siciliani, modellini di imbarcazioni e oggetti legati alla tradizione contadina. Una più piccola sezione archeologica raccoglie reperti terrestri e marini provenienti dal territorio.
            </p>
            <p style="margin-bottom: 1rem;">
            Articolato nelle tre sezioni naturalistica, etnoantropologica e archeologica, il Museo Regionale di Terrasini rappresenta oggi un importante centro di conservazione, studio e valorizzazione del patrimonio naturale e culturale della Sicilia occidentale.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Museum of Terrasini is located near the beach of Praiola and is housed in the historic Palazzo d'Aumale, a nineteenth-century building overlooking the sea. The museum permanently occupies the rooms of the palace — today in municipal ownership — through a convention between the Municipality of Terrasini and the Sicilian Region.
            </p>
            <p style="margin-bottom: 1rem;">
            The palace was built around 1835 at the behest of Don Vincenzo Grifeo, Prince of Partanna, as a facility for the storage of agricultural products, particularly wine. In 1860 it was purchased by Henri d'Orléans, Duke of Aumale, who expanded the structure to support the large-scale wine production of the Zucco estate. After the duke's death, the building went through a long period of abandonment and several unrealised reuse projects, until the restoration promoted by the Municipality of Terrasini and the Sicilian Region in the 1980s and 1990s.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum holds one of the most important naturalistic collections in Italy, comprising over 500,000 specimens spanning palaeontology, malacology, entomology, ornithology, mineralogy, and geology. Alongside this, a significant ethno-anthropological section is dedicated to Sicilian material culture, featuring Sicilian carts, model boats, and objects connected to rural tradition. A smaller archaeological section brings together terrestrial and marine finds from the local territory.
            </p>
            <p style="margin-bottom: 1rem;">
            Structured around its three naturalistic, ethno-anthropological, and archaeological sections, the Regional Museum of Terrasini today represents an important centre for the conservation, study, and promotion of the natural and cultural heritage of western Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Terrasini',
    'provincia': 'PA',
    'indirizzo': 'Lungomare Peppino Impastato - 90100 Terrasini (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 1120,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 9000,
        },
        {
            'nome': 'Beni naturalistici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Natural heritage',
            'quantita': 40,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-terrasini.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-19:00<br>Domenica e Festivi: 9:00-13:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-19:00<br>Sunday and Public Holidays: 9:00-13:00',
    'costo_biglietto': 'Intero: € 8.00, ridotto: € 4.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 8.00, reduced: € 4.00',
    'sito_web': 'https://www.museoartecontemporanea.it/museo_dAumale/',
    'telefono': '+39 0918 810989',
    'email': 'museo.arte.riso@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 26,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Regionale Antonino Salinas',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Antonino Salinas Regional Archaeological Museum',
    'categorie': [
        'stampe-fotografiche',
        'disegni-grafici-mappe',
        'beni-naturalistici',
        'reperti-archeologici',
        'dipinti',
        'sculture'
    ],
    'categorie_labels': [
        'Stampe fotografiche',
        'Disegni, grafici, mappe',
        'Beni naturalistici',
        'Reperti archeologici',
        'Dipinti',
        'Sculture'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Photographic prints',
        'Drawings, graphics, maps',
        'Natural heritage',
        'Archaeological finds',
        'Paintings',
        'Sculptures'
    ],
    'descrizione_breve': 'Il Museo Archeologico Regionale "Antonino Salinas" di Palermo è una delle istituzioni museali più importanti della Sicilia, dedicata alla storia e alle civiltà dell\'isola dalla Preistoria al Medioevo. È ospitato nell\'antico complesso dei Padri Filippini all\'Olivella e conserva ricchissime collezioni di arte punica, greca, etrusca e romana.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The "Antonino Salinas" Regional Archaeological Museum of Palermo is one of the most important museum institutions in Sicily, dedicated to the history and civilisations of the island from Prehistory to the Middle Ages. Housed in the ancient complex of the Filippini Fathers at the Olivella, it preserves extraordinarily rich collections of Punic, Greek, Etruscan, and Roman art.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale "Antonino Salinas" si trova a Palermo ed è uno dei più importanti musei archeologici d'Italia, grazie alla vastità e al valore delle sue collezioni, che documentano la storia della Sicilia dalla preistoria al Medioevo. Al suo interno sono conservati reperti dei principali popoli che hanno abitato l'isola, tra cui fenici, punici, greci, romani e bizantini, accanto a testimonianze di altre civiltà del Mediterraneo antico, come quella egizia ed etrusca. Tra i reperti più celebri spicca la Pietra di Palermo, fondamentale fonte per la conoscenza dell'Antico Regno egiziano.
            </p>
            <p style="margin-bottom: 1rem;">
            Nato nel 1814, il museo è stato museo nazionale fino al 1977 ed è intitolato ad Antonino Salinas, archeologo e numismatico palermitano che ne fu direttore dal 1873 al 1914. Una sezione significativa è dedicata ai reperti provenienti da scavi subacquei, con materiali che vanno dall'età punica a quella romana, come anfore, ancore, ceppi di piombo e iscrizioni.
            </p>
            <p style="margin-bottom: 1rem;">
            Di grande rilievo è la sezione fenicio-punica, che conserva, tra l'altro, due monumentali sarcofagi antropomorfi del V secolo a.C. e numerose stele e sculture provenienti da Mozia e Lilibeo. Ampio spazio è riservato anche a Selinunte, con le celebri metope dei templi e il grande frontone con Gorgone del tempio C, ricomposto sulla base dei disegni storici degli scavi.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo ospita inoltre importanti opere provenienti da vari centri della Sicilia antica, come Solunto, Agrigento e Siracusa. Tra queste spiccano l'Ariete di bronzo del III secolo a.C., attribuito alla cerchia di Lisippo, e numerose sculture e mosaici di età romana. Le collezioni del museo derivano in parte da acquisizioni e donazioni private, tra cui la collezione Salinas e la prestigiosa collezione etrusca Casuccini, considerata la più importante al di fuori della Toscana.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Archaeological Museum "Antonino Salinas" is located in Palermo and is one of the most important archaeological museums in Italy, thanks to the breadth and value of its collections, which document the history of Sicily from prehistory to the Middle Ages. It preserves finds from the principal peoples who inhabited the island, including Phoenicians, Punics, Greeks, Romans, and Byzantines, alongside testimonies of other ancient Mediterranean civilisations such as those of Egypt and Etruria. Among the most celebrated finds stands the Palermo Stone, a fundamental source for knowledge of the Egyptian Old Kingdom.
            </p>
            <p style="margin-bottom: 1rem;">
            Founded in 1814, the museum served as a national museum until 1977 and is named after Antonino Salinas, a Palermitan archaeologist and numismatist who served as its director from 1873 to 1914. A significant section is dedicated to finds from underwater excavations, with materials ranging from the Punic to the Roman period, including amphorae, anchors, lead anchor stocks, and inscriptions.
            </p>
            <p style="margin-bottom: 1rem;">
            Of great importance is the Phoenician-Punic section, which preserves, among other works, two monumental anthropomorphic sarcophagi from the 5th century BC and numerous stelae and sculptures from Mozia and Lilybaeum. Extensive space is also devoted to Selinunte, with the celebrated temple metopes and the great pediment with Gorgon from Temple C, reassembled on the basis of historical drawings from the excavations.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum also houses important works from various centres of ancient Sicily, including Solunto, Agrigento, and Syracuse. Among these stand out the bronze Ram of the 3rd century BC, attributed to the circle of Lysippos, and numerous sculptures and mosaics of the Roman period. The museum's collections derive in part from private acquisitions and donations, including the Salinas collection and the prestigious Casuccini Etruscan collection, considered the most important outside Tuscany.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Palermo',
    'provincia': 'PA',
    'indirizzo': 'Via Bara all\'Olivella 24 - 90133 Palermo (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 58927,
    'composizione_beni': [
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 45000,
        },
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 9000,
        },
        {
            'nome': 'Beni naturalistici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Natural heritage',
            'quantita': 40,
        },
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 3887,
        },
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 200,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 800,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/salinas.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-19:00<br>Dom: 9:00-13:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-19:00<br>Sun: 9:00-13:00',
    'costo_biglietto': 'Intero €6.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 6.00',
    'sito_web': 'https://www2.regione.sicilia.it/bbccaa/salinas/',
    'telefono': '+39 0916 116805',
    'email': 'museo.archeo.salinas@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/CulturalInstituteOrSite/ICCD_CF_3725810854161',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 27,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Soprintendenza Beni Culturali del Mare',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Superintendency for Maritime Cultural Heritage',
    'categorie': [
        'disegni-grafici-mappe',
        'stampe-fotografiche'
    ],
    'categorie_labels': [
        'Disegni, grafici, mappe',
        'Stampe fotografiche'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Drawings, graphics, maps',
        'Photographic prints'
    ],
    'descrizione_breve': 'La Soprintendenza per i Beni Culturali e Ambientali del Mare di Palermo è un ufficio specialistico della Regione Siciliana dedicato alla tutela, valorizzazione, ricerca e gestione dei beni culturali presenti nel patrimonio marino e nei fondali sottomarini dell\'isola.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Superintendency for Cultural and Environmental Heritage of the Sea in Palermo is a specialist office of the Sicilian Region dedicated to the protection, promotion, research, and management of cultural assets present in the island\'s marine heritage and underwater seabeds.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            La Soprintendenza per i Beni culturali e ambientali del Mare, comunemente nota come Soprintendenza del Mare, è un organo della Regione Siciliana deputato alla tutela, alla gestione e alla valorizzazione dei beni culturali e ambientali presenti nelle acque marine, con particolare riferimento alle risorse archeologiche sottomarine. Essa opera alle dipendenze del Dipartimento dei Beni culturali e dell'Identità siciliana dell'Assessorato regionale dei Beni culturali.
            </p>
            <p style="margin-bottom: 1rem;">
            Le origini della Soprintendenza del Mare risalgono al 1999, quando, per iniziativa di Sebastiano Tusa, il Dipartimento regionale dei Beni culturali istituì il G.I.A.S.S. (Gruppo d'Indagine Archeologica Subacquea Sicilia), successivamente trasformato nel S.C.R.A.S. (Servizio di Coordinamento delle Ricerche Archeologiche Sottomarine). Questo percorso portò, nel 2004, all'istituzione della prima Soprintendenza del Mare d'Italia, creata in Sicilia mediante un apposito articolo della legge finanziaria regionale, promosso dall'allora assessore ai Beni culturali Fabio Granata, con l'obiettivo di proteggere e valorizzare il patrimonio culturale legato al mare.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Superintendency for Cultural and Environmental Heritage of the Sea, commonly known as the Soprintendenza del Mare, is a body of the Sicilian Region responsible for the protection, management, and promotion of cultural and environmental heritage present in marine waters, with particular reference to underwater archaeological resources. It operates under the Department of Cultural Heritage and Sicilian Identity of the Regional Assessorate for Cultural Heritage.
            </p>
            <p style="margin-bottom: 1rem;">
            The origins of the Soprintendenza del Mare date back to 1999, when, at the initiative of Sebastiano Tusa, the Regional Department of Cultural Heritage established the G.I.A.S.S. (Sicilian Underwater Archaeological Investigation Group), subsequently transformed into the S.C.R.A.S. (Coordination Service for Underwater Archaeological Research). This process led, in 2004, to the establishment of the first Soprintendenza del Mare in Italy, created in Sicily through a dedicated article of the regional finance law, promoted by the then Assessor for Cultural Heritage Fabio Granata, with the objective of protecting and enhancing the cultural heritage linked to the sea.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Palermo',
    'provincia': 'PA',
    'indirizzo': 'Via Lungarini 9 - 90133 Palermo (PA)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 75,
    'composizione_beni': [
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 50,
        },
        {
            'nome': 'Stampe fotografiche',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Photographic prints',
            'quantita': 25,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/sbca-palermo.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Ven: 9:30-13:00<br>Mer: 9:30-13:00 16:00-17:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Fri: 9:30-13:00<br>Wed: 9:30-13:00 16:00-17:00',
    'costo_biglietto': 'Gratuito',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Free admission',
    'sito_web': 'https://www2.regione.sicilia.it/beniculturali/archeologiasottomarina/index.htm',
    'telefono': '+39 0916 170933',
    'email': 'sopmare@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 28,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Antiquarium di Segesta',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Antiquarium of Segesta',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'L\'Antiquarium di Segesta è il piccolo museo del Parco Archeologico di Segesta dove sono raccolti e esposti i reperti rinvenuti negli scavi del sito: oggetti ceramici, statuette in terracotta, elementi architettonici come gronde, iscrizioni in lingua elima e altri materiali che aiutano a ricostruire usi, riti e aspetti della vita religiosa e quotidiana dell\'antica città elima.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Antiquarium of Segesta is the small museum of the Segesta Archaeological Park, where finds from the site\'s excavations are collected and displayed: ceramic objects, terracotta statuettes, architectural elements such as roof gutters, inscriptions in the Elymian language, and other materials that help reconstruct the customs, rituals, and aspects of religious and daily life in the ancient Elymian city.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            L'Antiquarium di Segesta si trova all'interno del Parco Archeologico di Segesta, in provincia di Trapani, in prossimità dell'area monumentale che comprende il celebre tempio dorico e il teatro. La struttura museale svolge la funzione di spazio espositivo e di supporto alla comprensione storica e archeologica dell'antica città elima, offrendo al visitatore una lettura organica dei materiali rinvenuti nel sito e nel suo territorio.
            </p>
            <p style="margin-bottom: 1rem;">
            L'Antiquarium conserva reperti provenienti principalmente dagli scavi archeologici condotti a Segesta nel corso del Novecento, documentando le diverse fasi di vita della città, dalla preistoria all'età ellenistica e romana. I materiali esposti includono ceramiche, terrecotte architettoniche, elementi decorativi, oggetti di uso quotidiano ed epigrafi, che testimoniano sia la cultura materiale della popolazione elima sia i rapporti con il mondo greco e, successivamente, con quello romano.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo segue un criterio prevalentemente cronologico e tematico, permettendo di ricostruire lo sviluppo urbano e sociale di Segesta, le sue pratiche cultuali e le trasformazioni dell'abitato nel corso dei secoli. Particolare attenzione è dedicata ai contesti sacri e funerari, nonché ai materiali che attestano i contatti commerciali e culturali con le altre città della Sicilia antica e del Mediterraneo.
            </p>
            <p style="margin-bottom: 1rem;">
            L'Antiquarium svolge inoltre un'importante funzione didattica e divulgativa, integrando l'esperienza di visita al parco archeologico con pannelli esplicativi e apparati informativi che aiutano a contestualizzare i monumenti ancora visibili nell'area. In questo modo il museo rappresenta un punto di riferimento essenziale per la valorizzazione e la comprensione del patrimonio archeologico di Segesta e del suo ruolo nella storia della Sicilia occidentale.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Antiquarium of Segesta is located within the Archaeological Park of Segesta, in the province of Trapani, close to the monumental area comprising the celebrated Doric temple and the theatre. The museum serves as an exhibition space and a support for the historical and archaeological understanding of the ancient Elymian city, offering the visitor an organic reading of the materials found at the site and in its surrounding territory.
            </p>
            <p style="margin-bottom: 1rem;">
            The Antiquarium holds finds deriving principally from the archaeological excavations conducted at Segesta throughout the twentieth century, documenting the various phases of the city's life from prehistory through the Hellenistic and Roman periods. The displayed materials include ceramics, architectural terracottas, decorative elements, everyday objects, and inscriptions, which attest both to the material culture of the Elymian population and to its relations with the Greek world and, subsequently, with Rome.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition route follows a predominantly chronological and thematic approach, allowing the visitor to reconstruct the urban and social development of Segesta, its cultic practices, and the transformations of the settlement over the centuries. Particular attention is devoted to sacred and funerary contexts, as well as to materials attesting to commercial and cultural contacts with other cities of ancient Sicily and the Mediterranean.
            </p>
            <p style="margin-bottom: 1rem;">
            The Antiquarium also fulfils an important educational and outreach function, complementing the visit to the archaeological park with explanatory panels and informative displays that help contextualise the monuments still visible in the area. In this way the museum represents an essential point of reference for the promotion and understanding of the archaeological heritage of Segesta and its role in the history of western Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Calatafimi Segesta',
    'provincia': 'TP',
    'indirizzo': 'Area archeologica di Segesta - 91013 Calatafimi-Segesta (TP)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 1000,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 1000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/antiquarium-di-segesta.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-15:30',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-15:30',
    'costo_biglietto': 'Intero €14.00, ridotto €7.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 14.00, reduced: € 7.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/parco-archeologico-segesta/',
    'telefono': '+39 0924 952356',
    'email': 'urp.parco.archeo.segesta@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 29,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Regionale Lilibeo',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Lilibeo Regional Archaeological Museum',
    'categorie': [
        'sculture',
        'disegni-grafici-mappe',
        'beni-naturalistici',
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Sculture',
        'Beni naturalistici',
        'Disegni, grafici, mappe',
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Sculptures',
        'Natural heritage',
        'Drawings, graphics, maps',
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico Regionale Lilibeo a Marsala è ospitato in un ex stabilimento vinicolo ottocentesco sul promontorio di Capo Boeo ed espone le principali testimonianze della città antica di Lilibeo. Il percorso espositivo comprende reperti subacquei e materiali terrestri che illustrano la storia urbana, le necropoli puniche ed ellenistico-romane, culti e vita quotidiana fino al Medioevo.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Lilibeo Regional Archaeological Museum in Marsala is housed in a nineteenth-century former winery on the Capo Boeo promontory and displays the principal testimonies of the ancient city of Lilybaeum. The exhibition route includes underwater finds and terrestrial materials illustrating the city\'s urban history, Punic and Hellenistic-Roman necropolises, religious cults, and daily life through to the Middle Ages.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale Lilibeo si trova a Capo Boeo, a Marsala, ed è uno dei più importanti musei archeologici della Sicilia occidentale. È celebre per ospitare l'unico esemplare di nave punica giunto fino ai nostri giorni, affiancato dalla nave romana di Marausa, rendendolo un punto di riferimento internazionale per gli studi di archeologia navale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo ha sede in un antico baglio costruito intorno al 1880 come stabilimento vinicolo, situato alla periferia della città. La struttura è stata destinata a uso museale dalla Regione Siciliana nel 1986 e inaugurata ufficialmente nel 1999. Alla fine degli anni Duemila il complesso è stato ampliato con l'esproprio e l'acquisizione del vicino Baglio Tumbarello-Grignani, collegato al Baglio Anselmi tramite un passaggio coperto. Tra le opere di maggior rilievo conservate nel museo figura anche la Venere Lilybetana, nota come Venere Callipigia, una statua romana databile tra il I e il II secolo d.C., copia di un originale ellenistico del II secolo a.C.
            </p>
            <p style="margin-bottom: 1rem;">
            L'edificio è stato oggetto di importanti interventi di ristrutturazione per accogliere la nave punica, rinvenuta nel 1969 nelle acque al largo dell'Isola Grande, nei pressi dell'imboccatura settentrionale della laguna dello Stagnone. Questo straordinario reperto, unico nel suo genere, rappresenta il fulcro dell'esposizione ed è oggetto di costante interesse da parte di archeologi e studiosi provenienti da tutto il mondo. Dal 18 dicembre 2015 il museo ospita anche la nave romana di Marausa, recuperata davanti alla costa di Trapani e resa accessibile al pubblico a partire dall'aprile 2019.
            </p>
            <p style="margin-bottom: 1rem;">
            Accanto alle imbarcazioni antiche, il museo conserva un ricco patrimonio di reperti archeologici, tra cui ceramiche e terrecotte di età ellenistica e romana, epigrafi incise su lastre di pietra, anfore da trasporto, ceppi di ancora e materiali provenienti da relitti arabo-normanni affondati nell'area. Alle spalle del complesso museale si estende inoltre l'ampia area archeologica dell'antica città di Lilibeo, con resti di insulae romane, i cui mosaici sono esposti all'interno del museo, e un decumano perfettamente conservato.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Lilibeo Regional Archaeological Museum is located at Capo Boeo in Marsala and is one of the most important archaeological museums in western Sicily. It is celebrated for housing the only surviving example of a Punic warship, displayed alongside the Roman vessel of Marausa, making it an international point of reference for the study of nautical archaeology.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum is housed in an ancient baglio built around 1880 as a winery on the outskirts of the city. The building was designated for museum use by the Sicilian Region in 1986 and officially inaugurated in 1999. In the late 2000s the complex was expanded through the compulsory purchase and acquisition of the neighbouring Baglio Tumbarello-Grignani, connected to the Baglio Anselmi via a covered passageway. Among the most significant works housed in the museum is the Venus Lilybetana, known as the Venus Callipyge, a Roman statue datable between the 1st and 2nd centuries AD and a copy of a Hellenistic original of the 2nd century BC.
            </p>
            <p style="margin-bottom: 1rem;">
            The building underwent major renovation works to accommodate the Punic ship, discovered in 1969 in the waters off Isola Grande, near the northern entrance to the Stagnone lagoon. This extraordinary find, unique of its kind, represents the focal point of the exhibition and is the subject of constant interest from archaeologists and scholars from around the world. Since 18 December 2015 the museum has also housed the Roman vessel of Marausa, recovered off the coast of Trapani and made accessible to the public from April 2019.
            </p>
            <p style="margin-bottom: 1rem;">
            Alongside the ancient vessels, the museum preserves a rich heritage of archaeological finds, including ceramics and terracottas of the Hellenistic and Roman periods, inscriptions carved on stone slabs, transport amphorae, anchor stocks, and materials from Arab-Norman shipwrecks in the area. Behind the museum complex extends the broad archaeological area of the ancient city of Lilybaeum, with remains of Roman insulae — whose mosaics are displayed inside the museum — and a perfectly preserved decumanus.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Marsala',
    'provincia': 'TP',
    'indirizzo': 'Lungomare Boeo 30 - 91025 MARSALA (TP)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 3663,
    'composizione_beni': [
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 25,
        },
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 3500,
        },
        {
            'nome': 'Beni naturalistici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Natural heritage',
            'quantita': 32,
        },
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 106,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-lilibeo.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Dom: 9:00-19:30',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sun: 9:00-19:30',
    'costo_biglietto': 'Intero €10.00, ridotto €5.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 10.00, reduced: € 5.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/lilibeo-marsala/siti-archeologici/museo-archeologico-regionale-lilibeo/',
    'telefono': '+39 0923952535',
    'email': 'parco.archeo.lilibeo@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': None,
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 30,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo del Satiro Danzante',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Museum of the Dancing Satyr',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo del Satiro Danzante è un museo archeologico situato a Mazara del Vallo, all\'interno della ex chiesa di Sant\'Egidio, che prende il nome dalla sua opera più celebre: il Satiro Danzante, una grande statua bronzea di epoca greco-ellenistica ritrovata nei fondali del Canale di Sicilia negli anni \'90 e restaurata prima dell\'esposizione permanente.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Museum of the Dancing Satyr is an archaeological museum located in Mazara del Vallo, within the former church of Sant\'Egidio. It takes its name from its most celebrated work: the Dancing Satyr, a large bronze statue of the Greek-Hellenistic period recovered from the seabed of the Sicily Channel in the 1990s and restored prior to permanent display.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo del Satiro Danzante è un museo archeologico situato a Mazara del Vallo, istituito dalla Regione Siciliana nel 2003. Ha sede nella ex chiesa di Sant'Egidio e prende il nome dal suo reperto più celebre e prestigioso, la statua bronzea del Satiro danzante, una delle opere più straordinarie dell'arte greca giunte fino a noi. Dal 2019 il museo rientra nell'organizzazione del Parco Archeologico di Selinunte, Cave di Cusa e Pantelleria.
            </p>
            <p style="margin-bottom: 1rem;">
            L'esposizione ruota attorno alla celebre scultura in bronzo, recuperata dal mare alla fine degli anni Novanta nel Canale di Sicilia, ma comprende anche numerose testimonianze archeologiche di provenienza subacquea. Sono esposti infatti vasellame e frammenti statuari in bronzo, insieme a reperti rinvenuti durante campagne di ricerca condotte nelle acque antistanti la costa di Mazara del Vallo. Tra questi figurano bracieri in terracotta di epoca medievale, uno spatheion nordafricano databile al V secolo d.C., un askos acromo della prima metà del III secolo a.C. e diverse anfore da trasporto di età punica e romana.
            </p>
            <p style="margin-bottom: 1rem;">
            All'ingresso dell'unica grande sala del museo è proiettato un filmato documentario che racconta il ritrovamento del Satiro danzante e le fasi del suo recupero dal fondale marino, offrendo al visitatore un importante supporto introduttivo alla comprensione del valore storico e artistico dell'opera.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Museum of the Dancing Satyr is an archaeological museum located in Mazara del Vallo, established by the Sicilian Region in 2003. It is housed in the former church of Sant'Egidio and takes its name from its most celebrated and prestigious find — the bronze statue of the Dancing Satyr, one of the most extraordinary works of Greek art to have survived to the present day. Since 2019 the museum has formed part of the Archaeological Park of Selinunte, Cave di Cusa, and Pantelleria.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition revolves around the celebrated bronze sculpture, recovered from the sea in the late 1990s in the Sicily Channel, but also encompasses numerous archaeological testimonies of underwater origin. On display are bronze tableware and sculptural fragments, alongside finds recovered during research campaigns conducted in the waters off the coast of Mazara del Vallo. Among these are medieval terracotta braziers, a North African spatheion datable to the 5th century AD, an undecorated askos from the first half of the 3rd century BC, and several transport amphorae of the Punic and Roman periods.
            </p>
            <p style="margin-bottom: 1rem;">
            At the entrance to the museum's single large hall, a documentary film is projected recounting the discovery of the Dancing Satyr and the stages of its recovery from the seabed, providing the visitor with an important introductory aid to understanding the historical and artistic significance of the work.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Mazara del Vallo',
    'provincia': 'TP',
    'indirizzo': 'Piazza Plebiscito - 91026 Mazara del Vallo (TP)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 39,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 39,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-satiro-danzante.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-20:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-20:00',
    'costo_biglietto': 'Intero €8.00, ridotto €4.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 8.00, reduced: € 4.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/selinunte-cave-cusa-pantelleria/',
    'telefono': '+39 0923933917',
    'email': 'parco.archeo.selinunte@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 31,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Castello Grifeo',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Grifeo Castle Museum',
    'categorie': [
        'reperti-archeologici',
        'disegni-grafici-mappe',
        'sculture',
        'dipinti'
    ],
    'categorie_labels': [
        'Reperti archeologici',
        'Disegni, grafici, mappe',
        'Sculture',
        'Dipinti'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds',
        'Drawings, graphics, maps',
        'Sculptures',
        'Paintings'
    ],
    'descrizione_breve': 'Il Castello Grifeo di Partanna ospita ad oggi il Museo Regionale di Preistoria del Belìce, dove sono esposti reperti archeologici principalmente del Neolitico e dell\'età del Bronzo rinvenuti nel territorio, come ceramiche, selci, resti faunistici e un cranio trapanato con foro terapeutico, oltre a sezioni che illustrano la cultura materiale delle popolazioni preistoriche della valle.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Grifeo Castle in Partanna now houses the Regional Museum of Prehistory of the Belìce, displaying archaeological finds principally from the Neolithic and Bronze Age discovered in the territory — including ceramics, flint tools, faunal remains, and a trepanned skull with a therapeutic hole — alongside sections illustrating the material culture of the prehistoric populations of the valley.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo del Castello Grifeo ha sede nell'omonimo edificio medievale situato sulle pendici della collina su cui si è sviluppata l'attuale città di Partanna. Il castello, tra i meglio conservati della Sicilia occidentale, è stato oggetto di importanti interventi di restauro nel 2003 e nel 2007 e, dal 28 dicembre 2007, ospita il Museo Regionale di Preistoria del Belice, oltre ad essere utilizzato come sede di eventi culturali. L'edificio si articola su più livelli: piano terra, primo e secondo piano, il terzo piano della torre e un seminterrato.
            </p>
            <p style="margin-bottom: 1rem;">
            L'accesso principale conduce, dal portale sul lato nord-est, a un cortile interno a pianta rettangolare che funge da snodo per i diversi ambienti del castello; una scala coperta collega il cortile al giardino sottostante. Un secondo ingresso, contrassegnato dallo stemma della famiglia Adragna, immette negli ambienti baronali, mentre l'ingresso centrale, sormontato dallo stemma dei Grifeo, introduce nel salone più importante dell'edificio.
            </p>
            <p style="margin-bottom: 1rem;">
            Il salone conserva un affresco del 1777 raffigurante tre cavalieri cristiani durante la battaglia di Mazara: in primo piano è rappresentato il Gran Conte Ruggero nell'atto di uccidere l'arabo Mokarta, seguito da Giovanni I Grifeo, primo feudatario di Partanna, identificabile dallo scudo con il grifone araldico; sullo sfondo compaiono il mare e la città fortificata di Mazara. All'interno dello stesso ambiente è stata allestita una pinacoteca con pale d'altare provenienti da chiese distrutte, tra cui spicca il polittico della Madonna del Rosario del 1585 del pittore fiammingo Simon de Wobreck, i cui volti dei santi e della Madonna, danneggiati, sono stati volutamente lasciati senza integrazioni nel restauro.
            </p>
            <p style="margin-bottom: 1rem;">
            Dalla sala delle armi si accede ad altri ambienti del castello; su un lato del salone una piccola porta conduce a una stanza di clausura nota come "cella della monaca", tradizionalmente identificata come il luogo in cui avrebbe vissuto reclusa una religiosa appartenente alla famiglia Grifeo. Le restanti sale, ormai prive degli arredi originari, sono destinate all'esposizione archeologica preistorica e ospitano reperti neolitici e dell'età del bronzo provenienti dalla Contrada Stretto, area archeologica del territorio di Partanna. La collezione comprende vasellame, zanne di elefante, scheletri umani, asce e bicchieri campaniformi.
            </p>
            <p style="margin-bottom: 1rem;">
            Accanto al salone principale si trova l'antica sala da pranzo, collegata al giardino mediante una scala esterna. Nel giardino si aprono gli accessi ai locali sotterranei, dove si trovano le scuderie con volte a botte e cunicoli ipogei, probabilmente utilizzati in passato come collegamenti con altri edifici e oggi adibiti a sale per conferenze, e le cantine, che conservano grandi botti in noce di Slavonia costruite in situ e antichi torchi per la produzione dell'olio e del vino. In alcuni ambienti delle cantine è infine allestito un museo etno-antropologico che raccoglie strumenti e arnesi della tradizione contadina locale.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Grifeo Castle Museum is housed in the medieval building of the same name, situated on the slopes of the hill on which the present-day city of Partanna developed. The castle, among the best-preserved in western Sicily, underwent major restoration works in 2003 and 2007 and, from 28 December 2007, has housed the Regional Museum of Prehistory of the Belice, while also serving as a venue for cultural events. The building is arranged across multiple levels: ground floor, first and second floors, the third floor of the tower, and a basement.
            </p>
            <p style="margin-bottom: 1rem;">
            The main entrance leads, through the portal on the north-eastern side, to an internal rectangular courtyard that serves as the hub connecting the castle's various spaces; a covered staircase links the courtyard to the garden below. A second entrance, marked by the coat of arms of the Adragna family, gives access to the baronial quarters, while the central entrance, surmounted by the Grifeo coat of arms, opens into the building's most important hall.
            </p>
            <p style="margin-bottom: 1rem;">
            The hall preserves a fresco of 1777 depicting three Christian knights during the Battle of Mazara: in the foreground is the Great Count Roger in the act of slaying the Arab Mokarta, followed by Giovanni I Grifeo, first feudal lord of Partanna, identifiable by his shield bearing the heraldic griffin; in the background appear the sea and the fortified city of Mazara. Within the same room a picture gallery has been arranged, with altarpieces from destroyed churches, among which stands out the 1585 polyptych of the Madonna of the Rosary by the Flemish painter Simon de Wobreck, whose damaged faces of the saints and the Madonna were deliberately left unrestored.
            </p>
            <p style="margin-bottom: 1rem;">
            From the armour room one accesses other spaces in the castle; on one side of the hall a small door leads to a cloistered room known as the "nun's cell", traditionally identified as the place where a member of the Grifeo family lived in seclusion. The remaining rooms, now stripped of their original furnishings, are devoted to the prehistoric archaeological exhibition and house Neolithic and Bronze Age finds from Contrada Stretto, an archaeological area in the territory of Partanna. The collection includes pottery, elephant tusks, human skeletons, axes, and Bell Beaker cups.
            </p>
            <p style="margin-bottom: 1rem;">
            Adjacent to the main hall is the former dining room, connected to the garden by an external staircase. The garden provides access to the underground premises, which include barrel-vaulted stables and hypogeal tunnels — probably used in the past as connections to other buildings and now converted into conference rooms — and the cellars, which preserve large Slavonian walnut barrels built in situ and ancient presses for the production of oil and wine. In some of the cellar rooms an ethno-anthropological museum has been arranged, displaying tools and implements from local rural tradition.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Partanna',
    'provincia': 'TP',
    'indirizzo': 'Piazza Benvenuto Graffeo - 91028 Partanna (TP)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 685,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 572,
        },
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 36,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 67,
        },
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 10,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/castello-grifeo.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-19:30<br>Dom: 9:00-14:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-19:30<br>Sun: 9:00-14:00',
    'costo_biglietto': 'Intero €6.00, ridotto €3.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 6.00, reduced: € 3.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/selinunte-cave-cusa-pantelleria/siti-archeologici/castello-grifeo-partanna/',
    'telefono': '+39 0924923970',
    'email': 'parco.archeo.selinunte@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 32,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Baglio Florio',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Baglio Florio Museum',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Baglio Florio è uno spazio museale ricavato nel Baglio Florio, un edificio ottocentesco nel Parco Archeologico di Selinunte, un tempo destinato alla produzione vinicola della famiglia Florio. Oggi ospita reperti archeologici dell\'antica Selinunte che illustrano architettura sacra, riti e aspetti della vita religiosa della città greca, tra cui esempi di architettura dorica e materiali legati alle pratiche cultuali.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Baglio Florio Museum is a museum space created within the Baglio Florio, a nineteenth-century building in the Archaeological Park of Selinunte once used for wine production by the Florio family. Today it houses archaeological finds from ancient Selinunte illustrating sacred architecture, rituals, and aspects of the religious life of the Greek city, including examples of Doric architecture and materials linked to cultic practices.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Baglio Florio si trova all'interno del Parco Archeologico di Selinunte, in posizione adiacente al tempio G, uno dei monumenti più imponenti dell'antica città greca. La sede museale è ricavata in una struttura ottocentesca appartenuta alla famiglia Florio, originariamente destinata alla produzione del vino, successivamente recuperata e adattata a spazio espositivo.
            </p>
            <p style="margin-bottom: 1rem;">
            All'interno del museo sono conservati reperti che coprono un arco cronologico compreso tra l'età arcaica e quella ellenistica, offrendo una lettura significativa della storia religiosa e architettonica di Selinunte. L'esposizione è incentrata in particolare sugli aspetti legati alla fede e ai culti dell'antica polis, mettendo in evidenza l'architettura sacra e i riti celebrati in onore delle divinità.
            </p>
            <p style="margin-bottom: 1rem;">
            Tra i materiali esposti assumono particolare rilievo gli esempi di architettura dorica, tra cui i resti del cosiddetto tempio Y, un tempio periptero di ubicazione originaria sconosciuta. I suoi elementi architettonici, riutilizzati in antico nelle fortificazioni di Porta Nord, sono stati ricomposti ed esposti sul fondo della grande sala museale, valorizzati dalla struttura ad archi trasversi dell'edificio.
            </p>
            <p style="margin-bottom: 1rem;">
            Di eccezionale importanza è il ritrovamento, avvenuto nell'agosto 2023, di una testa di leone in marmo pregiato, conservata in condizioni pressoché perfette. Si tratta di una sima, ossia l'elemento terminale superiore del tetto di un tempio, alta circa 62 centimetri e dal peso superiore ai 250 chilogrammi. La sua rarità è legata sia allo stato di conservazione sia al materiale, un marmo importato dalle isole greche, probabilmente da Paro, insolito per il IV secolo a.C., periodo in cui tali decorazioni erano generalmente realizzate in terracotta e solo successivamente in pietra. La sima svolgeva una duplice funzione, decorativa e pratica, poiché oltre ad abbellire l'edificio sacro permetteva il deflusso dell'acqua piovana attraverso beccucci scolpiti a forma di testa di leone. 
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Baglio Florio Museum is located within the Archaeological Park of Selinunte, adjacent to Temple G, one of the most imposing monuments of the ancient Greek city. The museum premises are housed in a nineteenth-century structure that belonged to the Florio family, originally intended for wine production and subsequently recovered and adapted as an exhibition space.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum preserves finds spanning a chronological range from the archaic to the Hellenistic period, offering a significant reading of the religious and architectural history of Selinunte. The exhibition focuses in particular on aspects related to the faith and cults of the ancient polis, highlighting sacred architecture and the rituals celebrated in honour of the deities.
            </p>
            <p style="margin-bottom: 1rem;">
            Among the displayed materials, particular importance attaches to the examples of Doric architecture, including the remains of the so-called Temple Y, a peripteral temple of unknown original location. Its architectural elements, reused in antiquity in the fortifications of the North Gate, have been reassembled and displayed at the far end of the museum's large hall, enhanced by the building's transverse arch structure.
            </p>
            <p style="margin-bottom: 1rem;">
            Of exceptional importance is the discovery, made in August 2023, of a lion's head in fine marble, preserved in near-perfect condition. It is a sima — the upper terminal element of a temple roof — approximately 62 centimetres tall and weighing over 250 kilograms. Its rarity is linked both to its state of preservation and to the material: a marble imported from the Greek islands, probably from Paros, unusual for the 4th century BC, a period in which such decorations were generally made in terracotta and only later in stone. The sima served a dual function, both decorative and practical: in addition to adorning the sacred building, it allowed rainwater to drain away through carved lion-head spouts.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Selinunte',
    'provincia': 'TP',
    'indirizzo': 'Via Selinunte - 91022 Selinunte (Tp)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 708,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 708,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/baglio-florio.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-19:30<br>Dom: 9:00-13:30',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-19:30<br>Sun: 9:00-13:30',
    'costo_biglietto': 'Intero €2.50, ridotto €2.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 2.50, reduced: € 2.00',
    'sito_web': 'https://www.visitbelice.it/punti-di-interesse/museo-baglio-florio/',
    'telefono': '+39 092446277',
    'email': 'parco.archeo.selinunte@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 33,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Regionale Agostino Pepoli',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Agostino Pepoli Regional Museum',
    'categorie': [
        'reperti-archeologici',
        'disegni-grafici-mappe',
        'sculture',
        'dipinti'
    ],
    'categorie_labels': [
        'Reperti archeologici',
        'Disegni, grafici, mappe',
        'Sculture',
        'Dipinti'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds',
        'Drawings, graphics, maps',
        'Sculptures',
        'Paintings'
    ],
    'descrizione_breve': 'Il Museo Regionale "Agostino Pepoli" di Trapani è uno dei principali musei della Sicilia occidentale, ospitato nell\'antico ex convento dei Padri Carmelitani. È nato agli inizi del Novecento su iniziativa del conte Agostino Pepoli e raccoglie collezioni artistiche e decorative che raccontano la cultura e l\'artigianato locale dal XIII al XIX secolo: pittura, scultura, opere in corallo, oro, argento e maiolica, presepi, paramenti sacri, arredi e cimeli storici.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The "Agostino Pepoli" Regional Museum of Trapani is one of the principal museums of western Sicily, housed in the ancient former convent of the Carmelite Fathers. Founded in the early twentieth century on the initiative of Count Agostino Pepoli, it brings together artistic and decorative collections that recount the local culture and craftsmanship from the 13th to the 19th century: paintings, sculptures, works in coral, gold, silver, and majolica, nativity scenes, sacred vestments, furnishings, and historical memorabilia.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Regionale Agostino Pepoli di Trapani è uno dei più importanti musei della Sicilia ed è un museo della Regione Siciliana. Ha sede nell'antico convento trecentesco dei Carmelitani, adiacente alla basilica santuario di Maria Santissima Annunziata, in un contesto architettonico di grande valore storico e artistico per la città.
            </p>
            <p style="margin-bottom: 1rem;">
            Nato tra il 1906 e il 1908 come museo civico per iniziativa del conte Agostino Sieri Pepoli, il museo ebbe origine dalla sua collezione privata, successivamente arricchita dai dipinti di scuola napoletana donati dal generale Giovanbattista Fardella. Nel 1921 entrò a far parte delle collezioni anche la raccolta del conte Francesco Hernandez di Erice, comprendente presepi, ceramiche e reperti archeologici. Nel 1925 il museo divenne Regio Museo, dopo la seconda guerra mondiale Museo Nazionale e, dal 1977, museo della Regione Siciliana a seguito del trasferimento delle competenze sui beni culturali all'ente regionale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo, di carattere interdisciplinare, si articola in diverse sezioni che comprendono marmi e lapidi, dipinti, arti industriali, scultura rinascimentale e memorie del Risorgimento, offrendo una visione ampia e articolata della storia artistica, culturale e civile del territorio trapanese.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo ospita una ricchissima collezione di arti decorative, sculture e opere in corallo, argenti e manufatti presepiali, oltre a una prestigiosa pinacoteca che comprende, tra gli altri, Le Stimmate di San Francesco di Tiziano, un ritratto di Nunzio Nasi di Giacomo Balla, una Madonna con Bambino e angeli del XV secolo di scuola valenciana, una Pietà del 1380 di Roberto d'Oderisio e un Sant'Andrea del fiammingo Geronimo Gerardi. Di particolare rilievo è anche il Tesoro della Madonna di Trapani, frutto di secolari donazioni votive.
            </p>
            <p style="margin-bottom: 1rem;">
            Accanto alle opere d'arte, il museo conserva reperti archeologici rinvenuti nella provincia di Trapani e una significativa sezione dedicata al Risorgimento, con cimeli storici legati alla partecipazione della città all'Unità d'Italia, tra cui il vessillo del piroscafo garibaldino "Il Lombardo", busti marmorei di Giuseppe Garibaldi, Vittorio Emanuele II e Cavour, nonché una ghigliottina di epoca borbonica. Grazie alla ricchezza delle collezioni e alla varietà dei materiali esposti, il Museo Regionale Agostino Pepoli rappresenta oggi un punto di riferimento fondamentale per la conoscenza della storia e dell'identità culturale della Sicilia occidentale.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Agostino Pepoli Regional Museum of Trapani is one of the most important museums in Sicily and belongs to the Sicilian Region. It is housed in the ancient fourteenth-century Carmelite convent, adjacent to the basilica sanctuary of Maria Santissima Annunziata, in an architectural setting of great historical and artistic value for the city.
            </p>
            <p style="margin-bottom: 1rem;">
            Founded between 1906 and 1908 as a civic museum on the initiative of Count Agostino Sieri Pepoli, the museum originated from his private collection, subsequently enriched by Neapolitan school paintings donated by General Giovanbattista Fardella. In 1921 the collection of Count Francesco Hernandez of Erice also joined the holdings, comprising nativity scenes, ceramics, and archaeological finds. In 1925 the museum became a Royal Museum; after the Second World War it became a National Museum and, from 1977, a museum of the Sicilian Region following the transfer of cultural heritage responsibilities to the regional authority.
            </p>
            <p style="margin-bottom: 1rem;">
            The interdisciplinary exhibition route is structured across several sections encompassing marbles and stone inscriptions, paintings, industrial arts, Renaissance sculpture, and Risorgimento memorabilia, offering a broad and articulate vision of the artistic, cultural, and civic history of the Trapani territory.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum houses an extraordinarily rich collection of decorative arts, sculptures, and works in coral, silverware, and nativity scene artefacts, alongside a prestigious picture gallery that includes, among others, Titian's Stigmata of Saint Francis, a portrait of Nunzio Nasi by Giacomo Balla, a 15th-century Madonna and Child with Angels from the Valencian school, a Pietà of 1380 by Roberto d'Oderisio, and a Saint Andrew by the Flemish painter Geronimo Gerardi. Of particular significance is also the Treasury of the Madonna of Trapani, the fruit of centuries of votive offerings.
            </p>
            <p style="margin-bottom: 1rem;">
            Alongside the artworks, the museum preserves archaeological finds from the province of Trapani and a significant section dedicated to the Risorgimento, with historical memorabilia connected to the city's participation in Italian Unification, including the flag of the Garibaldian steamship "Il Lombardo", marble busts of Giuseppe Garibaldi, Vittorio Emanuele II, and Cavour, as well as a Bourbon-era guillotine. Thanks to the richness of its collections and the variety of materials on display, the Agostino Pepoli Regional Museum today represents a fundamental point of reference for the knowledge of the history and cultural identity of western Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Trapani',
    'provincia': 'TP',
    'indirizzo': 'Via Conte Agostino Pepoli 180 - 91100 Trapani (TP)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 705,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 320,
        },
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 10,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 225,
        },
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 150,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/agostino-pepoli.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-18:00<br>Dom: 9:00-13:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-18:00<br>Sun: 9:00-13:00',
    'costo_biglietto': 'Intero €8.00, ridotto €4.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 8.00, reduced: € 4.00',
    'sito_web': 'https://www2.regione.sicilia.it/beniculturali/museopepoli/museopepoli.html',
    'telefono': '+39 0923 553269',
    'email': 'museo.pepoli@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 34,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Regionale di Adrano',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Museum of Adrano',
    'categorie': [
        'reperti-archeologici',
        'disegni-grafici-mappe'
    ],
    'categorie_labels': [
        'Reperti archeologici',
        'Disegni, grafici, mappe'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds',
        'Drawings, graphics, maps'
    ],
    'descrizione_breve': 'Il Museo Regionale di Adrano è un museo archeologico e storico ospitato nel Castello Normanno nel centro di Adrano. Mostra ricche collezioni di reperti che raccontano la storia del territorio dalla Preistoria al Medioevo, dalla ceramica neolitica e oggetti dell\'età del Rame e del Bronzo, fino alle testimonianze greche, romane e medievali.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Museum of Adrano is an archaeological and historical museum housed in the Norman Castle in the centre of Adrano. It displays rich collections of finds recounting the history of the territory from Prehistory to the Middle Ages, from Neolithic ceramics and Copper and Bronze Age objects through to Greek, Roman, and medieval testimonies.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Regionale di Adrano è ospitato all'interno del monumentale Castello Normanno, imponente edificio medievale che domina la piazza principale della città e costituisce uno dei simboli storici più riconoscibili del territorio etneo. La scelta di questa sede conferisce al museo un forte valore identitario, mettendo in dialogo diretto il contenitore architettonico con le collezioni che raccontano la lunga storia dell'area di Adrano e della Sicilia centro-orientale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo conserva ed espone materiali provenienti sia da scavi archeologici sistematici sia da recuperi occasionali, comprendendo reperti rinvenuti nel territorio adranita e, per effetto della sua storia, anche in altre zone della Sicilia orientale. Accanto alle raccolte archeologiche, che costituiscono il nucleo principale dell'istituzione, il museo ospita una biblioteca, un archivio e una sezione dedicata alle collezioni storico-artistiche, configurandosi come un vero centro di documentazione e studio del territorio.
            </p>
            <p style="margin-bottom: 1rem;">
            Le origini del museo risalgono ai primi anni del Novecento. Nel 1902 il reverendo Salvatore Petronio Russo, appassionato studioso della storia locale, fondò il primo museo archeologico di Adrano, ospitato nella propria abitazione. Alla morte del fondatore, tuttavia, gran parte di questa prima collezione andò dispersa, anche se alcuni reperti sono oggi conservati tra i pezzi più significativi del museo attuale.
            </p>
            <p style="margin-bottom: 1rem;">
            Nel periodo tra le due guerre mondiali venne allestito un secondo museo presso il Regio Ginnasio-Liceo "Giovanni Verga", ma anche questa esperienza ebbe esito sfortunato: i bombardamenti della Seconda guerra mondiale causarono la perdita di molti materiali. Solo nel secondo dopoguerra, grazie all'impegno di studiosi e appassionati locali, l'idea di un museo adranita tornò a concretizzarsi, passando attraverso sedi provvisorie e modeste fino alla svolta del 1958, quando l'Amministrazione comunale destinò il Castello Normanno a sede museale.
            </p>
            <p style="margin-bottom: 1rem;">
            Pochi anni dopo, la Soprintendenza Archeologica di Siracusa istituì ufficialmente l'Antiquarium statale di Adrano. Negli anni successivi, interventi di restauro e ampliamento degli spazi consentirono una migliore sistemazione dei materiali, che si arricchirono grazie a nuove scoperte archeologiche, donazioni e scavi condotti non solo nel territorio adranita ma anche in altre aree della Sicilia orientale.
            </p>
            <p style="margin-bottom: 1rem;">
            Oggi il Museo Regionale di Adrano si presenta come un'istituzione di grande valore storico e scientifico, capace di raccontare, attraverso reperti e documenti, la complessa stratificazione culturale del territorio etneo. Inserito in un contesto architettonico di straordinario rilievo, il museo rappresenta un luogo privilegiato per comprendere la continuità insediativa, le tradizioni e le trasformazioni che hanno segnato Adrano dall'antichità fino all'età storica.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Museum of Adrano is housed within the monumental Norman Castle, an imposing medieval building that dominates the city's main square and stands as one of the most recognisable historical symbols of the Etna area. The choice of this venue lends the museum a strong sense of identity, establishing a direct dialogue between the architectural setting and the collections that recount the long history of the Adrano area and central-eastern Sicily.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum preserves and displays materials from both systematic archaeological excavations and chance recoveries, including finds unearthed in the Adrano territory and, by virtue of its history, in other parts of eastern Sicily as well. Alongside the archaeological collections — which form the principal core of the institution — the museum houses a library, an archive, and a section dedicated to historical and artistic collections, functioning as a true centre for documentation and study of the territory.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum's origins date back to the early twentieth century. In 1902 the Reverend Salvatore Petronio Russo, a passionate scholar of local history, founded the first archaeological museum of Adrano, housed in his own home. After the founder's death, however, much of this first collection was dispersed, although some finds are today among the most significant pieces in the current museum.
            </p>
            <p style="margin-bottom: 1rem;">
            In the interwar period a second museum was established at the Royal Grammar and High School "Giovanni Verga", but this experience also met with an unfortunate end: the bombing raids of the Second World War caused the loss of many materials. Only in the post-war period, through the efforts of local scholars and enthusiasts, did the idea of a museum in Adrano take shape again, passing through provisional and modest premises until the turning point of 1958, when the Municipal Administration designated the Norman Castle as the museum's home.
            </p>
            <p style="margin-bottom: 1rem;">
            A few years later, the Archaeological Superintendency of Syracuse officially established the state Antiquarium of Adrano. In subsequent years, restoration and expansion works allowed for a better arrangement of the materials, which were further enriched by new archaeological discoveries, donations, and excavations conducted not only in the Adrano territory but also in other areas of eastern Sicily.
            </p>
            <p style="margin-bottom: 1rem;">
            Today the Regional Museum of Adrano presents itself as an institution of great historical and scientific value, capable of recounting, through finds and documents, the complex cultural stratification of the Etna territory. Set within an architecturally extraordinary context, the museum represents a privileged place for understanding the continuity of settlement, the traditions, and the transformations that have marked Adrano from antiquity through to the historical age.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Adrano',
    'provincia': 'CT',
    'indirizzo': 'Piazza Umberto I - 95031 Adrano (CT)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 3535,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 2865,
        },
        {
            'nome': 'Disegni, grafici e mappe',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Drawings, graphics and maps',
            'quantita': 670,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-adrano.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Sab: 9:00-18:00<br>Dom: 9:00-13:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sat: 9:00-18:00<br>Sun: 9:00-13:00',
    'costo_biglietto': 'Intero €6.00, ridotto €3.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 6.00, reduced: € 3.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/catania-valle-aci/biglietti/area-archeologica-e-museo-regionale-di-adrano-adrano/',
    'telefono': '+39 0957 602608',
    'email': 'parco.archeo.catania@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 35,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo della Ceramica di Caltagirone',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Museum of Ceramics of Caltagirone',
    'categorie': [
        'reperti-archeologici',
        'sculture'
    ],
    'categorie_labels': [
        'Reperti archeologici',
        'Sculture'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds',
        'Sculptures'
    ],
    'descrizione_breve': 'Il Museo Regionale della Ceramica di Caltagirone è uno dei più importanti musei italiani dedicati alla storia dell\'arte ceramica. Documenta la produzione di ceramiche siciliane dalla preistoria fino ai primi del Novecento, con una collezione di oltre 2.500 reperti che mostrano tecniche, stili e forme antiche e moderne legate soprattutto alla tradizione calatina. La collezione comprende pezzi archeologici, ceramiche medievali, maioliche rinascimentali e barocche, oltre a vasi decorativi, oggetti d\'uso e opere di maestri locali.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Museum of Ceramics of Caltagirone is one of the most important Italian museums dedicated to the history of ceramic art. It documents Sicilian ceramic production from prehistory to the early twentieth century, with a collection of over 2,500 items showcasing ancient and modern techniques, styles, and forms linked above all to the Calatino tradition. The collection includes archaeological pieces, medieval ceramics, Renaissance and Baroque majolica, as well as decorative vases, everyday objects, and works by local masters.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo della Ceramica di Caltagirone è una delle istituzioni museali più importanti d'Italia dedicate all'arte ceramica e rappresenta, insieme al Museo Internazionale delle Ceramiche di Faenza, un punto di riferimento imprescindibile per la conoscenza di questa forma espressiva. Museo regionale della Sicilia, esso racconta una tradizione produttiva millenaria che ha reso Caltagirone uno dei centri ceramici più celebri del Mediterraneo.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo conserva ed espone circa 2.500 reperti, offrendo un percorso straordinariamente ampio che va dal IV millennio a.C. fino all'età contemporanea. La collezione consente di seguire l'evoluzione tecnica, stilistica e simbolica della ceramica siciliana, mettendo in luce continuità, innovazioni e contaminazioni culturali che si sono succedute nel tempo.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso espositivo è articolato in sette sezioni, pensate per offrire una lettura chiara e progressiva della storia della ceramica. La sala didattica introduce il visitatore alla produzione ceramica dalla preistoria ai giorni nostri, con reperti emblematici come un cratere attico a figure rosse del V secolo a.C., raffigurante una bottega di vasaio sotto la protezione di Atena, rinvenuto in una fornace attiva a Caltagirone in età greca.
            </p>
            <p style="margin-bottom: 1rem;">
            Le sezioni successive presentano le ceramiche preistoriche, protostoriche, sicule, siceliote, greche e bizantine, con manufatti di grande valore archeologico provenienti da numerosi siti del territorio, oltre a importanti testimonianze funerarie e a una selezione di ceramiche figurate e vetri romani. Un patio è dedicato ai modellini di forni medievali, che illustrano le tecniche produttive in età normanna e angioino-aragonese.
            </p>
            <p style="margin-bottom: 1rem;">
            Un ampio spazio è riservato alla ceramica medievale, con manufatti siculo-arabi e normanni che documentano la nascita e l'evoluzione della maiolica, dalle prime invetriature piombifere fino allo sviluppo dello smalto vero e proprio. Seguono le sezioni dedicate alla ceramica rinascimentale e barocca, con maioliche da mensa, oggetti liturgici, anfore, acquasantiere e decorazioni plastiche, spesso caratterizzate da una ricca iconografia religiosa e floreale.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso culmina in una grande sala che offre una panoramica completa della maiolica siciliana dal XVII al XIX secolo, con vasi ornamentali, albarelli, pavimenti maiolicati, lucerne antropomorfe e oggetti di uso quotidiano reinterpretati in chiave artistica. Di particolare rilievo sono le ceramiche d'autore, tra cui le terrecotte figurate di Giacomo Bongiovanni e i gruppi scultorei di Giuseppe Vaccaro e Giuseppe Failla, che testimoniano la vitalità artistica della produzione calatina tra Settecento e Ottocento.
            </p>
            <p style="margin-bottom: 1rem;">
            Il Museo della Ceramica di Caltagirone non è soltanto uno spazio espositivo, ma anche un centro di divulgazione e formazione, grazie a servizi didattici e strumenti multimediali che favoriscono una comprensione approfondita delle tecniche e del valore culturale della ceramica. Nel suo insieme, il museo si configura come una sintesi perfetta tra storia, arte e identità territoriale, celebrando una tradizione che ancora oggi rappresenta uno dei simboli più riconoscibili della Sicilia.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Museum of Ceramics of Caltagirone is one of the most important museum institutions in Italy dedicated to ceramic art and represents, alongside the International Museum of Ceramics in Faenza, an indispensable point of reference for the understanding of this expressive form. As a regional museum of Sicily, it recounts a millennia-old productive tradition that has made Caltagirone one of the most celebrated ceramic centres of the Mediterranean.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum preserves and displays approximately 2,500 items, offering an extraordinarily broad route spanning from the 4th millennium BC to the contemporary age. The collection allows visitors to trace the technical, stylistic, and symbolic evolution of Sicilian ceramics, highlighting the continuities, innovations, and cultural cross-fertilisations that have succeeded one another over time.
            </p>
            <p style="margin-bottom: 1rem;">
            The exhibition route is structured in seven sections, designed to offer a clear and progressive reading of the history of ceramics. The educational room introduces the visitor to ceramic production from prehistory to the present day, with emblematic pieces such as a 5th-century BC Attic red-figure krater depicting a potter's workshop under the protection of Athena, found in a kiln active in Caltagirone during the Greek period.
            </p>
            <p style="margin-bottom: 1rem;">
            The subsequent sections present prehistoric, protohistoric, Sicel, Siceliote, Greek, and Byzantine ceramics, with artefacts of great archaeological value from numerous sites in the territory, alongside important funerary testimonies and a selection of figured ceramics and Roman glass. A patio is dedicated to models of medieval kilns, illustrating production techniques in the Norman and Angevin-Aragonese periods.
            </p>
            <p style="margin-bottom: 1rem;">
            Extensive space is devoted to medieval ceramics, with Siculo-Arab and Norman artefacts documenting the birth and evolution of majolica, from the earliest lead glazes to the development of true tin-glaze enamel. This is followed by sections dedicated to Renaissance and Baroque ceramics, featuring tableware majolica, liturgical objects, amphorae, holy water stoups, and plastic decorations, often characterised by a rich religious and floral iconography.
            </p>
            <p style="margin-bottom: 1rem;">
            The route culminates in a large hall offering a comprehensive overview of Sicilian majolica from the 17th to the 19th century, with ornamental vases, albarelli, majolica floor tiles, anthropomorphic oil lamps, and everyday objects reinterpreted in an artistic key. Of particular note are the works of individual artists, including the figured terracottas of Giacomo Bongiovanni and the sculptural groups of Giuseppe Vaccaro and Giuseppe Failla, which attest to the artistic vitality of Calatino production between the eighteenth and nineteenth centuries.
            </p>
            <p style="margin-bottom: 1rem;">
            The Museum of Ceramics of Caltagirone is not merely an exhibition space, but also a centre for public engagement and education, thanks to educational services and multimedia tools that foster an in-depth understanding of ceramic techniques and cultural value. Taken as a whole, the museum stands as a perfect synthesis of history, art, and territorial identity, celebrating a tradition that to this day remains one of the most recognisable symbols of Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Caltagirone',
    'provincia': 'CT',
    'indirizzo': 'Via Giardini Pubblici - 95041 Caltagirone (CT)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 3008,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 600,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 2408,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/ceramica-caltagirone.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-18:30',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-18:30',
    'costo_biglietto': 'Intero €3,00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 3.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/catania-valle-aci/biglietti/museo-della-ceramica-caltagirone/',
    'telefono': '+39 093358418',
    'email': 'urp.parco.archeo.catania@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 36,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Ibleo',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Ibleo Archaeological Museum',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico Ibleo di Ragusa è un museo dedicato alla storia e all\'archeologia del territorio ibleo, con reperti che vanno dalla Preistoria alla tarda Antichità. Espone oltre 5.000 oggetti organizzati in sei sezioni cronologiche, con pezzi significativi come la lastra con il "Guerriero di Castiglione", fornaci antiche e mosaici paleocristiani che ricostruiscono la storia culturale del territorio.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Ibleo Archaeological Museum of Ragusa is a museum dedicated to the history and archaeology of the Ibleo territory, with finds ranging from Prehistory to Late Antiquity. It displays over 5,000 objects organised in six chronological sections, including significant pieces such as the slab with the "Warrior of Castiglione", ancient kilns, and early Christian mosaics that reconstruct the cultural history of the territory.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Ibleo di Ragusa rappresenta il principale punto di riferimento per la conoscenza della storia antica e dell'archeologia del territorio ibleo. Situato in via Natalelli, nei pressi di via Roma e in adiacenza alla testata nord del ponte nuovo, il museo occupa il primo piano del Palazzo Mediterraneo, edificio realizzato alla fine degli anni Cinquanta e concepito per accogliere funzioni culturali ed espositive.
            </p>
            <p style="margin-bottom: 1rem;">
            Il percorso museale è dedicato alla ricostruzione della lunga vicenda storica della provincia di Ragusa, coprendo un arco cronologico che va dal Neolitico fino alla tarda antichità. Attraverso reperti provenienti da scavi e rinvenimenti dell'area iblea, il museo restituisce un quadro articolato delle diverse fasi di popolamento e delle trasformazioni culturali che hanno interessato il territorio nel corso dei millenni.
            </p>
            <p style="margin-bottom: 1rem;">
            Particolare attenzione è riservata alle comunità siculi, documentate da materiali provenienti da abitati e necropoli, che testimoniano l'organizzazione sociale e le pratiche funerarie delle popolazioni indigene prima e durante il contatto con il mondo greco. Tra i reperti più celebri spicca il cosiddetto Guerriero di Castiglione, figura di grande valore simbolico e identitario, che rappresenta uno dei manufatti più noti dell'intero museo.
            </p>
            <p style="margin-bottom: 1rem;">
            Di notevole interesse è anche la sezione dedicata alla Kamarina antica, con materiali provenienti da una delle sue necropoli, che permettono di approfondire i rapporti tra le popolazioni indigene dell'interno e la colonia greca costiera. A questi si affiancano testimonianze della vita quotidiana e delle attività produttive del territorio, tra cui una fornace per la cottura dell'argilla proveniente dal sito di Scornavacche, ricostruita fedelmente all'interno del museo: un elemento di grande impatto didattico, che consente di comprendere concretamente le tecniche artigianali antiche.
            </p>
            <p style="margin-bottom: 1rem;">
            Nel suo insieme, il Museo Archeologico Ibleo si configura come un museo territoriale di forte valore scientifico e divulgativo, capace di raccontare la storia dell'altopiano ibleo attraverso oggetti, strutture ricostruite e contesti archeologici significativi. Pur nelle dimensioni contenute, esso svolge un ruolo fondamentale nella tutela e nella valorizzazione del patrimonio archeologico della Sicilia sud-orientale, offrendo al visitatore una chiave di lettura completa e coerente del passato più remoto di Ragusa e del suo comprensorio.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Ibleo Archaeological Museum of Ragusa is the principal point of reference for the knowledge of the ancient history and archaeology of the Ibleo territory. Located in Via Natalelli, near Via Roma and adjacent to the northern end of the new bridge, the museum occupies the first floor of the Palazzo Mediterraneo, a building constructed in the late 1950s and conceived to house cultural and exhibition functions.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum route is dedicated to reconstructing the long historical story of the province of Ragusa, covering a chronological span from the Neolithic to Late Antiquity. Through finds from excavations and discoveries in the Ibleo area, the museum provides an articulate picture of the various phases of settlement and the cultural transformations that have affected the territory over the millennia.
            </p>
            <p style="margin-bottom: 1rem;">
            Particular attention is devoted to the Sicel communities, documented by materials from settlements and necropolises that attest to the social organisation and funerary practices of the indigenous populations before and during their contact with the Greek world. Among the most celebrated finds stands the so-called Warrior of Castiglione, a figure of great symbolic and identity value that represents one of the best-known artefacts in the entire museum.
            </p>
            <p style="margin-bottom: 1rem;">
            Of considerable interest is also the section dedicated to ancient Kamarina, with materials from one of its necropolises that allow visitors to explore the relations between the indigenous inland populations and the Greek coastal colony. Alongside these are testimonies of everyday life and productive activities in the territory, including a clay-firing kiln from the site of Scornavacche, faithfully reconstructed inside the museum — an element of great educational impact that concretely conveys the ancient craft techniques.
            </p>
            <p style="margin-bottom: 1rem;">
            Taken as a whole, the Ibleo Archaeological Museum stands as a territorial museum of strong scientific and educational value, capable of recounting the history of the Ibleo plateau through objects, reconstructed structures, and significant archaeological contexts. Despite its contained size, it plays a fundamental role in the protection and promotion of the archaeological heritage of south-eastern Sicily, offering the visitor a complete and coherent key to understanding the most remote past of Ragusa and its surrounding area.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Ragusa',
    'provincia': 'RG',
    'indirizzo': 'Via Natalelli - 97100 Ragusa (RG)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 100,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 100,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-ibleo.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Lun-Dom: 9:00-19:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Mon-Sun: 9:00-19:00',
    'costo_biglietto': 'Intero €6.00, ridotto €3.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 6.00, reduced: € 3.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/kamarina-cava-ispica/siti-archeologici/museo-archeologico-ibleo-ragusa/',
    'telefono': '+39 0932 622963',
    'email': 'parco.archeo.kamarina@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 37,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico di Kamarina',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Archaeological Museum of Kamarina',
    'categorie': [
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Regionale di Kamarina è il museo archeologico collegato al Parco Archeologico di Kamarina, dedicato ai rinvenimenti dell\'antica città greca di Kamarina. Ospita una ricca collezione di reperti che vanno dalla Preistoria all\'età romana, incluse anfore commerciali, ceramiche, corredi delle necropoli locali, oggetti faunistici e preistorici e testimonianze di vita e commercio della città antica.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Museum of Kamarina is the archaeological museum connected to the Archaeological Park of Kamarina, dedicated to finds from the ancient Greek city of Kamarina. It houses a rich collection of items ranging from Prehistory to the Roman period, including commercial amphorae, ceramics, grave goods from local necropolises, faunal and prehistoric objects, and testimonies of the life and trade of the ancient city.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale di Kamarina, situato nei pressi di Scoglitti, in provincia di Ragusa, è stato per lungo tempo uno dei principali luoghi di riferimento per la conoscenza dell'antica città greca di Kamarina e del suo territorio. Organizzato in tre padiglioni e sette sale espositive, il museo offriva un percorso articolato e di grande valore scientifico, capace di integrare archeologia terrestre e subacquea. Oggi il museo risulta definitivamente chiuso, ma le sue collezioni e il suo impianto espositivo restano fondamentali per la ricostruzione storica del sito.
            </p>
            <p style="margin-bottom: 1rem;">
            Uno degli elementi più distintivi del museo era il padiglione di archeologia subacquea, che documentava in modo approfondito i traffici e la vita marittima lungo la costa camarinese. I reperti esposti provenivano da numerosi relitti individuati e indagati negli anni Novanta del Novecento nel mare antistante l'antica polis. Tra i materiali di maggiore rilievo figuravano elmi greci e italici, anfore da trasporto, ceramiche fini, strumenti di bordo e migliaia di monete, tra cui un eccezionale complesso di antoniniani in bronzo. Particolarmente suggestive erano le testimonianze dei relitti di età romana imperiale, come quello di Afrodite, con una raffinata statuetta bronzea della dea, e quello delle Colonne, da cui provengono oggetti di uso quotidiano e di pregio, che restituiscono un vivido spaccato della navigazione antica.
            </p>
            <p style="margin-bottom: 1rem;">
            Il padiglione orientale era dedicato alla storia più antica del territorio e alla fase arcaica della città. La sala della preistoria illustrava gli insediamenti dell'età del Bronzo, attraverso strumenti litici riconducibili alla cultura di Castelluccio, rinvenuti sia lungo la costa sia nell'entroterra. Seguiva la sezione dedicata alla Kamarina arcaica, con ricchi corredi funerari provenienti dalla necropoli di Rifriscolaro: vasi figurati, ceramiche corinzie e manufatti di grande qualità che documentavano i contatti culturali e commerciali della colonia nei secoli VI e V a.C.
            </p>
            <p style="margin-bottom: 1rem;">
            Un ruolo centrale era occupato dalle sale dedicate ai culti e all'architettura sacra. La cosiddetta Sala Persefone illustrava il santuario di Demetra e Kore, scavato da Paolo Orsi alla fine dell'Ottocento, attraverso statuette votive, protomi e arule che testimoniano la diffusione dei culti agrari e ctonii. La sala del tempio di Atena consentiva invece di leggere direttamente le strutture architettoniche dell'edificio sacro, con fondazioni, rampe e crepidomi che restituivano la monumentalità del complesso templare.
            </p>
            <p style="margin-bottom: 1rem;">
            Nel padiglione occidentale il percorso si concentrava sulla Kamarina di età classica, mettendo in evidenza l'organizzazione urbanistica della città, l'agorà e la rete viaria, oltre alla monetazione locale, uno degli elementi identitari più forti della polis. L'itinerario si concludeva con la grande sala dedicata alla necropoli di Passo Marinaro, dove erano esposti numerosi corredi funerari del V e IV secolo a.C., caratterizzati da ceramiche attiche a figure nere e a vernice nera, lucerne e oggetti rituali, affiancati da ricostruzioni e plastici del sito e della chora agricola.
            </p>
            <p style="margin-bottom: 1rem;">
            Nonostante la chiusura definitiva, il Museo Archeologico Regionale di Kamarina rimane un punto di riferimento essenziale nella storia della musealizzazione del patrimonio archeologico siciliano. Il suo progetto espositivo ha rappresentato un modello di integrazione tra scavo, territorio e racconto museale, contribuendo in modo decisivo alla valorizzazione scientifica e culturale di uno dei più importanti centri della Sicilia greca.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Archaeological Museum of Kamarina, situated near Scoglitti in the province of Ragusa, was for a long time one of the principal points of reference for knowledge of the ancient Greek city of Kamarina and its territory. Organised across three pavilions and seven exhibition rooms, the museum offered an articulate route of great scientific value, capable of integrating terrestrial and underwater archaeology. Today the museum is permanently closed, but its collections and exhibition layout remain fundamental for the historical reconstruction of the site.
            </p>
            <p style="margin-bottom: 1rem;">
            One of the museum's most distinctive features was the underwater archaeology pavilion, which provided an in-depth documentation of maritime trade and life along the Kamarina coast. The displayed finds came from numerous shipwrecks identified and investigated in the 1990s in the sea off the ancient polis. Among the most significant materials were Greek and Italic helmets, transport amphorae, fine ceramics, navigational instruments, and thousands of coins, including an exceptional assemblage of bronze antoniniani. Particularly evocative were the testimonies from Imperial Roman shipwrecks, such as the Aphrodite wreck — which yielded a refined bronze statuette of the goddess — and the Colonne wreck, from which everyday and luxury objects were recovered that provide a vivid glimpse of ancient seafaring.
            </p>
            <p style="margin-bottom: 1rem;">
            The eastern pavilion was dedicated to the earliest history of the territory and the archaic phase of the city. The prehistory room illustrated Bronze Age settlements through lithic tools attributable to the Castelluccio culture, found both along the coast and in the hinterland. This was followed by the section devoted to archaic Kamarina, with rich funerary assemblages from the Rifriscolaro necropolis: figured vases, Corinthian ceramics, and high-quality artefacts documenting the cultural and commercial contacts of the colony in the 6th and 5th centuries BC.
            </p>
            <p style="margin-bottom: 1rem;">
            A central role was played by the rooms dedicated to cults and sacred architecture. The so-called Persephone Room illustrated the sanctuary of Demeter and Kore, excavated by Paolo Orsi at the end of the nineteenth century, through votive statuettes, protomes, and arulae attesting to the spread of agrarian and chthonic cults. The room of the Temple of Athena, in turn, allowed visitors to read directly the architectural structures of the sacred building, with foundations, ramps, and crepidomas that conveyed the monumentality of the temple complex.
            </p>
            <p style="margin-bottom: 1rem;">
            In the western pavilion the route focused on Kamarina in the classical period, highlighting the city's urban layout, the agora, and the road network, as well as the local coinage — one of the strongest elements of the polis's identity. The itinerary concluded with the large hall dedicated to the Passo Marinaro necropolis, where numerous funerary assemblages of the 5th and 4th centuries BC were displayed, featuring Attic black-figure and black-glaze ceramics, oil lamps, and ritual objects, accompanied by reconstructions and scale models of the site and the agricultural chora.
            </p>
            <p style="margin-bottom: 1rem;">
            Despite its permanent closure, the Regional Archaeological Museum of Kamarina remains an essential point of reference in the history of the museumification of Sicilian archaeological heritage. Its exhibition design represented a model of integration between excavation, territory, and museum narrative, contributing decisively to the scientific and cultural promotion of one of the most important centres of Greek Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Scoglitti',
    'provincia': 'RG',
    'indirizzo': 'Strada Provinciale 102, Contrada Cammarana - 97019 Santa Croce Camarina (RG)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 100,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 100,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/kamarina.jpeg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Chiuso per lavori di restauro',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Closed for restoration works',
    'costo_biglietto': 'Intero €6.00, ridotto €3.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 6.00, reduced: € 3.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/kamarina-cava-ispica/biglietti/area-archeologica-e-museo-di-kamarina/',
    'telefono': '+39 3346040449',
    'email': 'parco.archeo.kamarina@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 38,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Galleria Regionale di Palazzo Bellomo',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Gallery of Palazzo Bellomo',
    'categorie': [
        'dipinti',
        'sculture'
    ],
    'categorie_labels': [
        'Dipinti',
        'Sculture'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Paintings',
        'Sculptures'
    ],
    'descrizione_breve': 'La Galleria Regionale di Palazzo Bellomo è un importante museo d\'arte situato nel centro storico di Ortigia a Siracusa, ospitato in un elegante edificio medievale originario dei secoli XIII–XIV con ampliamenti successivi. Espone una ricca collezione di arte figurativa, pittorica e decorativa che documenta la produzione artistica dal periodo bizantino, arabo‑normanno e medievale fino al XVIII secolo, con opere provenienti da chiese e conventi locali.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Gallery of Palazzo Bellomo is an important art museum located in the historic centre of Ortigia in Syracuse, housed in an elegant medieval building dating from the 13th–14th centuries with later additions. It displays a rich collection of figurative, pictorial, and decorative art documenting artistic production from the Byzantine, Arab-Norman, and medieval periods through to the 18th century, with works from local churches and convents.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            La Galleria Regionale di Palazzo Bellomo, situata nel cuore di Ortigia, rappresenta uno dei più significativi musei d'arte della Sicilia sud-orientale e un punto di riferimento essenziale per la conoscenza della produzione artistica medievale e moderna di Siracusa e del suo territorio. Inserita in un contesto urbano di straordinario valore storico, la galleria coniuga il fascino dell'architettura storica con un percorso espositivo di grande qualità.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo venne inaugurato nel 1948, in seguito alla separazione delle collezioni medievali e moderne da quelle archeologiche confluite nel Museo Paolo Orsi. Dopo una prima sistemazione museografica, l'allestimento definitivo prese forma negli anni Settanta e, a seguito di un lungo intervento di restauro e riallestimento, la galleria è stata riaperta al pubblico nel 2009 con un percorso rinnovato e più coerente dal punto di vista scientifico ed espositivo.
            </p>
            <p style="margin-bottom: 1rem;">
            Il contenitore museale è lo stesso Palazzo Bellomo, edificio di origine due-trecentesca, legato alla stagione sveva e successivamente rinnovato in età aragonese. Il palazzo conserva ancora oggi i segni delle sue diverse fasi costruttive: il pianterreno, con la struttura fortificata e il portale gotico, rimanda all'età sveva, mentre il piano superiore riflette i modelli del gotico civile catalano del Quattrocento, diffusi nel Mediterraneo occidentale. Questa stratificazione architettonica rende il palazzo non solo sede espositiva, ma parte integrante del racconto storico del museo.
            </p>
            <p style="margin-bottom: 1rem;">
            Le collezioni seguono un percorso cronologico che attraversa il Medioevo e l'età moderna, con opere di scultura, pittura e arti applicate provenienti da Siracusa e dalla sua provincia. Tra i pezzi di maggior rilievo figurano i sarcofagi dei Governatori della Camera Reginale, Giovanni Çabastida e Giovanni Cárdenas, importanti testimonianze della cultura funeraria e del potere amministrativo in età aragonese.
            </p>
            <p style="margin-bottom: 1rem;">
            Il fulcro della pinacoteca è rappresentato dalla celeberrima Annunciazione di Antonello da Messina (1474), uno dei capolavori assoluti del Rinascimento italiano, affiancata da opere di artisti come Antonello Gagini, Francesco Laurana, Mario Minniti, Guglielmo Borremans e Gaetano Zummo, che documentano l'evoluzione artistica dell'area siracusana tra Quattrocento e Settecento. Di particolare pregio sono anche le raccolte di argenti sacri, espressione della devozione e della raffinatezza artigianale delle chiese locali.
            </p>
            <p style="margin-bottom: 1rem;">
            Oggi la Galleria Regionale di Palazzo Bellomo si presenta come un museo moderno e accogliente, dotato di servizi per il pubblico come la libreria e la caffetteria, e si configura come un luogo privilegiato per comprendere la storia artistica di Siracusa, offrendo un'esperienza culturale che unisce arte, architettura e memoria urbana.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Gallery of Palazzo Bellomo, situated in the heart of Ortigia, represents one of the most significant art museums in south-eastern Sicily and an essential point of reference for the knowledge of the medieval and modern artistic production of Syracuse and its territory. Set within an urban context of extraordinary historical value, the gallery combines the appeal of historic architecture with an exhibition route of the highest quality.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum was inaugurated in 1948, following the separation of the medieval and modern collections from the archaeological ones that had flowed into the Paolo Orsi Museum. After an initial museographic arrangement, the definitive layout took shape in the 1970s and, following a lengthy restoration and rehang, the gallery was reopened to the public in 2009 with a renewed route, more coherent from a scientific and exhibition standpoint.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum premises are Palazzo Bellomo itself, a building of 13th-14th century origin, linked to the Swabian period and subsequently renovated in the Aragonese age. The palace still bears the marks of its various constructive phases: the ground floor, with its fortified structure and Gothic portal, evokes the Swabian era, while the upper floor reflects the models of 15th-century Catalan civic Gothic widespread in the western Mediterranean. This architectural layering makes the palace not merely an exhibition venue, but an integral part of the museum's historical narrative.
            </p>
            <p style="margin-bottom: 1rem;">
            The collections follow a chronological route spanning the Middle Ages and the modern period, with works of sculpture, painting, and applied arts from Syracuse and its province. Among the most outstanding pieces are the sarcophagi of the Governors of the Camera Reginale, Giovanni Çabastida and Giovanni Cárdenas, important testimonies of funerary culture and administrative power in the Aragonese period.
            </p>
            <p style="margin-bottom: 1rem;">
            The centrepiece of the picture gallery is the celebrated Annunciation by Antonello da Messina (1474), one of the absolute masterpieces of the Italian Renaissance, flanked by works by artists such as Antonello Gagini, Francesco Laurana, Mario Minniti, Guglielmo Borremans, and Gaetano Zummo, which document the artistic evolution of the Syracuse area between the 15th and 18th centuries. Of particular distinction are also the collections of sacred silverware, expressions of the devotion and craft refinement of the local churches.
            </p>
            <p style="margin-bottom: 1rem;">
            Today the Regional Gallery of Palazzo Bellomo presents itself as a modern and welcoming museum, equipped with public amenities such as a bookshop and a café, and stands as a privileged place for understanding the artistic history of Syracuse, offering a cultural experience that unites art, architecture, and urban memory.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Siracusa',
    'provincia': 'SR',
    'indirizzo': 'Via Capodieci 14/16 - 96100 Siracusa (SR)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 384,
    'composizione_beni': [
        {
            'nome': 'Dipinti',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Paintings',
            'quantita': 207,
        },
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 177,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/palazzo-bellomo.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-19:00<br>Dom: 09:00-13:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-19:00<br>Sun: 9:00-13:00',
    'costo_biglietto': 'Intero €10.00, ridotto €5.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 10.00, reduced: € 5.00',
    'sito_web': 'https://www.comune.siracusa.it/vivere-il-comune/luoghi/galleria-regionale-di-palazzo-bellomo#orari_apertura',
    'telefono': '+39 0931 69511',
    'email': 'urp.gall.bellomo@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/CulturalInstituteOrSite/ICCD_CF_8193522120261',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 39,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico di Lentini',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Archaeological Museum of Lentini',
    'categorie': [
        'beni-demoetno',
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Beni demoetnoantropologici',
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Ethno-anthropological heritage',
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico di Lentini è il museo regionale che racconta la storia antica di Lentini e del suo territorio, con reperti che coprono un arco cronologico dalla Preistoria all\'età medievale. Espone materiali provenienti dagli scavi dell\'antica colonia greca di Leontinoi e dai principali siti locali, tra cui ceramiche, oggetti di uso quotidiano, testimonianze delle necropoli, elementi dell\'abitato, delle fortificazioni e dei santuari periurbani.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Archaeological Museum of Lentini is the regional museum that recounts the ancient history of Lentini and its territory, with finds spanning a chronological range from Prehistory to the medieval period. It displays materials from excavations of the ancient Greek colony of Leontinoi and the principal local sites, including ceramics, everyday objects, testimonies from necropolises, and elements of the settlement, fortifications, and peri-urban sanctuaries.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale di Lentini è il principale luogo di conservazione e valorizzazione della storia antica di Lentini e del suo territorio, offrendo un percorso che attraversa millenni di civiltà, dalla preistoria fino all'età medievale. Il museo rappresenta un punto di riferimento fondamentale per la comprensione dell'antica Leontinoi, una delle più importanti poleis greche della Sicilia orientale, e del contesto storico-archeologico che la circonda.
            </p>
            <p style="margin-bottom: 1rem;">
            L'idea di istituire un museo a Lentini nasce già alla fine dell'Ottocento, quando Paolo Orsi, impegnato nella tutela del patrimonio archeologico siciliano, denunciò la dispersione e il traffico illecito dei reperti provenienti dall'area di Leontinoi. Negli anni successivi, grazie anche all'intervento di studiosi e ispettori locali, maturò la consapevolezza della necessità di creare una sede stabile che potesse custodire e proteggere le testimonianze archeologiche del territorio. Un primo nucleo museale vide la luce nel 1950 come Museo Civico, ma solo nel 1962 fu inaugurata l'attuale sede, progettata dall'architetto Vincenzo Cabianca e pensata specificamente per ospitare un'esposizione archeologica organica e scientificamente strutturata.
            </p>
            <p style="margin-bottom: 1rem;">
            Le collezioni del museo provengono in gran parte dalle campagne di scavo condotte nel secondo dopoguerra, in particolare nella valle San Mauro, nella zona delle necropoli e sul colle della Metapiccola, area di un importante insediamento indigeno dell'età del Ferro. A questi materiali si aggiungono i reperti emersi da ricerche più recenti effettuate nel territorio e nel tessuto urbano di Lentini, che hanno progressivamente arricchito e aggiornato il percorso espositivo.
            </p>
            <p style="margin-bottom: 1rem;">
            L'allestimento segue un criterio cronologico e topografico, accompagnando il visitatore dalle prime tracce di frequentazione umana del territorio, attraverso la fase della colonizzazione greca e lo sviluppo della città antica, fino alle trasformazioni dell'età tardo-romana, bizantina, araba e medievale. 
            </p>
            <p style="margin-bottom: 1rem;">
            Tra gli elementi di maggiore suggestione si segnala, all'ingresso del museo, l'affresco proveniente dalle Grotte del Crocifisso, raffigurante la Deposizione di Cristo. L'opera, rimossa dal contesto originario per ragioni conservative, è oggi esposta come testimonianza significativa della fase medievale e della continuità culturale del territorio.
            </p>
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico di Lentini si configura così come un luogo di memoria e di conoscenza, capace di raccontare la lunga storia del territorio lentinese attraverso reperti spesso poco noti ma di grande valore storico, contribuendo in modo significativo alla tutela e alla divulgazione del patrimonio archeologico della Sicilia sud-orientale.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Archaeological Museum of Lentini is the principal place for the conservation and promotion of the ancient history of Lentini and its territory, offering a route that traverses millennia of civilisation, from prehistory to the medieval period. The museum represents a fundamental point of reference for understanding ancient Leontinoi, one of the most important Greek poleis of eastern Sicily, and the historical-archaeological context that surrounds it.
            </p>
            <p style="margin-bottom: 1rem;">
            The idea of establishing a museum in Lentini dates back to the late nineteenth century, when Paolo Orsi, engaged in the protection of Sicilian archaeological heritage, denounced the dispersal and illicit trafficking of finds from the Leontinoi area. In the years that followed, thanks also to the intervention of local scholars and inspectors, awareness grew of the need to create a permanent home that could safeguard and protect the archaeological testimonies of the territory. A first museum nucleus came into being in 1950 as a Civic Museum, but only in 1962 was the current premises inaugurated, designed by architect Vincenzo Cabianca and conceived specifically to house an organic and scientifically structured archaeological exhibition.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum's collections derive largely from excavation campaigns conducted in the post-war period, particularly in the Valle San Mauro, in the necropolis zone, and on the hill of Metapiccola, the site of an important indigenous Iron Age settlement. These materials are supplemented by finds emerging from more recent research carried out in the territory and in the urban fabric of Lentini, which have progressively enriched and updated the exhibition route.
            </p>
            <p style="margin-bottom: 1rem;">
            The layout follows a chronological and topographical approach, guiding the visitor from the earliest traces of human presence in the territory, through the phase of Greek colonisation and the development of the ancient city, to the transformations of the late Roman, Byzantine, Arab, and medieval periods.
            </p>
            <p style="margin-bottom: 1rem;">
            Among the most evocative elements is the fresco from the Grotte del Crocifisso at the museum entrance, depicting the Deposition of Christ. The work, removed from its original context for conservation reasons, is today displayed as a significant testimony of the medieval phase and the cultural continuity of the territory.
            </p>
            <p style="margin-bottom: 1rem;">
            The Archaeological Museum of Lentini thus stands as a place of memory and knowledge, capable of recounting the long history of the Lentini territory through finds that are often little known but of great historical value, contributing significantly to the protection and dissemination of the archaeological heritage of south-eastern Sicily.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Lentini',
    'provincia': 'SR',
    'indirizzo': 'Via del Museo 1 - 96016 Lentini (SR)',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 6.0,
    'composizione_beni': [
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 5000,
        },
        {
            'nome': 'Beni demoetnoantropologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Ethno-anthropological heritage',
            'quantita': 1000,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/museo-lentini.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-17:00<br>Dom: 09:00-13:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-17:00<br>Sun: 9:00-13:00',
    'costo_biglietto': 'Intero €4.00, ridotto €2.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 4.00, reduced: € 2.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/leontinoi/siti-archeologici/museo-archeologico-di-lentini/',
    'telefono': '+39 0957 832962',
    'email': 'parco.archeo.leontinoi@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': '-',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

{
    'id': 40,

    # ========================================
    # INFORMAZIONI BASE
    # ========================================
    'titolo': 'Museo Archeologico Regionale "Paolo Orsi"',
    # EN: traduzione di 'titolo' — lasciare vuoto '' per usare il testo italiano
    'titolo_en': 'Regional Archaeological Museum "Paolo Orsi"',
    'categorie': [
        'beni-naturalistici',
        'sculture',
        'reperti-archeologici'
    ],
    'categorie_labels': [
        'Beni naturalistici',
        'Sculture',
        'Reperti archeologici'
    ],
    # EN: traduzione di 'categorie_labels' — lasciare vuoto '' per usare il testo italiano
    'categorie_labels_en': [
        'Natural heritage',
        'Sculptures',
        'Archaeological finds'
    ],
    'descrizione_breve': 'Il Museo Archeologico Regionale "Paolo Orsi" di Siracusa è uno dei più importanti musei archeologici d\'Europa, dedicato alla storia antica della Sicilia orientale dalla preistoria fino all\'età greco‑romana e paleocristiana. Il museo conserva vastissime collezioni di reperti archeologici, tra cui strumenti e oggetti delle culture preistoriche, ceramiche, statue arcaiche, rilievi, corredi funerari e materiali provenienti dagli scavi delle principali città antiche isolane.',
    # EN: traduzione di 'descrizione_breve' — lasciare vuoto '' per usare il testo italiano
    'descrizione_breve_en': 'The Regional Archaeological Museum "Paolo Orsi" of Syracuse is one of the most important archaeological museums in Europe, dedicated to the ancient history of eastern Sicily from prehistory through to the Greco-Roman and early Christian periods. The museum holds vast collections of archaeological finds, including tools and objects from prehistoric cultures, ceramics, archaic statues, reliefs, funerary assemblages, and materials from excavations of the principal ancient cities of the island.',
    'descrizione_completa': '''
            <p style="margin-bottom: 1rem;">
            Il Museo Archeologico Regionale Paolo Orsi di Siracusa rappresenta uno dei più importanti poli culturali del Mediterraneo e una tappa fondamentale per la conoscenza della storia antica della Sicilia. Intitolato all'archeologo Paolo Orsi, che ne fu direttore per quasi quarant'anni e protagonista di decisive campagne di scavo nell'isola orientale, il museo racconta un arco cronologico vastissimo che va dalla preistoria fino all'età romana e paleocristiana.
            </p>
            <p style="margin-bottom: 1rem;">
            La storia del museo affonda le radici nel Settecento, quando nacque come raccolta del Seminario, per poi trasformarsi nel corso dell'Ottocento in Museo Civico e successivamente in Museo Archeologico Nazionale. Nel Novecento, anche grazie all'intensa attività di scavo e alle nuove scoperte, divenne evidente la necessità di una sede più ampia e moderna. L'attuale complesso museale, inaugurato nel 1988 all'interno del giardino della storica Villa Landolina, è il risultato di un progetto architettonico innovativo firmato da Franco Minissi, che ha saputo coniugare funzionalità espositiva, luce naturale e rigore scientifico.
            </p>
            <p style="margin-bottom: 1rem;">
            Le collezioni sono organizzate in settori tematici che guidano il visitatore in un percorso chiaro e progressivo. Il piano terreno è dedicato alla preistoria e protostoria, con testimonianze che spaziano dai primi insediamenti umani ai grandi centri dell'età del Bronzo, come Pantalica e Thapsos. Di particolare suggestione sono i reperti naturalistici e paleontologici, tra cui i celebri elefanti nani della Grotta Spinagallo, simbolo dei fenomeni di adattamento faunistico della Sicilia antica.
            </p>
            <p style="margin-bottom: 1rem;">
            Un'ampia sezione è riservata alle colonie greche e alla Siracusa arcaica, con sculture, elementi architettonici e oggetti votivi provenienti da città come Megara Hyblaea, Leontinoi e Gela, che testimoniano il ruolo centrale dell'isola nei traffici e nella cultura del mondo greco. Le sub-colonie siracusane e i grandi centri della Sicilia orientale e meridionale completano il quadro della colonizzazione ellenica.
            </p>
            <p style="margin-bottom: 1rem;">
            Al piano superiore, il museo ospita i reperti dell'età ellenistico-romana, tra cui spiccano capolavori come la celebre Venere Landolina, sculture di divinità e filosofi, oreficerie e monete che restituiscono l'immagine di una Siracusa cosmopolita e raffinata. Una sezione specifica è dedicata al periodo paleocristiano, con il monumentale Sarcofago di Adelfia e materiali provenienti dalle catacombe cittadine, che documentano il passaggio dall'antichità pagana al cristianesimo.
            </p>
            <p style="margin-bottom: 1rem;">
            Nel seminterrato trova spazio il medagliere, una delle raccolte numismatiche più importanti della Sicilia, con preziose monete siracusane firmate dai grandi incisori dell'età classica, accanto a esemplari bizantini, cartaginesi e di epoche successive.
            </p>
            <p style="margin-bottom: 1rem;">
            Il museo non è solo luogo di conservazione, ma anche di divulgazione e innovazione: sale multimediali, audioguide, mostre temporanee di respiro internazionale e progetti digitali, come i tour virtuali, ne fanno un'istituzione viva e accessibile. Completano l'esperienza il parco della Villa Landolina, arricchito da reperti archeologici e resti di viabilità antica, e gli spazi per conferenze ed eventi culturali.
            </p>
        ''',
    # EN: traduzione di 'descrizione_completa' — lasciare vuoto '' per usare il testo italiano
    'descrizione_completa_en': '''
            <p style="margin-bottom: 1rem;">
            The Regional Archaeological Museum Paolo Orsi of Syracuse represents one of the most important cultural poles of the Mediterranean and a fundamental destination for knowledge of the ancient history of Sicily. Named after the archaeologist Paolo Orsi, who served as its director for nearly forty years and was the protagonist of decisive excavation campaigns in eastern Sicily, the museum covers an extraordinarily broad chronological span from prehistory through to the Roman and early Christian periods.
            </p>
            <p style="margin-bottom: 1rem;">
            The history of the museum has its roots in the eighteenth century, when it was born as a collection of the Seminary, before transforming during the nineteenth century into a Civic Museum and subsequently into a National Archaeological Museum. In the twentieth century, also thanks to the intensive excavation activity and new discoveries, the need for a larger and more modern premises became evident. The current museum complex, inaugurated in 1988 within the gardens of the historic Villa Landolina, is the result of an innovative architectural project by Franco Minissi, who succeeded in combining exhibition functionality, natural light, and scientific rigour.
            </p>
            <p style="margin-bottom: 1rem;">
            The collections are organised in thematic sectors that guide the visitor through a clear and progressive route. The ground floor is dedicated to prehistory and protohistory, with testimonies ranging from the earliest human settlements to the great Bronze Age centres such as Pantalica and Thapsos. Of particular fascination are the naturalistic and palaeontological finds, including the celebrated dwarf elephants of the Grotta Spinagallo, symbols of the faunal adaptation phenomena of ancient Sicily.
            </p>
            <p style="margin-bottom: 1rem;">
            An extensive section is devoted to the Greek colonies and archaic Syracuse, with sculptures, architectural elements, and votive objects from cities such as Megara Hyblaea, Leontinoi, and Gela, which attest to the island's central role in the trade and culture of the Greek world. The Syracusan sub-colonies and the great centres of eastern and southern Sicily complete the picture of Hellenic colonisation.
            </p>
            <p style="margin-bottom: 1rem;">
            On the upper floor, the museum houses finds of the Hellenistic-Roman period, among which stand out masterpieces such as the celebrated Venus Landolina, sculptures of deities and philosophers, goldwork, and coins that convey the image of a cosmopolitan and refined Syracuse. A specific section is dedicated to the early Christian period, with the monumental Sarcophagus of Adelfia and materials from the city's catacombs, documenting the transition from pagan antiquity to Christianity.
            </p>
            <p style="margin-bottom: 1rem;">
            In the basement the coin cabinet finds its place — one of the most important numismatic collections in Sicily — with precious Syracusan coins signed by the great engravers of the classical period, alongside Byzantine, Carthaginian, and later examples.
            </p>
            <p style="margin-bottom: 1rem;">
            The museum is not only a place of conservation but also of public engagement and innovation: multimedia rooms, audio guides, temporary exhibitions of international scope, and digital projects such as virtual tours make it a living and accessible institution. The experience is completed by the park of Villa Landolina, enriched by archaeological finds and remains of ancient road systems, and by spaces for conferences and cultural events.
            </p>
        ''',

    # ========================================
    # LOCALIZZAZIONE
    # ========================================
    'localita': 'Siracusa',
    'provincia': 'SR',
    'indirizzo': 'Viale Teocrito 66 - 96100 Siracusa SR',

    # ========================================
    # BENI DIGITALIZZATI
    # ========================================
    'beni_digitalizzati_totale': 10.55,
    'composizione_beni': [
        {
            'nome': 'Sculture',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Sculptures',
            'quantita': 50,
        },
        {
            'nome': 'Reperti archeologici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Archaeological finds',
            'quantita': 10000,
        },
        {
            'nome': 'Beni naturalistici',
            # EN: traduzione di 'nome' — lasciare vuoto per usare il testo italiano
            'nome_en': 'Natural heritage',
            'quantita': 500,
        },
    ],

    # ========================================
    # IMMAGINE
    # ========================================
    'immagine': '/static/img/paolo-orsi.jpg',

    # ========================================
    # ARCGIS STORY MAP
    # ========================================
    'storymap_url': None,

    # ========================================
    # CONTATTI E INFORMAZIONI VISITATORI
    # ========================================
    'orari_apertura': 'Mar-Sab: 9:00-19:00<br>Dom: 09:00-14:00',
    # EN: traduzione di 'orari_apertura' — lasciare vuoto '' per usare il testo italiano
    'orari_apertura_en': 'Tue-Sat: 9:00-19:00<br>Sun: 9:00-14:00',
    'costo_biglietto': 'Intero €10.00, ridotto €5.00',
    # EN: traduzione di 'costo_biglietto' — lasciare vuoto '' per usare il testo italiano
    'costo_biglietto_en': 'Full price: € 10.00, reduced: € 5.00',
    'sito_web': 'https://parchiarcheologici.regione.sicilia.it/siracusa-eloro-villa-tellaro-akrai/siti-archeologici/museo-archeologico-regionale-paolo-orsi/',
    'telefono': '+39 0931 489511',
    'email': 'parco.archeo.siracusa@regione.sicilia.it',

    # ========================================
    # LINK RISORSE ONLINE
    # ========================================
    'link_database': 'https://catalogo.beniculturali.it/search/Site/0c5f3f6d61ed6fff6493868b1e20a08e',
    'link_viewer': None,
    'link_api': 'https://api.catalogo.beniculturali.it/docs',

    # ========================================
    # CAMPI FISSI
    # ========================================
    'stato': 'completato',
    'stato_label': 'Completato',
    # EN: traduzione di 'stato_label' — lasciare vuoto '' per usare il testo italiano
    'stato_label_en': 'Completed',
    'data_inizio': '-',
    'data_fine_prevista': '-',
    'durata_mesi': '-',
    'avanzamento': '-',
    'importo': '-',
    'importo_formatted': '-',
},

]


# ========================================
# NOTE IMPORTANTI
# ========================================
"""
TRADUZIONE EN:
  Compila i campi _en con il testo inglese corrispondente.
  Se un campo _en e' vuoto ("") o assente, il portale mostrera' il testo italiano.

CAMPO STORY MAP:
  Se un cantiere non ha una Story Map, lascia storymap_url a None.
"""