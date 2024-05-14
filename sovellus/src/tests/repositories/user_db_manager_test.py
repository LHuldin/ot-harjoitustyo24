import unittest
from entities.user import User
from repositories.user_db_manager import user_db_manager


class TestuUserDBManager(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        user_db_manager.delete_all()
        # self.user_wrong = User(None, "afj", "345")
        self.user_test = User(None, "afjf", "3456")

    # def test_username_or_password_too_short(self):
    #    test = user_db_manager.add_user(None, "afj", "345")
    #    self.assertEqual(str(test), "False")

    # def test_username_and_password_length_ok(self):
    #    test = user_db_manager.add_user(None, "afjf", "3456")
    #    self.assertEqual(str(test), "True")

    def test_add_user(self):
        user_input = user_db_manager.add_user(self.user_test)
        user_output = user_db_manager.fetch_user("afjf")
        self.assertEqual(user_output.username, self.user_test.username)
