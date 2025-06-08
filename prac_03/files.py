# 1. Write name to a file using open/close
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
out_file.write(name)
out_file.close()

# 2. Read name from file using open/close and read()
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
print(f"Hi {name}!")

# 3. Read first two numbers from numbers.txt using with and readline()
with open("numbers.txt", 'r') as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4. Read all numbers from numbers.txt using with and for loop
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        total += int(line)
print(total) 