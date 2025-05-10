import abc
from typing import Optional

from domain.entities import User, Book
from domain.storage import DataStorage


class UserRepository(abc.ABC):
    data_storage: DataStorage

    @abc.abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abc.abstractmethod
    def save(self, user: User) -> None:
        pass


class BookRepository(abc.ABC):
    data_storage: DataStorage

    @abc.abstractmethod
    def find_all(self) -> list[Book]:
        pass

    @abc.abstractmethod
    def find_by_isbn(self, isbn: str) -> Optional[Book]:
        pass

    @abc.abstractmethod
    def exists_by_isbn(self, isbn: str) -> bool:
        pass

    @abc.abstractmethod
    def save(self, book: Book) -> None:
        pass

    @abc.abstractmethod
    def update_by_isbn(self, isbn: str, book: Book) -> None:
        pass

    @abc.abstractmethod
    def delete_by_isbn(self, isbn: str) -> None:
        pass
