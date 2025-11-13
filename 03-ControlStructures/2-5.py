###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input(f'Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month <= 3:
    quarter = 1
elif month >= 4 <= 6:
    quarter = 25
elif month >= 7 <= 9:
    quarter = 3  

print(f'Month {month} is in quarter {quarter}')