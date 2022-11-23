"""
CP1404 Practical 9
Silver service taxi
Tahlia Clennar
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness
        self.fanciness = fanciness
