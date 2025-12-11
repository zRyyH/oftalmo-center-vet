import config
import client


def get_access_token() -> str | None:
    resp = client.request(
        "POST",
        config.AUTH_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "client_credentials",
            "scope": config.AUTH_SCOPE,
            "client_id": config.CLIENT_ID,
        },
    )

    if resp and resp.status_code == 200:
        return resp.json()["access_token"]

    print(f"Erro ao obter token: {resp.text if resp else 'Sem resposta'}")
    return None


def get_extrato(mes: int, ano: int) -> dict | None:
    token = get_access_token()
    if not token:
        return None

    url = config.EXTRATO_URL.format(mes=mes, ano=ano)
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {token}",
        "client_id": config.CLIENT_ID,
    }
    params = {"numeroContaCorrente": config.CONTA_CORRENTE}

    resp = client.request("GET", url, headers=headers, params=params)

    if resp and resp.status_code == 200:
        return resp.json()

    print(f"Erro ao obter extrato: {resp.text if resp else 'Sem resposta'}")
    return None
