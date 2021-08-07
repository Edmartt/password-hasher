"""
Make use of the passlib library method called hash.

Helps to generate hashed passwords.
"""

from passlib.hash import pbkdf2_sha256


def get_password_hashed(password, salt_size):
    """
    Gets a string an converts it to hash pbkdf2.

    :params: password: string
    :params: salt_size: int
    """
    hashed_password = pbkdf2_sha256.using(salt_size).hash(password)
    return hashed_password
