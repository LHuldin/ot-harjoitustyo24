import unittest
from register import Register


class TestRegister(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_username_or_password_too_short(self):
        test = Register.write_file("afj", "345")
        self.assertEqual(str(test), "False")

    def test_username_and_password_length_ok(self):
        test = Register.write_file("afjf", "3456")
        self.assertEqual(str(test), "True")
