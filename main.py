"""
Project Atlas

Application Entry Point
"""

from config.settings import print_settings
from utils.logger import get_logger

logger = get_logger()


def test_logger():
    """Test all logger levels."""

    logger.debug("Debug message")
    logger.info("Information message")
    logger.warning("Warning message")
    logger.error("Error message")
    logger.success("Everything completed successfully")


def main():
    """Application entry point."""

    logger.info("Starting Project Atlas")

    print_settings()

    test_logger()

    logger.success("Configuration loaded successfully")


if __name__ == "__main__":
    main()

"""
Project Atlas

Application Entry Point
"""

from config.settings import print_settings
from database.database import Database
from utils.logger import get_logger

logger = get_logger()


def main():

    logger.info("Starting Project Atlas")

    print_settings()

    db = Database()

    db.connect()

    db.create_tables()

    db.close()

    logger.success("Project Atlas initialized successfully")


if __name__ == "__main__":
    main()

