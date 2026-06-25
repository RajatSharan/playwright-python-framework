# conftest.py
import pytest
import allure
import os
from utils.config import Config
from utils.test_data import TestData
from utils.logger import get_logger

logger = get_logger(__name__)


# ─── Browser context: viewport + ignore HTTPS errors ──────────────────────────

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Global browser context settings applied to every test."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
    }


# ─── Base URL: read from .env via Config ──────────────────────────────────────

@pytest.fixture(scope="session")
def base_url():
    """Provide base URL from environment config — never hardcode URLs in tests."""
    return Config.BASE_URL


# ─── Test data fixture ────────────────────────────────────────────────────────

@pytest.fixture
def user_data():
    """Generate fresh user registration data for each test."""
    data = TestData.registration_user()
    logger.debug(f"Generated user_data: email={data.get('email', 'N/A')}")
    return data


# ─── Screenshot + trace attachment on failure ────────────────────────────────

@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(page, request):
    """
    Automatically attach screenshot to Allure report on test failure.
    This runs after EVERY test. On failure: screenshot → attach → log.
    On pass: nothing extra happens.
    """
    yield  # test runs here

    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        try:
            screenshot_bytes = page.screenshot(full_page=True)
            allure.attach(
                screenshot_bytes,
                name=f"FAILURE - {request.node.name}",
                attachment_type=allure.attachment_type.PNG,
            )
            logger.error(f"Test FAILED: {request.node.name} — screenshot attached to Allure")
        except Exception as e:
            logger.warning(f"Could not capture screenshot: {e}")


# ─── Hook: mark test outcome so fixture above can read it ────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook that runs after each test phase (setup/call/teardown).
    We use it to store the test result on the item so our fixture above
    can check if the test passed or failed.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ─── Logging: log test start/end ─────────────────────────────────────────────

@pytest.fixture(autouse=True)
def log_test_lifecycle(request):
    """Log every test start and end for debugging in CI."""
    logger.info(f"▶ START: {request.node.nodeid}")
    yield
    logger.info(f"■ END:   {request.node.nodeid}")