from cli import CLI
from controllers import BookController, AuthController
from db import DB

class App:
    def __init__(self):
        self.db = DB()
        self.auth_controller = AuthController()
        self.book_controller = BookController()
        self.cli = CLI(self.book_controller)

    def run(self):
        self.db.initialize()

        # Authenticate using AuthController
        self.cli

        while True:
            choice = self.cli.show_main_menu()
            self.cli.route_command(choice)