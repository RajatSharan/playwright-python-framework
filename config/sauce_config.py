# config/sauce_config.py
import os
import json
from urllib.parse import quote


class SauceConfig:

    USERNAME:   str = os.getenv("SAUCE_USERNAME", "")
    ACCESS_KEY: str = os.getenv("SAUCE_ACCESS_KEY", "")
    REGION:     str = os.getenv("SAUCE_REGION", "eu-central-1")

    REGION_MAP = {
        "eu-central-1": "ondemand.eu-central-1.saucelabs.com",
        "us-west-1":    "ondemand.us-west-1.saucelabs.com",
        "us-east-4":    "ondemand.us-east-4.saucelabs.com",
    }

    @classmethod
    def get_connection_url(cls) -> str:
        """
        Build correct Playwright WebSocket URL for Sauce Labs.
        Playwright uses /playwright endpoint — NOT /wd/hub (that's Selenium).
        """
        host = cls.REGION_MAP.get(cls.REGION, "ondemand.eu-central-1.saucelabs.com")

        capabilities = {
            "browserName":    "chrome",
            "browserVersion": "latest",
            "platformName":   "Windows 11",
            "sauce:options": {
                "username":         cls.USERNAME,
                "accessKey":        cls.ACCESS_KEY,
                "name":             "Platnest Tests",
                "build":            os.getenv("GITHUB_RUN_NUMBER", "local-build"),
                "tunnelName":       os.getenv("SAUCE_TUNNEL_NAME", "platnest-tunnel"),
                "screenResolution": "1280x720",
            }
        }

        caps_encoded = quote(json.dumps(capabilities))

        # ✅ CORRECT: /playwright — NOT /wd/hub
        return (
            f"wss://{cls.USERNAME}:{cls.ACCESS_KEY}"
            f"@{host}:443/playwright"
            f"?capabilities={caps_encoded}"
        )

    @classmethod
    def validate(cls) -> bool:
        if not cls.USERNAME:
            raise ValueError("SAUCE_USERNAME is not set in .env")
        if not cls.ACCESS_KEY:
            raise ValueError("SAUCE_ACCESS_KEY is not set in .env")
        return True