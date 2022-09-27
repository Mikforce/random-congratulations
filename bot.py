#!/usr/bin/env python3
import telebot
from telebot import types
import random
from text import *
from auth_date import token

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['button'])
    def button(message):

        markup = types.InlineKeyboardMarkup(row_width=2)
        item = types.InlineKeyboardButton('Для нее', callback_data='she')
        item2 = types.InlineKeyboardButton('Для него', callback_data='he')
        item3 = types.InlineKeyboardButton('Поиск по сайтам', callback_data='web')
        item4 = types.InlineKeyboardButton('Картинка', callback_data='img')
        markup.add(item, item2, item3,item4)

        bot.send_message(message.chat.id, 'Привет! Выбери кого хочешь поздравить и я сгенерирую поздравление. Если тебе не понравится, повтори все с начала и я подберу что-то получше. ',
                     reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        def rand(str):
            item = random.SystemRandom().choice(str)
            return item

        rez = rand(dear) + rand(wish) + rand(be) + rand(empty)
        rez1 = rand(he1)
        rez2 = rand(web)

        def botmsg(text):
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=text)

        if call.message:
            if call.data == 'she':
                botmsg(rez)
            elif call.data == 'he':
                botmsg(rez1)
            elif call.data == 'web':
                botmsg(rez2)
            elif call.data == 'img':
                botmsg(str(f'https://pozdravik.com/prikolnye/besplatnye-{random.randint(1, 50)}.jpg'))

    bot.polling()

if __name__ == '__main__':

    telegram_bot(token)
