# Get user input
name = input("What is your name? ")

# Acknowledge user input
print(f"Hi {name}, it's great to meet you!")

# Write user name to 'guest.txt'
with open('guest.txt', 'w') as file_object:
    file_object.write(name + "\n")

# Append user name to 'guest_book.txt'
with open('guest_book.txt', 'a') as file_object:
    file_object.write(name + "\n")
