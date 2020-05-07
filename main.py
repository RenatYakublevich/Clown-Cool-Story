import telebot
from telebot import types
import test_main
import time
import re
import os
import test2
import mysql.connector
from mysql.connector import Error


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
        print("The error '{e}' occurred")

bot = telebot.TeleBot('токен')



@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton('📖Прочитать истории')
    item2 = types.KeyboardButton('📚Добавить свою историю')
    item3 = types.KeyboardButton('👨‍🔧О создателе')
    markup.add(item1,item2,item3)
    test2.create_userz(message.chat.id)
    gg = 'Привет, <b>' + message.from_user.first_name.title() + '</b>!\nХочешь прочитать или добавить кринжовую историю про себя или своего друга? Тогда тебе к нам\nНу что,поехали?)😏'.format(message.from_user, bot.get_me())
    bot.send_message(message.chat.id,gg,parse_mode='html',reply_markup=markup)
    bot.send_photo(message.chat.id, 'https://sun2.beltelecom-by-minsk.userapi.com/f0FkFdMP8XEOP54pAnoCSulnaqljjWJjoflD1w/48MQhmk4-5s.jpg')




@bot.message_handler(content_types=['text'])
def crypto_price_telegram(message):
    if message.chat.type == 'private':
        if message.text == '📖Прочитать истории':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
            item2 = types.KeyboardButton('Назад')
            item3 = types.KeyboardButton('Следующая история')
            item4 = types.KeyboardButton('👍Поставить лайк')

            markup.add(item2,item3,item4)


            bot.send_message(message.chat.id, test2.hax[test2.now_is(message.chat.id)] ,reply_markup=markup)
        if message.text == 'Следующая история':
            if int(test2.now_is(message.chat.id)) == (test2.couunt() - 1):
                test2.update_zero(message.chat.id)
                bot.send_message(message.chat.id, test2.hax[test2.now_is(message.chat.id)])
            else :
                test2.update_now(message.chat.id)
                print(test2.now_is(message.chat.id))
                bot.send_message(message.chat.id, test2.hax[test2.now_is(message.chat.id)])
        if message.text == 'Назад':
            welcome(message)
            test2.update_zero(message.chat.id)
        if message.text == '📚Добавить свою историю':
            bot.send_message(message.chat.id, 'Для добавления истории перейди на сайт и <b>поделись своей кул стори со всем миром аблсолютно анонимно!</b>\n\nhttps://cutt.ly/LylMio5',parse_mode='html')

        if message.text == '👨‍🔧О создателе':
            bot.send_message(message.chat.id, 'Создатель - Якублевич Ренат\nGithub - https://github.com/RenatYakublevich\nСотрудничество - https://vk.com/helloworldbastard')
        if message.text == '👍Поставить лайк':
            test2.go_like(message.chat.id,test2.now_is(message.chat.id) + 1)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'like':

                test2.go_like(message.chat.id,test2.now_is(message.chat.id))
                # remove inline buttons
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спасибо тебе за твою активность!😇",
                reply_markup=None)

    except Exception as e:
        print(repr(e))






bot.polling(none_stop=True)
