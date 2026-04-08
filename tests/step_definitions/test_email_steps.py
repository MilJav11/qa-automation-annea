import os
from dotenv import load_dotenv
from pytest_bdd import scenarios, given, when, then

# Toto načíta premenné zo súboru .env do systému
load_dotenv()

scenarios("email_workflow.feature")

@given("the user is logged into their email account")
def log_in(login_page):
    login_page.navigate("https://login.szn.cz/")
    
    # Načítame hodnoty zo systému pomocou kľúčov, ktoré sme definovali v .env
    user_email = os.getenv("TEST_EMAIL")
    user_password = os.getenv("TEST_PASSWORD")
    
    login_page.login(user_email, user_password)

@when("the user composes a new email for a contact from the list")
def compose_email(mail_page):
    # Fix 1: Posielame to bezpečne priamo na tvoj Seznam
    mail_page.compose_email_to("annea.test.milos@seznam.cz")

@when("the user attaches a document to the email")
def attach_document(mail_page):
    # Vygenerujeme si rýchly testovací súbor priamo v kóde
    with open("test_priloha_annea.txt", "w", encoding="utf-8") as f:
        f.write("Toto je testovacia príloha pre vypracovanie úlohy.")
    
    # A tu ho priložíme do e-mailu
    mail_page.attach_file("test_priloha_annea.txt")

@when("the user sends the email")
def send_email(mail_page):
    mail_page.send_email()

@then("the email should be successfully sent")
def verify_sent_email(page):
    # Fix 2: Čakáme na presne tento text, kým rýchlo nezmizne
    page.locator("text='E‑mail byl úspěšně odeslán.'").wait_for(state="visible", timeout=5000)

@then("the user logs out")
def log_out(mail_page):
    mail_page.logout()