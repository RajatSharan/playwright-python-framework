from pages.order_confirmation_page import OrderConfirmationPage


class testorderconfirmation():
    
    def verify_order_success_message(self,page):
    
        order_confirmation = OrderConfirmationPage(page)

        order_confirmation.verify_order_success_message()