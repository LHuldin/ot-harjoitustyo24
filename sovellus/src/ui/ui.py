from ui.login_gui import LoginGui
from ui.register_gui import RegisterGui
from ui.library_gui import LibraryGui


class UI:
    """Koko sovelluksen käyttöliittymä elementeistä vastaava luokka"""

    def __init__(self, root):
        """Konstruktori, joka luo uuden käyttöliittymästä vastaavan luokan.

        Args:
            root:
                TKinter-elementti, jonka päällä sovelluksen käyttöliittymä toimii.
        """

        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän."""
        self._root.minsize(500, 500)
        self._login()

    def _destroy_view(self):
        """Sammuttaa näkymä elementin."""
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _login(self):
        """Avaa kirjautumisen mahdollistavan näkymän."""
        self._destroy_view()
        self._current_view = LoginGui(
            self._root, self._library, self._register, self._login)
        self._current_view.pack()

    def _register(self):
        """Avaa käyttäjän rekisteröinnin mahdollistavan näkymän."""
        self._destroy_view()
        self._current_view = RegisterGui(
            self._root, self._library, self._login)
        self._current_view.pack()

    def _library(self):
        """Avaa kirjasto näkymän."""
        self._destroy_view()
        self._current_view = LibraryGui(self._root, self._login)
        self._current_view.pack()
