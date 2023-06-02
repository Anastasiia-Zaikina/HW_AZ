"""Implement your realization of the function filter"""


def filter_implementation(callback, sequence: list):
    """
    :param callback: function contains logic for element changes
    :param sequence: incoming data
    :return: list of updated elements
    """
    filtered_list = []
    for element in sequence:
        if callback(element):
            filtered_list.append(element)
    return filtered_list

if __name__ == '__main__':
    new_list = [1, 1, 2, 3, 4, 4]
    equal_or_less_2 = filter_implementation(lambda x: x <= 2, new_list)# Add it to show that I understand how to use this function
    print(equal_or_less_2)
