"""
CP1404 Practical 9
Unreliable Car
"""
from prac_09.car import Car


class UnreliableCar(Car):
    """Class that inherits from Car"""
    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance."""
        super().__init__(name, fuel)
        self.reliability = reliability
