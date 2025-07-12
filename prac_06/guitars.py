"""
Main program for managing a collection of guitars.

Estimated time: 15 minutes
"""

from guitar import Guitar

guitars = []

print("My guitars!")

# User input version
while True:
    name = input("Name: ")
    if name == "":
        break
    
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{guitar} added.\n")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

print("... snip ...")
print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
