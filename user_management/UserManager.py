from User import User
from UserInteraction import UserInteraction
from DatabaseHandler import *



    








user1 = User("John Smith", "01.01.1999", "12 34 56 78", "smith@mymail.com")
user2 = User("Ola Nordmann", "22.06.2002", "15 34 56 79", "ola@mymail.com")

users = []

users.append(user1)
users.append(user2)

for user in users:
    print(user)


DATABASE_NAME = "mytestdatabase"
TABLE_NAME = "users"


done = False
while not done:
    selected_operation = UserInteraction.ask_user_what_operation_to_perform()
    if selected_operation == "q":
        done = True
    elif selected_operation.isdigit() and int(selected_operation) in\
        range(1,5):
        print("was valid")
        if int(selected_operation) == 1:
            for user in get_all_rows_from_database(TABLE_NAME):
                print(user)
        elif int(selected_operation) == 2:
            # Create a new user and register in database if possible
            print("option 2")
        elif int(selected_operation) == 3:
            # Retrieve users from database matching search criteria
            print("option 3")
        else:
            # Delete user from database matching criteria
            print("option 4")
    else:
        print(("Did not recognize user input, please try again "
            "or press q to quit.\n"))





