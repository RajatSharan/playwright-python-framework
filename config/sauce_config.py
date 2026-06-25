# config/sauce_config.py
import os


class SauceConfig:
    """
    Sauce Labs cloud execution configuration.
    Credentials loaded from environment variables (never hardcoded).
    """

    USERNAME: str = os.getenv("SAUCE_USERNAME", "")
    ACCESS_KEY: str = os.getenv("SAUCE_ACCESS_KEY", "")

    # Sauce Labs remote WebDriver URL
    SAUCE_URL: str = (
        f"https://{USERNAME}:{ACCESS_KEY}"
        f"@ondemand.us-west-1.saucelabs.com:443/wd/hub"
    ) if USERNAME and ACCESS_KEY else ""

    # Browser capability profiles
    BROWSERS = {
        "chrome": {
            "browserName": "chrome",
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "sauce:options": {
                "build": os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "name": "Playwright Python Framework",
                "screenResolution": "1920x1080",
            }
        },
        "firefox": {
            "browserName": "firefox",
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "sauce:options": {
                "build": os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "name": "Playwright Python Framework",
            }
        },
        "edge": {
            "browserName": "MicrosoftEdge",
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "sauce:options": {
                "build": os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "name": "Playwright Python Framework",
            }
        },
    }   