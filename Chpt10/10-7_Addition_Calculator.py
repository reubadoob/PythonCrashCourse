# Continuously prompt user for 2 numbers
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("The result is: ", result)
        break
    except ValueError:
        print("Error: Invalid input. Please enter numbers only.")
