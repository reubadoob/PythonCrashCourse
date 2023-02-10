# Try-except block to handle file not found error
try:
    # Opening 'cats.txt' file
    with open("cats.txt") as file_object:
        contents = file_object.read()
        print(contents)

    # Opening 'dogs.txt' file
    with open("dogs.txt") as file_object:
        contents = file_object.read()
        print(contents)

# Exception handling for file not found error
except FileNotFoundError:
    print("One or both of the files were not found.")
