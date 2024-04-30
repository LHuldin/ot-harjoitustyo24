from database_connection import get_database_connection


class UserDBManager:

    def __init__(self, connection):
        self._connection = connection

    def add_user(self, username, password):
        if len(username) < 4 or len(password) < 4:
            return False

        if not self.user_exists(username):
            #connection = get_database_connection()
            cursor = self._connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self._connection.commit()
            return True
        return False


    def fetch_user(self, username):
        #connection = get_database_connection()
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()


    def user_exists(self, username):
        #connection = get_database_connection()
        cursor = self._connection.cursor()
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        return cursor.fetchone() is not None
    
    def delete_all(self):
        
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()

user_db_manager = UserDBManager(get_database_connection())