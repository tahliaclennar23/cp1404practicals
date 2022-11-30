"""
CP1404 Practical 9
Silver service taxi test
Tahlia Clennar
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test silver service taxi class"""
    silver_service_taxi = SilverServiceTaxi("Silver service taxi", 85, 5)
    print(
        f"{silver_service_taxi.name}, fuel = {silver_service_taxi.fuel}, {silver_service_taxi.current_fare_distance}"
        f" on current fare, ${silver_service_taxi.price_per_km} plus"
        f" flagfall of ${silver_service_taxi.flagfall} ")


main()
