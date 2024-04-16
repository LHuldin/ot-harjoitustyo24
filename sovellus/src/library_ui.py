import csv
from hardware import Hardware


class LibraryUI:
    def __init__(self, filename="hardware_data.csv"):
        self.filename = filename
        self.hardware_list = []

    def run(self):
        while True:
            print("\n1. Lisää laite")
            print("2. Näytä kaikki laitteet")
            print("3. Poistu kirjastosta")
            choice = input("Valitse toiminto (1-3): ")

            if choice == '1':
                self.add_and_save_hardware()

            elif choice == '2':
                self.load_and_show_hardware()

            elif choice == '3':
                print("Poistutaan kirjastosta")
                break

            else:
                print("Virheellinen valinta. Yritä uudelleen.")

    # seuraavassa on käytetty apuna chatgpt:n luomaa koodia

    def add_and_save_hardware(self):
        type = input("Laite tyyppi: ")
        model = input("Laitteen malli: ")
        manufacturer = input("Laitteen valmistaja: ")
        hardware = Hardware(type, model, manufacturer)
        self.load_hardware()
        self.hardware_list.append(hardware)
        self.save_hardware()
        print("Tallennettu:", hardware)

    def load_and_show_hardware(self):
        self.load_hardware()
        if self.hardware_list:
            for hardware in self.hardware_list:
                print(hardware)
        else:
            print("Ei tallennettuja laitteita.")

    def save_hardware(self):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Type', 'Model', 'Manufacturer'])
            for hardware in self.hardware_list:
                writer.writerow(
                    [hardware.type, hardware.model, hardware.manufacturer])

    def load_hardware(self):
        self.hardware_list = []
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header
                for row in reader:
                    if row:
                        hardware = Hardware(row[0], row[1], row[2])
                        self.hardware_list.append(hardware)
        except FileNotFoundError:
            pass
    # Chatgpt:n käyttö päättyy
