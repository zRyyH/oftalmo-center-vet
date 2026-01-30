from unicodedata import normalize, category
from datetime import datetime
import re


def remove_accents(text):
    if not text:
        return ""
    return "".join(c for c in normalize("NFD", str(text)) if category(c) != "Mn")


def clean_str(value):
    if not value:
        return ""
    return remove_accents(str(value)).upper()


def parse_date(value):
    if not value:
        return None

    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S.%fZ",
        "%d/%m/%Y %H:%M:%S",
        "%d/%m/%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).isoformat()
        except:
            pass
    return clean_str(value)


def parse_decimal_br(value):
    if not value:
        return 0.0
    if isinstance(value, (int, float)):
        return float(value)

    value = value.replace(".", "").replace(",", ".")
    try:
        return float(value)
    except:
        return 0.0


def clean_doc(value):
    if not value:
        return ""
    return re.sub(r"\D", "", str(value))


def normalize_brand(item):
    return {
        "id": item.get("id", ""),
        "brand": clean_str(item.get("brand")),
        "brand_simplesvet": clean_str(item.get("brand_simplesvet")),
        "type": clean_str(item.get("type")),
        "type_simplesvet": clean_str(item.get("type_simplesvet")),
        "gateway": clean_str(item.get("gateway")),
        "destination_account": clean_str(item.get("destination_account")),
        "info": clean_str(item.get("info")),
        "collection_id": item.get("collection_id", ""),
        "collection_name": clean_str(item.get("collection_name")),
        "created": parse_date(item.get("created")),
        "updated": parse_date(item.get("updated")),
    }


def normalize_sicoob(item):
    return {
        "id": item.get("id", ""),
        "transaction_id": item.get("transaction_id", ""),
        "tipo": clean_str(item.get("tipo")),
        "valor": float(item.get("valor", 0)),
        "descricao": clean_str(item.get("descricao")),
        "desc_inf_complementar": clean_str(item.get("desc_inf_complementar")),
        "cpf_cnpj": clean_doc(item.get("cpf_cnpj")),
        "numero_documento": item.get("numero_documento", ""),
        "data": parse_date(item.get("data")),
        "data_lote": parse_date(item.get("data_lote")),
        "collection_id": item.get("collection_id", ""),
        "collection_name": clean_str(item.get("collection_name")),
        "created": parse_date(item.get("created")),
        "updated": parse_date(item.get("updated")),
    }


def normalize_stone(item):
    return {
        "stone_id": item.get("STONE ID", ""),
        "stonecode": item.get("STONECODE", ""),
        "documento": clean_doc(item.get("DOCUMENTO")),
        "bandeira": clean_str(item.get("BANDEIRA")),
        "produto": clean_str(item.get("PRODUTO")),
        "categoria": clean_str(item.get("CATEGORIA")),
        "status": clean_str(item.get("ÚLTIMO STATUS")),
        "parcela": int(item.get("Nº DA PARCELA") or 0),
        "qtd_parcelas": int(item.get("QTD DE PARCELAS") or 0),
        "valor_bruto": parse_decimal_br(item.get("VALOR BRUTO")),
        "valor_liquido": parse_decimal_br(item.get("VALOR LÍQUIDO")),
        "desconto_mdr": parse_decimal_br(item.get("DESCONTO DE MDR")),
        "desconto_antecipacao": parse_decimal_br(item.get("DESCONTO DE ANTECIPAÇÃO")),
        "desconto_unificado": parse_decimal_br(item.get("DESCONTO UNIFICADO")),
        "data_venda": parse_date(item.get("DATA DA VENDA")),
        "data_vencimento": parse_date(item.get("DATA DE VENCIMENTO")),
        "data_vencimento_original": parse_date(item.get("DATA DE VENCIMENTO ORIGINAL")),
        "data_ultimo_status": parse_date(item.get("DATA DO ÚLTIMO STATUS")),
    }


def normalize_stone_sicoob_brands(data):
    return {
        "brands": [normalize_brand(item) for item in data.get("brands", [])],
        "sicoob": [normalize_sicoob(item) for item in data.get("sicoob", [])],
        "stone": [normalize_stone(item) for item in data.get("stone", [])],
    }


def processar_dados(dados):
    mapa_bandeiras = {item["info"]: item["brand"] for item in dados.get("brands", [])}

    mapa_stone = {}
    mapa_stone_simples = {}
    for item in dados.get("brands", []):
        mapa_stone[(item["brand"], item["type"])] = item["brand"]
        mapa_stone[(item["brand_simplesvet"], item["type"])] = item["brand"]
        if item["brand"]:
            mapa_stone_simples[item["brand"]] = item["brand"]
        if item["brand_simplesvet"]:
            mapa_stone_simples[item["brand_simplesvet"]] = item["brand"]

    sicoob_processado = []
    for item in dados.get("sicoob", []):
        if item.get("tipo") != "CREDITO":
            continue

        desc = item.get("desc_inf_complementar", "")

        bandeira = None
        for info, brand in mapa_bandeiras.items():
            if info in desc:
                bandeira = brand
                break

        if not bandeira:
            continue

        sicoob_processado.append(
            {
                "tipo": item.get("tipo"),
                "valor": item.get("valor"),
                "bandeira": bandeira,
                "data": item.get("data"),
                "descricao": item.get("descricao", ""),
                "desc_inf_complementar": item.get("desc_inf_complementar", ""),
            }
        )

    stone_processado = []
    for item in dados.get("stone", []):
        bandeira_original = item.get("bandeira")
        tipo = item.get("produto")

        bandeira = mapa_stone.get((bandeira_original, tipo))
        if not bandeira:
            bandeira = mapa_stone_simples.get(bandeira_original)
        if not bandeira:
            bandeira = bandeira_original

        if not bandeira:
            continue

        stone_processado.append(
            {
                "bandeira": bandeira,
                "tipo": tipo,
                "valor": item.get("valor_liquido"),
                "data": item.get("data_vencimento"),
            }
        )

    return {
        "sicoob": sicoob_processado,
        "stone": stone_processado,
    }
