import sqlite3

from config import SQLITE_FILENAME

class DB:
    def initialize(self):
        try:
            with sqlite3.connect(SQLITE_FILENAME) as connection:
                cursor = connection.cursor()
                with open('tables.sql', 'r') as file:
                    tables = file.read()
                    cursor.executescript(tables)
                with open('testdata.sql', 'r') as file:
                    statements = file.read()
                    cursor.executescript(statements)

        except sqlite3.Error as sqlite_error:
            print(f"SQLite error: {sqlite_error}")
        except IOError as io_error:
            print(f"IO error: {io_error}")
        except Exception as ex:
            print(f"An unexpected error occured: {ex}")
