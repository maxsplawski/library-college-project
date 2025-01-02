import sqlite3

from config import SQLITE_FILENAME

class DB:
    def initialize(self):
        with sqlite3.connect(SQLITE_FILENAME) as connection:
            cursor = connection.cursor()
            with open('tables.sql', 'r') as file:
                tables = file.read()
                cursor.executescript(tables)
                connection.commit()