import os
import random
import pickle

task = """Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
a. element is an integer that will be the left operand of the expression
b. element is an integer that will be the right operand of the expression
c. element is an integer from 1 to 3 where:
identifies the addition operation
identifies the subtraction operation
identifies the multiplication operation
d. You can put data into a text file with the text form or use the pickle module in binary form. If placed as text then each line should contain only elements of one tuple separated by spaces (eg "100 2 3"). The file must be created by a script in a pre-created \test\data directory tree. The directory tree must be created by the script. Push only the code to the repository (not directories or file)."""

# Task from a to c
list_of_tuples = []

for element in range(0, 100):
    el_1 = random.randint(0, 10)
    el_2 = random.randint(0, 10)
    el_3 = random.randint(1, 3)
    list_of_tuples.append((el_1, el_2, el_3))

# Task d
path = './test/data'
os.makedirs(path)

with open(path+'/data_for_tuples.txt', 'w+b') as file:
    data_to_write = pickle.dumps(list_of_tuples)
    file.write(data_to_write)
