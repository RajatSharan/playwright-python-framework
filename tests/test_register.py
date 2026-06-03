from pages.login_page import LoginPage
from pages.base_page import Basepage
from utils.config import Config

class TestRegister:
    
    def test_user_is_redirected_to_registration_page(self,page):
        login=LoginPage(page)
        login.navigate(Config.BASE_URL+'login')
        login.Register_New_Account()