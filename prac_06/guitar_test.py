"""CP1404 Practical 6- Testing
Tahlia Clennar
Estimated time: 15 minutes
Actual time:  minutes
"""
YEAR = 2022
from prac_06.guitar import Guitar


def run_guitar_tests():
    """Test previous guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.4

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another guitar", 2013, 5000)
    print(f"{guitar.name} get_age() - Expected {YEAR - year}. Got {YEAR - guitar.year}")
    print(f"{another_guitar.name} get_age ()- Expected {YEAR - 2000}. Got {YEAR - another_guitar.year}")
    print(f"{guitar.name} is_vintage()- Expected {True}. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected {False}. Got {another_guitar.is_vintage()}")
