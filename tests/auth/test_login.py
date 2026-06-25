# tests/auth/test_login.py
import pytest
import allure
from pages.login_page import LoginPage
from utils.config import Config


@allure.feature("Authentication")
class TestLogin:

    @pytest.mark.smoke
    @allure.story("Valid login redirects to dashboard")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self, page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.login(Config.USERNAME, Config.PASSWORD)
        page.wait_for_url("**dashboard**")
        assert "dashboard" in page.url, f"Expected dashboard URL but got: {page.url}"

    @pytest.mark.regression
    @allure.story("Forgot password link redirects correctly")
    @allure.severity(allure.severity_level.NORMAL)
    def test_forgot_password_link(self, page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.forgotPassword()
        page.wait_for_url("**forgot-password**")
        assert "forgot-password" in page.url, f"Expected forgot-password URL but got: {page.url}"