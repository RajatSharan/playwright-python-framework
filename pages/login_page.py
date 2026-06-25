from pages.base_page import BasePage
from utils.config import Config

class LoginPage(BasePage):
    USERNAME_FIELD  = "#username"
    PASSWORD_FIELD  = "#password"
    LOGIN_BUTTON   = "#signInButton"
    SIGNUP_BUTTON = "a[href='/register']"
    FORGOT_PASSWORD_BUTTON = "a[href='/forgot-password']"
    BACK_TO_LOGIN="a[herf='/login']"
  
    def login(self, username: str, password: str):
        self.fill(self.USERNAME_FIELD, username)
        self.fill(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def forgotPassword(self):
        self.click(self.FORGOT_PASSWORD_BUTTON)
        
    def Register_New_Account(self):
        self.click(self.SIGNUP_BUTTON)
        
    def login_as_default_user(self):
        self.navigate(Config.BASE_URL + "/login")
        self.login(Config.USERNAME, Config.PASSWORD)
    