from tkinter import Tk
from ui.ui import UI


def main():
    app = Tk()
    app.title("Retrolaite ja peli kirjasto")
    ui = UI(app)
    ui.start()
    app.mainloop()


if __name__ == "__main__":
    main()
