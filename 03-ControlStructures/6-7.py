#Write a program that asks the user for their age and then checks which age group they belong to:

#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older

age = int(input('Please enter your age: '))

if age < 13:
    print("You're a Child")
elif age >= 13 and age <= 19:
    print("youre a teenager")
elif age >= 20 and age  <= 64:
    print('youre an adult')
else:
    print('youre a senior')