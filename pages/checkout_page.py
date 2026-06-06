from pages.base_page import Basepage


class Checkout(Basepage):
    
    PLACE_ORDER_BUTTON ="button.btn-place-order"
    
    
    def click_place_order(self):
        self.click(self.PLACE_ORDER_BUTTON )
        