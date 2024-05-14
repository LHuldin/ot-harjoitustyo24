from database_connection import get_database_connection
from entities.user import User


class UserDBManager:

    def __init__(self, connection):
        self._connection = connection

    def add_user(self, user):  # username, password):
        # if len(username) < 4 or len(password) < 4:
        #    return False

        # if not self.user_exists(username):
        #    #connection = get_database_connection()
        #    cursor = self._connection.cursor()
        #    cursor.execute(
        #        "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        #    self._connection.commit()
        #    return True
        # return False

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def fetch_user(self, username):
        # connection = get_database_connection()
        print("Vielä täälläkin!!!!!!!!")
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        # cursor.fetchone()
        return User(row["id"], row["username"], row["password"]) if row else None

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    # def user_exists(self, username):
    #    #connection = get_database_connection()
    #    cursor = self._connection.cursor()
    #    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    #    return cursor.fetchone() is not None

    def delete_all(self):

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_db_manager = UserDBManager(get_database_connection())
