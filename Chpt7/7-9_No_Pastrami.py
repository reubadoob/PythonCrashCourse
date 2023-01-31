# Start of code
sandwich_orders = ['pastrami', 'BLT', 'PB&J', 'pastrami', 'Turkey', 'Veggie', 'Grilled Cheese', 'pastrami']

# Print a message stating the deli has run out of pastrami
print("The deli has run out of pastrami")

# Use a while loop to remove all occurrences of 'pastrami' from 'sandwich_orders'
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Loop through the list of 'sandwich_orders' and print a message for each order
for sandwich in sandwich_orders: 
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

# Print a message listing each sandwich that was made
print("All sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)

# End of code