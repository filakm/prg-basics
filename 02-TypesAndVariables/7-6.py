#
#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
# Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:

velocity = int(input('Input the speed of the vehicle: '))
speedlimit = 40 <= velocity <= 140
print(f"Speed is valid. {speedlimit}")