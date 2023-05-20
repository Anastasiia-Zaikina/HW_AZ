elements = [1, 2, 3, 4, 5, 6, 7, 8]

list_of_odd = []
list_of_even = []

for index, element in enumerate(elements):
    if index % 2 == 1:
     list_of_odd.append((index, element))
    elif index % 2 != 1:
        list_of_even.append((index, element))
