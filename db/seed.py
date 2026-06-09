"""
db/seed.py
----------
Script di popolamento (seed) del database MongoDB.
Legge i dati da cantieri_data.py e li inserisce nella collection "cantieri".

Esecuzione (dalla root del progetto):
    python db/seed.py

Opzioni:
    --reset     Svuota la collection prima di inserire (default: False)
    --verbose   Stampa ogni cantiere inserito
"""

import sys
import os
import argparse
from pymongo import IndexModel, ASCENDING

# Assicura che la root del progetto sia nel path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cantieri_data import CANTIERI_DATA
from db.connection import get_db


def prepare_document(cantiere: dict) -> dict:
    """
    Prepara un documento cantiere per MongoDB.
    - Usa 'id' come _id di MongoDB (evita duplicati su re-seed)
    - Pulisce i campi None per uniformità
    """
    doc = cantiere.copy()

    # Usa l'id del cantiere come _id MongoDB (evita duplicati)
    doc["_id"] = doc.pop("id")

    # Normalizza: sostituisce None con stringa vuota nei campi stringa opzionali
    optional_str_fields = [
        "link_viewer", "link_api", "link_database",
        "modello_3d_url", "modello_3d_poster", "modello_3d_sketchfab",
        "storymap_url", "telefono", "email", "sito_web",
    ]
    for field in optional_str_fields:
        if field in doc and doc[field] is None:
            doc[field] = ""

    return doc


def create_indexes(collection):
    """
    Crea gli indici utili per le query più frequenti dell'app.
    """
    indexes = [
        IndexModel([("provincia", ASCENDING)], name="idx_provincia"),
        IndexModel([("categorie", ASCENDING)], name="idx_categorie"),
        IndexModel([("stato", ASCENDING)], name="idx_stato"),
    ]
    collection.create_indexes(indexes)
    print("[DB] Indici creati: provincia, categorie, stato")


def seed(reset: bool = False, verbose: bool = False):
    db = get_db()
    collection = db["cantieri"]

    if reset:
        result = collection.delete_many({})
        print(f"[DB] Collection svuotata: {result.deleted_count} documenti rimossi.")

    # Prepara i documenti
    documents = [prepare_document(c) for c in CANTIERI_DATA]

    # Inserimento con upsert (non duplica se si riesegue senza --reset)
    inserted = 0
    updated = 0
    for doc in documents:
        result = collection.replace_one(
            {"_id": doc["_id"]},
            doc,
            upsert=True
        )
        if result.upserted_id is not None:
            inserted += 1
            if verbose:
                print(f"  [+] Inserito: {doc['titolo']} (id={doc['_id']})")
        else:
            updated += 1
            if verbose:
                print(f"  [~] Aggiornato: {doc['titolo']} (id={doc['_id']})")

    print(f"\n[DB] Seed completato:")
    print(f"     Inseriti: {inserted}")
    print(f"     Aggiornati: {updated}")
    print(f"     Totale nella collection: {collection.count_documents({})}")

    # Crea indici
    create_indexes(collection)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed MongoDB con i dati dei cantieri.")
    parser.add_argument("--reset", action="store_true", help="Svuota la collection prima di inserire")
    parser.add_argument("--verbose", action="store_true", help="Mostra ogni cantiere inserito/aggiornato")
    args = parser.parse_args()

    print("=" * 55)
    print("  SEED DATABASE - Beni Culturali Siciliani")
    print("=" * 55)
    seed(reset=args.reset, verbose=args.verbose)
