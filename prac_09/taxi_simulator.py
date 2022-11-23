"""
CP1404 Practical 9
Taxi simulator
Tahlia Clennar
"""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q(uit), c(hoose) taxi, d(rive)"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
        choice = input(">>> ").upper()

main()
