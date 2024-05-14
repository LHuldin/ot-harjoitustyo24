from database_connection import get_database_connection
from entities.user import User


class UserDBManager:
    """Luokka joka vastaa käyttäjätietoon liittyvistä tietokanta operaatioista"""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args: 
            connection: tietokantayhteydestä vastaava connection olio
        """
        self._connection = connection

    def add_user(self, user):
        """Lisää tietokantaan käyttäjän käyttäjänimen ja salasanan"""
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def fetch_user(self, username):
        """Palauttaa yhden käyttäjä olion annetun käyttäjänimen perusteella.

        Args:
            username: haettavan käyttäjän käyttäjänimi

        Returns:
            Palauttaa User-olion mikäli käyttäjä löytyy, 
            jos käyttäjää ei löydy palauttaa None

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return User(row["id"], row["username"], row["password"]) if row else None

    def delete_all(self):
        """Poistaa kaiken käyttäjätiedon tietokannasta 
        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM users")
        self._connection.commit()


user_db_manager = UserDBManager(get_database_connection())
