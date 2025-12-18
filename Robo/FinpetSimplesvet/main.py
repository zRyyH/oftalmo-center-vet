from vinculador import finpet_simplesvet, resumo_vinculacao
from services.service import get_data
import json

print("Buscando dados...")

dados = get_data()
finpet = dados.get("finpet", [])
releases = dados.get("releases", [])

print("Processando...")

resultados = finpet_simplesvet(finpet, releases, min_score=2)

resumo = resumo_vinculacao(resultados)
print(f"Total: {resumo['total']}")
print(f"Vinculados: {resumo['vinculados']}")
print(f"Não vinculados: {resumo['nao_vinculados']}")
print(f"Score médio: {resumo['score_medio']:.2f}")

for r in resultados[:5]:
    if r["release"]:
        print(
            f"\nFinpet {r['finpet']['id']} -> Release {r['release']['id']} (score: {r['score']})"
        )

with open("resultado.json", "w") as f:
    f.write(json.dumps(resultados, indent=4))
