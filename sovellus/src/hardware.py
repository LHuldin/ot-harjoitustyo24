class Hardware:
    def __init__(self, type, model, manufacturer):
        self.type = type
        self.model = model
        self.manufacturer = manufacturer

    def __repr__(self):
        return f"{self.type}: {self.model} ({self.manufacturer})"
