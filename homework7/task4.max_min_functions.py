"""Implement your own implementation of function max and min """


def max_implementation(sequence: list):
    max_value = sequence[0]
    for element in sequence[1:]:
        if element > max_value:
            max_value = element
    return max_value


def min_implementation(sequence: list):
    min_value = sequence[0]
    for element in sequence[1:]:
        if element < min_value:
            min_value = element
    return min_value

if __name__ == '__main__':
    new_list = [1, 2, 3, 4, 5]
    print(min_implementation(new_list))
