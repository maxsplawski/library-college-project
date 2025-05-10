from typing import Optional

from domain.entities import Book, User
from domain.repositories import UserRepository, BookRepository
from domain.storage import DataStorage


class SqlUserRepository(UserRepository):
    def __init__(self, data_storage: DataStorage):
        self.data_storage = data_storage

    def find_by_email(self, email: str) -> Optional[User]:
        row = self.data_storage.execute("SELECT * FROM users WHERE email = ?", (email,), fetch=True)
        if row is None:
            return None
        user = User(*row)
        return user

    def save(self, user: User) -> None:
        self.data_storage.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                                  (user.name, user.email, user.password))


class SqlBookRepository(BookRepository):
    def __init__(self, data_storage: DataStorage):
        self.data_storage = data_storage

    def find_all(self) -> list[Book]:
        rows = self.data_storage.execute("SELECT * FROM books", fetchall=True)
        books = list(map(lambda row: Book(*row), rows))
        return books

    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        row = self.data_storage.execute("SELECT * FROM books WHERE isbn = ?", (isbn,), fetch=True)
        if row is None:
            return None
        book = Book(*row)
        return book

    def exists_by_isbn(self, isbn: str) -> bool:
        row = self.data_storage.execute("SELECT * FROM books WHERE isbn = ?", (isbn,), fetch=True)
        return row is not None

    def save(self, book: Book) -> None:
        self.data_storage.execute("INSERT INTO books (isbn, author, title, pages) VALUES (?, ?, ?, ?)",
                                  (book.isbn, book.author, book.title, book.pages))

    def update_by_isbn(self, isbn: str, book: Book) -> None:
        self.data_storage.execute("UPDATE books SET author = ?, title = ?, pages = ? WHERE isbn = ?",
                                  (book.author, book.title, book.pages, isbn))

    def delete_by_isbn(self, isbn: str) -> None:
        self.data_storage.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
