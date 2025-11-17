# Most female names in Polish end with the letter "a". Write a program that prints the name entered from the keyboard, provided it is a female name. Sample result:

name = input('enter a female name: ')

if name.endswith('a'):
    print(f"{name} is a female name")
else:
    print(f'{name} is not a female name.')