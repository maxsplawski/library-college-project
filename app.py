import sqlite3

from cli import CLI
from db import DB
from repositories import UserRepository, BookRepository
from services import BookService, AuthService
from settings import SQLITE_FILENAME, APP_NAME


class App:
    def __init__(self):
        self.db = DB(SQLITE_FILENAME)
        self.user_repository = UserRepository(self.db)
        self.book_repository = BookRepository(self.db)
        self.auth_service = AuthService(self.user_repository)
        self.book_service = BookService(self.book_repository)
        self.cli = CLI(self.auth_service, self.book_service)

    def run(self):
        try:
            self.db.initialize()
            print(f"Welcome back to {APP_NAME}!")
            authenticated = False
            while not authenticated:
                authenticated = self.cli.authenticate()
            while True:
                print(f"\n--- {APP_NAME} ---")
                choice = self.cli.get_choice()
                self.cli.route_command(choice)
        except sqlite3.Error as sqlite_error:
            print(f"SQLite error: {sqlite_error}")
        except IOError as io_error:
            print(f"IO error: {io_error}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")