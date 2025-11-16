###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter($): '))
fuel_consumption = float(input ('Enter vehicles fuel consuptpion per 100km: '))
total_fuel_consumption = distance*fuel_consumption*0.01
total_cost = round(fuel_price*total_fuel_consumption,2)
print(f'The total fuel consuption on distance {distance} is: {total_fuel_consumption} liters')
print(f'The total cost of transport on the distance {distance}km is: {total_cost}$')