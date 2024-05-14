from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS library;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS hardware;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS software;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE hardware (
            id INTEGER PRIMARY KEY,
            type TEXT,
            model TEXT,
            manufacturer TEXT,
            user_id INTEGER REFERENCES users(id)
        );
    ''')

    cursor.execute('''
        CREATE TABLE software (
            id INTEGER PRIMARY KEY,
            name TEXT,
            mediatype TEXT,
            model TEXT,
            manufacturer TEXT,
            user_id INTEGER REFERENCES users(id)
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
