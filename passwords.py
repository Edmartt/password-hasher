"""This module has one class for managing password hashing with passlib."""
from hashing.hashing import get_password_hashed


class Password:
    """This class helps to implement password hashing with passlib library."""

    def __init__(self, password):
        """
        Get the string to converts into a property of the class.

        :params: password: the string to become a property of the class.
        """
        self.password = password

    @property
    def password(self):
        """If this property is read, an exception is raised."""
        raise AttributeError('This property can\'t be read')

    @password.setter
    def password(self, password):
        '''Password setter.
        :params: password: String to be hashed
        '''
        self.password_hash = get_password_hashed(password, 8)
