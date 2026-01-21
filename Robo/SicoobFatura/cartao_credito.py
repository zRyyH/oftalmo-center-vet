from datetime import datetime


def obter_faturas_cartao(dados: dict) -> list:
    releases = dados.get("releases", [])
    sicoob = dados.get("sicoob", [])

    faturas = [s for s in sicoob if s.get("numero_documento") == "MASTERCARD"]
    faturas_ordenadas = sorted(faturas, key=lambda x: x.get("data", ""))

    resultado = []
    for fatura in faturas_ordenadas:
        data_str = fatura.get("data", "")
        try:
            data_fatura = datetime.fromisoformat(data_str.replace("Z", "")).date()
        except:
            continue

        despesas_periodo = []
        for r in releases:
            if r.get("tipo") != "despesa":
                continue
            if r.get("forma_pagamento") != "CRE":
                continue
            if r.get("origem") == "ARR":
                continue

            r_data_str = r.get("data", "")
            try:
                r_data = datetime.fromisoformat(r_data_str.replace("Z", "")).date()
            except:
                continue

            if r_data == data_fatura:
                despesas_periodo.append(r)

        total_despesas = sum(abs(d.get("valor", 0)) for d in despesas_periodo)

        resultado.append(
            {
                "fatura": fatura,
                "data_fatura": data_fatura.strftime("%Y-%m-%d"),
                "valor_fatura": fatura.get("valor"),
                "despesas": despesas_periodo,
                "total_despesas": total_despesas,
                "quantidade_despesas": len(despesas_periodo),
            }
        )

    return resultado
