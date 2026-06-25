# config/sauce_config.py
"""
Sauce Labs Cloud Configuration
Handles connection to Sauce Labs cloud browsers for Playwright
"""

import os


class SauceConfig:
    """
    Sauce Labs cloud execution configuration.
    Credentials loaded from environment variables (never hardcoded).
    """

    # Sauce Labs credentials
    USERNAME: str = os.getenv("SAUCE_USERNAME", "")
    ACCESS_KEY: str = os.getenv("SAUCE_ACCESS_KEY", "")
    
    # Region (us-west-1 or eu-central-1)
    REGION: str = os.getenv("SAUCE_REGION", "us-west-1")
    
    # Data center URL
    DATA_CENTER: str = f"ondemand.{REGION}.saucelabs.com"

    @classmethod
    def get_connection_url(cls) -> str:
        """
        Get Sauce Labs WebSocket connection URL for Playwright.
        
        Format: wss://username:accesskey@ondemand.REGION.saucelabs.com/wd/hub
        
        Returns:
            Connection URL or empty string if credentials missing
        """
        if not cls.USERNAME or not cls.ACCESS_KEY:
            return ""
        
        return (
            f"wss://{cls.USERNAME}:{cls.ACCESS_KEY}"
            f"@{cls.DATA_CENTER}/wd/hub"
        )

    # Browser capability profiles for different browsers
    BROWSER_CAPABILITIES = {
        "chrome": {
            "browserName": "chrome",
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "sauce:options": {
                "build": os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "name": "Playwright Python Framework - Chrome",
                "screenResolution": "1920x1080",
            }
        },
        "firefox": {
            "browserName": "firefox",
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "sauce:options": {
                "build": os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "name": "Playwright Python Framework - Firefox",
                "screenResolution": "1920x1080",
            }
        },
        "edge": {
            "browserName": "MicrosoftEdge",
            "browserVersion": "latest",
            "platformName": "Windows 11",
            "sauce:options": {
                "build": os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "name": "Playwright Python Framework - Edge",
                "screenResolution": "1920x1080",
            }
        },
        "safari": {
            "browserName": "safari",
            "browserVersion": "latest",
            "platformName": "macOS 14",
            "sauce:options": {
                "build": os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "name": "Playwright Python Framework - Safari",
                "screenResolution": "1920x1080",
            }
        },
    }

    @classmethod
    def validate(cls) -> bool:
        """
        Validate Sauce Labs configuration.
        
        Returns:
            True if valid, raises ValueError otherwise
        """
        if not cls.USERNAME or not cls.ACCESS_KEY:
            raise ValueError(
                "Sauce Labs credentials not configured.\n"
                "Please set the following environment variables:\n"
                "  SAUCE_USERNAME - Your Sauce Labs username\n"
                "  SAUCE_ACCESS_KEY - Your Sauce Labs access key\n"
                "  SAUCE_REGION - Optional (default: us-west-1)\n"
                "\n"
                "Get credentials from: https://app.saucelabs.com/user-settings/api-keys"
            )
        return True

    @classmethod
    def get_capability(cls, browser: str) -> dict:
        """
        Get capability profile for a specific browser.
        
        Args:
            browser: Browser name (chrome, firefox, edge, safari)
            
        Returns:
            Browser capability dictionary
            
        Raises:
            KeyError if browser not supported
        """
        if browser not in cls.BROWSER_CAPABILITIES:
            raise KeyError(
                f"Unsupported browser: {browser}\n"
                f"Available: {', '.join(cls.BROWSER_CAPABILITIES.keys())}"
            )
        
        return cls.BROWSER_CAPABILITIES[browser]
