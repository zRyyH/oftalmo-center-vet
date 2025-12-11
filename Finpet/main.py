"""Sincronização Finpet → PocketBase (Cron)."""

import time
import schedule

from config import SYNC_INTERVAL_MINUTES
from repository import FinpetRepository
from service import fetch_transactions
from logger import log


def sync():
    transactions = fetch_transactions()
    stats = FinpetRepository().sync(transactions)

    log.info(f"Syncronizado: {stats['created']} | Erro: {stats['errors']}")


def main():
    log.info(f"Iniciado (intervalo: {SYNC_INTERVAL_MINUTES}min)")
    sync()
    schedule.every(SYNC_INTERVAL_MINUTES).minutes.do(sync)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
