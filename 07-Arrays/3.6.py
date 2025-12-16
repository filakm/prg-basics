def f(arr):
    count = 0
    sum = 0

    while count <len(arr):
        sum += arr[count]
        count +=1
    return sum/count
print(f([15, 8, 31, 47, 2, 19]))
