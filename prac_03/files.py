"""
Tahlia Clennar
CP1404 Practical 03- Files
Program to read and write to files
"""
FILE_NAME = "name.txt"
with open(FILE_NAME, 'w') as name_text:
    name = input("Enter your name: ")
    print(f"{name}", file=name_text)

with open(FILE_NAME, 'r') as name_text:
    text = name_text.read()
    print(f"Your name is {text}")

with open("numbers.txt", 'r') as numbers_text:
    first_number = int(numbers_text.readline())
    second_number = int(numbers_text.readline())
    print(f"The Total of the first two number is {first_number + second_number} ")

with open("numbers.txt", 'r') as numbers_text:
    total = 0  # initialising variable
    for line in numbers_text:
        number_in_line = int(line)
        total = total + number_in_line
    print(f"The total of all numbers is {total}")
