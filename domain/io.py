import abc


class BooksImporter(abc.ABC):
    @abc.abstractmethod
    def import_books(self) -> None:
        pass


class BooksExporter(abc.ABC):
    @abc.abstractmethod
    def export_books(self) -> None:
        pass
