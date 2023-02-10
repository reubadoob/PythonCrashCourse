try:
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter another number: "))

except ValueError:
    print("Invalid input. Please enter a number.")
else:
    result = num1 + num2
print(f"The result of adding the two numbers is: {result}")
