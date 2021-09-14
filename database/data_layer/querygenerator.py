import logging
from database.iconnector import IDatabaseConnector


class QueryGenerator:

    def __init__(self, db_connector: IDatabaseConnector) -> None:
        self.db_connector = db_connector

    def insert(self, query, *args) -> None:
        connection, cursor = self.db_connector.get_connection()
        try:
            cursor.execute(query, (*args))
            connection.commit()
        except connection.ProgrammingError as ex:
            logging.exception(ex)
        finally:
            connection.close()

    def create_table(self, query: str) -> None:
        connection, cursor = self.db_connector.get_connection()
        try:
            cursor.execute(query)
            connection.commit()
        except connection.ProgrammingError as ex:
            logging.exception(ex)
        finally:
            connection.close()
