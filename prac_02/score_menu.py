"""
CP1404 | Practical 2: Menu | Tahlia Clennar
Program to get a valid score and print result with stars
"""


def main():
    """main function"""
    # getting user input
    score = int(input("Enter score: "))
    # error checking
    while score > 100 or score < 0:
        print("Invalid score, enter score within range of 0-100")
        # getting user input again
        score = int(input("Enter score: "))
    # setting up menu
    menu = """
            P - Print score
            S- Print stars
            Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "P":
            print(get_score(score))
        elif choice == "S":
            print(print_stars(score))
        else:
            print_stars(score)
        print(menu)
        choice = input(">>> ").upper()


def get_score(score):
    """Function to take user's score and print result"""
    # conditional logic for user score

    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    """Print a number of asterisks equal to the length of the score"""
    print('*' * score)


main()
