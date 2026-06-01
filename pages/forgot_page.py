from pages.base_page import Basepage

class ForgotPage(Basepage):
    
    Back_to_Login_Link='text=Back to Login'
    
    
    def BacktoLogin(self):
        self.click(self.Back_to_Login_Link)