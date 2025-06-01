"""
Menu-driven program for score operations
"""

def main():
    """Main program with menu."""
    print("Welcome to the Score Menu Program")
    score = get_valid_score()
    
    MENU = """Menu:
G - Get a valid score
P - Print result
S - Show stars
Q - Quit"""
    
    choice = ""
    while choice.upper() != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(f"Result: {determine_score_result(score)}")
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Farewell! Thanks for using the Score Menu Program")
        else:
            print("Invalid choice")
        print()


def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score (0-100): "))
    return score


def print_stars(score):
    """Print as many stars as the score value."""
    print("*" * int(score))

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
    
main()