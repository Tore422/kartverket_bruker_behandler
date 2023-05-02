# Kartverket bruker behandler (Work in progress)


A simple Python program for managing users through a Command Line Interface (CLI).<br>
The program interacts with a MySQL database for persistent data storage of registered users.


## How to use

Start the program by calling the UserManager.py file through the command line.

The user is presented with operations that can be performed
* Listing all registered users
* Registering a new user
* Search for registered users matching search criteria
* Delete a registered user
* or pressing 'q' to quit the application


## Todo list

* Connect the program and the database
  * Need to convert user data to format valid for the database (not just VARCHAR)
  * Need to retrieve rows from database
* Implement code for creating a new user through the CLI
* Implement code for deleting a user through the CLI
  * Need to search amongst registered users
* Implement code for searching users matching criteria
  * Requires implementing code for querying the database for specific rows
  
