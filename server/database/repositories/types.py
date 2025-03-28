from abc import ABC, abstractmethod
from typing import Iterable


class BaseRepository(ABC):
    @abstractmethod
    def create(self, data: dict): ...

    @abstractmethod
    def read(self, pk: any): ...

    @abstractmethod
    def read_by(self, **filters): ...

    @abstractmethod
    def read_many(self, **filters): ...

    @abstractmethod
    def update(self, pk: any, data: dict): ...

    @abstractmethod
    def delete(self, pk: any): ...

    @abstractmethod
    def exists(self, **filters): ...
