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
        self.db.initialize()
        self.cli.show_auth_menu()
        print(f"\n--- {APP_NAME} ---")
        while True:
            choice = self.cli.show_main_menu()
            self.cli.route_command(choice)
