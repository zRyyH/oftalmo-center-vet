from browser import BrowserManager
from date_utils import format_period


class FinpetScrapper:
    """Scrapper para o sistema Finpet/Evoluservices."""

    BASE_URL = "https://app.evoluservices.com"

    def __init__(self, email: str, password: str):
        self._email = email
        self._password = password
        self._browser = BrowserManager()

    @property
    def _page(self):
        return self._browser.page

    def login(self):
        """Realiza login no sistema."""
        self._page.goto(self.BASE_URL)
        self._page.locator("#j_username").fill(self._email)
        self._page.locator("#j_password").fill(self._password)
        self._page.get_by_role("button", name="Fazer login").click()
        self._page.wait_for_load_state("networkidle")

    def get_receipts(self, start_date: str, end_date: str, limit: int = 1000) -> dict:
        """Obtém recebimentos do período especificado.

        Args:
            start_date: Data inicial (YYYY-MM-DD ou DD/MM/YYYY)
            end_date: Data final (YYYY-MM-DD ou DD/MM/YYYY)
            limit: Número máximo de registros

        Returns:
            Dados dos recebimentos em formato JSON
        """
        period = format_period(start_date, end_date)
        url = f"{self.BASE_URL}/merchant/payments/search?searchInput.period={period}&limit={limit}&start=0"

        with self._page.expect_response(
            lambda r: "payments/search" in r.url
        ) as response:
            self._page.goto(url)

        return response.value.json()

    def __enter__(self):
        self._browser.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._browser.stop()
