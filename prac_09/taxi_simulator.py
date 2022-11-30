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
    current_taxi = None
    total_cost = 0
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available: ")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                travel_distance = float(input("Drive how far? "))
                current_taxi.drive(travel_distance)
                cost = current_taxi.get_fare()
                total_cost += cost
                print(f"Your {current_taxi.name} trip cost you ${cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid choice")
        print(f"Bill to date: ${total_cost:.2f}")
        print(MENU)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
