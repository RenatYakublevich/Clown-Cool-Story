import telebot
from telebot import types
import test_main
import time
import re
import os

bot = telebot.TeleBot('токен')

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton('📖Прочитать истории')
    item2 = types.KeyboardButton('📚Добавить свою историю')

    markup.add(item1,item2)
    gg = 'Привет, <b>' + message.from_user.first_name.title() + '</b>!\nХочешь прочитать или добавить кринжовую историю про себя или своего друга? Тогда тебе к нам\nНу что,поехали?)😏\n\nСоздатель - Якублевич Ренат\nGithub - https://github.com/RenatYakublevich'.format(message.from_user, bot.get_me())
    bot.send_message(message.chat.id,gg,parse_mode='html',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def crypto_price_telegram(message):
    if message.chat.type == 'private':
        if message.text == '📖Прочитать истории':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
            item1 = types.KeyboardButton('Предыдущая история')
            item2 = types.KeyboardButton('Назад')
            item3 = types.KeyboardButton('Следующая история')

            markup.add(item1,item2,item3)

            bot.send_message(message.chat.id, test_main.text[test_main.now] ,reply_markup=markup)
        if message.text == 'Следующая история':
            if test_main.now == test_main.count:
                test_main.now = 0
                bot.send_message(message.chat.id, test_main.text[test_main.now])
            else:
                test_main.now +=1
                bot.send_message(message.chat.id, test_main.text[test_main.now])
        if message.text == 'Предыдущая история':
            if test_main.now == -(test_main.count):
                test_main.now = 0
                bot.send_message(message.chat.id, test_main.text[test_main.now])
            else:
                test_main.now -=1
                bot.send_message(message.chat.id, test_main.text[test_main.now])

        if message.text == 'Назад':
            welcome(message)
        if message.text == '📚Добавить свою историю':
            bot.send_message(message.chat.id, 'Для добавления истории перейди на сайт и <b>поделись своей кул стори со всем миром аблсолютно анонимно!</b>\n\nhttps://cutt.ly/LylMio5',parse_mode='html')










bot.polling(none_stop=True)
