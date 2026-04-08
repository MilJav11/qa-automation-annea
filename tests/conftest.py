import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.mail_page import MailPage

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(locale="sk-SK")
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def mail_page(page):
    return MailPage(page)