import re


def normalizar_parcela(parcela: str) -> tuple:
    if not parcela or "/" not in parcela:
        return None
    p = parcela.split("/")
    return (int(p[0]), int(p[1]))


def normalizar_parcela_release(parcela: str) -> tuple:
    if not parcela or parcela == "...":
        return None
    m = re.search(r"(\d+)\s*de\s*(\d+)", parcela)
    return (int(m.group(1)), int(m.group(2))) if m else None


def normalizar_data(data: str) -> str:
    return data[:10] if data else None


def extrair_auth_numbers(desc: str) -> list:
    """Extrai todos os códigos de 6 chars alfanuméricos."""
    if not desc:
        return []
    return [
        token.upper() for token in desc.split() if len(token) == 6 and token.isalnum()
    ]


def normalizar_auth(auth: str) -> str:
    """Normaliza auth para comparação case-insensitive."""
    return auth.upper() if auth else None


def normalizar_valor(v) -> float:
    return abs(float(v)) if v else 0.0


def normalizar_tipo(tipo_finpet: str) -> str:
    return {"MERCHANT": "receita", "SUPPLIER": "despesa"}.get(tipo_finpet)
