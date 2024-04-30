from database_connection import get_database_connection


def add_user(username, password):
    if len(username) < 4 or len(password) < 4:
        return False

    if not user_exists(username):
        connection = get_database_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        connection.commit()
        return True
    return False


def fetch_user(username):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    return cursor.fetchone()


def user_exists(username):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    return cursor.fetchone() is not None
