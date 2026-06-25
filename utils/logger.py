# utils/logger.py
import logging
import os
from datetime import datetime

# Create logs/ directory if it doesn't exist
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file named by date — one file per day
LOG_FILE = os.path.join(LOG_DIR, f"test_run_{datetime.now().strftime('%Y-%m-%d')}.log")


def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger configured to write to both console and a daily log file.
    Usage: logger = get_logger(__name__)
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  # already configured, avoid duplicate handlers

    logger.setLevel(logging.DEBUG)

    # Console handler — INFO level (don't flood terminal with DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s: %(message)s",
        datefmt="%H:%M:%S"
    ))

    # File handler — DEBUG level (full detail in log file)
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(
        "%(asctime)s [%(levelname)-8s] %(name)s:%(lineno)d — %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    ))

    logger.addHandler(console)
    logger.addHandler(file_handler)

    return logger