import abc


class BookExporter(abc.ABC):
    @abc.abstractmethod
    def export_books(self, destination: str) -> None:
        pass
