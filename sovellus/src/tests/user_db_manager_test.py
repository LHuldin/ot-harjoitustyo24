import unittest
from user_db_manager import *


class TestuUser_db_manager(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_username_or_password_too_short(self):
        test = add_user("afj", "345")
        self.assertEqual(str(test), "False")

    def test_username_and_password_length_ok(self):
        test = add_user("afjf", "3456")
        self.assertEqual(str(test), "True")
