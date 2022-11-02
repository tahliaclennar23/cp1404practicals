"""CP1404 Practical 6- programming language and languages
Tahlia Clennar
Estimated time: 30 minutes
Actual time:
"""


class ProgrammingLanguage:
    """Represent programming language."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
