from cosmetic_factory_class import Cosmetic_factory


class Skin_care_factory(Cosmetic_factory):
    def __init__(self, brand: str, year_founded: int, cosmetic_type: str, ingredients: list, package: str,
                 certificate: bool, audience_age: int):
        super().__init__(brand, year_founded, cosmetic_type, ingredients, package, certificate)
        self._audience_age = audience_age

    def show_age_recommendation(self):
        if self._audience_age in range(0, 21):
            print('You dont need to do something special with skin, just use SPF')
        elif self._audience_age in range(21, 36):
            print('It is better time to care about your skin. You could start using anti age cream')
        elif self._audience_age in range(36, 50):
            print('It is important to continue using anti age cream')
        else:
            print('Just enjoy your time')

    def get_factory_name(self):
        print(f'Skin care cosmetic factory: {self._brand}')
