# tests/conftest.py
import pytest
from pages.login_page import LoginPage
from utils.config import Config


@pytest.fixture
def logged_in_page(page):
    """
    Reusable fixture: returns a page already logged in.
    Use this in cart, checkout, dashboard, order-confirmation tests
    so you don't repeat login steps in every test.

    Usage in any test:
        def test_something(self, logged_in_page):
            dashboard = Dashboard(logged_in_page)
            ...
    """
    login = LoginPage(page)
    login.login_as_default_user()
    page.wait_for_url("**dashboard**")
    return page