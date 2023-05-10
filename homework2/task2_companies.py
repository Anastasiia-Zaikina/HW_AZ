eleks = ['Marta', 'John', 'Robert', 'Sasha', 'Julia']

toshiba = ['Peter', 'Kristin', 'Julia', 'Alex', 'Marta']

toshiba.extend(eleks)
eleks.clear()


print(toshiba)
print(eleks)