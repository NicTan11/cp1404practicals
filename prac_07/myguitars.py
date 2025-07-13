"""
CP1404/CP5632 Practical
Guitar Management Program - reads guitars from CSV, displays them, sorts by year, 
allows user input for new guitars, and saves back to CSV.
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main function to orchestrate the guitar management program."""
    print("My Guitars!")
    
    # Load guitars from file
    guitars = load_guitars(FILENAME)
    
    # Display guitars
    print("\nThese are my guitars:")
    display_guitars(guitars)
    
    # Sort guitars by year and display
    guitars.sort()
    print("\nThese are my guitars sorted by year (oldest to newest):")
    display_guitars(guitars)
    
    # Get new guitars from user
    print("\nEnter your new guitars (blank name to finish):")
    new_guitars = get_new_guitars()
    
    # Add new guitars to the list
    guitars.extend(new_guitars)
    
    # Save all guitars to file
    save_guitars(FILENAME, guitars)
    
    print(f"\n{len(guitars)} guitars saved to {FILENAME}")


def load_guitars(filename):
    """Load guitars from CSV file and return list of Guitar objects."""
    guitars = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                # Format: Name,Year,Cost
                if len(row) == 3:
                    name = row[0]
                    year = int(row[1])
                    cost = float(row[2])
                    guitar = Guitar(name, year, cost)
                    guitars.append(guitar)
    except FileNotFoundError:
        print(f"File {filename} not found. Starting with empty guitar list.")
    except ValueError as e:
        print(f"Error reading file: {e}")
    
    return guitars


def display_guitars(guitars):
    """Display a list of guitars in a formatted way."""
    if not guitars:
        print("No guitars to display.")
        return
    
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar}{vintage_string}")


def get_new_guitars():
    """Get new guitars from user input and return list of Guitar objects."""
    guitars = []
    
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
            
        # Get year with validation
        while True:
            try:
                year = int(input("Year: "))
                break
            except ValueError:
                print("Invalid input; enter a valid number")
        
        # Get cost with validation
        while True:
            try:
                cost = float(input("Cost: $"))
                break
            except ValueError:
                print("Invalid input; enter a valid number")
        
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
    
    return guitars


def save_guitars(filename, guitars):
    """Save guitars to CSV file."""
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for guitar in guitars:
                writer.writerow([guitar.name, guitar.year, guitar.cost])
    except IOError as e:
        print(f"Error saving file: {e}")


if __name__ == "__main__":
    main()
