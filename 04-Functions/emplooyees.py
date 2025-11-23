###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import keyboard # your own defined module

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = ...
age = ...
salary = ...
is_salary_hidden = input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', ...)
print(...)
print(...)
if ...:
    print('Salary')