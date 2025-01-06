from cli import CLI
from controllers import BookController, AuthController
from db import DB
from repositories import UserRepository, BookRepository


class App:
    def __init__(self):
        self.db = DB()
        self.user_repository = UserRepository(self.db)
        self.book_repository = BookRepository(self.db)
        self.auth_controller = AuthController(self.user_repository)
        self.book_controller = BookController(self.book_repository)
        self.cli = CLI(self.auth_controller, self.book_controller)

    def run(self):
        self.db.initialize()

        # Authenticate using AuthController
        # self.cli.show_auth_menu()

        while True:
            choice = self.cli.show_main_menu()
            self.cli.route_command(choice)