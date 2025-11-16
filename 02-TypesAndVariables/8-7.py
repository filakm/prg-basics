## Code to change integrals into binary and hexadecimal

number = int(input('Enter your number: '))

#binary formula
binary_number = bin(number)
#hex formula
hex_number = hex(number)

# Results 
print(f'Your number: {number}')
print(f'Your number in binary system: {binary_number}')
print(f'Your number in hexadecimal system: {hex_number}')