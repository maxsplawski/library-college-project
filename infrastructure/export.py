from datetime import datetime

from domain.export import BookExporter
from domain.repositories import BookRepository


class CsvBookExporter(BookExporter):
    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def export_books(self, destination: str) -> None:
        instant = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        filename = f"books_{instant}.csv"
        books = self.book_repository.find_all()
        with open(f"{destination}/{filename}", "w") as file:
            for book in books:
                file.write(f"{f"{book.id},{book.isbn},{book.author},{book.title},{book.pages}"}\n")

            print(f"Exported {len(books)} books to {destination}/{filename}")
