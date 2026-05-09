import sqlite3

DATABASE_NAME = "database/rescue_sl.db"


def create_connection():

    connection = sqlite3.connect(
        DATABASE_NAME,
        check_same_thread=False
    )

    return connection


connection = create_connection()

cursor = connection.cursor()


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT,

        password TEXT,

        role TEXT,

        district TEXT,

        created_at TEXT
    )
"""
)


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        disaster_type TEXT,

        description TEXT,

        image_path TEXT,

        district TEXT,

        latitude REAL,

        longitude REAL,

        status TEXT,

        severity TEXT,

        verification_count INTEGER,

        ai_confidence INTEGER,

        created_at TEXT
    )
"""
)


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS verifications(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        report_id INTEGER,

        user_id INTEGER,

        verification_status TEXT,

        created_at TEXT
    )
"""
)


cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS volunteers(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        district TEXT,

        availability TEXT,

        contact_number TEXT,

        skills TEXT
    )
"""
)

connection.commit()