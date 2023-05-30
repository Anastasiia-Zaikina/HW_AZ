"""Write a function is_prime that takes 1 argument - a number from 2 to 1000, and returns True if it is a prime number, and False otherwise."""

def is_prime(number: int):
    for divider in range(2, number):
        if (number % divider) == 0:
            return False
    return True
