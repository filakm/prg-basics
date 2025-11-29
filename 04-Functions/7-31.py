#Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 53.

#Tip: xn = x * xn-1

def power(x, n):
    if x  == 0:
        return 0
    if n == 0:
        return 1
    else:
        return x*x**(n-1)
    
print(power(5,3))