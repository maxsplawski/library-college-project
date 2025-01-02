import time

from config import APP_NAME
from db import DB

class App:
    def __init__(self):
        self.db = DB()

    def run(self):
        start = time.time()
        print(f"Starting {APP_NAME}...")
        self.db.initialize()
        end = time.time()
        print(f"Completed initialization in {end - start:.2f} seconds")