
casino_blacklist = ['John Smitt', 'Sara Chesvik', 'Lora Lips']

poker_blacklist = ['Marta Denvich', 'Alex Morting', 'Sara Chesvik', 'John Smitt']

alcohol_blacklist = ['Lara Finh', 'Sara Chesvik', 'Alex Vine']

in_all_blacklists = set(casino_blacklist).intersection(poker_blacklist).intersection(alcohol_blacklist)

print(in_all_blacklists)
