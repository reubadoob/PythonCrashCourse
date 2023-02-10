filename = "text.txt"
with open(filename, 'r') as file:
    contents = file.read()
    word_count = contents.count('the')
    print(f"The word 'the' appears {word_count} times in the file {filename}")
