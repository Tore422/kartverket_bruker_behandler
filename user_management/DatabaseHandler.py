import mysql.connector

from user_management.User import User

def create_database(database_name):
    mycursor.execute("CREATE DATABASE " + database_name)

def use_database(database_name):
    mycursor.execute("USE " + database_name)

def show_databases():
    mycursor.execute("SHOW DATABASES")

def drop_table(table_name):
    mycursor.execute("DROP TABLE " + table_name)

def show_tables():
    mycursor.execute("SHOW TABLES")

def insert_into_table(table_name, column_names, column_value_types, values):
    sql = "INSERT INTO " + table_name + " ("
    for name in column_names:
        sql = sql + name + ", "
    sql = sql[:-2] + ") VALUES ("
    for value_type in column_value_types:
        sql = sql + value_type + ", "
    sql = sql[:-2] + ")"
    mycursor.execute(sql, values)
    mydb.commit()

def create_table(table_name, column_names, column_value_types):
    sql = "CREATE TABLE " + table_name + " ("
    for name, value_type in zip(column_names, column_value_types):
        sql = sql + name + " " + value_type + ", "
    sql = sql[:-2] + ")"
    mycursor.execute(sql)














mydb = mysql.connector.connect(
    host = "localhost",
    user = "user",
    password = "password"
)


mycursor = mydb.cursor()

database_name = "mytestdatabase"
use_database(database_name)

table_name = "users"
column_names = ["id", "name", "date_of_birth", "phone_number", 
                "email_address"]
DATABASE_TYPE_VARCHAR = "VARCHAR(255)"
column_value_types = ["INT AUTO_INCREMENT PRIMARY KEY", 
                      DATABASE_TYPE_VARCHAR, DATABASE_TYPE_VARCHAR, 
                      DATABASE_TYPE_VARCHAR, DATABASE_TYPE_VARCHAR]
create_table(table_name, column_names, column_value_types)

user1 = User("John Smith", "01.01.1999", "12 34 56 78", "smith@mymail.com")
names = ["name", "date_of_birth", "phone_number", "email_address"]
value_types = ["%s", "%s", "%s", "%s"]
values = [user1.name, user1.date_of_birth, user1.phone_number, 
          user1.email_address]
#insert_into_table("users", names, value_types, values)
#print(mycursor.rowcount, "record inserted.")
#print("1 record inserted, ID:", mycursor.lastrowid)











