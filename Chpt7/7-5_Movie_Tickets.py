# Welcome message
print("Welcome to the movie theater!")

# Loop to repeatedly ask for age input until a valid age is entered
while True:
    # Get age input from user
    age = int(input("Please enter your age: "))

    # Check if age is less than 3 and print ticket cost
    if age < 3:
        print("Your ticket is free.")
        break
    # Check if age is between 3 and 12 inclusive and print ticket cost
    elif age >= 3 and age <= 12:
        print("Your ticket costs $10.")
        break
    # Check if age is greater than 12 and print ticket cost
    elif age > 12:
        print("Your ticket costs $15.")
        break

# Thank you message
print("Thank you for choosing our theater!")