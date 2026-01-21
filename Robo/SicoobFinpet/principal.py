from .planilha import criar_planilha
from .conciliador import conciliar
from .vinculador import vincular


def executar_sicoob_finpet(dados):
    sicoob = dados.get("sicoob", [])
    finpet = dados.get("finpet", [])
    brands = dados.get("brands", [])

    vinculados = vincular(sicoob, finpet, brands)
    resultado = conciliar(vinculados)

    criar_planilha(resultado, "Relatorios/Sicoob Finpet.xlsx")

    return resultado