class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def perimeter(self):
      return self.a*4

square1 = Square(4)
area = square1.area()
paramiter = square1.perimeter()
square2 = Square(6)
area1 = square2.area()
paramiter1 = square2.perimeter()

print('Square with side 4:')
print(f'Area is {area}, Perimeter is {paramiter} ')
print ('Square with side 6:')
print(f'Area is {area1}, Perimeter is {paramiter1} ')