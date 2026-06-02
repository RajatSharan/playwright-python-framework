from pages.base_page import Basepage

class ForgotPage(Basepage):
    
    EMAIL="#email"
    RESET_BUTTON="#resetPasswordBtn"
    
    
    Back_to_Login_Link='text=Back to Login'
    
    
    def BacktoLogin(self):
        self.click(self.Back_to_Login_Link)
    
    def Email_Address(self,email:str):
        self.fill(self.EMAIL,email)
        self.click(self.RESET_BUTTON)
    
    def reset_password_button(self):
        return self.page.locator("button[type='submit']")