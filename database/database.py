"""
==========================================
Project Atlas Database
------------------------------------------
Handles all database connections.

Author: Adekeye Adeoye
==========================================
"""

import sqlite3

from config.settings import DATABASE_FILE
from utils.logger import get_logger

logger = get_logger()


class Database:
    """SQLite database manager."""

    def __init__(self):
        self.connection = None

    def connect(self):
        """Connect to SQLite database."""

        try:
            self.connection = sqlite3.connect(DATABASE_FILE)
            logger.success("Connected to SQLite database.")

        except sqlite3.Error as error:
            logger.error(f"Database connection failed: {error}")

    def close(self):
        """Close database connection."""

        if self.connection:
            self.connection.close()
            logger.info("Database connection closed.")
    def create_tables(self):
        """Create database tables."""

        cursor = self.connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS clubs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            team_name TEXT UNIQUE NOT NULL,

            nickname TEXT,

            stadium TEXT,

            state TEXT,

            email TEXT,

            phone TEXT,

            website TEXT,

            facebook TEXT,

            instagram TEXT,

            x TEXT,

            tiktok TEXT,

            youtube TEXT,

            founded INTEGER,

            logo TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        self.connection.commit()

        logger.success("Database tables created.")