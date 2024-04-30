import unittest
from repositories.user_db_manager import user_db_manager



class TestuUserDBManager(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        user_db_manager.delete_all()

    def test_username_or_password_too_short(self):
        test = user_db_manager.add_user("afj", "345")
        self.assertEqual(str(test), "False")

    def test_username_and_password_length_ok(self):
        test = user_db_manager.add_user("afjf", "3456")
        self.assertEqual(str(test), "True")
