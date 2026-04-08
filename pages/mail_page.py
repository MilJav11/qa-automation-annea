from .base_page import BasePage

class MailPage(BasePage):
    def compose_email_to(self, contact_email):
        try:
            self.page.get_by_test_id("cw-button-agree-with-ads").click(timeout=3000)
        except:
            pass

        self.page.get_by_text("Nová zpráva").click()
        
        self.page.get_by_role("textbox", name="Komu…").fill(contact_email)
        self.page.get_by_role("textbox", name="Předmět:").fill("Test z automatizácie")
        
        self.page.locator(".area").first.fill("Ahoj, posielam prílohu zo zadania.")

    def attach_file(self, file_path):
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_role("button", name="Přiložit soubory").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def send_email(self):
        self.page.get_by_role("button", name="Odeslat e‑mail").click()

    def logout(self):
        self.page.get_by_role("button", name="Uživatel – osobní menu").click()
        self.page.get_by_role("link", name="Odhlásit se").click()