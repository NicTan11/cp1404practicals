"""
CP1404 Practical
Basic list operations - numbers analysis and username checking
"""


def main():
    # Numbers exercise
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    # Username checking
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 
                'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 
                'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    
    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()

