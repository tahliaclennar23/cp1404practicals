"""

"""
import random

LENGTH_QUICK_PICK = 6
QUICK_PICK_MAXIMUM = 45
QUICK_PICK_MINIMUM = 1


quick_picks = int(input("How many quick picks?: "))

for i in range(quick_picks):
    quick_pick = []
    for j in range(LENGTH_QUICK_PICK):
        random_number = random.randint(QUICK_PICK_MINIMUM, QUICK_PICK_MAXIMUM)
        quick_pick.append(random_number)
    print(quick_pick)
