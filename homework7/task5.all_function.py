"""Implement your own all function"""

def all_implementation (sequence):
    for element in sequence:
        if not element:
            return False
    return True

if __name__ == '__main__':
    new_list = [1, 2, 0]
    print(all_implementation(new_list))
