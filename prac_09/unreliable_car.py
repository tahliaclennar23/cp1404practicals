"""
CP1404 Practical 9
Tahlia Clennar
Unreliable Car
"""
from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Class that inherits from Car"""

    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car if random number is less than car's reliability."""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
            distance_travelled = super().drive(distance)
            return distance_travelled
