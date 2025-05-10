import sqlite3

from domain.domains import BookDomain, AuthDomain
from domain.export import BookExporter
from domain.repositories import UserRepository, BookRepository
from domain.storage import DataStorage
from domain.view import View
from infrastructure.export import CsvBookExporter
from infrastructure.repositories import SqlUserRepository, SqlBookRepository
from infrastructure.storage import SqliteDataStorage
from infrastructure.view import CommandLineInterfaceView
from settings import SQLITE_FILENAME, APP_NAME


class App:
    data_storage: DataStorage
    user_repository: UserRepository
    book_repository: BookRepository
    book_exporter: BookExporter
    auth_service: AuthDomain
    book_service: BookDomain
    view: View

    def __init__(self):
        self.data_storage = SqliteDataStorage(SQLITE_FILENAME)
        self.user_repository = SqlUserRepository(self.data_storage)
        self.book_repository = SqlBookRepository(self.data_storage)
        self.book_exporter = CsvBookExporter(self.book_repository)
        self.auth_service = AuthDomain(self.user_repository)
        self.book_service = BookDomain(self.book_repository, self.book_exporter)
        self.view = CommandLineInterfaceView(self.auth_service, self.book_service)

    def run(self):
        try:
            self.data_storage.initialize()
            print(f"Welcome back to {APP_NAME}!")
            authenticated = False
            while not authenticated:
                authenticated = self.view.authenticate()
            while True:
                print(f"\n--- {APP_NAME} ---")
                choice = self.view.get_command()
                self.view.route_command(choice)
        except sqlite3.Error as sqlite_error:  # maybe delete
            print(f"SQLite error: {sqlite_error}")
        except IOError as io_error:
            print(f"IO error: {io_error}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")
