"""
Randomly returns two numbers between 1 and 6
"""

import random
# Generate two random integer between 1 and 6 (inclusive)
dice1 = random.randrange(1,6)
dice2 = random.randrange(1,6)
# Tell the user what the result was
print("Your dices show {} and {}".format(dice1,dice2))