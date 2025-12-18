from datetime import datetime
from urllib.parse import quote


def format_period(start_date: str, end_date: str) -> str:
    """Formata período de datas para URL do Finpet.

    Args:
        start_date: Data inicial (YYYY-MM-DD ou DD/MM/YYYY)
        end_date: Data final (YYYY-MM-DD ou DD/MM/YYYY)

    Returns:
        String codificada para URL no formato esperado pela API
    """
    start_fmt = _parse_date(start_date)
    end_fmt = _parse_date(end_date)

    period = f"{start_fmt} 00:00:00;{end_fmt} 23:59:59"
    return quote(period, safe="")


def _parse_date(date_str: str) -> str:
    """Converte data para formato DD/MM/YYYY."""
    if "-" in date_str:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%d/%m/%Y")
    return date_str
