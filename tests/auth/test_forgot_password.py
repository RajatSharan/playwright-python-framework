# tests/auth/test_forgot_password.py
import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from utils.config import Config


@allure.feature("Authentication")
class TestForgotPassword:

    @pytest.mark.smoke
    @allure.story("Reset password request submits successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_reset_password_request_is_successful(self, page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.forgotPassword()
        forgot_password = ForgotPage(page)
        forgot_password.Email_Address(Config.USERNAME)

    @pytest.mark.regression
    @allure.story("Back to login link works from forgot password page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_back_to_login_link_is_working(self, page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.forgotPassword()
        forgot_password = ForgotPage(page)
        forgot_password.reset_password_button()

    @pytest.mark.regression
    @allure.story("Reset button is disabled when email field is empty")
    @allure.severity(allure.severity_level.NORMAL)
    def test_reset_button_is_disabled_without_email(self, page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.forgotPassword()
        forgot_password = ForgotPage(page)
        forgot_password.verify_element_is_disabled(forgot_password.reset_password_button())