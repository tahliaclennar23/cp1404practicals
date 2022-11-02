"""CP1404 Practical 6- Testing
Tahlia Clennar
Estimated time: 15 minutes
Actual time:  minutes
"""
from prac_06.guitar import Guitar


def run_guitar_tests():
    """Test previous guitar class"""
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.4

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another guitar", 2013, 5000)
