"""
Tahlia Clennar
CP1404 Practical 03- Files
Program to read and write to files
"""
FILE_NAME = "name.txt"
with open(FILE_NAME, 'w') as name_txt:
    name = input("Enter your name: ")
    print(f"{name}", file=name_txt)
with open(FILE_NAME, 'r') as name_txt:
    text = name_txt.read()
    print(f"Your name is {text}")

