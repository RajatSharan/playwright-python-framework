from pages.base_page import Basepage

class LoginPage(Basepage):
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
    