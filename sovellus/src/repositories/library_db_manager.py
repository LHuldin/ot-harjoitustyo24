from database_connection import get_database_connection
from entities.hardware import Hardware
from entities.software import Software


class Library_db_manager:
    """Luokka joka vastaa kirjaston tietueisiin liittyvistä tietokanta operaatioista"""

    def __init__(self, connection):
        """Luokan konstruktori.

        Args: 
            connection: tietokantayhteydestä vastaava connection olio
        """
        self._connection = connection

    def add_hardware(self, hardware):
        """Luo laite tiedon tietokantaan

        Args:
            hardware: tallennettava laite tieto Hardware oliona

        Returns:
            Palauttaa luodun laite tiedon Hardware oliona.

        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO hardware (type, model, manufacturer, user_id) VALUES (?, ?, ?, ?)",
                       (hardware.type, hardware.model, hardware.manufacturer, hardware.user_id))
        self._connection.commit()
        return hardware

    def add_software(self, software):
        """Luo ohjelmisto tiedon tietokantaan

        Args:
            software: tallennettava ohjelmisto tieto Software oliona

        Returns:
            Palauttaa luodun ohjelmisto tiedon Software oliona.

        """
        cursor = self._connection.cursor()
        cursor.execute("INSERT INTO software (name, mediatype, model, manufacturer, user_id) VALUES (?, ?, ?, ?, ?)",
                       (software.name, software.mediatype, software.model, software.manufacturer, software.user_id))
        self._connection.commit()
        return software

    def fetch_hardware(self, id):
        """Palauttaa kaikki käyttäjän laite tietueet.

        Args:
            id: käyttäjän ja laitteen yhdistävä tieto

        Returns:
            Palauttaa listan laite tiedoista

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM hardware WHERE user_id = ?", (str(id),))
        return cursor.fetchall()

    def fetch_software(self, id):
        """Palauttaa kaikki käyttäjän ohjelmisto tietueet.

        Args:
            id: käyttäjän ja laitteen yhdistävä tieto

        Returns:
            Palauttaa listan ohjelmisto tiedoista

        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM software WHERE user_id = ?", (str(id),))
        return cursor.fetchall()

    def remove_hw(self, item_id):
        """Poistaa tietokannasta yhden hardware tietueen id tiedon perusteella
        
        Args:
            item_id: tietueen tetokannassa oleva id numero 
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM hardware WHERE id = ?", (item_id))
        self._connection.commit()

    def remove_sw(self, item_id):
        """Poistaa tietokannasta yhden software tietueen id tiedon perusteella
        
        Args:
            item_id: tietueen tetokannassa oleva id numero 
        """
        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM software WHERE id = ?", (item_id))
        self._connection.commit()

    def delete_all(self):
        """Poistaa kaiken hardware ja software tauluihin liittyvän tiedon tietokannasta 
        """

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM software")
        self._connection.commit()

        cursor = self._connection.cursor()
        cursor.execute("DELETE FROM hardware")
        self._connection.commit()


library_db_manager = Library_db_manager(get_database_connection())
