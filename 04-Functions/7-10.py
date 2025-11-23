#   Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:

def f(x,y):
    num_of_neg = 0
    for digit in range(x,y):
        if digit < 0 and digit%2==0:
            num_of_neg += 1
    return num_of_neg

print(f(-1,11))