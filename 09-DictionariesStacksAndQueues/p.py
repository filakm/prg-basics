class Car:
 def __init__(self, brand, model, year):
     self.brand = brand  # Object attribute
     self.model = model  # Object attribute
     self.year = year    # Object attribute

 def display_info(self):
     print(f"Car: {self.brand} {self.model}, Year: {self.year}")



car1 = Car('Ford','Focus',2021)
car1.display_info()
car1.brand = 'Opel'
xyz = car1.model
print(car1.year)