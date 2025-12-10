def read_from_file(name):
    with open(name) as file:
        content = file.read()
        return content
    
file_content = read_from_file('pets.txt')

sum = 0
for line in file_content:
    words = str(line).split()
    if str(line).count('.') >=1:
        sum -=1
    num = len(words)
    sum += num


print(file_content)
print(sum)