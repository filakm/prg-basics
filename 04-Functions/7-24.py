#An expression contains operators for adding and subtracting single-digit numbers. 
# Define a function f(expression) that returns the value of the expression. Sample result:

def f(expression):

    expression = str(expression).replace(" ", "")

    # Start with a running total. The first number is always the initial value.
    # We find the first digit by assuming the first character is a number.
    total = int(expression[0])
    
    # Iterate through the rest of the expression, stepping by 2 (operator, number, operator, number...)
    # We start the loop from index 1
    for i in range(1, len(expression), 2):
        operator = expression[i]
        # The number follows immediately after the operator
        number = int(expression[i+1])
        
        if operator == '+':
            total += number
        elif operator == '-':
            total -= number
        # If there were other operators, we'd add 'elif' blocks here
        else:
            raise ValueError(f"Unknown operator found: {operator}")
            
    return total

print(f('2+3-4+5-0'))
    