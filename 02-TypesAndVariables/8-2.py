###
# Calculation of circle area and circumference 
#

# determine radius and PI values
radius = int(input('Please input the radius of the circle cm: '))
pi=3.14
# calculate area 
area = round(pi*radius**2,2)
# calculate circumference 
circumference = round(2*pi*radius,2)
# print results
print(f'With given radius: {radius} the area of a circle is: {area} and the circumference is: {circumference}')