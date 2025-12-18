import re
import numpy as np
from normalizers import (
    normalizar_parcela,
    normalizar_parcela_release,
    normalizar_data,
    extrair_auth_numbers,
    normalizar_valor,
    normalizar_tipo,
    normalizar_auth,
)

TIPO_MAP = {"MERCHANT": 1, "SUPPLIER": 2}
TIPO_REL_MAP = {"receita": 1, "despesa": 2}


def data_para_int(data_str: str) -> int:
    if not data_str:
        return 0
    d = data_str[:10].replace("-", "")
    return int(d) if d.isdigit() else 0


def preprocessar_finpet(finpet: list) -> tuple:
    """Retorna (array numÃ©rico, lista de auths normalizados)."""
    n = len(finpet)
    arr = np.zeros((n, 6), dtype=np.int64)
    auths = []

    for i, fp in enumerate(finpet):
        p = normalizar_parcela(fp.get("installment_number"))
        if p:
            arr[i, 0], arr[i, 1] = p
        arr[i, 2] = int(normalizar_valor(fp.get("value")) * 100)
        arr[i, 3] = data_para_int(fp.get("date_received"))
        arr[i, 4] = data_para_int(fp.get("date_estimated"))
        arr[i, 5] = TIPO_MAP.get(fp.get("type"), 0)
        auths.append(normalizar_auth(fp.get("authorization_number")))

    return arr, auths


def preprocessar_releases(releases: list) -> tuple:
    """Retorna (array numérico, lista de listas de auths)."""
    n = len(releases)
    arr = np.zeros((n, 5), dtype=np.int64)
    auths = []

    for i, rel in enumerate(releases):
        p = normalizar_parcela_release(rel.get("parcela"))
        if p:
            arr[i, 0], arr[i, 1] = p
        arr[i, 2] = int(normalizar_valor(rel.get("valor")) * 100)
        arr[i, 3] = data_para_int(rel.get("data"))
        arr[i, 4] = TIPO_REL_MAP.get(rel.get("tipo"), 0)
        auths.append(extrair_auth_numbers(rel.get("descricao", "")))

    return arr, auths


def calcular_comparacoes(fp: dict, rel: dict) -> tuple:
    """Retorna (score, comparaÃ§Ãµes detalhadas)."""
    score = 0
    comp = {}

    # Tipo
    tipo_esp = normalizar_tipo(fp.get("type"))
    comp["tipo"] = {
        "finpet": fp.get("type"),
        "release": rel.get("tipo"),
        "match": tipo_esp == rel.get("tipo"),
    }

    # Parcela
    p1 = normalizar_parcela(fp.get("installment_number"))
    p2 = normalizar_parcela_release(rel.get("parcela"))
    match = bool(p1 and p2 and p1 == p2)
    comp["parcela"] = {
        "finpet": fp.get("installment_number"),
        "release": rel.get("parcela"),
        "match": match,
    }
    if match:
        score += 1

    # Valor
    v1, v2 = normalizar_valor(fp.get("value")), normalizar_valor(rel.get("valor"))
    diff = round(v1 - v2, 2)
    match = abs(diff) <= 0.01
    comp["valor"] = {
        "finpet": fp.get("value"),
        "release": rel.get("valor"),
        "diff": diff,
        "match": match,
    }
    if match:
        score += 1

    # Data
    d_est = normalizar_data(fp.get("date_estimated"))
    d_rec = normalizar_data(fp.get("date_received"))
    d_rel = normalizar_data(rel.get("data"))
    match = bool(d_rel and (d_est == d_rel or d_rec == d_rel))
    comp["data"] = {
        "finpet_estimated": fp.get("date_estimated"),
        "finpet_received": fp.get("date_received"),
        "release": rel.get("data"),
        "match": match,
    }
    if match:
        score += 1

    # Auth (case-insensitive)
    auth_fp = normalizar_auth(fp.get("authorization_number"))
    auth_candidates = extrair_auth_numbers(rel.get("descricao", ""))
    auth_match = auth_fp in auth_candidates if auth_fp else False
    comp["auth"] = {
        "finpet": auth_fp,
        "release": auth_fp if auth_match else None,
        "match": auth_match,
    }
    if auth_match:
        score += 1

    # Cliente
    nums = re.findall(r"\d+", fp.get("client_name") or "")
    desc = rel.get("descricao") or ""
    match = bool(nums) and all(n in desc for n in nums)
    comp["cliente"] = {"finpet": nums, "release": desc, "match": match}
    if match:
        score += 1

    return score, comp
