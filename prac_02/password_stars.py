"""
CP1404 | Practical 02: Menus | Tahlia Clennar
Program to ...
"""


def main():
    """main function"""

    # getting user input
    password = input("Enter Password: ")

    # setting minimum password length
    minimum_password_length = 8

    # error checking
    while len(password) < minimum_password_length:
        print("Password must be at least {} characters".format(minimum_password_length))

        # getting user input again
        password = input("Enter Password: ")

    # printing asterisks as long as word
    print('*' * len(password))


# main
main()
