from pages.base_page import Basepage
from pages.login_page import LoginPage


class CartPage(Basepage):
    
    checkout='.btn.btn-success.btn-place-order'
    
    
    def click_on_Checkout(self):
        self.click(self.checkout)
        