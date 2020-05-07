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

def create_userz(telegram_id):
    create_users = """
        INSERT INTO
          `users` (`telegram_id`)
        VALUES
          ('""" + str(telegram_id) + """');
                    """
    execute_query(connection, create_users)

def couunt_users():
    count = "SELECT COUNT(*) FROM `users`"
    counts = execute_read_query(connection, count)
    counts = str(counts)
    counts = counts[2]
    counts = int(counts)
    return counts

def count_is(telegram_id):
    gg = """SELECT telegram_id = """ + str(telegram_id) + """
            FROM history_likes
            GROUP BY telegram_id
            HAVING count(distinct id)=1"""
    zxc = execute_read_query(connection, gg)
    zxc = str(zxc)
    return zxc

def count_is_HH(telegram_id):
    gg = """SELECT telegram_id = """ + str(telegram_id) + """
            FROM users
            GROUP BY telegram_id
            HAVING count(distinct id)=1"""
    zxc = execute_read_query(connection, gg)
    zxc = str(zxc)
    return zxc

def now_is(telegram_id):
    select_users = "SELECT * FROM `users` WHERE `telegram_id` = '" + str(telegram_id) + "'"
    users = str(execute_read_query(connection, select_users))
    users = users.split(',')  #2 это now
    users = users[2]
    users = users[1]
    users = int(users)
    return users


def update_now(telegram):
        update_post_description = "UPDATE `users` SET now = now + 1 WHERE telegram_id = " + str(telegram)

        execute_query(connection,  update_post_description)

def update_zero(telegram):
    update_post_description = "UPDATE `users` SET now = 0 WHERE telegram_id = " + str(telegram)

    execute_query(connection,  update_post_description)

def go_like(telegram,id_post):
        create_users = """
            INSERT INTO
              `history_likes` (`telegram_id`,`history_id`)
            VALUES
              (""" + str(telegram) + """,""" + str(id_post) +  """);
                        """
        execute_query(connection, create_users)

def like_is():
    gg = "SELECT* FROM `history_likes` HAVING COUNT(*) = 1"
    zxc = execute_read_query(connection, gg)
    zxc = str(zxc)
    return zxc

ggq = "SELECT `history_text` FROM `history_list` "
hax = execute_read_query(connection, ggq)
def couunt():
    count = "SELECT COUNT(*) FROM `history_list`"
    counts = execute_read_query(connection, count)
    counts = str(counts)
    counts = counts[2]
    counts = int(counts)
    return counts
