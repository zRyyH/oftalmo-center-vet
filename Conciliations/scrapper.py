from browser import BrowserManager
from date_utils import format_conciliation_url


class SimplesvetScrapper:
    """Scrapper para o sistema SimplesVet."""

    BASE_URL = "https://app.simples.vet/login/login.php"

    def __init__(self, email: str, password: str):
        self._email = email
        self._password = password
        self._browser = BrowserManager()

    @property
    def _page(self):
        return self._browser.page

    def login(self):
        """Realiza login no SimplesVet."""
        self._page.goto(self.BASE_URL)

        self._page.get_by_role("textbox", name="Email").fill(self._email)
        self._page.get_by_role("textbox", name="Senha").fill(self._password)
        self._page.get_by_role("button", name="Entrar no SimplesVet").click()
        self._page.wait_for_load_state("networkidle")

    def get_conciliations(self, start_date: str, end_date: str) -> dict:
        """Obtém conciliações do período especificado.

        Args:
            start_date: Data inicial (YYYY-MM-DD)
            end_date: Data final (YYYY-MM-DD)

        Returns:
            Dados das conciliações em formato JSON
        """
        url = format_conciliation_url(start_date, end_date)
        response = self._page.request.get(url)
        return response.json()

    def __enter__(self):
        self._browser.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._browser.stop()
