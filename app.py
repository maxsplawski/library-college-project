from cli import CLI
from services import BookService, AuthService
from db import DB
from repositories import UserRepository, BookRepository


class App:
    def __init__(self):
        self.db = DB()
        self.user_repository = UserRepository(self.db)
        self.book_repository = BookRepository(self.db)
        self.auth_service = AuthService(self.user_repository)
        self.book_service = BookService(self.book_repository)
        self.cli = CLI(self.auth_service, self.book_service)

    def run(self):
        self.db.initialize()
        self.cli.show_auth_menu()
        choice = self.cli.show_main_menu()
        self.cli.route_command(choice)