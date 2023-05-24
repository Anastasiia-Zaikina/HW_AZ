import pickle

task = """Using the created file in task 1, read the file and perform mathematical operations on each element.
Output the result of the operation to the console. You cannot use imports to import from the first task module."""

path = './test/data/data_for_tuples.txt'
with open(path, 'r+b') as file:
    byte_text = file.read()

result_of_pickle = pickle.loads(byte_text)
result = []

for element in result_of_pickle:
    last_element = element[-1]
    if last_element == 1:
        result.append(element[0] + element[1])
    elif last_element == 2:
        result.append(element[0] - element[1])
    elif last_element == 3:
        result.append(element[0] * element[1])
print(result)
