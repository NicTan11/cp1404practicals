"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Valid integer was entered, so we can finish
    except ValueError:  # Catch ValueError when non-integer input is entered
        print("Please enter a valid integer.")
print("Valid result is:", result)
