from datetime import datetime


def format_date_range(start_date: str, end_date: str) -> str:
    """Formata intervalo de datas para o padrão SimplesVet.

    Args:
        start_date: Data inicial (YYYY-MM-DD ou DD/MM/YYYY)
        end_date: Data final (YYYY-MM-DD ou DD/MM/YYYY)

    Returns:
        String no formato DD/MM/YYYY-DD/MM/YYYY
    """
    start = _to_br_format(_normalize_date(start_date))
    end = _to_br_format(_normalize_date(end_date))
    return f"{start}-{end}"


def _normalize_date(date_str: str) -> str:
    """Normaliza data para formato YYYY-MM-DD."""
    if "/" in date_str:
        dt = datetime.strptime(date_str, "%d/%m/%Y")
        return dt.strftime("%Y-%m-%d")
    return date_str


def _to_br_format(date_str: str) -> str:
    """Converte YYYY-MM-DD para DD/MM/YYYY."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return dt.strftime("%d/%m/%Y")
