"""
==========================================
Project Atlas Club Repository
------------------------------------------
Handles CRUD operations for NPFL clubs.

Author: Adekeye Adeoye
==========================================
"""

from database.database import Database
from utils.logger import get_logger


logger = get_logger()


class ClubRepository:
    """Handle database operations for clubs."""

    def __init__(self, database: Database):
        """
        Initialize the club repository.

        Args:
            database: Active Database instance.
        """

        self.database = database

    # ======================================
    # CREATE
    # ======================================

    def add_club(
        self,
        team_name,
        nickname=None,
        stadium=None,
        state=None,
        email=None,
        phone=None,
        website=None,
        tiktok=None,
        instagram=None,
        x=None,
        facebook=None,
        youtube=None,
        founded=None,
        logo=None,
    ):
        """Add a new club to the database."""

        if not self.database.connection:
            logger.error(
                "Cannot add club: database is not connected."
            )
            return None

        query = """
            INSERT INTO clubs (
                team_name,
                nickname,
                stadium,
                state,
                email,
                phone,
                website,
                tiktok,
                instagram,
                x,
                facebook,
                youtube,
                founded,
                logo
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        values = (
            team_name,
            nickname,
            stadium,
            state,
            email,
            phone,
            website,
            tiktok,
            instagram,
            x,
            facebook,
            youtube,
            founded,
            logo,
        )

        try:

            cursor = self.database.connection.cursor()

            cursor.execute(query, values)

            self.database.connection.commit()

            club_id = cursor.lastrowid

            logger.success(
                f"Club added successfully: {team_name} "
                f"(ID: {club_id})"
            )

            return club_id

        except Exception as error:

            self.database.connection.rollback()

            logger.error(
                f"Failed to add club '{team_name}': {error}"
            )

            return None

    # ======================================
    # READ — ONE CLUB
    # ======================================

    def get_club(self, team_name):
        """Retrieve a club by team name."""

        if not self.database.connection:
            logger.error(
                "Cannot retrieve club: database is not connected."
            )
            return None

        query = """
            SELECT *
            FROM clubs
            WHERE team_name = ?
        """

        cursor = self.database.connection.cursor()

        cursor.execute(query, (team_name,))

        row = cursor.fetchone()

        if row:

            columns = [
                column[0]
                for column in cursor.description
            ]

            return dict(zip(columns, row))

        logger.warning(
            f"Club not found: {team_name}"
        )

        return None

    # ======================================
    # READ — ALL CLUBS
    # ======================================

    def get_all_clubs(self):
        """Retrieve all clubs."""

        if not self.database.connection:
            logger.error(
                "Cannot retrieve clubs: database is not connected."
            )
            return []

        query = """
            SELECT *
            FROM clubs
            ORDER BY team_name ASC
        """

        cursor = self.database.connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()

        columns = [
            column[0]
            for column in cursor.description
        ]

        return [
            dict(zip(columns, row))
            for row in rows
        ]

    # ======================================
    # UPDATE
    # ======================================

    def update_club(self, team_name, **fields):
        """Update one or more fields for a club."""

        if not self.database.connection:
            logger.error(
                "Cannot update club: database is not connected."
            )
            return False

        if not fields:
            logger.warning(
                "No fields provided for update."
            )
            return False

        allowed_fields = {
            "nickname",
            "stadium",
            "state",
            "email",
            "phone",
            "website",
            "tiktok",
            "instagram",
            "x",
            "facebook",
            "youtube",
            "founded",
            "logo",
            "data_status",
            "last_verified",
        }

        invalid_fields = set(fields) - allowed_fields

        if invalid_fields:

            logger.error(
                f"Invalid update fields: {invalid_fields}"
            )

            return False

        set_clause = ", ".join(
            f"{field} = ?"
            for field in fields
        )

        query = f"""
            UPDATE clubs
            SET {set_clause},
                updated_at = CURRENT_TIMESTAMP
            WHERE team_name = ?
        """

        values = list(fields.values())
        values.append(team_name)

        try:

            cursor = self.database.connection.cursor()

            cursor.execute(query, values)

            self.database.connection.commit()

            if cursor.rowcount == 0:

                logger.warning(
                    f"No club updated: {team_name}"
                )

                return False

            logger.success(
                f"Club updated successfully: {team_name}"
            )

            return True

        except Exception as error:

            self.database.connection.rollback()

            logger.error(
                f"Failed to update '{team_name}': {error}"
            )

            return False

    # ======================================
    # DELETE
    # ======================================

    def delete_club(self, team_name):
        """Delete a club from the database."""

        if not self.database.connection:
            logger.error(
                "Cannot delete club: database is not connected."
            )
            return False

        query = """
            DELETE FROM clubs
            WHERE team_name = ?
        """

        try:

            cursor = self.database.connection.cursor()

            cursor.execute(
                query,
                (team_name,)
            )

            self.database.connection.commit()

            if cursor.rowcount == 0:

                logger.warning(
                    f"Club not found: {team_name}"
                )

                return False

            logger.success(
                f"Club deleted successfully: {team_name}"
            )

            return True

        except Exception as error:

            self.database.connection.rollback()

            logger.error(
                f"Failed to delete '{team_name}': {error}"
            )

            return False