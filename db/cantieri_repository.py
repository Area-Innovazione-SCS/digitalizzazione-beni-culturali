"""
db/cantieri_repository.py
--------------------------
Layer di accesso ai dati per la collection "cantieri".
Tutte le query MongoDB sono centralizzate qui — app.py non tocca mai
direttamente il driver pymongo.

Uso in app.py:
    from db.cantieri_repository import Cantieri

    tutti = Cantieri.get_all()
    singolo = Cantieri.get_by_id(3)
    filtrati = Cantieri.get_by_provincia("PA")
"""

from bson import ObjectId
from db.connection import get_db


def _collection():
    """Restituisce la collection 'cantieri' dal db corrente."""
    return get_db()["cantieri"]


def _clean(doc: dict) -> dict:
    """
    Converte _id → id per compatibilità con i template Jinja2 esistenti.
    I template usano cantiere.id, non cantiere._id.
    """
    if doc and "_id" in doc:
        doc["id"] = doc.pop("_id")
    return doc


class Cantieri:
    """
    Interfaccia statica per le query sui cantieri.
    Ogni metodo restituisce dict Python (non oggetti pymongo).
    """

    @staticmethod
    def get_all(projection: dict = None) -> list[dict]:
        """
        Restituisce tutti i cantieri, ordinati per id.
        Parametro opzionale 'projection' per limitare i campi (es. lista cantieri).
        """
        cursor = _collection().find({}, projection or {}).sort("_id", 1)
        return [_clean(doc) for doc in cursor]

    @staticmethod
    def get_all_summary() -> list[dict]:
        """
        Versione leggera per la pagina lista cantieri:
        restituisce solo i campi necessari per le card.
        """
        projection = {
            "titolo": 1,
            "titolo_en": 1,
            "descrizione_breve": 1,
            "descrizione_breve_en": 1,
            "categorie": 1,
            "categorie_labels": 1,
            "categorie_labels_en": 1,
            "provincia": 1,
            "localita": 1,
            "immagine": 1,
            "stato": 1,
            "stato_label": 1,
            "stato_label_en": 1,
            "beni_digitalizzati_totale": 1,
        }
        cursor = _collection().find({}, projection).sort("_id", 1)
        return [_clean(doc) for doc in cursor]

    @staticmethod
    def get_by_id(cantiere_id: int) -> dict | None:
        """
        Restituisce un singolo cantiere per id numerico.
        Restituisce None se non trovato.
        """
        doc = _collection().find_one({"_id": cantiere_id})
        return _clean(doc) if doc else None

    @staticmethod
    def get_by_provincia(provincia: str) -> list[dict]:
        """
        Filtra i cantieri per provincia (es. "PA", "CT").
        """
        cursor = _collection().find(
            {"provincia": provincia.upper()}
        ).sort("_id", 1)
        return [_clean(doc) for doc in cursor]

    @staticmethod
    def get_by_categoria(categoria_slug: str) -> list[dict]:
        """
        Filtra i cantieri che contengono una certa categoria
        (es. "negativi-lastre", "reperti-archeologici").
        """
        cursor = _collection().find(
            {"categorie": categoria_slug}
        ).sort("_id", 1)
        return [_clean(doc) for doc in cursor]

    @staticmethod
    def get_province() -> list[str]:
        """
        Restituisce la lista delle province distinte presenti nel db.
        """
        return sorted(_collection().distinct("provincia"))

    @staticmethod
    def get_categorie() -> list[str]:
        """
        Restituisce la lista delle categorie distinte.
        """
        return sorted(_collection().distinct("categorie"))

    @staticmethod
    def count_total_beni() -> int:
        """
        Somma totale dei beni digitalizzati su tutti i cantieri.
        """
        pipeline = [
            {"$group": {"_id": None, "totale": {"$sum": "$beni_digitalizzati_totale"}}}
        ]
        result = list(_collection().aggregate(pipeline))
        return result[0]["totale"] if result else 0

    @staticmethod
    def count_by_provincia() -> list[dict]:
        """
        Restituisce conteggio cantieri per provincia.
        Utile per la pagina statistiche.
        """
        pipeline = [
            {"$group": {
                "_id": "$provincia",
                "num_cantieri": {"$sum": 1},
                "beni_totali": {"$sum": "$beni_digitalizzati_totale"}
            }},
            {"$sort": {"_id": 1}}
        ]
        return list(_collection().aggregate(pipeline))

    @staticmethod
    def search(query: str) -> list[dict]:
        """
        Ricerca testuale semplice su titolo e descrizione_breve.
        Per una ricerca full-text avanzata, creare un indice text su MongoDB.
        """
        import re
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        cursor = _collection().find({
            "$or": [
                {"titolo": {"$regex": pattern}},
                {"descrizione_breve": {"$regex": pattern}},
                {"localita": {"$regex": pattern}},
            ]
        }).sort("_id", 1)
        return [_clean(doc) for doc in cursor]
