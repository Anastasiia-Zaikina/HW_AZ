"""Describe mammals using principles from the lesson.
You should implement different fields(At least 2 for the Parent class) and methods (At least 2)."""

from abc import ABC, abstractmethod
from datetime import date


class Factory(ABC):
    def __init__(self, brand: str, year_founded: int, products: list):
        self._brand = brand
        self._year_founded = year_founded
        self._products = products

    def count_age(self):
        today = date.today()
        return today.year - self._year_founded

    @abstractmethod
    def get_factory_name(self): ...
