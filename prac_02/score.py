"""
CP1404 | Practical 2: Scores | Tahlia Clennar
Program to determine score status and display random score
"""
import random


def main():
    """Provide result of user score and random score"""
    score = float(input("Enter score: "))
    print(get_score(score))

    random_score = random.randint(0, 100)
    print("Random Score: {}". format(random_score))
    print(get_score(random_score))


def get_score(score):
    """take user score and print result"""
    if score > 100 or score < 0:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
