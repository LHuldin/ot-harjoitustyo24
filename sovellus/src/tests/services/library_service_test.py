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

    def test_fetch_hardware(self):
        library_service.add_hardware("laptop", "t420", "Lenovo")
        library_service.add_hardware("laptop", "t450", "Lenovo")
        items = library_service.fetch_hardware()
        self.assertEqual(len(items), 2)

    def test_remove_hardware(self):
        library_service.add_hardware("laptop", "t420", "Lenovo")
        library_service.add_hardware("laptop", "t450", "Lenovo")
        library_service.remove_hardware("1")
        items = library_service.fetch_hardware()
        self.assertEqual(len(items), 1)

    def test_remove_software(self):
        library_service.add_software("Mario", "moduli", "nes", "nintendo")
        library_service.add_software("zelda2", "moduli", "nes", "nintendo")
        library_service.add_software("mgs1", "CD", "PS1", "Konami")
        library_service.remove_software("1")
        items = library_service.fetch_software()
        self.assertEqual(len(items), 2)
