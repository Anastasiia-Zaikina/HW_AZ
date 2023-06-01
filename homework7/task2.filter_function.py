"""Implement your realization of the function filter"""


def filter_implementation(function, list_data: list):
    filtered_list = []
    for element in list_data:
        if function(element):
            filtered_list.append(element)
    return filtered_list


if __name__ == '__main__':
    new_list = [1, 1, 2, 3, 4, 4]
    equal_or_less_2 = filter_implementation(lambda x: x <= 2, new_list)
    print(equal_or_less_2)
