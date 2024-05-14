import unittest
from services.user_service import user_service
from repositories.user_db_manager import user_db_manager


class TestUserService(unittest.TestCase):

    def setUp(self):
        user_db_manager.delete_all()
        self.username = "test"
        self.password = "Test1234"

    def test_register_user(self):
        test_user = user_service.register_user(self.username, self.password)
        self.assertEqual(test_user.username, self.username)
