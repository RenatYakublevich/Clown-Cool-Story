import telebot
from telebot import types
import test_main
import time
import re
import os
import mysql.connector
from mysql.connector import Error
from itertools import groupby

def countrovn():
    count = open('history.txt')
    count = count.read()
    count1 = len(count)
    xd = 0
    count_final = 0
    while count1 > xd:
        if count[xd] == '=':
            count_final += 1
        xd +=1
    return count_final \

bot = telebot.TeleBot('токен')

now = 0

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton('📖Прочитать истории')
    item2 = types.KeyboardButton('📚Добавить свою историю')
    item3 = types.KeyboardButton('👨‍🔧О создателе')
    item4 = types.KeyboardButton('⭐️Сохраненные истории')
    markup.add(item1,item2,item3,item4)
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
            item4 = types.KeyboardButton('⭐️Сохранить историю')

            markup.add(item2,item3,item4)

            story = open('history.txt')
            story = story.read()
            story = story.split('=')
            bot.send_message(message.chat.id,story[0],reply_markup=markup)

        if message.text == 'Следующая история':

            global now
            story = open('history.txt')
            story = story.read()
            story = story.split('=')
            if now >= countrovn():
                now = 0
                bot.send_message(message.chat.id,story[now])
                now +=1
            else :
                now +=1
                bot.send_message(message.chat.id,story[now])
        if message.text == 'Назад':
            welcome(message)
        if message.text == '📚Добавить свою историю':
            msg = bot.send_message(message.chat.id, '✍️Отправь мне свою историю и я добавлю её в базу данных')
            bot.register_next_step_handler(msg, process1)

        if message.text == '👨‍🔧О создателе':
            bot.send_message(message.chat.id, 'Создатель - Якублевич Ренат\nGithub - https://github.com/RenatYakublevich\nСотрудничество - https://vk.com/helloworldbastard')

        if message.text == '⭐️Сохранить историю':
            my_file = open("favourite.txt", 'a')
            my_file.write('_' + str(now))
            my_file.close()
            listFav = open("favourite.txt", 'r')
            skii = listFav.read()
        if message.text == '⭐️Сохраненные истории':
            story = open('history.txt')
            story = story.read()
            story = story.split('=')
            saveStory = open('favourite.txt')
            saveStory = saveStory.read()
            count = saveStory.split('_')
            def f(l):
                n = []
                for i in l:
                    if i not in n:
                        n.append(i)
                return n
            new_count = f(count)
            trucount = 0

            while len(new_count) > trucount:
                bot.send_message(message.chat.id, story[int(new_count[trucount])])
                trucount +=1


def process1(message):
    try:
        gg = message.text

        f = open('history.txt', 'a')
        f.write("\n" + '=' + gg)
        f.close()

        bot.reply_to(message,'📝Мы записали вашу тру стори в базу данных!')
    except Exception as e:
        bot.reply_to(message, 'oooops')






bot.polling(none_stop=True)
