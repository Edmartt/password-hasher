from .querygenerator import QueryGenerator


class PasswordStorage():

    def store_password(self, password, querygen: QueryGenerator):
        """Store the hashed password in a MariaDB/MySQL database.

        :params: password: the hashed string to store on the db server
        """
        query = 'INSERT INTO passwords(password) VALUES(%s)'
        querygen.select(query, (password,))
