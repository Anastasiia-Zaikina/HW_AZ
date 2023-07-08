"""Create an iterator that accepts a sequence and can iterate over values over a given range.
CustomIterator(sequence, start_index, end_index)"""


class CustomIterator:

    def __new__(cls, sequence, start_index: int, end_index: int):
        if start_index >= end_index or end_index > len(sequence):
            raise TypeError('Invalid initial params')
        instance = super().__new__(cls)
        return instance

    def __init__(self, sequence, start_index: int, end_index: int):
        self.__sequence = sequence
        self.__end_index = end_index
        self.__current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index <= self.__end_index:
            result = self.__sequence[self.__current_index]
            self.__current_index += 1
            return result
        else:
            raise StopIteration
