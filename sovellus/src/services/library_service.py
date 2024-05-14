from repositories.library_db_manager import library_db_manager
from entities.hardware import Hardware
from entities.software import Software
from services.user_service import user_service


class Library_service:

    def __init__(self):
        self._library_db = library_db_manager

    

    def add_hardware(self, item_type, model, manufacturer):
        user = user_service.user_now()
        if item_type and model and manufacturer:
            try:
                self._library_db.add_hardware(
                    Hardware(item_type, model, manufacturer, user.user_id))
                return True
            except:
                return False
        else:
            return False

    def add_software(self, name, mediatype, model, manufacturer):
        user = user_service.user_now()
        print("testaillaan")
        print(user.user_id)
        if name and mediatype and model and manufacturer:
            try:
                self._library_db.add_software(Software(
                    name, mediatype, model, manufacturer, user.user_id))

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

    

    def fetch_hardware(self):
        user = user_service.user_now()
        id = user.user_id
        print("service")
        print(id)
        try:
            items = self._library_db.fetch_hardware(id)
            return items
        except:
            return False

    def fetch_software(self):
        user = user_service.user_now()
        id = user.user_id
        try:
            items = self._library_db.fetch_software(id)
            return items
        except:
            return False


library_service = Library_service()
