"""Implement your own print function. It should work on all operating systems. You can't use build-in print function"""

import sys

def print_implementation(print_text:str):
    sys.stdout.write(print_text)

if __name__ == '__main__':
    print_implementation()
