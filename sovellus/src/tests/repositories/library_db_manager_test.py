import unittest
from entities.hardware import Hardware
from entities.software import Software
from repositories.library_db_manager import library_db_manager


class TestLibrary_db_Manager(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        library_db_manager.delete_all()
        self.sw_test = Software("Mario", "Moduli", "NES", "Nintendo", "10")
        self.hw_test = Hardware("Laptop", "T490", "Lenovo", "10")

    # def test_add_software(self):
    #    sw_input = library_db_manager.add_software(self.sw_test)
    #    sw_list = library_db_manager.fetch_software(self.sw_test.user_id)
    #    for i in sw_list:
    #        test =
    #        if i == self.sw_test:
    #            sw_output = i
    #    self.assertEqual(sw_output.name, self.sw_test.name)

    # def test_add_hardware(self):
    #    user_input = user_db_manager.add_user(self.user_test)
    #    user_output = user_db_manager.fetch_user("afjf")
    #    self.assertEqual(user_output.username, self.user_test.username)
