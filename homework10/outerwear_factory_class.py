from clothes_factory_class import Clothes_factory


class Outerwear_factory(Clothes_factory):
    def __init__(self, brand: str, year_founded: int, cloth_type: str, fabrics: list, gender: str, water_proof: bool,
                 wind_stopper: bool):
        super().__init__(brand, year_founded, cloth_type, fabrics, gender)
        self._water_proof = water_proof
        self._wind_stopper = wind_stopper

    def create_clothes(self, chosen_gender: str):
        self.check_gender(chosen_gender)
        print(f'New {self._cloth_type} outerwear is created with {self._fabrics} fabrics')

    def get_factory_name(self):
        print(f'Outerwear factory: {self._brand}')

    def show_when_use(self):
        if self._wind_stopper is True and self._water_proof is False:
            print('It is perfect for windy weather')
        elif self._water_proof is True and self._wind_stopper is False:
            print('It is perfect for rainy weather')
        elif self._water_proof is True and self._wind_stopper is True:
            print(f'Bad weather is not a problem with this {self._cloth_type}')
        else:
            print('It is better not to wear it when it is windy or rainy weather')
