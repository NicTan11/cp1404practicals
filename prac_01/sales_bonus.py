"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""Get sales number from user"""
sales = float(input("Enter sales: $"))

"""Loop until negative number is entered"""
while sales >= 0:
    if sales < 1000:
        bonus = 0.10 * sales
    else:
        bonus = 0.15 * sales

    print(f"Bonus: ${bonus: .2f}")
    """Ask for the next sales input"""
    sales = float(input("Enter sales: $"))

print("Thankyou")
