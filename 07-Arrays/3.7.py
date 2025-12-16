def f(arr): 
    longest = ""
    for name in arr:
        count = len(name)
        if count > len(longest):
            longest = name
    return longest
print(f(['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']))
