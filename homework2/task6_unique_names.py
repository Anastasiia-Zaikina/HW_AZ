
non_unique_names = ['John Dow', 'Marta Dow', 'Stiven Stew', 'John Dow', 'Sasha Bow']

unique_names = list(dict.fromkeys(non_unique_names))

print(unique_names)
