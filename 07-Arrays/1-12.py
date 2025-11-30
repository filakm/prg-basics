#Monthly expenses and their corresponding expense categories are included in the arrays below. 
# Write a program that calculates which expense category was the most expensive.

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]


n=0
n = abs(n)
x = max(expenses)

lst = ""

for category in categories:
    for expense in expenses[n:n+1]:
        price = expense
    lst = category + str(price)
    n+=1
    if price == x:
        print(f'the most expen is {category}')


