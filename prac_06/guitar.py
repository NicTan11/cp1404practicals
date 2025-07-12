"""
Guitar class for storing guitar information.

Estimated time: 20 minutes
"""

import datetime


class Guitar:
    """A class to represent a guitar with its characteristics."""
    
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost
    
    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
    
    def get_age(self):
        """Return the age of the guitar in years."""
        current_year = datetime.datetime.now().year
        return current_year - self.year
    
    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50 