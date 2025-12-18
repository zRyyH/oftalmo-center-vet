def find_brand_by_info(desc_inf_complementar, brands):
    """Encontra brand pelo campo info em brands."""
    for b in brands:
        if b.get("info") and b["info"] in desc_inf_complementar:
            return b.get("brand")
    return None


def normalize_date(date_str):
    """Extrai apenas a data (YYYY-MM-DD) de uma string datetime."""
    if not date_str:
        return None
    return date_str[:10]


def find_finpet_matches(sicoob_data, brand, finpet):
    """Retorna registros finpet que batem com data e brand."""
    matches = []
    for f in finpet:
        if (
            normalize_date(f.get("date_received")) == normalize_date(sicoob_data)
            and f.get("payment_brand") == brand
        ):
            matches.append(f)
    return matches


def sicoob_finpet(sicoob, finpet, brands):
    """Vincula registros finpet aos registros sicoob."""
    result = []

    for s in sicoob:
        desc = s.get("desc_inf_complementar", "")
        brand = find_brand_by_info(desc, brands)

        vinculo = {"sicoob": s, "finpet": []}

        if brand:
            vinculo["finpet"] = find_finpet_matches(s.get("data"), brand, finpet)

        result.append(vinculo)

    return result
