task = """Write a function with the following signature: def display_box(width: int, height: int, character="*") . 
This function will draw a simple ASCII-art rectangle (non-filled) of the given height and width, using character to print the lines."""

def display_box(width: int, height: int, character="*"):
    horizontal_line = character * width
    empty_line = character + " " * (width - 2) + character
    print(horizontal_line)
    for element in range(height - 2):
        print(empty_line)
    print(horizontal_line)

