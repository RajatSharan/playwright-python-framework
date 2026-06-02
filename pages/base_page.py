from playwright.sync_api import Page,expect

class Basepage:
    
    def __init__(self,page:Page):
        self.page=page
    
    def navigate(self,url:str):
        self.page.goto(url)
    
    def click(self, locator: str):
        self.page.locator(locator).click()
    
    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)
    
    def verify_element_is_disabled(self, locator):
        expect(locator).to_be_disabled()
    
    def verify_element_is_enabled(self, locator):
        expect(locator).to_be_enabled()

    def verify_element_is_visible(self, locator):
        expect(locator).to_be_visible()

    def verify_text(self, locator, text):
        expect(locator).to_have_text(text)
    
    
    
    