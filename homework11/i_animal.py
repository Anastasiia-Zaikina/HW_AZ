from abc import ABC, abstractmethod


class IAnimal(ABC):

    @abstractmethod
    def move(self): ...

    @abstractmethod
    def stop(self): ...

    @abstractmethod
    def eat(self, food: str): ...
