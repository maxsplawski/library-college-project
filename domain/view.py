import abc

from domain.domains import BookDomain, AuthDomain


class View(abc.ABC):
    auth_domain: AuthDomain
    book_domain: BookDomain

    @abc.abstractmethod
    def authenticate(self) -> bool:
        pass

    @abc.abstractmethod
    def attempt_login(self) -> bool:
        pass

    @abc.abstractmethod
    def attempt_registration(self) -> bool:
        pass

    @abc.abstractmethod
    def get_command(self) -> str:
        pass

    @abc.abstractmethod
    def route_command(self, command: str) -> None:
        pass
