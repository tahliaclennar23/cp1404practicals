import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""5 is the lowest number & 20 is the largest number
3 is the lowest number & 9 is the largest number, could not produce 4 due to step size
5.5 is the largest number & 2.5 is the smallest number
"""
print(random.randint(1, 100))

