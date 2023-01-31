sandwich_orders = ['BLT', 'PB&J', 'Turkey', 'Veggie', 'Grilled Cheese']

finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich")
    finished_sandwiches.append(sandwich)

print("All sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)