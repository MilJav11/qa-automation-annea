from .base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        # Handle Seznam cookie consent banner if present
        try:
            self.page.get_by_role("button", name="Souhlasím").click(timeout=3000)
        except:
            pass

        # Fill username
        email_input = self.page.get_by_role("textbox", name="Prihláste sa pomocou e-mailu").or_(
            self.page.get_by_label("E-mailová adresa", exact=True)
        ).first
        email_input.fill(username)
        
        # Click continue
        continue_btn = self.page.get_by_role("button", name="Pokračovať").or_(
            self.page.get_by_role("button", name="Pokračovat")
        ).first
        continue_btn.click()
        
        # Fill password
        self.page.get_by_role("textbox", name="Heslo").first.fill(password)
        
        # Click login
        login_btn = self.page.get_by_role("button", name="Prihlásiť sa").or_(
            self.page.get_by_role("button", name="Přihlásit se")
        ).first
        login_btn.click()

        self.page.wait_for_timeout(4000)

        self.page.goto("https://email.seznam.cz/")