from pages.login_page import LoginPage
from pages.base_page import Basepage
from utils.config import Config
from pages.register_page import RegisterPage
from utils.test_data import  TestData
import pytest

class TestRegister:
    
    @pytest.mark.regression
    def test_user_is_redirected_to_registration_page(self,page):
        login=LoginPage(page)
        login.navigate(Config.BASE_URL+'login')
        login.Register_New_Account()
     
    @pytest.mark.smoke   
    def test_user_registration_is_successful(self, page,user_data):
        login=LoginPage(page)
        login.navigate(Config.BASE_URL+'login')
        login.Register_New_Account()
        register = RegisterPage(page)
        register.fill_registration_form(user_data)
        register.accept_terms()
        register.click_register()
        print(register.verify_registration_successful())
