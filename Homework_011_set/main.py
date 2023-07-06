import os
import functions

# users
# count users
# add user
# remove user
# error when full

maxUsers = 5
users = set()

os.system('cls')
print('start')

while True:
    functions.print_menu()
    choice = input('Enter your choice: ')
    print()

    if choice == '0':
        break
    elif choice == '1':
        functions.print_users(users)
    elif choice == '2':
        functions.print_count_users(users)
    elif choice == '3':
        functions.add_user(users, maxUsers)
    elif choice == '4':
        functions.remove_user(users)
    else:
        print('Invalid choice')

    input('Press Enter to continue ...')
    os.system('cls')

print('end')