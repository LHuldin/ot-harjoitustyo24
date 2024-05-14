from entities.user import User
from repositories.user_db_manager import user_db_manager


class UserService:

    def __init__(self, userdb=user_db_manager):
        self._userdb = userdb
        self._user = None

    def register_user(self, username, password):

        if len(username) < 4:
            raise InvalidCredentialsError(
                "Username should be at least 4 characters long")
        if len(password) < 4:
            raise InvalidCredentialsError(
                "Password should be at least 4 characters long")

        user = self._userdb.add_user(
            User(None, username, password))
        self._user = user

        return user

    def user_now(self):

        return self._user

    def login(self, username, password):
        print("Pääseekö edes tänne!!!")
        user = self._userdb.fetch_user(username)

        if not user or user.password != password:
            print("VOi helvetti")
            # raise InvalidCredentialsError

        self._user = user
        print("Täällä ollaan!!!")

        return user

    def logout(self):
        self._user = None


user_service = UserService()
