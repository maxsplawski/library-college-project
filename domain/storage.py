import abc
from typing import Optional, Tuple, Any, Union, List


class DataStorage(abc.ABC):
    @abc.abstractmethod
    def initialize(self) -> None:
        pass

    @abc.abstractmethod
    def execute(
            self,
            query: str,
            params: Optional[Tuple[Any, ...]] = None,
            fetch: bool = False,
            fetchall: bool = False
    ) -> Union[None, Tuple, List[Tuple]]:
        pass
