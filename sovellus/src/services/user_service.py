from entities.user import User
from repositories.user_db_manager import user_db_manager


class UserService:
    """Ohjelman käyttäjiin liittyvästä sovelluslogiikasta vastaava luokka"""

    def __init__(self, userdb=user_db_manager):
        self._userdb = userdb
        self._user = None

    def register_user(self, username, password):
        """Luo uuden käyttäjän

        Args:
            username: käyttäjän käyttäjänimi 
            password: käyttäjän salasana
        Returns:
            funtio palauttaa luodun User olion
        """

        if len(username) < 4:
            return False
        if len(password) < 4:
            return False

        user = self._userdb.add_user(
            User(None, username, password))
        self._user = user

        return user

    def user_now(self):
        """Palauttaa tällä hetkellä kirjautuneen käyttäjän User olion"""

        return self._user

    def login(self, username, password):
        """Hoitaa kirjautumisen tarkastamalla löytyykö käyttäjän tiedot pysyväis tallennuksesta"""
        user = self._userdb.fetch_user(username)

        if not user or user.password != password:
            return False

        self._user = user
        print("Täällä ollaan!!!")

        return user

    def logout(self):
        """Kirjaa käyttäjän ulos"""
        self._user = None


user_service = UserService()
