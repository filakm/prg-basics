#Define the function f(n), which returns the n-th value of the Fibonacci sequence.
#  The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
# Each subsequent value is the sum of the previous two. Sample result:

def f(n):
      if n == 1:
         return 0
      elif n == 2:
         return 1
      else:
         return f(n-1)+ f(n-2)
   
print(f(9))