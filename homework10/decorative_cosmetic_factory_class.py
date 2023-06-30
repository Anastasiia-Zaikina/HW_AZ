from cosmetic_factory_class import Cosmetic_factory


class Decorative_cosmetic_factory(Cosmetic_factory):
    def __init__(self, brand: str, year_founded: int, cosmetic_type: str, ingredients: list, package: str,
                 certificate: bool, shade: str):
        super().__init__(brand, year_founded, cosmetic_type, ingredients, package, certificate)
        self._shade = shade

    def change_shade(self, new_shade: str):
        if isinstance(new_shade, str):
            self._shade = new_shade
        else:
            raise TypeError(f'Shade should be a string, not a {type(new_shade)}')

    def get_factory_name(self):
        print(f'Decorative cosmetic factory: {self._brand}')
