import tkinter as tk
from tkinter import messagebox, simpledialog
from services.library_service import Library_service


def launch_library_gui():
    service = Library_service()

    def add_item():
        item_type = entry_type.get()
        model = entry_model.get()
        manufacturer = entry_manufacturer.get()
        # system = entry_system.get()
        if item_type and model and manufacturer:
            service.add_item(item_type, model, manufacturer)
            messagebox.showinfo("Success", "Item added successfully")
            update_item_list()
        else:
            messagebox.showerror("Error", "Täytä kaikki kentät")

    def add_hardware():
        item_type = entry_type.get()
        model = entry_model.get()
        manufacturer = entry_manufacturer.get()
        if item_type and model and manufacturer:
            service.add_item(item_type, model, manufacturer)
            messagebox.showinfo("Success", "Item added successfully")
            update_hardware_list()
        else:
            messagebox.showerror("Error", "Täytä kaikki kentät")

    def add_software():
        system = entry_system.get()
        item_type = entry_type.get()
        model = entry_model.get()
        manufacturer = entry_manufacturer.get()
        if item_type and model and manufacturer:
            service.add_item(system, item_type, model, manufacturer)
            messagebox.showinfo("Success", "Item added successfully")
            update_software_list()
        else:
            messagebox.showerror("Error", "Täytä kaikki kentät")

    def remove_item():
        item_id = simpledialog.askstring(
            "Poista tuote", "Anna tuotteen ID poistaaksesi sen:")
        if item_id:
            service.remove_item(item_id)
            messagebox.showinfo("Success", "Tuote poistettu")
            update_item_list()
        else:
            messagebox.showerror(
                "Error", "tällä ID numerolla ei löydy tuotetta")

    def update_item_list():
        items = service.fetch_items()
        listbox_items.delete(0, tk.END)
        for item in items:
            listbox_items.insert(
                tk.END, f'ID: {item[0]}, Tyyppi: {item[1]}, Malli: {item[2]}, Valmistaja: {item[3]}')

    def update_hardware_list():
        items = service.fetch_items()
        listbox_hardware.delete(0, tk.END)
        for item in items:
            listbox_hardware.insert(
                tk.END, f'ID: {item[0]}, Tyyppi: {item[1]}, Malli: {item[2]}, Valmistaja: {item[3]}')

    def update_software_list():
        items = service.fetch_items()
        listbox_software.delete(0, tk.END)
        for item in items:
            listbox_software.insert(
                tk.END, f'ID: {item[0]}, Systeemi: {item[1]}, Tyyppi: {item[2]}, Malli: {item[3]}, Valmistaja: {item[4]}')

    root = tk.Tk()
    root.title("Kirjaston hallinta")

    # item_type_hs = tk.StringVar(value="hardware")
    # tk.Radiobutton(root, text="Hardware", variable=item_type_hs, value=1).grid(row=0, column=0)
    # tk.Radiobutton(root, text="Software", variable=item_type_hs, value=2).grid(row=0, column=1)

    # def update_fields():
    #    if item_type_hs.get() == 1:  # Hardware
    #        entry_system.grid_remove()
    #        tk.Label(root, text="Systeemi").grid_remove()
    #    else:  # Software
    #        entry_system.grid()
    #        tk.Label(root, text="Systeemi").grid()
    # update_fields()

    # tk.Label(root, text="Systeemi").grid(row=3, column=0)
    # entry_system = tk.Entry(root)
    # entry_system.grid(row=1, column=1)

    tk.Label(root, text="Tyyppi").grid(row=2, column=0)
    entry_type = tk.Entry(root)
    entry_type.grid(row=2, column=1)

    tk.Label(root, text="Malli").grid(row=3, column=0)
    entry_model = tk.Entry(root)
    entry_model.grid(row=3, column=1)

    tk.Label(root, text="Valmistaja").grid(row=4, column=0)
    entry_manufacturer = tk.Entry(root)
    entry_manufacturer.grid(row=4, column=1)

    add_button = tk.Button(root, text="Lisää tuote", command=add_item)
    add_button.grid(row=5, column=0)

    remove_button = tk.Button(root, text="Poista tuote", command=remove_item)
    remove_button.grid(row=5, column=1)

    listbox_items = tk.Listbox(root, width=60, height=10)
    listbox_items.grid(row=6, column=0, columnspan=2)
    update_item_list()

    # listbox_hardware = tk.Listbox(root, width=60, height=10)
    # listbox_hardware.grid(row=7, column=0, columnspan=2)
    # update_hardware_list()

    # listbox_software = tk.Listbox(root, width=60, height=10)
    # listbox_software.grid(row=8, column=0, columnspan=2)
    # update_software_list()

    root.mainloop()
