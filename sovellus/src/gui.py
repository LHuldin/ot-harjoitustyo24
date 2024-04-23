import tkinter as tk
from tkinter import ttk, Canvas, PhotoImage, NW

class GUI:
    def __init__(self, root):
        self._root = root


    def start(self):
        heading_label = ttk.Label(master=self._root, text="Kirjaudu")

        username_label = ttk.Label(master=self._root, text="Käyttäjänimi")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Salasana")
        password_entry = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Kirjaudu sisään")
        button2 = ttk.Button(master=self._root, text="Siirry tästä rekisteröitymään", command=self.open_register_window)
        button3 = ttk.Button(master=self._root, text="Katso kuva", command=self.open_picture_window)

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        button.grid(row=3, column=0, columnspan=2)
        
        button2.grid(row=4, column=0, columnspan=2)

        button3.grid(row=5, column=0, columnspan=2)


    def open_register_window(self):
        register_window = tk.Toplevel(self._root)
        register_window.title("Rekisteröidy")

        register_heading_label = ttk.Label(register_window, text="Rekisteröidy")
        register_heading_label.grid(row=0, column=0, columnspan=2)

        username_label = ttk.Label(register_window, text="Uusi käyttäjänimi")
        username_entry = ttk.Entry(register_window)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label = ttk.Label(register_window, text="Uusi salasana")
        password_entry = ttk.Entry(register_window)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        register_button = ttk.Button(register_window, text="Rekisteröidy")
        register_button.grid(row=3, column=0, columnspan=2)

    def open_picture_window(self):
        picture_window = tk.Toplevel(self._root)
        #root = Tk()
        canvas = Canvas(picture_window, width = 300, height = 300)
        canvas.pack()
        img = PhotoImage(file="data/testikuva07042024.ppm")
        canvas.create_image(20, 20, anchor=NW, image=img)
        picture_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    app.start()
    root.mainloop()

