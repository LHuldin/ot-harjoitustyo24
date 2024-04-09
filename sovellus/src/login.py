class Login:
    
    
    def login(self):
        username = input("Käyttäjätunnus: ")
        password = input("Salasana: ")
        with open("users.txt", "r") as file:
            for line in file:
                u, p = line.strip().split(":")
                if u == username and p == password:
                    print("Kirjautuminen onnistui!")
                    return True
        print("Virheellinen käyttäjätunnus tai salasana.")
        return False
