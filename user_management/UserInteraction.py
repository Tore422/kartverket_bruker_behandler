class UserInteraction:

    @staticmethod
    def ask_user_what_operation_to_perform():
        print("What action would you like to perform?")
        print(("1: List all registered users.\n"
            "2: Register a new user.\n"
            "3: Search for registered users matching search criteria.\n"
            "4: Delete a registered user."))
        user_selection = input(("Please input a number between 1 and 4, "
                                "or q to quit: "))
        # Prevents out of bounds exception if no input is provided
        user_selection = user_selection + " "  
        return user_selection[0]

