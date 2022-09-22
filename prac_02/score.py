"""
CP1404 | Practical 2: Scores | Tahlia Clennar
Program to determine score status and display random score
"""
import random


def main():
    """main function"""
    # getting user input
    score = float(input("Enter score: "))
    print(get_score(score))

    # getting random score
    random_score = random.randint(0, 100)
    print("Random Score: {}". format(random_score))
    print(get_score(random_score))


def get_score(score):
    """Function to take user's score and print result"""
    # conditional logic for user score
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
