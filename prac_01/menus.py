"""
CP1404 | Practical 01: Menus | Tahlia Clennar
Program to make menus by combining looping with selection
"""
# getting user input
name = input("Enter name: ")

# setting up menu
MENU = """H - Hello "name"
G - Goodbye "name"
Q - Quit"""
print(MENU)

# getting choice & treating as upper case letter
choice = input(">>> ").upper()

# conditional logic for handling choice
while choice != "Q":
    if choice == "H":
        print("Hello: {}".format(name))
    elif choice == "G":
        print("Goodbye: {}".format(name))
    else:
        print("Invalid message")

# displaying menu again
    print(MENU)
    choice = input(">>> ").upper()
print("Finished")







