###
# House lighting with three bulbs and two switches
# Checking how many bulbs are illuminating the house
#
light_switch1 = False # False - switch off, True - switch on
light_switch2 = True
bulbs_on = 0
if light_switch1 == True:
    bulbs_on += 1
if light_switch2 == True:
    bulbs_on += 2
if light_switch1 and light_switch2 == True:
    print(f'{bulbs_on} lights bulbs are on')
elif light_switch1 == True and light_switch2 == False:
    print(f'Room has {bulbs_on} bulbs on')
elif light_switch1 == False and light_switch2 == True:
    print(f'Room has {bulbs_on} bulbs on')
else:
    print('The room has no light bulbs on')