"""CP1404 Practical 7- My guitars
Tahlia Clennar"""
import csv
from prac_07.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""

    guitars = []

    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
        guitars.sort()
    in_file.close()

    for guitar in guitars:
        print(guitar)
    name = input("Name: ") #ignore pycharm warning
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name}({year}) : ${cost:,.2f} added.")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")
    guitars.sort()
    output_file = open("guitars.csv", 'w')
    for guitar in guitars:
        print(guitar)
        print(f"{guitar.name}, {guitar.year}, {guitar.cost}",
              file=output_file)
    output_file.close()
    print(f"{len(guitars)} guitars saved to guitars.csv")


main()
