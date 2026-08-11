"""
==========================================
Project Atlas Database Schema
------------------------------------------
Defines the structure of the NPFL Atlas
database.

Author: Adekeye Adeoye
==========================================
"""

CLUBS_TABLE = """
CREATE TABLE IF NOT EXISTS clubs (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    team_name TEXT NOT NULL UNIQUE,

    nickname TEXT,

    stadium TEXT,

    state TEXT,

    email TEXT,

    phone TEXT,

    website TEXT,

    tiktok TEXT,

    instagram TEXT,

    x TEXT,

    facebook TEXT,

    youtube TEXT,

    founded INTEGER,

    logo TEXT,

    data_status TEXT DEFAULT 'unverified',

    last_verified TIMESTAMP,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);
"""