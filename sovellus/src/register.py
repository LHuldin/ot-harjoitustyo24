class Register:
    def register(self):
        username = input("Valitse vähintään 4 merkkiä pitkä käyttäjätunnus: ")
        password = input("Valitse vähintään 4 merkkiä pitkä salasana: ")
        if len(username) or len(password) < 4:
            print("Liian lyhyt käyttäjätunnus tai salasana")
        else:
            with open("users.txt", "a") as file:
                file.write(f"{username}:{password}\n")
            print("Rekisteröityminen onnistui!")