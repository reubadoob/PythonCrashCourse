# read the file 'learning_python.txt'
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.replace('Python', 'Ruby') * 3)

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace('Python', 'Ruby'))
