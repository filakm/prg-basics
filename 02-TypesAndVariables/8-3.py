###
# Write a program, a temperature converter, that reads temperature in degrees Celsius from the keyboard. 
# Then, the program calculates and prints the temperature in Kelvin and Fahrenheit.
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
temp = int(input('Please enter the temperature in Celsius: '))
# from C to F
temp_F= round(temp*1.8+32, 1)
# from C to K
temp_K= round(temp+273.15, 2)
# results
print(f'The temperature in C: {temp}, is {temp_F} degrees Fahrenheit and {temp_K} degrees Kelvin.')