import sqlite3
import time

from config import SQLITE_FILENAME, APP_NAME

class DB:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def initialize(self):
        try:
            start = time.time()
            print(f"Starting {APP_NAME}...")

            with sqlite3.connect(SQLITE_FILENAME) as connection:
                cursor = connection.cursor()
                with open('tables.sql', 'r') as file:
                    tables = file.read()
                    cursor.executescript(tables)
                with open('testdata.sql', 'r') as file:
                    statements = file.read()
                    cursor.executescript(statements)

            end = time.time()
            print(f"Completed initialization in {end - start:.2f} seconds")

        except sqlite3.Error as sqlite_error:
            print(f"SQLite error: {sqlite_error}")
        except IOError as io_error:
            print(f"IO error: {io_error}")
        except Exception as ex:
            print(f"An unexpected error occured: {ex}")
