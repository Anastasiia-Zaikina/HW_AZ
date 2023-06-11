"""Create a decorator that prints to the console the name of the function that was called. The function should work as intended.
For example, create a pair of functions for the arithmetic operations of summation and multiplication.
When calling these functions, the result of the operation must be returned and the name of the function that was called
must be displayed in the console with the result. Small hint (__name__)"""


def func_name_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'__{func.__name__}__')
        return func(*args, **kwargs)

    return wrapper


@func_name_decorator
def sum_numbers(number_1: int, number_2: int):
    return number_1 + number_2


@func_name_decorator
def multiply_numbers(number_1: int, number_2: int):
    return number_1 * number_2
