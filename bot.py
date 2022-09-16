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

        bot.send_message(message.chat.id, 'Привет! Выбери кого хочешь поздравить и я сгенерирую поздравление. Ели тебе не '
                                      'понравиться повтори все с начала и я подберу что то получше ',
                     reply_markup=markup)


    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        def ran(dear, wish, be, empty):
            item = random.SystemRandom().choice(dear)
            item1 = random.SystemRandom().choice(wish)
            item2 = random.SystemRandom().choice(be)
            item3 = random.SystemRandom().choice(empty)

            return item, item1, item2, item3

        rez = ran(dear=dear, wish=wish, be=be, empty=empty)
        rez1 = random.SystemRandom().choice(he1)
        rez2 = random.SystemRandom().choice(web)
        qqq = str(rez)
        res_str = qqq.translate({ord(i): None for i in '()'})
        qqqq = res_str.translate({ord(i): None for i in "'"})

        if call.message:
            if call.data == 'she':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=str(qqqq))
            elif call.data == 'he':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=str(rez1))
            elif call.data == 'web':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=str(rez2))
            elif call.data == 'img':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=str(f'https://pozdravik.com/prikolnye/besplatnye-{random.randint(1, 50)}.jpg'))



    bot.polling()

if __name__ == '__main__':

    telegram_bot(token)
