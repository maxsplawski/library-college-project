import time

from cli import CLI
from config import APP_NAME
from controllers import Controller
from db import DB

class App:
    def __init__(self):
        self.db = DB()
        self.controller = Controller()
        self.cli = CLI(self.controller)

    def run(self):
        start = time.time()
        print(f"Starting {APP_NAME}...")
        self.db.initialize()
        end = time.time()
        print(f"Completed initialization in {end - start:.2f} seconds")

        while True:
            choice = self.cli.show_menu()
            self.cli.route_command(choice)