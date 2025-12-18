from bs4 import BeautifulSoup


def parse_value(text: str) -> float:
    """Converte texto de valor brasileiro para float."""
    if not text:
        return 0.0
    return float(text.strip().replace(".", "").replace(",", "."))


def transform_releases(html: str) -> dict:
    """Converte HTML de lançamentos para JSON estruturado."""
    soup = BeautifulSoup(html, "html.parser")

    result = {"saldo_anterior": 0.0, "lancamentos": []}

    for row in soup.select("tr"):
        # Saldo anterior
        if "Saldo anterior" in row.get_text():
            saldo_cell = row.select_one("th.text-info")
            if saldo_cell:
                result["saldo_anterior"] = parse_value(saldo_cell.get_text())
            continue

        # Lançamentos
        if "linhaRegistro" not in row.get("class", []):
            continue

        receita = row.select_one(".tdReceita")
        despesa = row.select_one(".tdDespesa")

        lancamento = {
            "id": row.get("id"),
            "data": row.select_one(".tdData").get_text(strip=True),
            "descricao": row.select_one(".tdDescricao").get_text(" ", strip=True),
            "fornecedor": row.select_one(".tdFornecedor").get_text(strip=True),
            "parcela": row.select_one(".tdParcela").get_text(strip=True) or None,
            "valor": (
                parse_value(receita.get_text())
                if receita
                else -parse_value(despesa.get_text())
            ),
            "tipo": "receita" if receita else "despesa",
            "status": row.get("data-status"),
            "origem": row.get("data-origem"),
            "vencimento": row.get("data-vencimento"),
            "forma_pagamento": row.get("data-tipofromapagamento"),
        }

        result["lancamentos"].append(lancamento)

    return result["lancamentos"]
