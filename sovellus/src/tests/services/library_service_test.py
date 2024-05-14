import unittest
from services.library_service import library_service
from services.user_service import user_service
from repositories.library_db_manager import library_db_manager
from repositories.user_db_manager import user_db_manager


class TestLibraryService(unittest.TestCase):
    def setUp(self):
        library_db_manager.delete_all()
        user_db_manager.delete_all()
        user_service.register_user("aapo", "1234")
        self.user = user_service.login("aapo", "1234")

    def test_add_hardware_works(self):
        value = library_service.add_hardware("laptop", "t460", "Lenovo")
        self.assertEqual(value, True)

    def test_add_software_works(self):
        value = library_service.add_software(
            "Mario", "moduli", "nes", "nintendo")
        self.assertEqual(value, True)
