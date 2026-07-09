"""
==========================================
Project Atlas
------------------------------------------
Description:
Central configuration file for Project Atlas.
All application settings, project paths,
environment variables and constants are
managed from this file.

Author:
Adekeye Adeoye

Created:
2026
==========================================
"""

# ======================================
# Imports
# ======================================

from pathlib import Path
from dotenv import load_dotenv
import os

# ======================================
# Load Environment Variables
# ======================================

load_dotenv()

# ======================================
# Project Information
# ======================================

PROJECT_NAME = "NPFL Atlas"
VERSION = "1.0.0"
AUTHOR = "Adekeye Adeoye"

# ======================================
# Project Root
# ======================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ======================================
# Directory Structure
# ======================================

# Main Directories
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"
DATABASE_DIR = PROJECT_ROOT / "database"
ASSETS_DIR = PROJECT_ROOT / "assets"
LOG_DIR = PROJECT_ROOT / "logs"
DOCS_DIR = PROJECT_ROOT / "docs"
TESTS_DIR = PROJECT_ROOT / "tests"

# Data Directories
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXPORTS_DIR = DATA_DIR / "exports"

# Raw Data Subdirectories
RAW_CLUBS_DIR = RAW_DATA_DIR / "clubs"
RAW_PLAYERS_DIR = RAW_DATA_DIR / "players"
RAW_FIXTURES_DIR = RAW_DATA_DIR / "fixtures"
RAW_SOCIAL_DIR = RAW_DATA_DIR / "social"
RAW_STADIUMS_DIR = RAW_DATA_DIR / "stadiums"

# Processed Data Subdirectories
PROCESSED_CLUBS_DIR = PROCESSED_DATA_DIR / "clubs"
PROCESSED_PLAYERS_DIR = PROCESSED_DATA_DIR / "players"
PROCESSED_FIXTURES_DIR = PROCESSED_DATA_DIR / "fixtures"
PROCESSED_SOCIAL_DIR = PROCESSED_DATA_DIR / "social"

# Export Directories
CSV_EXPORT_DIR = EXPORTS_DIR / "csv"
EXCEL_EXPORT_DIR = EXPORTS_DIR / "excel"
JSON_EXPORT_DIR = EXPORTS_DIR / "json"

# Asset Directories
LOGOS_DIR = ASSETS_DIR / "logos"
STADIUMS_DIR = ASSETS_DIR / "stadiums"
PLAYERS_DIR = ASSETS_DIR / "players"
COACHES_DIR = ASSETS_DIR / "coaches"
KITS_DIR = ASSETS_DIR / "kits"

# ======================================
# Database Settings
# ======================================

DATABASE_NAME = "atlas.db"
DATABASE_FILE = DATABASE_DIR / DATABASE_NAME

# ======================================
# Environment Variables
# ======================================

APP_ENV = os.getenv("APP_ENV", "development")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Future API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

RAPID_API_KEY = os.getenv("RAPID_API_KEY", "")

# ======================================
# Crawler Settings
# ======================================

DEFAULT_TIMEOUT = 30

MAX_RETRIES = 3

REQUEST_DELAY = 2

HEADLESS_BROWSER = True

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/138.0.0.0 Safari/537.36"
)

# ======================================
# Social Media Platforms
# ======================================

SOCIAL_PLATFORMS = [
    "Instagram",
    "Facebook",
    "X",
    "TikTok",
    "YouTube",
]

# ======================================
# Supported Export Formats
# ======================================

EXPORT_FORMATS = [
    "csv",
    "excel",
    "json",
]

# ======================================
# Required Project Directories
# ======================================

REQUIRED_DIRECTORIES = [

    # Main
    CONFIG_DIR,
    DATA_DIR,
    DATABASE_DIR,
    ASSETS_DIR,
    LOG_DIR,
    DOCS_DIR,
    TESTS_DIR,

    # Data
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    EXPORTS_DIR,

    # Raw
    RAW_CLUBS_DIR,
    RAW_PLAYERS_DIR,
    RAW_FIXTURES_DIR,
    RAW_SOCIAL_DIR,
    RAW_STADIUMS_DIR,

    # Processed
    PROCESSED_CLUBS_DIR,
    PROCESSED_PLAYERS_DIR,
    PROCESSED_FIXTURES_DIR,
    PROCESSED_SOCIAL_DIR,

    # Exports
    CSV_EXPORT_DIR,
    EXCEL_EXPORT_DIR,
    JSON_EXPORT_DIR,

    # Assets
    LOGOS_DIR,
    STADIUMS_DIR,
    PLAYERS_DIR,
    COACHES_DIR,
    KITS_DIR,
]

# ======================================
# Automatically Create Directories
# ======================================

for directory in REQUIRED_DIRECTORIES:
    directory.mkdir(parents=True, exist_ok=True)

# ======================================
# Helper Functions
# ======================================

def print_settings():
    """
    Display the current application configuration.
    Useful for testing and debugging.
    """

    print("=" * 70)
    print(PROJECT_NAME)
    print("=" * 70)

    print(f"Version            : {VERSION}")
    print(f"Author             : {AUTHOR}")
    print(f"Environment        : {APP_ENV}")
    print(f"Debug Mode         : {DEBUG}")
    print(f"Log Level          : {LOG_LEVEL}")
    print()

    print(f"Project Root       : {PROJECT_ROOT}")
    print(f"Database File      : {DATABASE_FILE}")
    print(f"Assets Directory   : {ASSETS_DIR}")
    print(f"Data Directory     : {DATA_DIR}")
    print(f"Logs Directory     : {LOG_DIR}")
    print()

    print("Crawler Settings")
    print("----------------------------")
    print(f"Timeout            : {DEFAULT_TIMEOUT} seconds")
    print(f"Retries            : {MAX_RETRIES}")
    print(f"Request Delay      : {REQUEST_DELAY} seconds")
    print(f"Headless Browser   : {HEADLESS_BROWSER}")

    print("=" * 70)