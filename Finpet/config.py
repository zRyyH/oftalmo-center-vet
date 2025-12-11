"""Configurações da aplicação."""

from os import getenv
from dotenv import load_dotenv

load_dotenv()

POCKETBASE_URL = getenv("POCKETBASE_URL")
POCKETBASE_EMAIL = getenv("POCKETBASE_EMAIL")
POCKETBASE_PASSWORD = getenv("POCKETBASE_PASSWORD")
COLLECTION_NAME = getenv("COLLECTION_NAME", "finpet")

FINPET_EMAIL = getenv("FINPET_EMAIL")
FINPET_PASSWORD = getenv("FINPET_PASSWORD")

DAYS_RANGE = int(getenv("DAYS_RANGE", "5"))
SYNC_INTERVAL_MINUTES = int(getenv("SYNC_INTERVAL_MINUTES", "30"))