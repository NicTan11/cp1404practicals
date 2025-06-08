import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1?
# I saw random integers between 5 and 20
# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20 (inclusive)

# What did you see on line 2?
# I saw random odd numbers: 3, 5, 7, 9
# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4?
# No, because the step value of 2 means it only produces odd numbers starting from 3: 3, 5, 7, 9

# What did you see on line 3?
# I saw random floating-point numbers between 2.5 and 5.5
# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5

# Write code to produce a random number between 1 and 100 inclusive
print(random.randint(1, 100))
