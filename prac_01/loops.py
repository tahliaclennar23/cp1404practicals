"""
CP1404 | Practical 01: Loops | Tahlia Clennar
"""

# displaying odd numbers between 1 and 20
for i in range(1, 20+1, 2):
    print(i, end=' ')
print()

# counting in 10's from 0 to 100
for i in range(1, 100+1, 10):
    print(i, end=' ')
print()

# counting down from 20 to 1
for i in range(20, 1-1, -1):
    print(i, end=' ')
print()

# printing n stars
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print('*', end=' ')
print()

# printing n lines of increasing stars
for i in range(number_of_stars+1):
    print(i * '*')
print()

