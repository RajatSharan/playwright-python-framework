# conftest.py
import pytest
import allure
import os
import threading
from utils.config import Config
from utils.test_data import TestData
from utils.logger import get_logger
from config.sauce_config import SauceConfig

logger = get_logger(__name__)


def pytest_configure(config):
    try:
        Config.validate()
        logger.info("✅ Configuration validated successfully")
    except EnvironmentError as e:
        logger.error(f"❌ Configuration error: {e}")
        raise


@pytest.fixture(scope="session")
def browser():
    use_sauce_labs = os.getenv("USE_SAUCE_LABS", "false").lower() == "true"

    logger.info(f"\n{'='*70}")
    logger.info(f"EXECUTION MODE: {'SAUCE LABS CLOUD ☁️' if use_sauce_labs else 'LOCAL BROWSER 🖥️'}")
    logger.info(f"{'='*70}\n")

    if use_sauce_labs:
        browser_instance = _connect_sauce_labs_in_thread()
    else:
        browser_instance = _launch_local_browser_in_thread()

    yield browser_instance

    try:
        browser_instance.close()
        logger.info("✅ Browser closed")
    except Exception:
        pass


def _launch_local_browser_in_thread():
    result = {}
    error = {}

    def run():
        try:
            from playwright.sync_api import sync_playwright
            pw = sync_playwright().start()
            result["playwright"] = pw
            result["browser"] = pw.chromium.launch(headless=True)
            logger.info("✅ Local browser launched successfully")
        except Exception as e:
            error["error"] = e

    t = threading.Thread(target=run)
    t.start()
    t.join()

    if "error" in error:
        raise error["error"]
    return result["browser"]


def _connect_sauce_labs_in_thread():
    try:
        SauceConfig.validate()
    except ValueError as e:
        logger.error(f"❌ {e}")
        raise

    sauce_url = SauceConfig.get_connection_url()
    logger.info("🌐 Connecting to Sauce Labs...")

    result = {}
    error = {}

    def run():
        try:
            from playwright.sync_api import sync_playwright
            pw = sync_playwright().start()
            result["playwright"] = pw
            result["browser"] = pw.chromium.connect(
                sauce_url,
                timeout=120000
            )
            logger.info("✅ Connected to Sauce Labs successfully!")
        except Exception as e:
            error["error"] = e

    t = threading.Thread(target=run)
    t.start()
    t.join(timeout=130)

    if t.is_alive():
        raise TimeoutError("Sauce Labs connection timed out")

    if "error" in error:
        logger.error(f"❌ Failed to connect: {error['error']}")
        raise error["error"]

    return result["browser"]


@pytest.fixture
def page(browser):
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        ignore_https_errors=True,
    )
    page = context.new_page()
    page.set_default_timeout(int(Config.TIMEOUT))
    logger.info("📄 New page created")
    yield page
    context.close()
    logger.info("📄 Page closed and cleaned up")


@pytest.fixture(scope="session")
def base_url():
    return Config.BASE_URL


@pytest.fixture
def user_data():
    data = TestData.registration_user()
    logger.debug(f"Generated user: {data.get('email', 'N/A')}")
    return data


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(page, request):
    yield
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


@pytest.fixture(autouse=True)
def log_test_lifecycle(request):
    logger.info(f"\n▶  START: {request.node.name}")
    yield
    logger.info(f"■  END:   {request.node.name}\n")


@pytest.fixture(scope="session", autouse=True)
def add_environment_info():
    try:
        os.makedirs("allure-results", exist_ok=True)
        use_sauce_labs = os.getenv("USE_SAUCE_LABS", "false").lower() == "true"
        execution_type = "Sauce Labs Cloud ☁️" if use_sauce_labs else "Local Browser 🖥️"
        sauce_region = SauceConfig.REGION if use_sauce_labs else "N/A"

        with open("allure-results/environment.properties", "w", encoding="utf-8") as f:
            f.write(f"Environment={Config.ENV}\n")
            f.write(f"Base URL={Config.BASE_URL}\n")
            f.write(f"Execution Type={execution_type}\n")
            f.write(f"Sauce Region={sauce_region}\n")

        logger.info("✅ Allure environment information added successfully")
    except Exception as e:
        logger.warning(f"⚠️ Unable to create Allure environment details: {e}")