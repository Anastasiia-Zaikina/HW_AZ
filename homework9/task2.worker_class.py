"""Create a class with a description of the worker. Any worker. employees."""
from datetime import date


class Worker:
    def __init__(self, name: str, date_of_birthday: date, department: str, position: str, salary: int):
        self.__name = name
        self.__date_of_birthday = date_of_birthday
        self.company = 'Toshiba'
        self.__department = department
        self.__position = position
        self.__salary = salary

    @staticmethod
    def show_holidays():
        print('01.01, 07.01, 22.01, 08.03, 16.04, 01.05, 09.05, 04.06, 28.06, 28.07, 23.08, 14.10, 06.12, 25.12')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) < 15:
            self.__name = new_name
        else:
            raise TypeError(f'Name should be a string of length less than 15: {type(new_name)} : {len(new_name)}')

    @property
    def date_of_birthday(self):
        return self.__date_of_birthday

    def count_age(self):
        today = date.today()
        age = today.year - self.__date_of_birthday.year
        if today.month < self.__date_of_birthday.month or (
                today.month == self.__date_of_birthday.month and today.day < self.__date_of_birthday.day):
            age -= 1
        return age

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, new_department):
        if isinstance(new_department, str):
            self.__department = new_department
        else:
            raise TypeError(f'Department should be a string not a {type(new_department)}')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        if isinstance(new_position, str):
            self.__position = new_position
        else:
            raise TypeError(f'Position should be a string not a {type(new_position)}')

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, int) and new_salary > 0:
            self.__salary = new_salary
        else:
            raise TypeError(f"Salary should be an integer not a {type(new_salary)} and couldn't be 0")

    def count_netto_salary(self, tax, ssc):
        netto = self.__salary - ((self.__salary * tax) / 100) - ssc
        return netto

    @classmethod
    def create_worker_with_bonus(cls, name, age, department, position, salary, bonus):
        salary_with_bonus = salary + bonus
        return cls(name, age, department, position, salary_with_bonus)
