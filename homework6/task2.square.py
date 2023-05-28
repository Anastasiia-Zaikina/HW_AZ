import math
task = """Write a function square that takes 1 argument, the side of the square, and returns 3 values using a tuple): 
the perimeter of the square, the area of the square, and the diagonal of the square."""

def square(side: int):
    perimeter = side * 4
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return (perimeter, area, diagonal)

if __name__ == "__main__":
    print(square(2))
