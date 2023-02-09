import random

# A list of 10 numbers and 5 letters
numbers_letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

# A list to hold the randomly selected 4 numbers or letters
my_ticket = [0, 'a', 2, 'c']

# A variable to keep track of the number of times the loop runs
num_loops = 0

# Keep running the loop until the randomly generated string matches 'my_ticket'
while True:
    # Increment the number of loops every time the loop runs
    num_loops += 1

    # Randomly select 4 numbers or letters from 'numbers_letters'
    random_ticket = random.sample(numbers_letters, 4)

    # Check if the randomly generated ticket matches 'my_ticket'
    if random_ticket == my_ticket:
        break

# Print a message reporting the number of times the loop had to run to match 'my_ticket'
print(f"It took {num_loops} loops to generate a match for my ticket: {my_ticket}")
