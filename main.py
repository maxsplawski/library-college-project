import time

from config import APP_NAME
from db import DB

def main():
    start = time.time()
    print(f"Starting {APP_NAME}...")
    db = DB()
    db.initialize()
    end = time.time()
    print(f"Completed initialization in {end - start:.2f} seconds")

if __name__ == "__main__":
    main()