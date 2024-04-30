from repositories.library_db_manager import library_db_manager


class Library_service:

    def __init__(self):
        self._library_db = library_db_manager

    def add_item(self, item_type, model, manufacturer):
        if item_type and model and manufacturer:
            try:
                self._library_db.add_item(item_type, model, manufacturer)
                return True
            except:
                return False
        else:
            return False

    def add_hardware(self, item_type, model, manufacturer):
        if item_type and model and manufacturer:
            try:
                self._library_db.add_hardware(item_type, model, manufacturer)
                return True
            except:
                return False
        else:
            return False

    def add_software(self, system, item_type, model, manufacturer):
        if system and item_type and model and manufacturer:
            try:
                self._library_db.add_software(
                    system, item_type, model, manufacturer)
                return True
            except:
                return False
        else:
            return False

    def remove_item(self, item_id):
        if item_id:
            try:
                self._library_db.remove_item(item_id)
                return True
            except:
                return False
        else:
            return False

    def fetch_items(self):
        try:
            items = self._library_db.fetch_items()
            return items
        except:
            return False

    def fetch_hardware(self):
        try:
            items = self._library_db.fetch_hardware()
            return items
        except:
            return False

    def fetch_software(self):
        try:
            items = self._library_db.fetch_software()
            return items
        except:
            return False


library_service = Library_service()
