# conftest.py
import pytest
import allure
import os
from playwright.sync_api import sync_playwright
from utils.config import Config
from utils.test_data import TestData
from utils.logger import get_logger
from config.sauce_config import SauceConfig

logger = get_logger(__name__)


# ─── VALIDATE CONFIGURATION EARLY ────────────────────────────────────────
def pytest_configure(config):
    """Runs before test collection - validate config early."""
    try:
        Config.validate()
        logger.info("✅ Configuration validated successfully")
    except EnvironmentError as e:
        logger.error(f"❌ Configuration error: {e}")
        raise


# ─── BROWSER FIXTURE: LOCAL vs SAUCE LABS ───────────────────────────────
@pytest.fixture(scope="session")
def browser():
    """
    Provides browser instance based on environment:
    - Local: Uses installed Chromium (headless)
    - Sauce Labs: Connects via WebSocket to cloud browser
    """
    use_sauce_labs = os.getenv("USE_SAUCE_LABS", "false").lower() == "true"
    
    logger.info(f"\n{'='*70}")
    logger.info(f"EXECUTION MODE: {'SAUCE LABS CLOUD ☁️' if use_sauce_labs else 'LOCAL BROWSER 🖥️'}")
    logger.info(f"{'='*70}\n")
    
    if use_sauce_labs:
        return _get_sauce_labs_browser()
    else:
        return _get_local_browser()


def _get_local_browser():
    """Launch local Chromium browser."""
    logger.info("🖥️  Launching local Chromium browser...")
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    logger.info("✅ Local browser launched successfully")
    return browser


def _get_sauce_labs_browser():
    """Connect to Sauce Labs cloud browser via WebSocket."""
    try:
        SauceConfig.validate()  # Check credentials exist
    except ValueError as e:
        logger.error(f"❌ {e}")
        raise
    
    sauce_url = SauceConfig.get_connection_url()
    logger.info(f"🌐 Connecting to Sauce Labs: {sauce_url.split('@')[0]}@***")
    
    playwright = sync_playwright().start()
    
    try:
        browser = playwright.chromium.connect(sauce_url)
        logger.info("✅ Connected to Sauce Labs browser successfully!")
        return browser
    except Exception as e:
        logger.error(f"❌ Failed to connect to Sauce Labs: {e}")
        raise


# ─── PAGE FIXTURE: Creates fresh page for each test ──────────────────────
@pytest.fixture
def page(browser):
    """Create a new page (tab) for each test."""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True,
    )
    page = context.new_page()
    page.set_default_timeout(int(Config.TIMEOUT))
    
    logger.info(f"📄 New page created")
    yield page
    
    context.close()
    logger.info(f"📄 Page closed and cleaned up")


# ─── BASE URL ────────────────────────────────────────────────────────────
@pytest.fixture(scope="session")
def base_url():
    """Provide base URL from config."""
    return Config.BASE_URL


# ─── TEST DATA ───────────────────────────────────────────────────────────
@pytest.fixture
def user_data():
    """Generate fresh test data for each test."""
    data = TestData.registration_user()
    logger.debug(f"Generated user: {data.get('email', 'N/A')}")
    return data


# ─── SCREENSHOT ON FAILURE ──────────────────────────────────────────────
@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(page, request):
    """Auto-capture screenshot on test failure."""
    yield  # Test runs here
    
    # Check if test failed
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        try:
            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                screenshot_bytes,
                name=f"FAILURE_{request.node.name}.png",
                attachment_type=allure.attachment_type.PNG,
            )
            logger.error(f"❌ Test failed: {request.node.name} (screenshot attached)")
        except Exception as e:
            logger.warning(f"⚠️  Could not capture screenshot: {e}")


# ─── PYTEST HOOK: Mark test outcome ─────────────────────────────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Store test result so fixture above can detect failures."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ─── TEST LOGGING ────────────────────────────────────────────────────────
@pytest.fixture(autouse=True)
def log_test_lifecycle(request):
    """Log test start and end."""
    logger.info(f"\n▶  START: {request.node.name}")
    yield
    logger.info(f"■  END:   {request.node.name}\n")


# ─── ALLURE ENVIRONMENT INFO ────────────────────────────────────────────
@pytest.fixture(scope="session", autouse=True)
def add_environment_info():
    """Add environment info to Allure report."""
    use_sauce_labs = os.getenv("USE_SAUCE_LABS", "false").lower() == "true"
    
    allure.environment(
        execution_type="Sauce Labs Cloud ☁️" if use_sauce_labs else "Local Browser 🖥️",
        base_url=Config.BASE_URL,
        environment=Config.ENV,
        sauce_region=SauceConfig.REGION if use_sauce_labs else "N/A",
    )