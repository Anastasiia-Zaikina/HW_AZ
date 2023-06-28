from factory_class import Factory
from abc import abstractmethod


class Clothes_factory(Factory):
    def __init__(self, brand: str, year_founded: int, cloth_type: str, fabrics: list, gender: str):
        super().__init__(brand, year_founded, products=['Outerwear', 'Clothes', 'Underwear'])
        self._cloth_type = cloth_type
        self._fabrics = fabrics
        self._gender = gender

    @abstractmethod
    def create_clothes(self, chosen_gender: str): ...

    def check_gender(self, chosen_gender: str):
        if chosen_gender not in self._gender:
            raise TypeError(f'You could create clothes only for {self._gender}')
