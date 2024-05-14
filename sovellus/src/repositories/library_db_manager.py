from database_connection import get_database_connection
from entities.hardware import Hardware
from entities.software import Software


class Library_db_manager:

    def __init__(self, connection):
        self._connection = connection

    def add_hardware(self, hardware):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO hardware (type, model, manufacturer, user_id) VALUES (?, ?, ?, ?)",
                       (hardware.type, hardware.model, hardware.manufacturer, hardware.user_id))
        self._connection.commit()
        return hardware

    def add_software(self, software):
        print("Lisää testailua")
        cursor = self._connection.cursor()
        print("näkyykö tämä")
        print(software.name)
        print(software.user_id)
        cursor.execute("INSERT INTO software (name, mediatype, model, manufacturer, user_id) VALUES (?, ?, ?, ?, ?)",
                       (software.name, software.mediatype, software.model, software.manufacturer, software.user_id))
        self._connection.commit()
        return software

    def fetch_hardware(self, id):
        print(id)
        print("hardis haku")
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM hardware WHERE user_id = ?", (str(id),))
        return cursor.fetchall()

    def fetch_software(self, id):
        print("softa haku")
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM software WHERE user_id = ?", (str(id),))
        return cursor.fetchall()

    def remove_hw(self, item_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM hardware WHERE id = ?", (item_id))
        self._connection.commit()

    def remove_sw(self, item_id):
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM software WHERE id = ?", (item_id))
        self._connection.commit()

    def delete_all(self):

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM software")
        self._connection.commit()

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM hardware")
        self._connection.commit()


library_db_manager = Library_db_manager(get_database_connection())
