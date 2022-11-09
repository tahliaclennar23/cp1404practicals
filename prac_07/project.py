"""CP1404 Practical 7- Project
Tahlia Clennar
Time started: 8.15am
Estimated time: 1 hour
Actual time:
"""


class Project:
    """Represent Project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise values"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Provide project information"""
        return f"{self.name}, Start Date {self.start_date}, Priority {self.priority}, Cost Estimate ${self.cost_estimate}, " \
               f"Completion Percentage {self.completion_percentage}%"

    def complete_project(self):
        """See if the project is complete"""
        return self.completion_percentage == 100

    def __lt__(self, other):
        """Allows priority sorting"""
        return self.priority < other.priority
