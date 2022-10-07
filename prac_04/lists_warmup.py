"""
CP1404 | Practical 4: Lists | Tahlia Clennar
Program to write Lists
"""


numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers [:-1] =[3, 1, 4, 1, 5, 9]
# numbers [3:4] =[1]
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers= False
# numbers + [6, 5, 3]= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# change first element to "ten"
numbers[0] = "ten"
# change last element to 1
numbers[6] = 1
# print all elements except the first two
print(numbers[2:])
# print whether 9 is an element of numbers
print(9 in numbers)


