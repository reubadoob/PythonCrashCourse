while True:  # while loop will repeat until a 'break' statement is executed
    topping = input("Please enter the pizza topping you want or type 'quit' to exit: ")  # prompt user for topping
    if topping == 'quit':  # check if user entered 'quit'
        break  # if user entered 'quit' break out of loop
    else:  # if user did not enter 'quit'
        print("Adding " + topping + " to your pizza!")  # print a statement confirming the topping was added