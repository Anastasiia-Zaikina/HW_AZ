"""Implement your own implementation of the function map"""


def map_implementation(callback, sequence: list):
    """
    :param callback: function contains logic for element changes
    :param sequence: incoming data
    :return: list of updated elements
    """
    changed_list = []
    for element in sequence:
        updated_el = callback(element)
        changed_list.append(updated_el)
    return changed_list

if __name__ == '__main__':
    new_list = ['Viktor', 'Lana', 'Sveta']
    res = map_implementation(lambda x: x + 'A', new_list) # Add it to show that I understand how to use this function
    print(res)
