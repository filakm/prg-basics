
def star(n):
    for i in str(n):
        d = int(i)*"*"
    return d
    
arr = [2, 6, 4, 9, 7]
count = 0
m=0
while count < len(arr):
    print(f'{arr[m]}:{star(arr[m])} ')
    m+=1
    count+=1