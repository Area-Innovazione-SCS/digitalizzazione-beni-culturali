"""
db/connection.py
----------------
Modulo di connessione a MongoDB.
Gestisce la connessione singola (pattern singleton) per tutta l'app Flask.

Uso:
    from db.connection import get_db
    db = get_db()
    cantieri = list(db.cantieri.find())
"""

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

# Carica le variabili da .env
load_dotenv()

# Variabile di modulo per il client singleton
_client = None


def get_client() -> MongoClient:
    """
    Restituisce il client MongoDB (singleton).
    Crea la connessione la prima volta, la riusa nelle successive.
    """
    global _client
    if _client is None:
        uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
        _client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        # Verifica immediata della connessione
        try:
            _client.admin.command("ping")
            print(f"[DB] Connesso a MongoDB: {uri}")
        except ConnectionFailure as e:
            _client = None
            raise RuntimeError(
                f"[DB] Impossibile connettersi a MongoDB ({uri}).\n"
                f"Assicurati che MongoDB sia in esecuzione: sudo systemctl start mongod\n"
                f"Errore: {e}"
            )
    return _client


def get_db():
    """
    Restituisce il database configurato in .env (MONGO_DBNAME).
    """
    client = get_client()
    dbname = os.getenv("MONGO_DBNAME", "beni_culturali")
    return client[dbname]


def close_connection():
    """
    Chiude la connessione MongoDB.
    Da chiamare all'uscita dell'app se necessario.
    """
    global _client
    if _client is not None:
        _client.close()
        _client = None
        print("[DB] Connessione chiusa.")
