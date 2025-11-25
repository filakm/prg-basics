#Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers. Sample result:


def f1(number1,number2,number3):
    if number1<number2<number3:
        diff = number3-number1
        return diff
    elif number2<number1<number3:
        diff = number3-number2
        return diff
    elif number3<number1<number2:
        diff = number2-number3
        return diff
    elif number1<number3<number2:
        diff = number2-number1
        return diff
    elif number3<number1<number1:
        diff = number1-number3
        return diff
    elif number2<number3<number1:
        diff = number1-number2
        return diff
def f2(number1,number2,number3):
    largest = max(number1,number2,number3)
    smallest = min(number1,number2,number3)
    diff = largest - smallest
    return diff
           
print(f2(3,1,7))