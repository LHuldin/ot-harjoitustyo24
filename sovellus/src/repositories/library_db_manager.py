from database_connection import get_database_connection


class Library_db_manager:

    def __init__(self, connection):
        self._connection = connection

    def add_item(self, type, model, manufacturer):
        # connection = get_database_connection()
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO library (type, model, manufacturer) VALUES (?, ?, ?)",
                       (type, model, manufacturer))
        self._connection.commit()

    def add_hardware(self, type, model, manufacturer):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO hardware (type, model, manufacturer) VALUES (?, ?, ?)",
                       (type, model, manufacturer))
        self._connection.commit()

    def add_software(self, system, type, model, manufacturer):
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO software (system, type, model, manufacturer) VALUES (?, ?, ?, ?)",
                       (system, type, model, manufacturer))
        self._connection.commit()

    def fetch_items(self):
        # connection = get_database_connection()
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM library")
        return cursor.fetchall()

    def fetch_hardware(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM hardware")
        return cursor.fetchall()

    def fetch_software(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM software")
        return cursor.fetchall()

    def remove_item(self, item_id):
        # connection = get_database_connection()
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM library WHERE id = ?", (item_id))
        self._connection.commit()


library_db_manager = Library_db_manager(get_database_connection())
