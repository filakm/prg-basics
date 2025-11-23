#Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. 
# The available operators are +,-,*,%,**. Sample result:


def f(number1, number2, operator):
    if operator == '+':
        sum = number1+number2
        return sum
    elif operator =="-":
        sum = number1-number2
        return sum
    elif operator =="*":
        sum = number1*number2
        return sum
    elif operator =="%":
        sum = number1%number2
        return sum
    elif operator=='**':
        sum = number1**number2
        return sum
    else:
        return 'error'
    
print(f(2,3,'-'))