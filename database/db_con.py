"""Connection for MySQL/MariaDB server."""
from os import environ
import mysql.connector


class Database:

    host = environ.get("DB_HOST")
    user = environ.get("DB_USER")
    password = environ.get("DB_PASSWORD")
    database = environ.get("DB_NAME")

    def get_connection(self):
        """Connect to the db server.

        For a succesfull connection, you to set
        the environment variables DB_HOST, DB_USER,
        DB_PASSWORD and DB_NAME
        """
        connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
            )

        cursor = connection.cursor(dictionary=True)

        return connection, cursor
