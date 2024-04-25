import tkinter as tk
from gui import GUI


def main():
    root = tk.Tk()
    app = GUI(root)
    app.start()
    root.mainloop()


if __name__ == "__main__":
    main()
