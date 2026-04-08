from .base_page import BasePage

class MailPage(BasePage):
    def compose_email_to(self, contact_email):
        # 1. Ošetrenie reklamy (ak by náhodou vyskočila)
        try:
            self.page.get_by_test_id("cw-button-agree-with-ads").click(timeout=3000)
        except:
            pass

        # 2. Klik na Novú správu (hľadáme text v SPAN-e)
        self.page.get_by_text("Nová zpráva").click()
        
        # 3. Vyplnenie polí (podľa tvojho Codegenu)
        self.page.get_by_role("textbox", name="Komu…").fill(contact_email)
        self.page.get_by_role("textbox", name="Předmět:").fill("Test z automatizácie")
        
        # 4. Telo správy
        self.page.locator(".area").first.fill("Ahoj, posielam prílohu zo zadania.")

    def attach_file(self, file_path):
        # Použijeme metódu, ktorú Playwright miluje najviac
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_role("button", name="Přiložit soubory").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def send_email(self):
        self.page.get_by_role("button", name="Odeslat e‑mail").click()

    def logout(self):
        # Klikne na profilovú ikonu vpravo hore (AT)
        self.page.get_by_role("button", name="Uživatel – osobní menu").click()
        # Klikne na odhlásenie
        self.page.get_by_role("link", name="Odhlásit se").click()