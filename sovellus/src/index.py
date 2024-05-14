# import tkinter as tk
from tkinter import Tk
from ui.ui import UI
# from ui.gui import GUI


def main():
    app = Tk()
    app.title("Retro kone kirjasto")
    ui = UI(app)
    ui.start()
    app.mainloop()

    # root = tk.Tk()
    # app = GUI(root)
    # app.start()
    # root.mainloop()


if __name__ == "__main__":
    main()
