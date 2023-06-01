"""Implement your own implementation of the function map"""


def map_implementation(function, list_data: list):
    changed_list = []
    for element in list_data:
        updated_el = function(element)
        changed_list.append(updated_el)
    return changed_list


if __name__ == '__main__':
    new_lis = [30, 40, 50]
    res = map_implementation(lambda x: x + 10, new_lis)
    print(res)
