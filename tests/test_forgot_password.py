from pages.base_page import Basepage
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from utils.config import Config

class TestForgotPassword:
    
    def test_reset_password_request_is_successful(self,page):
        login = LoginPage(page)
        login.navigate(Config.BASE_URL + "/login")
        login.forgotPassword()
        forgotpassword= ForgotPage(page)
        forgotpassword.Email_Address(Config.USERNAME)
    
    def test_to_verify_Back_To_Login_Link_is_Working(self,page):
        Login=LoginPage(page)
        Login.navigate(Config.BASE_URL + "/login")
        Login.forgotPassword()
        forgotpassword= ForgotPage(page)
        forgotpassword.click(forgotpassword.Back_to_Login_Link)
    
    def test_reset_button_is_disabled_without_email(self,page):
        Login=LoginPage(page)
        Login.navigate(Config.BASE_URL + "/login")
        Login.forgotPassword()
        forgot_password=ForgotPage(page)
        forgot_password.verify_element_is_disabled(forgot_password.reset_password_button())