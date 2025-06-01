def main():
    """Main program that gets a password and prints asterisks."""
    password = get_password()
    print_asterisks(password)


def get_password():
    """Get and validate the user's password."""
    minimum_length = 8
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long")
        password = input("Enter password: ")
    return password


def print_asterisks(password, symbol='*'):
    """Print a line of symbols with the same length as the password."""
    print(symbol * len(password))


main()
