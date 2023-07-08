from time import sleep

from i_animal import IAnimal
from i_transport import ITransport


# inheritance
# abstraction
class Horse(IAnimal, ITransport):

    def __init__(self, max_cargo_capacity: int, max_distance: int):
        # hiding
        self.__max_distance = max_distance
        self.__max_cargo_capacity = max_cargo_capacity
        self.__is_hungry = True

    @property
    def max_cargo_capacity(self):
        return self.__max_cargo_capacity

    @property
    def distance_limit(self):
        return self.__max_distance

    @staticmethod
    def allowed_food():
        return ['Oats', 'Hay', 'Carrots']

    # polymorphism
    def move(self):
        if self.__is_hungry is True:
            raise TypeError("I can't move. I'm starving")
        else:
            print("I'm running like a wind...")

    def stop(self):
        print("I'm tired. I need some rest")

    def eat(self, food: str):
        if food in self.allowed_food():
            print('It was delicious')
            self.__is_hungry = False
        else:
            raise TypeError("I can't eat it")

    # encapsulation
    def carriage(self, weight: int, distance: int):
        if weight > self.max_cargo_capacity():
            raise TypeError("It is to much weight for me")

        loaded_on = (weight * 100) / self.max_cargo_capacity()
        max_possible_distance = min(self.distance_limit(), distance - ((distance * loaded_on) / 100))
        distance_traveled = 0
        while distance_traveled < max_possible_distance:
            self.move()
            distance_traveled += 1
            sleep(1)

        if max_possible_distance == self.distance_limit():
            self.stop()
        else:
            print("I've finished my journey")
