#Define a function sum_natural(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n.
#  Apply recursion. 
# Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum_natural(n):
    if n == 1:
        return 1
    else:
        return n + sum_natural(n-1)
start_range = 1
end_range = 10

# Sprawdzenie, czy podana liczba n jest naturalna (dodatnia)
if end_range < 1:
    print("Podana liczba musi być liczbą naturalną (większą lub równą 1).")
else:
    # Wywołanie funkcji dla gornej granicy zakresu (10)
    result = sum_natural(end_range)
    print(f"Suma liczb naturalnych w zakresie od {start_range} do {end_range} wynosi: {result}")
