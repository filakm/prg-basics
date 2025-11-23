#Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns the sum of the even digits. 
# When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:

def f(number, even):
    if even == True:
        sum = 0
        for digit in str(number):
            if int(digit)%2==0:
                sum =  sum+ int(digit)
        return sum
    elif even == False:
        sum = 0
        for digit in str(number):
            if int(digit)%2==1:
                sum =+sum+int(digit)
        return sum
    
print(f(13115, True))