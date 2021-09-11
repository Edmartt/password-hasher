import logging
from database.iconnector import IDatabaseConnector


class QueryGenerator:

    def __init__(self, db_connector: IDatabaseConnector):
        self.db_connector = db_connector

    def select(self, query, *args, all=False):
        connection, cursor = self.db_connector.get_connection()
        try:
            cursor.execute(query, (*args))
            connection.commit()
        except connection.ProgrammmingError as ex:
            logging.exception(ex)

        finally:
            connection.close()
