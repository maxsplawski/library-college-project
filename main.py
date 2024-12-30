from db import DB

def main():
    db = DB("library.db")
    db.initialize()

if __name__ == "__main__":
    main()