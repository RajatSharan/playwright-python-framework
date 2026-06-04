# 🎭 Playwright Python Automation Framework

> A production-ready, scalable UI test automation framework built with **Playwright**, **Pytest**, **Allure Reports**, and **Faker** — following the **Page Object Model** design pattern.

---

## ⚡ Quick Start (5 Minutes Setup)

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install

# 5. Run all tests
python run.py
```

> ✅ That's it! Your first test run should be up in under 5 minutes.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Running Tests](#-running-tests)
- [Test Execution Strategy](#-test-execution-strategy)
- [Allure Reporting](#-allure-reporting)
- [Framework Features](#-framework-features)
- [Project Structure](#-project-structure)
- [Best Practices](#-best-practices)

---

## 🧩 Project Overview

This framework provides a **robust, maintainable, and scalable** foundation for end-to-end UI test automation. It is designed to support fast feedback cycles, clear test reporting, and easy onboarding for new team members.

### Core Technologies

| Tool | Purpose |
|------|---------|
| [Playwright](https://playwright.dev/python/) | Browser automation — supports Chromium, Firefox, and WebKit |
| [Pytest](https://docs.pytest.org/) | Test runner with powerful fixtures, markers, and plugin support |
| [Allure Reports](https://docs.qameta.io/allure/) | Rich, interactive HTML reports with steps, screenshots, and history |
| [Faker](https://faker.readthedocs.io/) | Dynamic, realistic test data generation |
| [Page Object Model](https://playwright.dev/python/docs/pom) | Design pattern that separates UI locators from test logic |

---

## 🔧 Prerequisites

Before setting up this project, make sure the following are installed on your system:

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| Python | 3.9+ | `python --version` |
| Git | Latest | `git --version` |
| pip | Latest | `pip --version` |
| Node.js *(for Allure CLI)* | 14+ | `node --version` |

> **Note:** Playwright downloads its own browser binaries and does **not** require a separately installed browser.

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> You should see `(venv)` at the start of your terminal prompt once activated.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

This downloads Chromium, Firefox, and WebKit browser binaries locally.

### 5. Verify Installation

```bash
pytest --version
playwright --version
```

Expected output:
```
pytest 7.x.x
Version 1.x.x
```

---

## ▶️ Running Tests

All test execution is managed through `run.py` for a consistent, one-command experience.

### Run All Tests

```bash
python run.py
```

### Run Smoke Tests Only

```bash
python run.py smoke
```

### Run Regression Tests Only

```bash
python run.py regression
```

### Run a Specific Test File

```bash
pytest tests/test_register.py
```

### Run a Specific Test Case

```bash
pytest tests/test_register.py::TestRegister::test_user_registration_is_successful
```

### Additional Pytest Options

```bash
# Run in headed mode (see the browser)
pytest --headed

# Run on a specific browser
pytest --browser firefox
pytest --browser webkit

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x
```

---

## 🎯 Test Execution Strategy

### 🟢 Smoke Tests
Smoke tests cover the **critical, high-priority flows** of the application — the paths that must work for the app to be considered functional. They are fast, minimal, and run on every deployment or build.

Marked with: `@pytest.mark.smoke`

### 🔵 Regression Tests
Regression tests provide **broader coverage** across all features and edge cases. They are run on scheduled pipelines or before releases to ensure no existing functionality has broken.

Marked with: `@pytest.mark.regression`

### Using Markers

Markers are defined in `pytest.ini` and applied as decorators in your test files:

```python
import pytest

@pytest.mark.smoke
def test_login_is_successful(page):
    ...

@pytest.mark.regression
def test_user_profile_update(page):
    ...
```

Run tests by marker directly:

```bash
pytest -m smoke
pytest -m regression
pytest -m "smoke or regression"
```

---

## 📊 Allure Reporting

### Automatic Reports (via `run.py`)

Allure results are generated **automatically** when you run tests through `run.py`. No additional configuration is needed.

```bash
python run.py
# Report will be generated and served automatically
```

### Manual Report Generation

```bash
# Step 1: Run tests and collect results
pytest --alluredir=allure-results

# Step 2: Serve the interactive report in your browser
allure serve allure-results
```

### Installing Allure CLI

```bash
# Using npm
npm install -g allure-commandline

# Or using Scoop (Windows)
scoop install allure

# Or using Homebrew (Mac)
brew install allure
```

> **Tip:** Allure reports include test steps, screenshots on failure, execution timelines, and history trends — making it easy to diagnose flaky or failing tests.

---

## ✨ Framework Features

### 📁 Page Object Model (POM)
Every page of the application has a dedicated class in the `pages/` directory. Locators and actions are encapsulated within the page class, keeping tests clean and readable.

```python
# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("button[type='submit']")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
```

### 🧱 Reusable Base Page
A `BasePage` class in `pages/` provides shared methods (e.g., wait for element, scroll, take screenshot) that all page objects can inherit.

### 🧪 Faker Test Data Generation
Dynamic test data is generated using `Faker` to avoid hardcoded values and enable variety across test runs.

```python
from faker import Faker
fake = Faker()

email = fake.email()
name = fake.name()
password = fake.password(length=12)
```

### 🔩 Pytest Fixtures
`conftest.py` defines reusable fixtures for browser setup, page initialization, and test data — shared automatically across all test files.

### 📈 Allure Reporting
Tests are instrumented with Allure decorators for detailed, visual reports.

```python
import allure

@allure.feature("Registration")
@allure.story("New user can register successfully")
def test_user_registration_is_successful(register_page):
    ...
```

### 🏷️ Smoke and Regression Suite Support
Tests are tagged with `@pytest.mark.smoke` or `@pytest.mark.regression` to enable targeted execution in CI/CD pipelines.

---

## 📂 Project Structure

```
project/
│
├── pages/                      # Page Object classes (one per page/component)
│   ├── base_page.py            # Shared/reusable base methods
│   ├── login_page.py
│   ├── register_page.py
│   └── dashboard_page.py
│
├── tests/                      # Test files organized by feature
│   ├── test_login.py
│   ├── test_register.py
│   └── test_dashboard.py
│
├── utils/                      # Helper utilities
│   ├── data_generator.py       # Faker-based test data factories
│   └── helpers.py              # Generic reusable helper functions
│
├── reports/                    # Allure results and report output
│   └── allure-results/
│
├── conftest.py                 # Pytest fixtures (browser, page, data)
├── pytest.ini                  # Pytest configuration and markers
├── run.py                      # Entry point for test execution
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

---

## ✅ Best Practices

| Practice | Details |
|----------|---------|
| 🚫 **Exclude `venv/`** | Add `venv/` to `.gitignore`. Never commit your virtual environment. |
| 🔐 **Keep secrets out of code** | Store credentials, base URLs, and tokens in config files or environment variables — not in test files. |
| ♻️ **Reuse page methods** | Never duplicate locator logic. If a page action is used more than once, it belongs in the Page Object. |
| 📦 **Separate test data** | Keep test data in `utils/data_generator.py` or fixtures. Avoid hardcoding values directly inside test functions. |
| 🏷️ **Always mark your tests** | Apply `@pytest.mark.smoke` or `@pytest.mark.regression` to every test for targeted execution. |
| 📸 **Use Allure attachments** | Attach screenshots and logs on test failure for easier debugging in reports. |
| 🔄 **Keep tests independent** | Each test should set up and tear down its own state. Never rely on test execution order. |

---

## 📦 Requirements

Key packages used in this framework (see `requirements.txt` for full list):

```
playwright
pytest
pytest-playwright
allure-pytest
faker
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes using conventional commits: `git commit -m "feat: add login page object"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---


Made with 🎭 Playwright + 🐍 Python

</div>
