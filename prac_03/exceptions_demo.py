"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

# ANSWERS:
# 1. ValueError will occur when the user enters something that cannot be converted to an integer,
#    such as a string (like "hello"), a float with decimal point (like "3.5"), or empty input.
# 2. ZeroDivisionError will occur when the user enters 0 as the denominator.
# 3. Yes, we can avoid ZeroDivisionError by checking if the denominator is 0 before performing the division.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    
    # Check for zero denominator to avoid ZeroDivisionError
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
        
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
