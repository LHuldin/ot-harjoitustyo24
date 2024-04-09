from login import Login
from register import Register

class UI:
    def __init__(self):
    
        self.login = Login()
        self.register = Register()

    def ui(self):

        while True:
            print("\n1. Kirjaudu sisään\n2. Rekisteröidy\n3. Lopeta")
            choice = input("Valitse toiminto (1-3): ")
            if choice == "1":
                self.login.login()
            elif choice == "2":
                self.register.register()
            elif choice == "3":
                print("Ohjelma lopetetaan.")
                break
            else:
                print("Virheellinen valinta. Yritä uudelleen.")