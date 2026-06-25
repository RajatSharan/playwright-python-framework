from playwright.sync_api import Page, expect
from utils.logger import get_logger


class BasePage:
    """
    Base class for all Page Objects.
    Provides common actions: navigate, click, fill, verify.
    All page classes should inherit from this.
    """

    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to: {url}")
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")

    def click(self, locator: str):
        self.logger.debug(f"Clicking: {locator}")
        self.page.locator(locator).click()

    def fill(self, locator: str, text: str):
        self.logger.debug(f"Filling '{locator}' with value (masked)")
        self.page.locator(locator).fill(text)

    def get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()

    def is_visible(self, locator: str) -> bool:
        return self.page.locator(locator).is_visible()

    def verify_element_is_visible(self, locator):
        expect(self.page.locator(locator) if isinstance(locator, str) else locator).to_be_visible()

    def verify_element_is_enabled(self, locator):
        expect(self.page.locator(locator) if isinstance(locator, str) else locator).to_be_enabled()

    def verify_element_is_disabled(self, locator):
        expect(self.page.locator(locator) if isinstance(locator, str) else locator).to_be_disabled()

    def verify_text(self, locator, text: str, timeout: int = None):
        if isinstance(locator, str):
            locator = self.page.locator(locator)
        kwargs = {"timeout": timeout} if timeout else {}
        self.logger.debug(f"Verifying text: '{text}'")
        expect(locator).to_have_text(text, **kwargs)

    def verify_url_contains(self, partial_url: str):
        expect(self.page).to_have_url(f".*{partial_url}.*")

    def check(self, locator: str):
        self.page.locator(locator).check()

    def take_screenshot(self, name: str = "screenshot") -> bytes:
        self.logger.info(f"Taking screenshot: {name}")
        return self.page.screenshot(full_page=True)