"""Starts the application."""
import getpass

from passwords import Password
from database.db_con import MariaDatabase
from database.data_layer.passwordstorage import PasswordStorage
from database.data_layer.querygenerator import QueryGenerator

if __name__ == '__main__':

    password = getpass.getpass(
        prompt='Type your plaintext password (it won\'t be echoed): ',
        stream=100)

    hash_object = Password(password)
    hash_object.password = password

    print('Your hashed password: {}'.format(hash_object.password_hash))
    storage = PasswordStorage()
    querygen = QueryGenerator(MariaDatabase())

    storage.store_password(password, querygen)
