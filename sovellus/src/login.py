class Login:
    def __init__(self):
        self.username = None
        self.password = None
    
    
    def login(self):
        self.username = input("Käyttäjätunnus: ")
        self.password = input("Salasana: ")
        Login.read_file(self.username, self.password)

    def read_file(username, password):
        with open("users.txt", "r") as file:
            for line in file:
                u, p = line.strip().split(":")
                if u == username and p == password:
                    print("Kirjautuminen onnistui!")
                    return True
        print("Virheellinen käyttäjätunnus tai salasana.")
        return False
