from clothes_factory_class import Clothes_factory


class Underwear_factory(Clothes_factory):
    def __init__(self, brand: str, year_founded: int, fabrics: list, gender: str, cloth_type: str,
                 thermal_underwear: bool):
        super().__init__(brand, year_founded, cloth_type, fabrics, gender)
        self._thermal_underwear = thermal_underwear

    def create_clothes(self, chosen_gender: str):
        self.check_gender(chosen_gender)
        print(f'New {self._cloth_type} underwear is created with {self._fabrics} fabrics')

    def get_factory_name(self):
        print(f'Underwear factory: {self._brand}')

    def check_thermal(self):
        if self._thermal_underwear is True:
            print('It is good idea to use it for sport')
        else:
            print('It is a simple underwear')
