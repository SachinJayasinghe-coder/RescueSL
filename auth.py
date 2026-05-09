from database import connection
from database import cursor

import datetime


def register_user(
    name,
    email,
    password,
    district
):

    cursor.execute(
        """
        INSERT INTO users(

            name,
            email,
            password,
            role,
            district,
            created_at

        )

        VALUES(?,?,?,?,?,?)
        """,

        (
            name,
            email,
            password,
            "citizen",
            district,
            str(datetime.datetime.now())
        )
    )

    connection.commit()


def login_user(
    email,
    password
):

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE email=? AND password=?
        """,

        (
            email,
            password
        )
    )

    user = cursor.fetchone()

    return user