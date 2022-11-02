"""CP1404 Practical 6- Playing the Guitars(not really)
Tahlia Clennar
Estimated time: 20 minutes
Actual time: 27 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Use guitar class to get details of guitars, and add to list and print details"""
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print(f"{name}({year}) : {cost:,.2f} added.")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")

    print("These are my guitars:")
    if guitars:
        max_guitar_name_length = max(len(guitar.name) for guitar in guitars)
        for i, guitar in enumerate(guitars, 1):
            vintage = "(vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>{max_guitar_name_length}} ({guitar.year}),"
                  f"worth ${guitar.cost:10,.2f}{vintage}")
    else:
        print("No guitars")


main()
