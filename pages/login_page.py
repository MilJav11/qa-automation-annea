from .base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        # 1. Vyplnenie údajov (toto ti už fungovalo)
        self.page.get_by_role("textbox", name="Prihláste sa pomocou e-mailu").fill(username)
        self.page.get_by_role("button", name="Pokračovať").click()
        self.page.get_by_role("textbox", name="Heslo").fill(password)
        self.page.get_by_role("button", name="Prihlásiť sa").click()
        
        # 2. POISTKA: Ak nás Seznam hodil na ucet.seznam.cz, klikneme na logo
        # Používame selektor alt='logo', ktorý si našiel
        if "ucet.seznam.cz" in self.page.url:
            self.page.get_by_alt_text("logo").first.click()