YEAR = 2022


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

    def get_age(self):
        """Return age of guitar"""
        return YEAR - self.year

