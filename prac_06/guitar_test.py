"""
Test program for the Guitar class.

Estimated time: 10 minutes
"""

from guitar import Guitar
import datetime

# Create test guitars
gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 1000.00)

# Test get_age() method
current_year = datetime.datetime.now().year
expected_gibson_age = current_year - 1922
expected_another_age = current_year - 2013

print(f"Gibson L-5 CES get_age() - Expected {expected_gibson_age}. Got {gibson.get_age()}")
print(f"Another Guitar get_age() - Expected {expected_another_age}. Got {another_guitar.get_age()}")

# Test is_vintage() method
expected_gibson_vintage = expected_gibson_age >= 50
expected_another_vintage = expected_another_age >= 50

print(f"Gibson L-5 CES is_vintage() - Expected {expected_gibson_vintage}. Got {gibson.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected {expected_another_vintage}. Got {another_guitar.is_vintage()}")

# Test __str__ method
print(f"\nString representation test:")
print(f"Gibson: {gibson}")
print(f"Another Guitar: {another_guitar}") 