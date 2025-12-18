def conciliar(sicoob_finpet):
    resultado = []

    for item in sicoob_finpet:
        sicoob = item.get("sicoob", {})
        finpet = item.get("finpet", [])

        if not finpet:
            continue

        soma_merchant = sum(
            f["beneficiary_value"] for f in finpet if f.get("type") == "MERCHANT"
        )

        valor_sicoob = sicoob.get("valor", 0)
        diferenca = round(valor_sicoob - soma_merchant, 2)
        conciliado = diferenca == 0

        resultado.append(
            {
                "valor_sicoob": valor_sicoob,
                "data": sicoob.get("data"),
                "soma_merchant": soma_merchant,
                "desc_inf_complementar": sicoob.get("desc_inf_complementar"),
                "conciliado": conciliado,
                "diferenca": diferenca,
            }
        )

    return resultado
