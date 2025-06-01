"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def determine_score_result(score):
    """
    Determine the result based on the score.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    # Get user's score and print result
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"Result: {result}")

    # Generate random score and print result
    random_score = random.uniform(0, 100)
    random_result = determine_score_result(random_score)
    print(f"\nRandom score: {random_score:.1f}")
    print(f"Result: {random_result}")


main()
