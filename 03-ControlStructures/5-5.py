###
# Sums numbers entered by user
#
total_sum = 0
number_of_inputs = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    number_of_inputs += 1
    arithmetic_mean = total_sum/number_of_inputs
print(f"The total sum of the numbers is: {total_sum} and arithmetic mean is: {arithmetic_mean}")