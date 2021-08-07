"""This module has one class for managing password hashing with passlib."""

from database.db_con import get_connection
from hashing.hashing import get_password_hashed


class Password:
    """This class helps to implement password hashing with passlib library."""

    def __init__(self, password):
        """
        Get the string to converts into a property of the class.

        :params: password: the string to become a property of the class.
        """
        self.password_hash = password

    @property
    def password(self):
        """If this property is read, an exception is raised."""
        raise AttributeError('This property can\'t be read')

    @password.setter
    def password(self, password):
        self.password_hash = get_password_hashed(password, 8)

    @staticmethod
    def store_password(password):
        """Store the hashed password in a MariaDB/MySQL database.

        :params: password: the string to store on the db server
        """
        connection, cursor = get_connection()
        query = 'INSERT INTO passwords(password) VALUES(%s)'

        try:
            cursor.execute(query, (password,))
            connection.commit()
            print('Password stored in database')
        except Exception as ex:
            raise ex

        finally:
            connection.close()
