filename = 'reasons.txt'

with open(filename, 'a') as file_object:
    while True:
        reason = input("Why do you like programming? (Enter 'q' to quit)")
        if reason == 'q':
            break
        file_object.write(reason + '\n')

print("Thanks for your responses. They have been added to the file.")
