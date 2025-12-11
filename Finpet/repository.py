"""Repositório para operações no PocketBase."""

from pocketbase import PocketBase

from config import (
    COLLECTION_NAME,
    POCKETBASE_URL,
    POCKETBASE_EMAIL,
    POCKETBASE_PASSWORD,
)
from logger import log


class FinpetRepository:
    """Gerencia operações na collection finpet."""

    def __init__(self):
        self.pb = PocketBase(POCKETBASE_URL)
        self.pb.admins.auth_with_password(POCKETBASE_EMAIL, POCKETBASE_PASSWORD)
        self.collection = self.pb.collection(COLLECTION_NAME)

    def exists(self, id_t: str) -> bool:
        """Verifica se transação já existe."""
        result = self.collection.get_list(1, 1, {"filter": f'id_t = "{id_t}"'})
        return len(result.items) > 0

    def sync(self, transactions: list[dict]) -> dict:
        """Sincroniza transações. Retorna estatísticas."""
        stats = {"created": 0, "skipped": 0, "errors": 0}

        for t in transactions:
            t["id_t"] = t.pop("id")

            try:
                if self.exists(t["id_t"]):
                    stats["skipped"] += 1
                    continue

                self.collection.create(t)
                stats["created"] += 1
                log.info(f"Nova transação: {t['id_t']}")

            except Exception as e:
                stats["errors"] += 1
                log.error(f"Falha {t['id_t']}: {e}")

        return stats