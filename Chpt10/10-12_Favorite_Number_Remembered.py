import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
print("I know your favorite number! It is " + str(favorite_number))
