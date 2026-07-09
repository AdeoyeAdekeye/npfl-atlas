"""
==========================================
Project Atlas Logger
------------------------------------------
Central logging configuration for the
application.

Author: Adekeye Adeoye
==========================================
"""

import sys
from loguru import logger

from config.settings import LOG_DIR, LOG_LEVEL

# Remove default logger
logger.remove()

# Console Logger
logger.add(
    sys.stdout,
    level=LOG_LEVEL,
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level:<8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan> | "
        "{message}"
    ),
)

# File Logger
logger.add(
    LOG_DIR / "atlas.log",
    level=LOG_LEVEL,
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level:<8} | "
        "{name}:{function}:{line} | "
        "{message}"
    ),
)


def get_logger():
    """Return configured logger."""
    return logger