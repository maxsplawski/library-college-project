from typing import Optional

from db import DB
from entities import Book, User


class UserRepository:
    def __init__(self, db: DB):
        self.db = db

    def find_by_email(self, email: str) -> Optional[User]:
        row = self.db.execute("SELECT * FROM users WHERE email = ?", (email,), fetch=True)
        if row is None:
            return None
        user = User(*row)
        return user

    def save(self, user: User):
        self.db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                        (user.name, user.email, user.password))

class BookRepository:
    def __init__(self, db: DB):
        self.db = db

    def find_all(self) -> list[Book]:
        rows = self.db.execute("SELECT * FROM books", fetchall=True)
        books = list(map(lambda row: Book(*row), rows))
        return books

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        row = self.db.execute("SELECT * FROM books WHERE isbn = ?", (isbn,), fetch=True)
        if row is None:
            return None
        book = Book(*row)
        return book

    def exists_by_isbn(self, isbn: str) -> bool:
        row = self.db.execute("SELECT * FROM books WHERE isbn = ?", (isbn,), fetch=True)
        return row is not None

    def save(self, book: Book):
        self.db.execute("INSERT INTO books (isbn, author, title, pages) VALUES (?, ?, ?, ?)",
                       (book.isbn, book.author, book.title, book.pages))

    def update_by_isbn(self, isbn: str, book: Book):
        self.db.execute("UPDATE books SET author = ?, title = ?, pages = ? WHERE isbn = ?",
                        (book.author, book.title, book.pages, isbn))

    def delete_by_isbn(self, isbn: str):
        self.db.execute("DELETE FROM books WHERE isbn = ?",(isbn,))