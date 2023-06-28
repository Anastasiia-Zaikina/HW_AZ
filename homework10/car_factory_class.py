from transport_factory_class import Transport_factory


class Car_transport_factory(Transport_factory):
    def __init__(self, brand: str, year_founded: int, purpose: str, passenger_seats_limit: int, transmission_type: str,
                 fuel: str):
        super().__init__(brand, year_founded, purpose, passenger_seats_limit)
        self._transmission_type = transmission_type
        self._fuel = fuel

    def create_transport(self, passenger_seats: int):
        self.check_passengers_seats(passenger_seats)
        print(f'New car was created with brand: {self._brand} for purpose: {self._purpose} \n'
              f'with {self._transmission_type} transmission type and {self._fuel} fuel')

    def get_factory_name(self):
        print(f'Car factory: {self._brand}')
