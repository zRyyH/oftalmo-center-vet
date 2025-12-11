"""Serviço para buscar transações do Finpet."""

from datetime import datetime, timedelta

from scrapper import FinpetScrapper

from config import DAYS_RANGE, FINPET_EMAIL, FINPET_PASSWORD


def fetch_transactions() -> list[dict]:
    """Busca e retorna lista de transações."""
    hoje = datetime.now()
    data_inicial = (hoje - timedelta(days=DAYS_RANGE)).strftime("%Y-%m-%d")
    data_final = (hoje + timedelta(days=DAYS_RANGE)).strftime("%Y-%m-%d")

    with FinpetScrapper(email=FINPET_EMAIL, password=FINPET_PASSWORD) as scrapper:
        scrapper.login()
        raw = scrapper.get_receipts(data_inicial, data_final)

    return (
        raw.get("merchantPaymentSearchDTO", {}).get("paymentList", {}).get("list", [])
    )
