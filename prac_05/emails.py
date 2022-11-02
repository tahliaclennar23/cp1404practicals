"""
Tahlia Clennar
CP1404 Practical 05- Emails
Program to store user's emails and names in a dictionary.
Estimate:45 minutes
Actual time: 1 hour (with breaks)

"""


def main():
    """ Get email as input and extract name"""
    email = input("Enter email: ")
    email_to_name = {}
    while email != "":
        name = extract_name(email)
        email_to_name[email] = name
        correct_name = input(f"Is your name {name}? (Y/n): ")
        if correct_name.upper() != 'Y' and correct_name.upper() != '':
            name = input("Name: ")
            email_to_name[email] = name
        email = input("Enter email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name in proper format"""
    name_email_list = email.split("@")
    name = name_email_list[0].title()
    name = name.replace(".", " ")
    return name


main()
