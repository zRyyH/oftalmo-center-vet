"""Parser de releases SimplesVet."""

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


def parse_int(value: Any) -> int | None:
    if value is None or value == "" or value == "-":
        return None
    return int(value)


def parse_date(value: Any, ano: int | None = None) -> str | None:
    if not value or value == "-":
        return None

    formats = [
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%fZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d/%m",
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(value, fmt)
            if fmt == "%d/%m" and ano:
                dt = dt.replace(year=ano)
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            continue

    return None


def extrair_ano(value: Any) -> int | None:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%d/%m/%Y").year
    except ValueError:
        return None


def safe_get(obj: Any, *keys):
    """Acessa chaves aninhadas com seguranÃ§a."""
    for key in keys:
        if obj is None or not isinstance(obj, dict):
            return None
        obj = obj.get(key)
    return obj


def parse_release(raw: dict) -> dict:
    """Converte release raw para formato normalizado."""
    ano = extrair_ano(raw.get("vencimento"))

    return {
        "id_r": parse_str(raw.get("id")),
        "data": parse_date(raw.get("data"), ano),
        "descricao": parse_str(raw.get("descricao")),
        "fornecedor": parse_str(raw.get("fornecedor")),
        "parcela": parse_str(raw.get("parcela")),
        "valor": parse_float(raw.get("valor")),
        "tipo": parse_str(raw.get("tipo")),
        "status": parse_str(raw.get("status")),
        "origem": parse_str(raw.get("origem")),
        "vencimento": parse_date(raw.get("vencimento")),
        "forma_pagamento": parse_str(raw.get("formaPagamento")),
    }


def parse_releases(raw_data: dict | list) -> list[dict]:
    """Converte lista de releases."""
    if isinstance(raw_data, dict):
        items = raw_data.get("data", raw_data.get("items", []))
    else:
        items = raw_data

    return [parse_release(item) for item in items]
