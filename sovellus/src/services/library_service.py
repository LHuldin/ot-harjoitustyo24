from repositories.library_db_manager import library_db_manager
from entities.hardware import Hardware
from entities.software import Software
from services.user_service import user_service


class Library_service:
    """Ohjelman hardware ja software tietueiden käsittelystä vastaan sovelluslogiikan luokka"""

    def __init__(self):
        self._library_db = library_db_manager

    def add_hardware(self, item_type, model, manufacturer):
        """Hoitaa laite tiedon lisäämisen käyttöliittymästä tulleen tiedon avaulla lisäten siihen
        personoivan käytääjä tiedon"""
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
        """Hoitaa ohjelmisto tiedon lisäämisen käyttöliittymästä tulleen tiedon avaulla lisäten siihen
        personoivan käytääjä tiedon"""
        user = user_service.user_now()
        if name and mediatype and model and manufacturer:
            try:
                self._library_db.add_software(Software(
                    name, mediatype, model, manufacturer, user.user_id))

                return True
            except:
                return False
        else:
            return False

    def remove_hardware(self, item_id):
        """Tiedon poistosta ID tiedon avulla vastaava funktio"""
        if item_id:
            try:
                self._library_db.remove_hw(item_id)
                return True
            except:
                return False
        else:
            return False

    def remove_software(self, item_id):
        """Tiedon poistosta ID tiedon avulla vastaava funktio"""
        if item_id:
            try:
                self._library_db.remove_sw(item_id)
                return True
            except:
                return False
        else:
            return False

    def fetch_hardware(self):
        """Hakee tietokannasta käyttäjää vastaavan tiedon siellä olevista laitteista"""
        user = user_service.user_now()
        id = user.user_id
        try:
            items = self._library_db.fetch_hardware(id)
            return items
        except:
            return False

    def fetch_software(self):
        """Hakee tietokannasta käyttäjää vastaavan tiedon siellä olevista ohjelmistoista"""
        user = user_service.user_now()
        id = user.user_id
        try:
            items = self._library_db.fetch_software(id)
            return items
        except:
            return False


library_service = Library_service()
