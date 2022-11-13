"""CP1404 Practical 7- Guitar class
Tahlia Clennar
"""

YEAR = 2022
VINTAGE_YEAR = 50


class Guitar:
    """Represent programming language."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise values"""
        self.name = name
        self.cost = cost
        self.year = year

    def __str__(self):
        """Return guitar details"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Return year less than other year"""
        return self.year < other.year

    def get_age(self):
        """Return age of guitar"""
        return YEAR - self.year

    def is_vintage(self):
        """Return true if guitar is 50 or more years old"""
        return self.get_age() >= VINTAGE_YEAR
