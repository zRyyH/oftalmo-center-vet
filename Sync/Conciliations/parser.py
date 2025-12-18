"""Parser de conciliações SimplesVet."""

from datetime import datetime
from typing import Any


def parse_str(value: Any) -> str | None:
    if value is None or value == "" or value == "-":
        return None
    return str(value)


def parse_float(value: Any) -> float | None:
    if value is None or value == "" or value == "-":
        return None
    return float(value)


def parse_date(value: Any) -> str | None:
    if not value or value == "-":
        return None

    formats = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%d/%m/%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).isoformat()
        except ValueError:
            continue

    return str(value)


def safe_get(obj: Any, *keys):
    """Acessa chaves aninhadas com segurança."""
    for key in keys:
        if obj is None or not isinstance(obj, dict):
            return None
        obj = obj.get(key)
    return obj


def parse_conciliation(raw: dict) -> dict:
    """Converte conciliação raw para formato normalizado."""
    return {
        "id_c": parse_str(raw.get("id")),
        "data": parse_date(raw.get("data")),
        "incluido_em": parse_date(raw.get("incluidoEm")),
        "tipo": parse_str(safe_get(raw, "tipo", "chave")),
        "status": parse_str(safe_get(raw, "status", "chave")),
        "valor": parse_float(raw.get("valor")),
        "taxa_bandeira": parse_float(safe_get(raw, "taxaBandeira", "valor")),
        "taxa_bandeira_pct": parse_float(safe_get(raw, "taxaBandeira", "porcentagem")),
        "taxa_antecipacao": parse_float(safe_get(raw, "taxaAntecipacao", "valor")),
        "taxa_antecipacao_pct": parse_float(
            safe_get(raw, "taxaAntecipacao", "porcentagem")
        ),
        "taxa_aluguel": parse_float(raw.get("taxaAluguel")),
        "arredondamento": parse_float(raw.get("arredondamento")),
        "bandeira": parse_str(safe_get(raw, "bandeira", "nome")),
        "operadora": parse_str(safe_get(raw, "integrador", "nome")),
        "conta_origem": parse_str(
            safe_get(raw, "transferencia", "origem", "conta", "nome")
        ),
        "conta_destino": parse_str(
            safe_get(raw, "transferencia", "destino", "conta", "nome")
        ),
        "descricao": parse_str(raw.get("descricao")),
        "observacao": parse_str(raw.get("observacao")),
    }


def parse_conciliations(raw_data: dict | list) -> list[dict]:
    """Converte lista de conciliações."""
    if isinstance(raw_data, dict):
        items = raw_data.get("data", raw_data.get("items", []))
    else:
        items = raw_data

    return [parse_conciliation(item) for item in items]
