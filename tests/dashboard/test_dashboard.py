from pytest_playwright.pytest_playwright import context

from pages.base_page import Basepage
from pages.login_page import LoginPage 
from utils.config import Config
from pages.dashboard_page import Dashboard
import pytest

class TestDashboard:

    @pytest.mark.regression
    def test_MyOrderLink_redirects_to_My_Order_page(self,page):
        login=LoginPage(page)
        login.login_as_default_user()
        page.wait_for_url("**dashboard**")
        dashboard= Dashboard(page)
        dashboard.MY_Order_Link()
      
    @pytest.mark.smoke   
    #@pytest.mark.parametrize("plantname", ["Monstera", "Snake Plant", "Fiddle Leaf Fig"])
    def test_user_can_search_for_plant(self,page):
        login=LoginPage(page)
        login.login_as_default_user()
        dashboard= Dashboard(page)
        plant = "Snake Plant"
        dashboard.search_plant(plant) 
        initial_count = dashboard.get_cart_count()
        dashboard.click_buy_now()
        page.wait_for_load_state("networkidle")
        page.reload(wait_until="networkidle")
        expected_count = str(initial_count + 1)
        dashboard.verify_text(dashboard.cartCountBadge, expected_count,timeout=5000)
        dashboard.click_Cart_Icon()
        page.wait_for_timeout(3000)
        