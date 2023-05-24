task = """You have the file text.txt(attached). Please count how many times each letter appears in this file."""

with open('text_for_task_3.txt') as file:
    data = file.read()

all_letters = {}

for element in data.lower():
    if element.isalpha():
        if element in all_letters:
            all_letters[element] += 1
        else:
            all_letters[element] = 1

