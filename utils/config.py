# utils/config.py
import os
from dotenv import load_dotenv

# Load .env file from project root
load_dotenv()

class Config:
    # --- WEB ---
    BASE_URL: str = os.getenv("BASE_URL", "http://platnest.test")

    # --- Credentials ---
    USERNAME: str = os.getenv("APP_USERNAME", "")
    PASSWORD: str = os.getenv("APP_PASSWORD", "")

    # --- Timeouts ---
    TIMEOUT: int = int(os.getenv("TIMEOUT", "30000"))

    # --- Environment ---
    ENV: str = os.getenv("ENV", "staging")

    # --- Sauce Labs (for Phase 3) ---
    SAUCE_USERNAME: str = os.getenv("SAUCE_USERNAME", "")
    SAUCE_ACCESS_KEY: str = os.getenv("SAUCE_ACCESS_KEY", "")

    @classmethod
    def validate(cls):
        """Call this in conftest.py to catch missing config early."""
        missing = []
        if not cls.BASE_URL:
            missing.append("BASE_URL")
        if not cls.USERNAME:
            missing.append("USERNAME")
        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {missing}\n"
                f"Copy .env.example to .env and fill in the values."
            )