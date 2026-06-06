from pages.base_page import Basepage
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.cart_page import CartPage
import pytest

class TestCart:
    
    @pytest.mark.smoke   
    def test_user_can_place_order_successfully(self,page):
        login = LoginPage(page)
        login.login_as_default_user()
        dashboard=Dashboard(page)
        dashboard.search_and_select_plant(plant_name = "Snake Plant")
        cart= CartPage(page)
        cart.click_on_Checkout()
        page.wait_for_timeout(3000)
        