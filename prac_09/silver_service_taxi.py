"""
CP1404 Practical 9
Silver service taxi
Tahlia Clennar
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Class that inherits from taxi class"""
    flagfall = 4.50

    def __init__(self, name, fuel, odometer, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness
        self.fanciness = fanciness
        self.current_fare_distance = 0

    def get_fare(self):
        """Return the price for the taxi trip."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus" \
               f"flagfall of ${self.flagfall}"
