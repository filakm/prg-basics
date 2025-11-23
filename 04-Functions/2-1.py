#the largest number: 7,5,6,3,8,2
#the smallest number: 4,7,2,3,9,8
#length of the phrase: "computer science"
#letter read from the keyboard
#number representing the string "20303"
#binary string representing decimal number 304
#hexadecimal string representing decimal number 304
#integer representing the Unicode code of the € sign
#absolute value of -17

###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print(f'Max number of 7,5,6,3,8,2 is', {max_number})

min_number = min(4,7,2,3,9,8)
print(f'Min number of 4,7,2,3,9,8 is', {min_number})

str_length = len("computer science")
print(f'The number of characters in "computer science" is', {str_length})

letter = input("input: ")
print(f"{letter}")

str_numb = int("20303")
print(f'the number is {str_numb}')

str_bin = str(bin(304))
print(f'the bin is: {str_bin}')

hex_str = str(hex(304))
print(f'the hex is: {hex_str}')

sign = int(ord("€"))
print(f'the unicode for € is: {sign}')

abs = abs(-17)
print(f'the absolute value is: {abs}')