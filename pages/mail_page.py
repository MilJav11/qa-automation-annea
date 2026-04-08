from .base_page import BasePage

class MailPage(BasePage):
    def compose_email_to(self, contact_email):
        # Handle cookie/ad consent if present
        try:
            self.page.get_by_test_id("cw-button-agree-with-ads").click(timeout=3000)
        except:
            pass

        # Safeguard: Wait for the mailbox page to fully load after login
        self.page.wait_for_load_state("networkidle")

        # Click compose button
        compose_btn = self.page.locator('a[href*="compose"], :text-is("Napsat e-mail"), :text-is("Nová zpráva")').first
        compose_btn.click()
        
        # SLOWDOWN: Short pauses between filling fields to mimic human behavior
        self.page.wait_for_timeout(500)
        self.page.get_by_role("textbox", name="Komu…").fill(contact_email)
        
        self.page.wait_for_timeout(500)
        self.page.get_by_role("textbox", name="Předmět:").fill("Annea QA Assignment - Automated Test")
        
        self.page.wait_for_timeout(500)
        self.page.locator(".area").first.fill("Hello,\n\nSending the assignment attachment.\n\nBest regards.\n\nMiloš")

    def attach_file(self, file_path):
        # Open file chooser and upload
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_role("button", name="Přiložit soubory").click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)
        
        # CRITICAL SLOWDOWN: Wait 3 seconds for Seznam to finish uploading the attachment
        self.page.wait_for_timeout(3000)

    def send_email(self):
        # Short pause before hitting send to ensure the UI is fully ready
        self.page.wait_for_timeout(1000)
        self.page.get_by_role("button", name="Odeslat e‑mail").click()

    def logout(self):
        # Wait a moment before logging out to ensure the "sent" process completes
        self.page.wait_for_timeout(2000)
        self.page.get_by_role("button", name="Uživatel – osobní menu").click()
        self.page.get_by_role("link", name="Odhlásit se").click()