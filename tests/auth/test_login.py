import pytest
from pages.login_page import LoginPage
from utils.config import Config
from pages.forgot_page import ForgotPage

class TestLogin:

    @pytest.mark.smoke
    def test_valid_login(self, page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.login(Config.USERNAME, Config.PASSWORD)
        page.wait_for_url("**dashboard**")
        assert "dashboard" in page.url, f"Expected dashboard but got: {page.url}"
    
    @pytest.mark.regression
    def test_forgotPassword_Link(self,page):
        login= LoginPage(page)
        login.navigate(Config.BASE_URL+"/login")
        login.forgotPassword()
        page.wait_for_url("**forgot-password**")
        assert "forgot-password" in page.url,f"Expected Forgot Password: {page.url}"