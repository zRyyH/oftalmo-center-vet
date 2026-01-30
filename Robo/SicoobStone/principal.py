from .normalizers import normalize_stone_sicoob_brands, processar_dados
from .planilha import gerar_planilha_sicoob
from .extract_data import extrair_dados
from .conciliations import conciliar
import json


def executar_sicoob_stone(dados):
    dados.update({"stone": extrair_dados("Stone/extrato.xlsx")})
    dados_normalizados = normalize_stone_sicoob_brands(dados)
    dados_processados = processar_dados(dados_normalizados)
    dados_conciliados = conciliar(dados_processados)
    gerar_planilha_sicoob(dados_conciliados, "Relatorios/Sicoob Stone.xlsx")

    with open("Entradas/sicoob_stone.json", "w") as FileW:
        FileW.write(json.dumps(dados_processados, indent=4))

    return dados_conciliados
