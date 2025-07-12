"""
Client program to test the ProgrammingLanguage class.

Estimated time: 10 minutes
"""

from programming_language import ProgrammingLanguage

# Create three ProgrammingLanguage objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Test the __str__ method
print(python)

# Create a list containing the three objects
languages = [python, ruby, visual_basic]

# Loop through and print names of dynamically typed languages
print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
