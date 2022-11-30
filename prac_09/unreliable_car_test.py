"""
CP1404 Practical 9
Unreliable car test
Tahlia Clennar
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test Unreliable car class"""
    car = UnreliableCar("Not reliable", 100, 50)
    car = UnreliableCar("Silver service taxi", 85, 5)
    print(f"{car.name} drove {car.drive(10)} km")


main()
