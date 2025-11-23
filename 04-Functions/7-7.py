#The binary numerical system uses two symbols to represent a number: 0 and 1. 
# Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, or False otherwise. Sample result:


def f(binary_number):
    for digit in binary_number:
        if digit not in ['0', '1']:
            return False
    return True
        


print(f('11110a'))