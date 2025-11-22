#Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard. Sample result:

#Enter time (24-hour format): 16:32
#Time in 12-hour format: 4:32pm

format1 = input('enter time (hh:mm): ')

if int(format1[0:2]) < 12:
    am_hours = format1[0:2]
    minutes = format1[2:]
    print(f'in the 24 hour format: {format1}')
    print(f'in the 12 hour format: {am_hours}{minutes} am')
elif int(format1[0:2]) > 12 and int(format1[0:2]) < 24:
    pm_hours = int(format1[0:2])-12
    minutes = format1[2:]
    print(f'in the 24 hour format: {format1}')
    print(f'in the 12 hour format: {pm_hours}{minutes} pm')    
elif int(format1[0:2]) == 24:
    am_hours = int(format1[0:2])-12
    minutes = format1[2:]
    print(f'in the 24 hour format: {format1}')
    print(f'in the 12 hour format: {am_hours}{minutes} am')    
else:
    pm_hours = format1[0:2]
    minutes = format1[2:]
    print(f'in the 24 hour format: {format1}')
    print(f'in the 12 hour format: {pm_hours}{minutes} pm')