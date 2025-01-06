from typing import Optional

from entities import Book
from repositories import BookRepository, UserRepository


class AuthController:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def login(self):
        print("To be implemented")

    def register(self):
        print("To be implemented")

class BookController:
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

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