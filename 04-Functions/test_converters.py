import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'532cm = {converters.cm_to_m(532)}m')
print(f'3cm = {converters.cm_to_i(3)}inches')
print(f'5 feet and 6 inches = {converters.f_i_to_cm(5,6)}cm')

