from pages.checkout_page import Checkout
from pages.login_page import LoginPage
from pages.dashboard_page import Dashboard
from pages.cart_page import CartPage
from pages.order_confirmation_page import OrderConfirmationPage

class TestPurchasePlantFlow:

    def test_user_can_purchase_plant_successfully(self,page):
        login=LoginPage(page)
        login.login_as_default_user()
        dashboard=Dashboard(page)
        dashboard.search_and_select_plant(plant_name='Fiddle Leaf')
        cart=CartPage(page)
        cart.click_on_Checkout()
        checkout=Checkout(page)
        checkout.click_place_order()
        orderconfirmation=OrderConfirmationPage(page) 
        orderconfirmation.verify_order_success_message()


    