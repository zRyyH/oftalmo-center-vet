"""Sincronização SimplesVet → PocketBase (Cron)."""

import time
import schedule

from datetime import datetime
from config import SYNC_INTERVAL_MINUTES
from repository import ReleaseRepository
from service import fetch_releases
from logger import log


def sync():
    hoje = datetime.now()
    conciliations = fetch_releases(hoje=hoje)
    stats = ReleaseRepository().sync(conciliations)

    log.info(
        f"Criados: {stats['created']} | Atualizados: {stats['updated']} | "
        f"Erros: {stats['errors']} | Data: {hoje.strftime('%Y-%m-%d %H:%M')}"
    )


def main():
    log.info(f"Iniciado (intervalo: {SYNC_INTERVAL_MINUTES}min)")
    sync()
    schedule.every(SYNC_INTERVAL_MINUTES).minutes.do(sync)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
