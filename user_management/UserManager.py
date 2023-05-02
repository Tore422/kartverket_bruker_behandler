from User import User
from UserInteraction import UserInteraction
from DatabaseHandler import *

def register_user_in_the_database(user):
    names = ["name", "date_of_birth", "phone_number", "email_address"]
    value_types = ["%s", "%s", "%s", "%s"]
    values = [user.name, user.date_of_birth, user.phone_number, 
            user.email_address]
    try:
        insert_into_table(TABLE_NAME, names, value_types, values)
    except:
        print("Something went wrong while trying to register "\
              "the user in the database.")
        raise
    else:
        print("Successfully registered the user in the database.")

def perform_selected_operation(selected_operation):
    if int(selected_operation) == 1:
        for user in get_all_rows_from_database(TABLE_NAME):
            print(user)
    elif int(selected_operation) == 2:
        register_user_in_the_database(user2)
    elif int(selected_operation) == 3:
        # Retrieve users from database matching search criteria
        print("option 3")
    else:
        # Delete user from database matching criteria
        print("option 4")

def start_program():
    done = False
    while not done:
        print("")  # Separates the console output to make it easier to read
        selected_operation = UserInteraction.ask_user_what_operation_to_perform()
        if selected_operation == "q":
            done = True
        elif selected_operation.isdigit() and int(selected_operation) in\
            range(1,5):
            perform_selected_operation(selected_operation)
        else:
            print(("Did not recognize user input, please try again "
                "or press q to quit."))


user1 = User("John Smith", "01.01.1999", "12 34 56 78", "smith@mymail.com")
user2 = User("Ola Nordmann", "22.06.2002", "15 34 56 79", "ola@mymail.com")

DATABASE_NAME = "mytestdatabase"
TABLE_NAME = "users"

start_program()
