from .base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.page.get_by_role("textbox", name="Prihláste sa pomocou e-mailu").fill(username)
        self.page.get_by_role("button", name="Pokračovať").click()
        self.page.get_by_role("textbox", name="Heslo").fill(password)
        self.page.get_by_role("button", name="Prihlásiť sa").click()
        
    
        if "ucet.seznam.cz" in self.page.url:
            self.page.get_by_alt_text("logo").first.click()