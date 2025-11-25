#Define the function f(x,y), which returns the
#  sum of numbers in the range <x,y> 
# that are completely divisible by 2 and 3 and not 
# divisible by 4. 
# Sample result:

def f(x,y):
    sum = 0
    for n in range(x,y+1):
          
            if n%2 ==0 and n%3 == 0 and n%4 !=0:
                sum += n
                
    return sum

print(f(1,20))