"""CP1404 Practical 6- programming language and languages
Tahlia Clennar
Estimated time: 30 minutes
Actual time: 23 minutes
"""


class ProgrammingLanguage:
    """Represent programming language."""

    def __init__(self, name="", typing="", reflection=False, year=0):
        """Initialise values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Provide coding information"""
        return f"{self.name}, {self.typing} Typing, Reflection= {self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """See if typing is dynamic"""
        return self.typing == "Dynamic"
