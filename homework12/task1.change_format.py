"""Describe any object of your choice in the class. I want the object to be printed to the console in the following format:
class_name: {
key: value
}"""


class Worker:
    def __init__(self, name: str, age: int, position: str):
        self.__name = name
        self.__age = age
        self.__position = position

    def __str__(self):
        res_string = f'{self.__class__.__name__}:{{\n\t"name": {self.__name}\n\t"age": {self.__age}\n\t"position": {self.__position}\n}}'
        return res_string
