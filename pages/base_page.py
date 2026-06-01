from playwright.sync_api import Page

class Basepage:
    
    def __init__(self,page:Page):
        self.page=page
    
    def navigate(self,url:str):
        self.page.goto(url)
    
    def click(self, locator: str):
        self.page.locator(locator).click()
    
    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)
    
    
    
    