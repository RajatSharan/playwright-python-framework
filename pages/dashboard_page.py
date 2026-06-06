from pages.base_page import Basepage
from pages.login_page import LoginPage 
from utils.config import Config


class Dashboard(Basepage):
    
    logo ="text=PlantNest";
    dashboardMenu = "text=Dashboard";
    myOrdersMenu = "text=My Orders";
    profileMenu = "text=Profile";
    cartMenu = "text=Cart";
    cartIcon = 'a:has-text("Cart")';
    logoutButton = ("text=Logout");
    searchButton = ('button:has-text("Search")');
    collectionTitle = ("text=Our Green Collection");
    plantCards = (".card.product-card");
    buyNowButtons = ("button:has-text('Buy Now')")
    buyNowButton=".add-to-cart-btn"
    searchResults = (".card.product-card");
    plantNames = (".card.product-card h5");
    cartCountBadge = ("#cart-count");
    searchInput = ('#search-input')

    
    def MY_Order_Link(self):
        self.click(self.myOrdersMenu)
        
    def search_plant(self,plantname:str):
        self.fill(self.searchInput,plantname)
        self.click(self.searchButton)
    
    def click_buy_now(self):
        self.click(self.buyNowButton)
        
    def get_cart_count(self) -> int:
        # Get the text, convert to int
       count_str = self.page.locator(self.cartCountBadge).inner_text().strip()
       return int(count_str) if count_str.isdigit() else 0
   
    def click_Cart_Icon(self):
        self.click(self.cartIcon)
        
    def search_and_select_plant(self, plant_name):
        self.search_plant(plant_name) 
        self.click_buy_now()
        self.click_Cart_Icon()
        