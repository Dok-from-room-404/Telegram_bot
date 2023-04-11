



from telebot import TeleBot
from const import *


bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    '''Приветствие пользователя '''
    # Стикер приветствия
    bot.send_sticker(message.chat.id, open('static//img/lili_hello.png', 'rb'))
    
    # Пишем "Добро пожаловать 'имя пользователя'!"
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!".format(message.from_user))


@bot.message_handler(content_types=["text"])
def wright(message):
    '''Необходима для взаимодействия с пользователем'''
    # message - то что написал пользователь
    # Пишем то, что написал пользователь
    bot.send_message(message.chat.id, message.text)
    
    
    
    
# Старт бота
bot.polling(none_stop=True)


# t.me/liliindexsbot - ссылка на бота