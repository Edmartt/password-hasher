"""Connection for MySQL/MariaDB server."""
import logging
from os import environ
import mariadb
from .iconnector import IDatabaseConnector


class MariaDatabase(IDatabaseConnector):

    def __init__(self):
        self.host = environ.get("DB_HOST")
        self.user = environ.get("DB_USER")
        self.password = environ.get("DB_PASSWORD")
        self.database = environ.get("DB_NAME")

    def get_connection(self):
        """Connect to the db server.

        For a succesfull connection, you need to set
        the environment variables DB_HOST, DB_USER,
        DB_PASSWORD and DB_NAME
        """
        try:
            connection = mariadb.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                    )

            cursor = connection.cursor(dictionary=True)
            return connection, cursor

        except mariadb.ProgrammingError as ex:
            logging.exception(ex)
