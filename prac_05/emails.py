"""
Tahlia Clennar
CP1404 Practical 05- Emails
Program to store user's emails and names in a dictionary.
Estimate:45 minutes

"""
email = input("Enter email: ")
name_email_list = []
while email != "":
    name_email_list = email.split("@")
    name = name_email_list[0].title()
    name = name.replace(".", " ")
    print(name)
    email = input("Enter email: ")

