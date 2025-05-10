import os

APP_NAME = "Library"
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = f"{ROOT_DIR}/db"
SQLITE_FILENAME = f"{DB_DIR}/library.db"
INSERT_TESTDATA = False
EXPORT_DESTINATION = f"{ROOT_DIR}/exports"
