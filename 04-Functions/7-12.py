#Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:

def f(n):
    num_of = int(n)
    if num_of >= 2:
        return  (num_of-1)*("*"+"/")+"*"
    else:
        return  num_of*"*"   
    
print(f(7))