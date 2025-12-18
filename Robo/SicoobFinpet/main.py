from services.service import get_data
from conciliator import sicoob_finpet
from generated import gerar_excel
from conci import conciliar
import json


print("START")
dados = get_data(limit=99999)
print("PROCESSANDO")

datao = sicoob_finpet(dados["sicoob"], dados["finpet"], dados["brands"])
kkk = conciliar(datao)

gerar_excel(kkk)