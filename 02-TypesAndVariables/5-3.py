
a_string = input('a= ')
a= int(a_string)
b_string = input('b= ')
b = int(b_string)
c_string = input('c= ')
c = int(c_string)
cuboid_volume = a*b*c
cuboid_surface_area = 2*(a*b+b*c+a*c)
print(f'Cuboid volume is {cuboid_volume}')
print(f'Cuboid surface area is {cuboid_surface_area}')
