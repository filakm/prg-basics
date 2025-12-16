#def f(arr):
#    while len(arr)>=3:
#        for i in arr:
#            v =+ i
#            for i in arr:
#                if i!=v:
#                    return i
def f(arr):
    """
    Returns the number in the array that is different from the other numbers.
    The array is guaranteed to have at least 3 integers, with all numbers 
    equal except for exactly one unique number.
    """
    # Count the occurrences of each number
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1
    
    # Return the number with a count of 1
    for num, count in counts.items():
        if count == 1:
            return num
if __name__ == "__main__":
    print(f([1,6,6,6,6,6,6]))
