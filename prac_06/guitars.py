"""CP1404 Practical 6- Playing the Guitars(not really)
Tahlia Clennar
Estimated time: 20 minutes
Actual time:   minutes
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name}({year}) : {cost:,.2f} added.")
