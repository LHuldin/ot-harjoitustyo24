from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')
    
    cursor.execute('''
        DROP TABLE IF EXISTS library;
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
        CREATE TABLE library (
            id INTEGER PRIMARY KEY,
            type TEXT,
            model TEXT,
            manufacturer TEXT
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
