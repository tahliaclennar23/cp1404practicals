"""
Tahlia Clennar
CP1404 Practical 4- "Quick Pick" Lottery Ticket Generator
Program for generating quick pick lists
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
        while random_number in quick_pick:
            random_number = random.randint(QUICK_PICK_MINIMUM, QUICK_PICK_MAXIMUM)
        quick_pick.append(random_number)
        quick_pick.sort()
    print(' '.join("{:2}".format(pick) for pick in quick_pick))
