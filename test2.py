import mysql.connector
from mysql.connector import Error
import telebot

def be_ready(mod):
    if mod == 1:
        return True
    elif mod == 2:
        return False


def message_plus():
    if message.text[0] == '+':
        return True


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection
connection = create_connection("localhost", "mysql", "mysql","history_list")

def execute_query(connection, query):
     cursor = connection.cursor()
     try:
         cursor.execute(query)
         connection.commit()
         print("Query executed successfully")
     except Error as e:
         print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")




select_users = "SELECT `history_text` from `history_list`"
users = execute_read_query(connection, select_users)

count = "SELECT COUNT(*) FROM `history_list`"
counts = execute_read_query(connection, count)
counts = str(counts)
counts = counts[2]
counts = int(counts)
now = 0
