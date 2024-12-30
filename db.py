import sqlite3

class DB:
    def __init__(self, filename: str):
        self.filename = filename

    def initialize(self):
        with sqlite3.connect(self.filename) as connection:
            cursor = connection.cursor()
            with open('tables.sql', 'r') as file:
                tables = file.read()
                cursor.executescript(tables)
                connection.commit()