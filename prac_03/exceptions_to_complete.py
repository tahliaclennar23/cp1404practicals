"""
Tahlia Clennar
CP1404 Practical 03
Program to get valid integer from user
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
# safe to ignore 'undefined value' error
