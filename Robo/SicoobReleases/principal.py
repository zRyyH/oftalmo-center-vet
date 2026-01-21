from .planilha import criar_planilha
from .conciliador import conciliar


def executar_sicoob_releases(dados):
    resultado = conciliar(dados)
    itens = resultado.get("itens", [])

    if itens:
        criar_planilha(itens, "Relatorios/Sicoob Lançamentos.xlsx")

    return resultado
