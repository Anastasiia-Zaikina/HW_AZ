task = """You have a file of unknown length. Write a function that will remove all numbers from each line of the file."""

def remove_all_numbers(path_to_file: str):
    with open(path_to_file) as file:
        data = ''.join(character for character in file.read() if not character.isdigit())
    with open(path_to_file, 'w') as file:
        file.write(data)

# I have created a file to check this function
