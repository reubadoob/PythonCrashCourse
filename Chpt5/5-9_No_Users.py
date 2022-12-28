users_list = []
if users_list:
    for user in users_list:
        if user == 'admin':
            print("Hello Admin! Would you like a system update?")
        else:
            print(f"Hello {user.title()} what can I help you with today")
else:
    print("The user list is empty! We need users!")
