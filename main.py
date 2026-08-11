"""
Project Atlas

Application Entry Point
"""

from config.settings import print_settings
from database.database import Database
from database.repository import ClubRepository
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
    """Application entry point."""

    logger.info("Starting Project Atlas")

    print_settings()

    db = Database()

    db.connect()

    db.create_tables()

    repository = ClubRepository(db)

    # ======================================
    # TEST CREATE
    # ======================================

    repository.add_club(
        team_name="Test Football Club",
        nickname="Testers",
        stadium="Test Stadium",
        state="Lagos",
        email="test@example.com",
        phone="+2348000000000",
        website="https://example.com",
        instagram="@testfc",
        x="@testfc",
        facebook="TestFC",
        tiktok="@testfc",
    )

    # ======================================
    # TEST READ
    # ======================================

    club = repository.get_club(
        "Test Football Club"
    )

    logger.info(
        f"Retrieved club: {club}"
    )

    # ======================================
    # TEST UPDATE
    # ======================================

    repository.update_club(
        "Test Football Club",
        nickname="Updated Testers",
        state="Ogun",
    )

    # ======================================
    # VERIFY UPDATE
    # ======================================

    updated_club = repository.get_club(
        "Test Football Club"
    )

    logger.info(
        f"Updated club: {updated_club}"
    )

    # ======================================
    # TEST ALL CLUBS
    # ======================================

    clubs = repository.get_all_clubs()

    logger.info(
        f"Total clubs: {len(clubs)}"
    )

    # ======================================
    # TEST DELETE
    # ======================================

    repository.delete_club(
        "Test Football Club"
    )

    # ======================================
    # VERIFY DELETE
    # ======================================

    deleted_club = repository.get_club(
        "Test Football Club"
    )

    logger.info(
        f"After deletion: {deleted_club}"
    )

    db.close()

    logger.success(
        "Project Atlas initialized successfully."
    )


if __name__ == "__main__":
    main()

