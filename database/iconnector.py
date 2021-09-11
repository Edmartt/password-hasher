from abc import ABC, abstractmethod
import mariadb


class IDatabaseConnector(ABC):

    @abstractmethod
    def get_connection(self) -> mariadb.connection:
        pass
