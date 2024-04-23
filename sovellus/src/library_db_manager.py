from database_connection import get_database_connection

def add_item(type, model, manufacturer):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO library (type, model, manufacturer) VALUES (?, ?, ?)", (type, model, manufacturer))
    connection.commit()

def fetch_items():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM library")
    return cursor.fetchall()

def remove_item(item_id):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM library WHERE id = ?", (item_id))
    connection.commit()