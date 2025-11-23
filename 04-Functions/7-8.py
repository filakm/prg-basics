#The vending machine accepts 1, 2 and 5 PLN coins. 
# Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. 
# Sample result:


def f(amount_to_pay):
    coins_5 = amount_to_pay//5  
    remaining = amount_to_pay%5
    coins_2 = remaining//2
    remaining= remaining%2
    coins_1 = remaining
    amount_of_coins = coins_5+coins_2+coins_1
    return amount_of_coins

print(f(23))