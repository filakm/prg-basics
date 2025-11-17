#he parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:

# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
# Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.

time = int(input("Please enter the amount of hours of parking: "))


if time >= 1 and time <= 2:
    print('Fee is 5 PLN')
elif time >= 3 and time <= 6 :
    print('Fee is 15 PLN')
elif time > 6:
    print('Fee is 20 PLN')
else:
    print('No fee')