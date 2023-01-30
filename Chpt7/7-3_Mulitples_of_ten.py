tens = input("Give me a number!")
tens = int(tens)

if tens % 10 == 0:
    print(f"\nThe number {tens}, you have provided is divisible by 10")
else:
    print(f"\n {tens} is not divisible by 10")