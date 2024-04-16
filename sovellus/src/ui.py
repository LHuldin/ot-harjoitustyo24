from login import Login
from register import Register
from library_ui import LibraryUI


class UI:
    def __init__(self):

        self.login = Login()
        self.register = Register()
        self.library_ui = LibraryUI()

    def ui(self):

        while True:
            print("\n1. Kirjaudu sisään\n2. Rekisteröidy\n3. Lopeta")
            choice = input("Valitse toiminto (1-3): ")
            if choice == "1":
                self.login.login()
                self.library_ui.run()
            elif choice == "2":
                self.register.register()
            elif choice == "3":
                print("Ohjelma lopetetaan.")
                break
            else:
                print("Virheellinen valinta. Yritä uudelleen.")
