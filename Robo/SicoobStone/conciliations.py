from collections import defaultdict


def conciliar(dados):
    # Agrupa sicoob por (data, bandeira) mantendo detalhes
    sicoob_por_chave = defaultdict(list)
    for r in dados["sicoob"]:
        chave = (r["data"][:10], r["bandeira"])
        sicoob_por_chave[chave].append(r)

    # Agrupa stone por (data, bandeira)
    stone_por_chave = defaultdict(list)
    for r in dados["stone"]:
        chave = (r["data"][:10], r["bandeira"])
        stone_por_chave[chave].append(r)

    todas_chaves = set(sicoob_por_chave.keys()) | set(stone_por_chave.keys())

    conciliados = []
    nao_conciliados = []

    for chave in todas_chaves:
        data, bandeira = chave
        lista_sicoob = sicoob_por_chave.get(chave, [])
        lista_stone = stone_por_chave.get(chave, [])

        valor_sicoob_total = round(sum(r["valor"] for r in lista_sicoob), 2)
        valor_stone_total = round(sum(r["valor"] for r in lista_stone), 2)

        # Pega descrições do primeiro registro sicoob (se existir)
        descricao = lista_sicoob[0]["descricao"] if lista_sicoob else ""
        desc_inf = lista_sicoob[0]["desc_inf_complementar"] if lista_sicoob else ""

        # Pega datas específicas
        data_sicoob = lista_sicoob[0]["data"][:10] if lista_sicoob else ""
        data_stone = lista_stone[0]["data"][:10] if lista_stone else ""

        registro = {
            "data_sicoob": data_sicoob,
            "data_stone": data_stone,
            "valor_sicoob": valor_sicoob_total,
            "valor_stone": valor_stone_total,
            "descricao": descricao,
            "desc_inf_complementar": desc_inf,
            "bandeira": bandeira,
        }

        if valor_sicoob_total == valor_stone_total and lista_sicoob and lista_stone:
            registro["conciliado"] = "SIM"
            conciliados.append(registro)
        else:
            registro["conciliado"] = "NÃO"
            nao_conciliados.append(registro)

    return {"conciliados": conciliados, "nao_conciliados": nao_conciliados}
