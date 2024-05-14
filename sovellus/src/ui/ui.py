from ui.login_gui import LoginGui
from ui.register_gui import RegisterGui
from ui.library_gui import LibraryGui
from ui.add_hw_gui import AddHWGui


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._root.minsize(500, 500)
        self._login()

    def _destroy_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _login(self):
        self._destroy_view()
        self._current_view = LoginGui(
            self._root, self._library, self._register, self._login)
        self._current_view.pack()

    def _register(self):
        self._destroy_view()
        self._current_view = RegisterGui(
            self._root, self._library, self._login)
        self._current_view.pack()

    def _library(self):
        self._destroy_view()
        print("nyt melkein kirjastossa")
        self._current_view = LibraryGui(self._root, self._login)
        self._current_view.pack()

    def _add_hw(self):
        pass

    def _add_sw(self):
        pass
