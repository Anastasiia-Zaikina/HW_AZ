task = """Write a function that takes in a string and returns the string with all the vowels removed"""

information_about_susan = 'Susan loves apples'

def remove_vowels(text: str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''.join(character for character in text if character not in vowels)
    return result
