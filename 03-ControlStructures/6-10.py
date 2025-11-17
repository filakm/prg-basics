# Write a program that calculates a dog's age in dog's years. For the first two years, a dog's life is equal to 10.5 human years.
#  After that, each dog year is equal to 4 human years. Sample result:


#results
dog = float(input("Enter dogs age: "))
human_year = 0


#formulas
if dog <= 2:
    human_year = dog * 10.5
else:
    human_year= 2*10.5
    human_year += (dog-2)*4
print(f'your dogs age {dog} is {human_year} in human years')