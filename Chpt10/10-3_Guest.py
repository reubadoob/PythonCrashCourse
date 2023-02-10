# Prompt user for their name
name = input("What is your name? ")

# Acknowledge user input
print(f"Hi {name}! Thank you for entering your name.")

# Write user name to a file
with open("guest.txt", "w") as file:
    file.write(name)