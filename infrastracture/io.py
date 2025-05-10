from domain.io import BooksImporter, BooksExporter
from repositories import SqlBookRepository


class CsvBooksImporter(BooksImporter):
    def __init__(self, book_repository: SqlBookRepository):
        self.book_repository = book_repository

    def import_books(self) -> None:
        pass


class CsvBooksExporter(BooksExporter):
    def __init__(self, book_repository: SqlBookRepository):
        self.book_repository = book_repository

    def export_books(self) -> None:
        pass
