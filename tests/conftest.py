import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.mail_page import MailPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        # Otvorí prehliadač a spomalí ho, aby si videl, čo robí
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def mail_page(page):
    return MailPage(page)