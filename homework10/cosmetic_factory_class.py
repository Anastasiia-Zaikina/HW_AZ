from factory_class import Factory


class Cosmetic_factory(Factory):
    def __init__(self, brand: str, year_founded: int, cosmetic_type: str, ingredients: list, package: str,
                 certificate: bool):
        super().__init__(brand, year_founded, products=['Skin Care', 'Decorative'])
        self._cosmetic_type = cosmetic_type
        self._ingredients = ingredients
        self._package = package
        self._certificate = certificate

    def create_cosmetic(self):
        if self._certificate is True:
            print(
                f'The {self._cosmetic_type} is created: contains {self._ingredients}, and have {self._package} package')
        else:
            raise TypeError(f'You could not create a {self._cosmetic_type} without certificate')

    def add_ingredient(self, new_ingredient):
        self._ingredients.append(new_ingredient)
