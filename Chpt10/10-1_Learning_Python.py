# read the file 'learning_python.txt'
filename = 'learning_python.txt'

# 1. Print the contents of 'learning_python.txt' 3 times
with open(filename) as file_object:
    contents = file_object.read()
    print(contents * 3)

# 2. Print the contents of 'learning_python.txt' by reading the entire file
with open(filename) as file_object:
    print(file_object.read())

# 3. Print the contents of 'learning_python.txt' by looping over the file object
with open(filename) as file_object:
    for line in file_object:
        print(line)

# 4. Print the contents of 'learning_python.txt' by storing the lines in a list and then working with them outside the 'with' block
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line)
