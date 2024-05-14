
from tkinter import ttk, Canvas, PhotoImage, NW, messagebox, constants
from services.user_service import user_service


class RegisterGui:
    """Käyttäjän rekisteröitymisestä vastaava näkymä.
    """

    def __init__(self, root, register, login):
        """Konstruktori, joka luo uuden rekisteröitymisnäkymän.

        Args:
            root:
                TKinter-elementti, jonka sisään näkymä alustetaan.
            login:
                Kutsuttava-arvo, jota kutsutaan kun käyttäjä luodaan ja siirretään kirjautumissivulle.
            register:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään kirjastonäkymään.
        """

        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._frame = None
        self._register = register
        self._login = login

        self._start()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _add_user(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            messagebox.showerror(
                "Error", "Sekä käyttäjänimi että salasana tarvitaan")
            return

        try:
            user_service.register_user(username, password)

            self._login()
            # self._register()
        except:
            messagebox.showerror("Error", "Lisäys tietokantaan ei onnistunut")

    def _start(self):

        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(
            master=self._frame, text="Rekisteröidy, anna vähintään 4 merkkiä pitkä käyttäjänimi ja salasana")

        username_label = ttk.Label(
            master=self._frame, text="Uusi käyttäjänimi")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Uusi salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        self._password_entry.grid(row=2, column=1)

        register_button = ttk.Button(
            master=self._frame, text="Rekisteröidy", command=self._add_user)  # (
        register_button.grid(row=3, column=0, columnspan=2)
