# tests/cart/test_cart.py
import pytest
import allure
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.cart_page import CartPage


@allure.feature("Cart")
class TestCart:

    @pytest.mark.smoke
    @allure.story("User can add item to cart and proceed to checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_can_place_order_successfully(self, logged_in_page):
        # logged_in_page fixture handles login — no repeated login code here
        dashboard = Dashboard(logged_in_page)
        dashboard.search_and_select_plant(plant_name="Snake Plant")

        cart = CartPage(logged_in_page)
        cart.click_on_Checkout()

        # Wait for checkout page to load instead of hardcoded sleep
        logged_in_page.wait_for_url("**checkout**")
        assert "checkout" in logged_in_page.url, \
            f"Expected checkout page but got: {logged_in_page.url}"