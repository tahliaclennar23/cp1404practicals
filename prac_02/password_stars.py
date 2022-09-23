"""
CP1404 | Practical 02: Password Check with Functions | Tahlia Clennar
Program to get password and error check for suitable length
"""


def main():
    """Check if password entered is suitable"""
    minimum_password_length = 8
    password = get_password(minimum_password_length)
    print_asterisks(password)


def get_password(minimum_password_length):
    """Get password and check if password is valid length"""
    password = input("Enter Password: ")
    while len(password) < minimum_password_length:
        print("Password must be at least {} characters".format(minimum_password_length))
        password = input("Enter Password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to length of password"""
    print('*' * len(password))


main()
