from datetime import datetime
from urllib.parse import urlencode, quote


def format_conciliation_url(
    start_date: str, end_date: str, page: int = 1, per_page: int = 10000
) -> str:
    """Gera URL de conciliação da API SimplesVet.

    Args:
        start_date: Data inicial (YYYY-MM-DD)
        end_date: Data final (YYYY-MM-DD)
        page: Página atual
        per_page: Itens por página

    Returns:
        URL completa para buscar conciliações
    """
    start = _normalize_date(start_date)
    end = _normalize_date(end_date)

    params = {
        "periodo": f"{start}|{end}",
        "data[after]": start,
        "data[before]": end,
        "periodoObj": f'{{"inicio":"{start}","fim":"{end}"}}',
        "_pagina": page,
        "_porPagina": per_page,
        "_ordenarPor[data]": "ASC",
    }

    base = "https://api.simples.vet/app/v3/financeiro/conciliacao-cartoes"
    return f"{base}?{urlencode(params)}"


def _normalize_date(date_str: str) -> str:
    """Normaliza data para formato YYYY-MM-DD."""
    if "/" in date_str:
        dt = datetime.strptime(date_str, "%d/%m/%Y")
        return dt.strftime("%Y-%m-%d")
    return date_str
