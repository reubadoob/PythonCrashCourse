current_users = ['admin', 'alice', 'ALICE', 'bob', 'charlie', 'denise']
new_users = ['eric', 'frank', 'geoff', 'alice', 'ALICE']

for new_user in new_users:
    if new_user in current_users:
        print(f"\nUsername '{new_user}' is taken. Please provide a new user name")
    else:
        print(f"\nUsername'{new_user}' is available!")
