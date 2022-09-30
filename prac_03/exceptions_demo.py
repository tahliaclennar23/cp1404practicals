"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the numerator and denominator aren't valid numbers
2. When will a ZeroDivisionError occur? When the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
valid_input = False
while not valid_input:

    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            valid_input = True
            print("Cannot divide by zero!")
        else:
            fraction = numerator / denominator
            print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Finished.")
    valid_input = True
