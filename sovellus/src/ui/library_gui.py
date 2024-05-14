# import tkinter as tk
from tkinter import ttk, constants
from tkinter import messagebox, simpledialog
from services.library_service import library_service
from services.user_service import user_service
import tkinter as tk


class LibraryGui:

    def __init__(self, root, outlogger):

        self._root = root
        self._outlogger = outlogger
        self._user = user_service.user_now()
        self._frame = None
        self._hw_item_type_entry = None
        self._hw_model_entry = None
        self._hw_manufacture_entry = None
        self._sw_name_entry = None
        self._sw_mediatype_entry = None
        self._sw_model_entry = None
        self._sw_manufacturer_entry = None
        self._todo_list_frame = None
        self._todo_list_view = None

        self._start()

        print("nyt kirjastossa!!!")

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _start(self):

        self._frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(
            master=self._frame, text="Tervetuloa kirjastoon")
        heading_label.grid(row=0, column=0, columnspan=2)
        ttk.Button(self._frame, text="Lisää Laite",
                   command=self._open_add_hardware_window).grid(row=1, column=0)
        ttk.Button(self._frame, text="Lisää Peli",
                   command=self._open_add_software_window).grid(row=1, column=1)
        self._hw_listbox = tk.Listbox(self._frame, height=10, width=50)
        self._hw_listbox.grid(row=2, column=0, columnspan=2)
        self._sw_listbox = tk.Listbox(self._frame, height=10, width=50)
        self._sw_listbox.grid(row=3, column=0, columnspan=2)
        self.update_hardware_list()
        self.update_software_list()
        remove_hwbutton = tk.Button(self._frame, text="Poista Laite", command=self.remove_hardware)
        remove_hwbutton.grid(row=4, column=0)
        remove_swbutton = tk.Button(self._frame, text="Poista Peli", command=self.remove_software)
        remove_swbutton.grid(row=4, column=1)
        
        
        ttk.Button(self._frame, text="Kirjaudu ulos",
                   command=self._outlogger).grid(row=5, column=2)

    def _open_add_hardware_window(self):
        self._add_window = tk.Toplevel(self._root)
        self._add_window.title("Lisää Laite")

        ttk.Label(self._add_window, text="Laite Tyyppi:").grid(
            row=0, column=0)
        hw_type_entry = tk.Entry(self._add_window)
        hw_type_entry.grid(row=0, column=1)

        ttk.Label(self._add_window, text="Laite Malli:").grid(
            row=1, column=0)
        hw_model_entry = tk.Entry(self._add_window)
        hw_model_entry.grid(row=1, column=1)

        ttk.Label(self._add_window, text="Laite Valmistaja:").grid(
            row=2, column=0)
        hw_manufacturer_entry = tk.Entry(self._add_window)
        hw_manufacturer_entry.grid(row=2, column=1)

        ttk.Button(self._add_window, text="Lisää", command=lambda: self.add_hardware(hw_type_entry.get(
        ), hw_model_entry.get(), hw_manufacturer_entry.get())).grid(row=3, column=0, columnspan=2)

    def _open_add_software_window(self):
        self._add_window = tk.Toplevel(self._root)
        self._add_window.title("Lisää Peli")

        ttk.Label(self._add_window, text="Pelin Järjestelmä:").grid(
            row=0, column=0)
        sw_system_entry = tk.Entry(self._add_window)
        sw_system_entry.grid(row=0, column=1)

        ttk.Label(self._add_window, text="Pelin Mediatyyppi:").grid(
            row=1, column=0)
        sw_mediatype_entry = tk.Entry(self._add_window)
        sw_mediatype_entry.grid(row=1, column=1)

        ttk.Label(self._add_window, text="Pelin Malli:").grid(
            row=2, column=0)
        sw_model_entry = tk.Entry(self._add_window)
        sw_model_entry.grid(row=2, column=1)

        ttk.Label(self._add_window, text="Pelin Valmistaja:").grid(
            row=3, column=0)
        sw_manufacturer_entry = tk.Entry(self._add_window)
        sw_manufacturer_entry.grid(row=3, column=1)

        ttk.Button(self._add_window, text="Lisää", command=lambda: self.add_software(sw_system_entry.get(
        ), sw_mediatype_entry.get(), sw_model_entry.get(), sw_manufacturer_entry.get())).grid(row=4, column=0, columnspan=2)

    def add_hardware(self, item_type, model, manufacturer):
        if item_type and model and manufacturer:
            library_service.add_hardware(item_type, model, manufacturer)
            messagebox.showinfo("Success", "Laite lisätty")
            self.update_hardware_list()
            self._add_window.destroy()
        else:
            messagebox.showerror("Error", "Täytä kaikki kentät")

    def add_software(self, name, mediatype, model, manufacturer):
        if name and mediatype and model and manufacturer:
            print(name)
            print(mediatype)
            library_service.add_software(name, mediatype, model, manufacturer)
            messagebox.showinfo("Success", "Peli lisätty")
            self.update_software_list()
            self._add_window.destroy()
        else:
            messagebox.showerror("Virhe", "Täytä kaikki kentät")

    def remove_hardware(self):
        item_id = simpledialog.askstring(
            "Poista tuote", "Anna laitteen ID poistaaksesi sen:")
        if item_id:
            library_service.remove_hardware(item_id)
            messagebox.showinfo("Success", "Laite poistettu")
            self.update_hardware_list()
        else:
            messagebox.showerror(
                "Error", "tällä ID numerolla ei löydy laitetta")
            
    def remove_software(self):
        item_id = simpledialog.askstring(
            "Poista tuote", "Anna pelin ID poistaaksesi sen:")
        if item_id:
            library_service.remove_software(item_id)
            messagebox.showinfo("Success", "Peli poistettu")
            self.update_software_list()
        else:
            messagebox.showerror(
                "Error", "tällä ID numerolla ei löydy peliä")


    def update_hardware_list(self):
        items = library_service.fetch_hardware()
        self._hw_listbox.delete(0, tk.END)

        print("testi")
        for item in items:
            self._hw_listbox.insert(
                tk.END, f'ID: {item[0]}, Tyyppi: {item[1]}, Malli: {item[2]}, Valmistaja: {item[3]}')

    def update_software_list(self):
        items = library_service.fetch_software()
        self._sw_listbox.delete(0, tk.END)
        print("testi2")
        for item in items:
            self._sw_listbox.insert(
                tk.END, f'ID: {item[0]}, Systeemi: {item[1]}, Tyyppi: {item[2]}, Malli: {item[3]}, Valmistaja: {item[4]}')
