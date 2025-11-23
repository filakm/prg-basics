

def check(x):
    user_y = int(input('enter lowest value in range: '))
    user_z = int(input('enter highest value in range: '))
    y=user_y
    z= user_z
    if x in range(y,z):
        return 'yes'
    else:
        return 'no'