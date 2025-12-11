from api import get_extrato
from datetime import date
import json


def main():
    hoje = date.today()
    extrato = get_extrato(hoje.month, hoje.year)["resultado"]["transacoes"]

    if extrato:
        print(json.dumps(extrato))
    else:
        print("Falha ao obter extrato")


if __name__ == "__main__":
    main()
