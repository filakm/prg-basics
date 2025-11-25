#Products are marked with a special code consisting of 3 digits
#  and afourth control digit. The forth digit is determined by
#  calculating the remainder of dividing the sum of the first 
# three digits by 7. Define a function f(product_code) that 
# returns True if the product code is correct or False otherwise. 
# Sample result:

def f(product_code):
    if str(product_code).isdigit() and len(product_code) ==4:
        sum = 0
        for char in product_code[0:3]:
            sum += int(char)
        last_digit = sum%7
        if str(last_digit) == str(product_code)[3:]:    
            return True
        else:
            return False
    else:
        return False
    
print(f('2035'))
