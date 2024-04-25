# Tämä koko moduuli on pieniä muokkauksia lukuunottamatta chat gpt generoimaa koodia

import tkinter as tk
from tkinter import messagebox, simpledialog
import library_db_manager


def launch_library_gui():
    def add_item():
        item_type = entry_type.get()
        model = entry_model.get()
        manufacturer = entry_manufacturer.get()
        if item_type and model and manufacturer:
            library_db_manager.add_item(item_type, model, manufacturer)
            messagebox.showinfo("Success", "Item added successfully")
            update_item_list()
        else:
            messagebox.showerror("Error", "All fields are required")

    def remove_item():
        item_id = simpledialog.askstring(
            "Remove Item", "Enter the ID of the item to remove:")
        if item_id:
            library_db_manager.remove_item(item_id)
            messagebox.showinfo("Success", "Item removed successfully")
            update_item_list()
        else:
            messagebox.showerror("Error", "ID is required")

    def update_item_list():
        items = library_db_manager.fetch_items()
        listbox_items.delete(0, tk.END)
        for item in items:
            listbox_items.insert(
                tk.END, f'ID: {item[0]}, Tyyppi: {item[1]}, Malli: {item[2]}, Valmistaja: {item[3]}')

    root = tk.Tk()
    root.title("Library Management")

    tk.Label(root, text="Tyyppi").grid(row=0, column=0)
    entry_type = tk.Entry(root)
    entry_type.grid(row=0, column=1)

    tk.Label(root, text="Malli").grid(row=1, column=0)
    entry_model = tk.Entry(root)
    entry_model.grid(row=1, column=1)

    tk.Label(root, text="Valmistaja").grid(row=2, column=0)
    entry_manufacturer = tk.Entry(root)
    entry_manufacturer.grid(row=2, column=1)

    add_button = tk.Button(root, text="Lisää tuote", command=add_item)
    add_button.grid(row=3, column=0)

    remove_button = tk.Button(root, text="Poista tuote", command=remove_item)
    remove_button.grid(row=3, column=1)

    listbox_items = tk.Listbox(root, width=60, height=10)
    listbox_items.grid(row=4, column=0, columnspan=2)
    update_item_list()

    root.mainloop()


if __name__ == "__main__":
    launch_library_gui()
