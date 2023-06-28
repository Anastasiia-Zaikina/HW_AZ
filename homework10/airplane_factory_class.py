from transport_factory_class import Transport_factory


class Airplane_factory(Transport_factory):
    def __init__(self, brand: str, year_founded: int, purpose: str, passenger_seats_limit: int, is_military: bool,
                 engine_type: str):
        super().__init__(brand, year_founded, purpose, passenger_seats_limit)
        self._is_military = is_military
        self._engine_type = engine_type

    def create_transport(self, passenger_seats: int):
        self.check_passengers_seats(passenger_seats)
        print(f'New airplane was created with brand: {self._brand} for purpose: {self._purpose} \n'
              f'with {self._engine_type} engine type')

    def get_factory_name(self):
        print(f'Airplane factory: {self._brand}')

    def check_for_military(self):
        if self._is_military is True:
            print('You could use it also for military purposes')
        else:
            raise TypeError(f'You could use it only for {self._purpose} purposes')
