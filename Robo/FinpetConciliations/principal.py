from .planilha import criar_planilha
from .conciliador import conciliar


def executar_finpet_conciliacoes(dados: dict):
    finpet = dados.get("finpet", [])
    conciliations = dados.get("conciliations", [])
    brands = dados.get("brands", [])

    resultado = conciliar(finpet, conciliations, brands)

    criar_planilha(resultado, "Relatorios/Finpet Conciliações.xlsx")

    return resultado
