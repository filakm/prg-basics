#Define a function f(number) that returns the sum of repeated digits in a number. Sample result:

def f(number):
    sum = 0
    for char in str(number):
        if str(number).count(char) > 1:
            sum +=int(char)
    return sum
    
print(f(513553007))