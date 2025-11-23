import module5
x = int(input('enter your number: '))
user_y = int(input('enter lowest value in range: '))
user_z = int(input('enter highest value in range: '))

result = module5.check(x)
print(f'number {x} is in range <{user_y},{user_z}>: {result}')
