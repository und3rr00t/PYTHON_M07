from abc import ABC, abstractmethod
from typing import Any


class HealCapability(ABC):

    @abstractmethod
    def heal(self) -> str:
        ...


class TransformCapability(ABC):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._transformed: bool = False

    @property
    def transformed(self) -> bool:
        return self._transformed

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
