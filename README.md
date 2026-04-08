# Annea QA Automation Assignment

Professional E2E test suite for Seznam.cz email workflow using Playwright and Python.

## 🚀 Features

- **BDD Framework:** Human-readable tests using Gherkin (Pytest-BDD).
- **Page Object Model:** Clean separation of test logic and UI selectors.
- **CI/CD Integrated:** GitHub Actions workflow included.
- **Security:** Credential management via environment variables.

## 🛠️ Setup

1. Clone the repo.
2. Create a `.env` file with `TEST_EMAIL` and `TEST_PASSWORD`.
3. Run `pip install -r requirements.txt`.
4. Run `playwright install chromium`.
5. Execute tests using `pytest`.
