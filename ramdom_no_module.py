import random

# Define the specified numbers
numbers = [-1, 0, 1]

# Generate a random choice from the specified numbers
random_number = random.choice(numbers)

print(random_number)

#1 - Generating a random float between 0.0 and 1.0:
import random

random_float = random.random()
print(random_float)

#2 - Generating a random integer within a specified range:
import random

random_integer = random.randint(1, 10)  # Generates a random integer between 1 and 10 (inclusive)
print(random_integer)

#3 - Generating a random float within a specified range:
import random

random_float_range = random.uniform(1.0, 10.0)  # Generates a random float between 1.0 and 10.0
print(random_float_range)

#4 - Choosing a random element from a list:
import random

items = ['apple', 'banana', 'cherry']
random_choice = random.choice(items)
print(random_choice)

#5 - Shuffling a list randomly:
import random

items = [1, 2, 3, 4, 5]
random.shuffle(items)  # Shuffles the list in place
print(items)

#6 - Generating a list of random numbers:
import random

random_numbers = [random.randint(1, 100) for _ in range(10)]  # Generates a list of 10 random integers between 1 and 100
print(random_numbers)

