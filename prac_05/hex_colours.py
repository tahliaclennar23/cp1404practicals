"""
Tahlia Clennar
CP1404 Practical 05- Hexadecimal colour codes
Program to look up Hexadecimal colour codes from dictionary
"""

colour_to_code = {"absolute zero": "#0048ba", "acid green": "#bobf1a", "aliceblue": "fof8ff", "amber": "#ffbf00",
                  "aqua": "#00ffff", "black": "#000000", "cobalt": "#0047ab", "coral": "#ff7f50", "crystal": "#a7d8de",
                  "denim": "#1560bd"}

colour = input("Colour: ").lower()
while colour != "":
    try:
        print(colour, "is", colour_to_code[colour])
    except KeyError:
        print("Invalid short state")
    colour = input("Colour: ").lower()
