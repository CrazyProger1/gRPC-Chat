from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def create(self): ...

    @abstractmethod
    def read(self): ...

    @abstractmethod
    def read_many(self): ...

    @abstractmethod
    def update(self): ...

    @abstractmethod
    def delete(self): ...
