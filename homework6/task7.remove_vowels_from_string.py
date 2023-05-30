"""Write a function that takes in a string and returns the string with all the vowels removed"""

information_about_susan = 'Susan lOves Apples'

def remove_vowels(text: str):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    result = ''.join(character for character in text if character not in vowels)
    return result


if __name__ == '__main__':
    print(remove_vowels(information_about_susan))