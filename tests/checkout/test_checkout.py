from pages.checkout_page import Checkout
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.cart_page import CartPage
import pytest
class TestCheckout:
    
    @pytest.mark.smoke  
    def test_verify_user_able_to_place_order(self,page):
        login=LoginPage(page)
        login.login_as_default_user()
        dashboard=Dashboard(page)
        dashboard.search_and_select_plant(plant_name = "Snake Plant")
        cart=CartPage(page)
        cart.click_on_Checkout()
        checkout=Checkout(page)
        checkout.click_place_order()
        page.wait_for_timeout(3000)