import mysql.connector

from User import User

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

def get_all_rows_from_database(table_name):
    mycursor.execute("SELECT * FROM " + table_name)
    users = mycursor.fetchall()
    return users

def get_rows_from_database_matching_condition(table_name, column_name,
                                              filter_value):
    sql = "SELECT * FROM " + table_name + " WHERE " + column_name \
    + "='" + filter_value + "'"
    mycursor.execute(sql)
    users = mycursor.fetchall()
    return users
    










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
#create_table(table_name, column_names, column_value_types)

#print(mycursor.rowcount, "record inserted.")
#print("1 record inserted, ID:", mycursor.lastrowid)










