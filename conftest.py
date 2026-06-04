import pytest
from utils.test_data import TestData

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport"            : {"width": 1280, "height": 720},
        "ignore_https_errors" : True,
    }

# This runs after EVERY test automatically
@pytest.fixture(autouse=True)
def close_after_test(page):
    yield                  # test runs here

    try:
        page.close()       # close page gracefully
    except Exception:
        pass  
    
@pytest.fixture
def user_data():
    return TestData.registration_user()