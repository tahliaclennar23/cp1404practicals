"""
CP1404 | Practical 1: Debugging | Tahlia Clennar
Broken program to determine score status
"""


def main():
    """main function"""
    # getting user input
    score = float(input("Enter score: "))
    # conditional logic for user score
    if score > 100 or score < 0:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
