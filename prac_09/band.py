"""
CP1404 Practical 9
Band
Tahlia Clennar
"""


class Band:
    """Create band class"""

    def __init__(self, name=""):
        """Initialise a band class instance."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string with musicians"""
        return f"{self.name} ({','.join([musician.__str__() for musician in self.musicians])}"

    def add(self, instrument):
        """Add a musician to the band."""
        self.musicians.append(instrument)

    def play(self):
        """Return a string showing the musicians and their instruments."""
        if not self.musicians:
            return f"{self.name} needs an instrument!"
        return '\n'.join(([musician.play() for musician in self.musicians]))

