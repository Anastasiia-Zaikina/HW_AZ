"""Describe the Train object. The class must contain fields and a method for adding wagons
(it is necessary to add objects, and instances of the wagon class). Describe the class Wagon together with the train.
The Wagon must contain a list of passengers and allow adding passengers. In the Wagon can be 10 passengers for example.
When using the len function on a Wagon, I want to see the number of passengers. When using len on a train,
I want to see a list of Wagons without a locomotive. Each wagon must have a number.
When printing a wagon to the console, I want to see the following "[n]" where n is the number of the wagon."""


class Train:
    def __init__(self):
        self._wagons = []

    def __add__(self, wagon):
        return self._wagons.append(wagon)

    def __repr__(self):
        final_str = '<=[HEAD]'
        self._wagons.sort(key=lambda x: x.get_number())

        for wagon in self._wagons:
            final_str += f'-{wagon}'

        return final_str

    def __len__(self):
        return len(self._wagons[1:])


class Wagon:
    def __init__(self, passengers: list, max_seats: int, wagon_number: int):
        self._passengers = passengers
        self._max_seats = max_seats
        self._wagon_number = wagon_number

    def get_number(self):
        return self._wagon_number

    def __len__(self):
        return len(self._passengers)

    def __add__(self, passenger: str):
        if len(self._passengers) < self._max_seats:
            return self._passengers.append(passenger)
        else:
            raise TypeError('Limit of passengers exceeded')

    def __repr__(self):
        return f"[{self._wagon_number}]"
