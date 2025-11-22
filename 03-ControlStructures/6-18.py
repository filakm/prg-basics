#Let x and y denote the coordinates of a point on the plane. 
# Write a program that determines in which quadrant of the coordinate system the point P(x, y) is located 
# or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.
#  Sample result:
#   x = 5
#   y = 2
#   Point P(5,2) is in the first quadrant of the coordinate system
coordinates = input('enter the coordinates (x,y): ')
if int(coordinates[0:1]) > 0 and int(coordinates[2:]) > 0:
    quadrant = "first"
elif int(coordinates[0:1]) > 0 and int(coordinates[2:])< 0: 
    quadrant = "second"
elif int(coordinates[0:1]) < 0 and int(coordinates[2:])< 0:
     quadrant = "third"
   
elif int(coordinates[0:1]) < 0 and int(coordinates[2:])> 0:
    quadrant ="fourth"      
else:
    quadrant = "center of the coordinate system"
print(f'Point ({coordinates}) is in {quadrant} quadrant')
