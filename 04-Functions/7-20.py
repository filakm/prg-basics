#Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:
import math

def is_prime(num):
    """Checks if a number is prime."""
    if num <= 1:
        return False
    # Check for factors from 2 up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    """Returns the n-th prime number."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

print(f(5))
