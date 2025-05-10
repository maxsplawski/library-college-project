import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = f"{ROOT_DIR}/db"
APP_NAME = "Library"
SQLITE_FILENAME = f"{DB_DIR}/library.db"
INSERT_TESTDATA = False
EXPORT_DESTINATION = "exports"
