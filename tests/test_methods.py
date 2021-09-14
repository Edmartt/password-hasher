import unittest
from passwords import Password
from hashing.hashing import get_password_hashed


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.password_object = Password('password')
        self.pass1 = get_password_hashed('password', 8)
        self.pass2 = get_password_hashed('password', 8)

    def tearDown(self):
        pass

    def test_password_salts_random(self):
        self.assertTrue(self.pass1 != self.pass2)
        self.assertFalse(self.pass1 == self.pass2)

    def test_hash_is_pbkdf2(self):
        self.assertTrue(self.pass1.startswith('$pbkdf2'))

    def test_forbbiden_password_read(self):
        with self.assertRaises(AttributeError):
            self.password_object.password

    def test_password_setter(self):
        self.password_object.password = 'password1'
        self.assertTrue(self.password_object.password_hash is not None)
