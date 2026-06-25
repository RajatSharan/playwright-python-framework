from pages.base_page import BasePage

class OrderConfirmationPage(BasePage):

    SUCCESS_MESSAGE = "text=Thank you for your purchase!"
    
    def verify_order_success_message(self):
        self.verify_text(
        self.SUCCESS_MESSAGE,
        "Thank you for your purchase! Your order has been placed successfully."
    )