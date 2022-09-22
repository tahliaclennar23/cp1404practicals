"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion | Tahlia Clennar
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # getting user input
        fahrenheit = float(input("Fahrenheit: "))
        # applying conversion formula
        celsius = 5 / 9 * (fahrenheit - 32)
        # displaying the value calculated
        print("Result: {:.2f} C".format(celsius))
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")