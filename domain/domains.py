import hashlib
from typing import Optional

from domain.entities import Book, User
from domain.export import BookExporter
from domain.repositories import UserRepository, BookRepository


class AuthDomain:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self, email: str, password: str) -> bool:
        user = self.user_repository.find_by_email(email)
        if user:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return user.password == hashed_password
        else:
            return False

    def register(self, email: str, password: str):
        name = email.split("@")[0]
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user = User(None, name, email, hashed_password)
        self.user_repository.save(user)

    def get_user(self, email: str) -> Optional[User]:
        return self.user_repository.find_by_email(email)


class BookDomain:
    def __init__(self, book_repository: BookRepository, book_exporter: BookExporter):
        self.book_repository = book_repository
        self.books_exporter = book_exporter

    def get_books(self) -> list[Book]:
        return self.book_repository.find_all()

    def get_book(self, isbn: str) -> Optional[Book]:
        return self.book_repository.find_by_isbn(isbn)

    def add_book(self, book: Book) -> Book:
        self.book_repository.save(book)
        return self.book_repository.find_by_isbn(book.isbn)

    def update_book(self, book: Book) -> Book:
        self.book_repository.update_by_isbn(book.isbn, book)
        return self.book_repository.find_by_isbn(book.isbn)

    def delete_book(self, isbn: str):
        self.book_repository.delete_by_isbn(isbn)

    def export_books(self, destination: str):
        self.books_exporter.export_books(destination)
