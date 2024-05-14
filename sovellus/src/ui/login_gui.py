from tkinter import ttk, constants
from services.user_service import user_service


class LoginGui:

    def __init__(self, root, login, register, outlogger):

        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._frame = None
        self._register = register
        self._loggedin = login
        self._outlogger = outlogger

        self._start()

    def _login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            user_service.login(username, password)
            print("Tänne päästy1111")
            self._loggedin()
            print("Tänne päästy2222")
        except:
            print("VIRHE PERKELE")
            self._outlogger()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _start(self):
        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(master=self._frame, text="Kirjaudu")

        username_label = ttk.Label(master=self._frame, text="Käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._login
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Rekisteröi uusi käyttäjä",
            command=self._register
        )

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1)

        login_button.grid(row=3, column=0, columnspan=2)

        register_button.grid(row=4, column=0, columnspan=2)

        self._frame.grid_columnconfigure(1, weight=1)
