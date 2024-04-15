class Register:
    def __init__(self):
        self.username = None
        self.password = None
    def register(self):
        self.username = input("Valitse vähintään 4 merkkiä pitkä käyttäjätunnus: ")
        self.password = input("Valitse vähintään 4 merkkiä pitkä salasana: ")
        Register.write_file(self.username, self.password)

    def write_file(username, password):
        if len(username) < 4 or len(password) < 4:
            print("Liian lyhyt käyttäjätunnus tai salasana")
            return False
        else:
            with open("users.txt", "a") as file:
                file.write(f"{username}:{password}\n")
            print("Rekisteröityminen onnistui!")
            return True
