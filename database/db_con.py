"""Connection for MySQL/MariaDB server."""
from os import environ
import mysql.connector


def get_connection():
    """Connect to the db server.

    For a succesfull connection, you to set
    the environment variables DB_HOST, DB_USER,
    DB_PASSWORD and DB_NAME
    """
    connection = mysql.connector.connect(
        host=environ.get("DB_HOST"),
        user=environ.get("DB_USER"),
        password=environ.get("DB_PASSWORD"),
        database=environ.get("DB_NAME")
        )
    cursor = connection.cursor(dictionary=True)

    return connection, cursor
