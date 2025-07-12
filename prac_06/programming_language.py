"""
ProgrammingLanguage class for storing programming language information.

Estimated time: 15 minutes
"""


class ProgrammingLanguage:
    """A class to represent a programming language with its characteristics."""
    
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    
    def is_dynamic(self):
        """Return True if the language is dynamically typed, False otherwise."""
        return self.typing == "Dynamic"
    
    def __str__(self):
        """Return a string representation of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
