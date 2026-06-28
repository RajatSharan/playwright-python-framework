# tests/auth/test_register.py
import pytest
import allure
from pages.login_page import LoginPage
from pages.base_page import BasePage         # ← FIXED: was Basepage
from pages.register_page import RegisterPage
from utils.config import Config
from utils.test_data import TestData


@allure.feature("Registration")
class TestRegister:

    @pytest.mark.regression
    @allure.story("Register link on login page redirects to registration")
    @allure.severity(allure.severity_level.NORMAL)
    def test_user_is_redirected_to_registration_page(self, page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.Register_New_Account()
        assert "register" in page.url.lower(), f"Expected registration URL but got: {page.url}"

    @pytest.mark.smoke
    @allure.story("New user can register successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_registration_is_successful(self, page, user_data):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.Register_New_Account()

        register = RegisterPage(page)
        register.fill_registration_form(user_data)
        register.accept_terms()
        register.click_register()

        result = register.verify_registration_successful()
        assert result, "Registration successful! Please log in."