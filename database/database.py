"""
==========================================
Project Atlas Database
------------------------------------------
Handles all database connections.

Author: Adekeye Adeoye
==========================================
"""

import sqlite3
from database.schema import CLUBS_TABLE
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
        """Create all database tables."""

        if not self.connection:
            logger.error(
            "Cannot create tables: database is not connected."
            )
            return

        try:
            cursor = self.connection.cursor()

            cursor.execute(CLUBS_TABLE)

            self.connection.commit()

            logger.success("Database tables created.")

        except sqlite3.Error as error:

            self.connection.rollback()

            logger.error(
            f"Failed to create database tables: {error}"
            )
    def get_tables(self):
        """Return all tables in the database."""

        if not self.connection:
            logger.error(
            "Cannot inspect database: not connected."
            )
            return []

        cursor = self.connection.cursor()

        cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
        """)

        tables = cursor.fetchall()

        return [table[0] for table in tables]