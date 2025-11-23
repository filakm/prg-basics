
def f(n):
    # Use range(1, n + 1) to generate numbers from 1 up to and including n
    numbers = []
    for i in range(1, n + 1):
        numbers.append(str(i))
    # Join the list of number strings into a single string
    return "".join(numbers)

# Sample result for f(5):
print(f(5))