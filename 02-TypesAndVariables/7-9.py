### 1 or 6 dice rolls

import random

dice_roll = random.randint (1,6)
roll_1 = dice_roll == 1
roll_6 = dice_roll == 6
special_roll = roll_1 or roll_6
print(f'Dice rolled: {dice_roll}')
print(f'Dice rolled (1,6) {special_roll}')