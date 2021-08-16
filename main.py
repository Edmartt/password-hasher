"""Starts the application."""
import getpass

from passwords import Password

if __name__ == '__main__':

    password = getpass.getpass(
        prompt='Type your plaintext password (it won\'t be echoed): ',
        stream=100)

    hash_object = Password(password)
    hash_object.password = password

    print('Your hashed password: {}'.format(hash_object.password_hash))

    Password.store_password(hash_object.password_hash)
