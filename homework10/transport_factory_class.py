from abc import abstractmethod
from factory_class import Factory


class Transport_factory(Factory):
    def __init__(self, brand: str, year_founded: int, purpose: str, passenger_seats_limit: int):
        super().__init__(brand, year_founded, products=['Car', 'Airplane', 'Train'])
        self._purpose = purpose
        self._passenger_seats_limit = passenger_seats_limit

    @abstractmethod
    def create_transport(self, passenger_seats: int): ...

    def check_passengers_seats(self, passenger_seats: int):
        if passenger_seats > self._passenger_seats_limit:
            raise TypeError(
                f'You try to install {passenger_seats} seats, when the limit is {self._passenger_seats_limit}')
