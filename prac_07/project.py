"""
CP1404/CP5632 Practical
Project class for project management system
"""

import datetime


class Project:
    """Project class for storing and managing project information."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __repr__(self):
        """Return string representation of a Project."""
        return str(self)

    def __lt__(self, other):
        """Less than comparison for sorting projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Check if project is complete (100% completion)."""
        return self.completion_percentage >= 100

    def is_started_after(self, date):
        """Check if project starts after the given date."""
        return self.start_date > date

    def update_completion(self, new_percentage):
        """Update the completion percentage."""
        self.completion_percentage = new_percentage

    def update_priority(self, new_priority):
        """Update the priority."""
        self.priority = new_priority 