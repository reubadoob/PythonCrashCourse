import json

# read the favorite number from the file
with open('fav_num.txt', 'r') as file:
    fav_num = json.load(file)

# print the message
print(f"I know your favorite number! It is {fav_num}")
