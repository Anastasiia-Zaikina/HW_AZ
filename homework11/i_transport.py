from abc import ABC, abstractmethod


class ITransport(ABC):

    @abstractmethod
    def carriage(self, weight: int, distance: int): ...

    @abstractmethod
    def max_cargo_capacity(self): ...

    @abstractmethod
    def distance_limit(self): ...
