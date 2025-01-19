import sqlite3
import time
from typing import Tuple, List, Optional, Any, Union

from settings import DB_DIR, INSERT_TESTDATA, APP_NAME


class DB:
    def __init__(self, sqlite_database: str):
        self.sqlite_database = sqlite_database

    def initialize(self):
        try:
            start = time.time()
            print(f"Starting {APP_NAME}...")

            with sqlite3.connect(self.sqlite_database) as connection:
                cursor = connection.cursor()
                with open(f"{DB_DIR}/tables.sql", 'r') as file:
                    tables = file.read()
                    cursor.executescript(tables)
                if INSERT_TESTDATA:
                    with open(f"{DB_DIR}/testdata.sql", 'r') as file:
                        statements = file.read()
                        cursor.executescript(statements)

            end = time.time()
            print(f"Completed initialization in {end - start:.2f} seconds")

        except sqlite3.Error as sqlite_error:
            print(f"SQLite error: {sqlite_error}")
        except IOError as io_error:
            print(f"IO error: {io_error}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

    def execute(
            self,
            query: str,
            params: Optional[Tuple[Any, ...]] = None,
            fetch: bool = False,
            fetchall: bool = False
    ) -> Union[None, Tuple, List[Tuple]]:
        try:
            with sqlite3.connect(self.sqlite_database) as connection:
                cursor = connection.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                connection.commit()
                if fetch:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()

        except sqlite3.Error as sqlite_error:
            print(f"SQLite error: {sqlite_error}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")
