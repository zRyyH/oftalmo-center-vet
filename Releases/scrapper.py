from browser import BrowserManager
from date_utils import format_date_range
from transformer import transform_releases

class SimplesvetScrapper:
    """Scrapper para o sistema SimplesVet."""

    BASE_URL = "https://app.simples.vet/login/login.php"
    RELEASES_URL = "https://app.simples.vet/financeiro/lancamento/lancamento_load.php"

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

    def get_releases(self, start_date: str, end_date: str) -> dict:
        """Obtém lançamentos financeiros do período.

        Args:
            start_date: Data inicial (YYYY-MM-DD)
            end_date: Data final (YYYY-MM-DD)

        Returns:
            Dados dos lançamentos em formato JSON
        """
        form_data = {
            "p__lan_dat_ordem": format_date_range(start_date, end_date),
            "p__cta_int_codigo": "T",
            "p__cta_int_codigo_text": "Todas as contas",
            "p__cat_int_codigo": "",
            "p__cat_int_codigo_text": "Todas as categorias",
            "p__selecionado": "",
            "p__tipo_exportar": "",
            "p__usu_int_codigo_relatoriolog": "",
            "p__for_int_codigo": "",
            "p__for_int_codigo_text": "",
            "p__lan_cha_status": "",
            "p__lan_cha_status_text": "",
            "p__lan_cha_natureza": "",
            "p__lan_cha_natureza_text": "",
            "p__lan_cha_competencia": "CX",
            "p__lan_cha_competencia_text": "",
            "p__fpg_int_codigo": "",
            "p__fpg_int_codigo_text": "",
            "p__frb_int_codigo": "",
            "p__frb_int_codigo_text": "",
            "p__cta_cha_tipo": "",
            "p__cta_cha_tipo_text": "",
            "p__lan_txt_descricao": "",
            "p__cai_int_id": "",
            "p__lan_dec_valor": "",
            "p__lan_var_documento": "",
            "AMBIENTE": "4bac1806d6cbcbf548df329af0065a2b566d7383",
        }

        response = self._page.request.post(self.RELEASES_URL, form=form_data)
        return transform_releases(response.text())

    def __enter__(self):
        self._browser.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._browser.stop()
