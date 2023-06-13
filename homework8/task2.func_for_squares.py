"""Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive.
The solution should work and not freeze your computer."""


def return_squares():
    for number in range(0, 1000000001, 2):
        yield number ** 2


squares_for_numbers = return_squares()
