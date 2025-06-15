"""
CP1404 Practical
Quick Pick Program - Lottery Ticket Generator
"""
import random

NUMBERS_PER_QUICK_PICK = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Generate random quick picks based on user input."""
    number_of_quick_picks = int(input("How many quick picks? "))
    
    for i in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        # Format the numbers with width of 3 for neat alignment
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate a single quick pick of unique random numbers in sorted order."""
    numbers = []
    while len(numbers) < NUMBERS_PER_QUICK_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in numbers:
            numbers.append(number)
    return sorted(numbers)


main()
