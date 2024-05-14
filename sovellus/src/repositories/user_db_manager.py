from database_connection import get_database_connection
from entities.user import User


class UserDBManager:

    def __init__(self, connection):
        self._connection = connection

    def add_user(self, user):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def fetch_user(self, username):
        print("Vielä täälläkin!!!!!!!!")
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return User(row["id"], row["username"], row["password"]) if row else None

    def fetch_all(self):
        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def delete_all(self):

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_db_manager = UserDBManager(get_database_connection())
