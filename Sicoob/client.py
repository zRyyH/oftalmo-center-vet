import requests
import config


def request(method: str, url: str, **kwargs) -> requests.Response | None:
    try:
        return requests.request(
            method=method,
            url=url,
            cert=(config.CERT_CRT, config.CERT_KEY),
            timeout=30,
            **kwargs,
        )
    except requests.RequestException as e:
        print(f"Erro na requisiÃ§Ã£o: {e}")
        return None
