"""Starts the application."""

from passwords import Password

if __name__ == '__main__':

    password = input("Type your plain password: ")

    hash_function = Password(password)
    hash_function.password = password

    print(hash_function.password_hash)

    Password.store_password(hash_function.password_hash)
