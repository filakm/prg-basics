###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = (a+b+c)/2
    ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return ar
area = triangle_area(3,4,5)
area1 = triangle_area(5,12,13)
area2 = triangle_area(7,24,25)
print(f'The area of ​​a triangle with sides (3,4,5) is {area}')
print(f'The area of ​​a triangle with sides (5,12,13) is {area1}')
print(f'The area of ​​a triangle with sides (7,24,25) is {area2}')