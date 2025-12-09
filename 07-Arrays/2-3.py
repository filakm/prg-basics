
# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates total monthly expenses per category
total_food = 0
total_transport = 0
total_utilities = 0

for week in monthly_expenses:
    total_food += week[0]
    total_transport += week[1]
    total_utilities += week[2]

# Calculates total weekly expenses
week_totals = []
for week in monthly_expenses:
    # Use the built-in sum() function for simplicity
    week_totals.append(sum(week))

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')