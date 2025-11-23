#Define the function f(n), which returns numbers from 1 to n as a string. Sample result:

def f(n):
    numbers = []
    for i in range (1,n+1):
        numbers.append(str(i))
    return "".join(numbers)


print(f(4))