#A palindrome is an expression that sounds the same when read backwards. 
# Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. Sample result:

def f(palindrome):
    return palindrome == palindrome[::-1]

print(f('oko'))