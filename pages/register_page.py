from pages.base_page import Basepage
from playwright.sync_api import expect



class RegisterPage(Basepage):
    
    FIRST_NAME = "#firstName"
    LAST_NAME = "#lastName"
    USERNAME = "#username"
    EMAIL = "#email"
    PHONE_NUMBER = "#phoneNumber"
    ADDRESS = "#address"
    PASSWORD = "#password"
    CONFIRM_PASSWORD = "#confirmPassword"
    TERMS = "#terms"
    REGISTER_BUTTON = "button[type='submit']"
    
    def fill_registration_form(self,user):
        self.fill(self.FIRST_NAME, user["first_name"])
        self.fill(self.LAST_NAME, user["last_name"])
        self.fill(self.USERNAME, user["username"])
        self.fill(self.EMAIL, user["email"])
        self.fill(self.PHONE_NUMBER, user["phone_number"])
        self.fill(self.ADDRESS, user["address"])
        self.fill(self.PASSWORD, user["password"])
        self.fill(self.CONFIRM_PASSWORD, user["confirm_password"])
    
    def accept_terms(self):
        self.check(self.TERMS)

    def click_register(self):
        self.click(self.REGISTER_BUTTON)
        
    def verify_registration_successful(self):
        self.verify_text(
            self.page.get_by_role("alert"),
            "Registration successful! Please log in."
        )