



from telebot import TeleBot, types
from random import choice
from const import *


bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    '''Приветствие пользователя '''
    # Список стикеров для приветствия пользователя
    sp = ["static//img/lili_hello.png", "static//img/lili.png"]
    # Стикер приветствия
    bot.send_sticker(message.chat.id, open(choice(sp), 'rb'))
    # Список приветствий для пользователя
    sp = ["Добро пожаловать,", "Привет,", "Привет, пользователь"]
    # Пишем  приветствие для пользователя
    bot.send_message(message.chat.id, "{hello} {user}!".format(user = message.from_user.first_name, 
                                                               hello = choice(sp)))
                     
    bot.send_message(message.chat.id, "Я {bot}, могу скачивать видео и аудио".format(bot = bot.get_me().first_name))
    
    #   print(message.text)
    #   message.text = "jugiug"
    #   print(message.text)
    wright(message)
    

@bot.message_handler(content_types=["text"])
def wright(message):
    '''Необходима для взаимодействия с пользователем'''
    # message - то что написал пользователь
    # Пишем то, что написал пользователь
    if message.text == "YouTube":
        ...
    elif message.text == "TikTok":
        ...
    elif message.text == "VK":
        ...
    else:
        markup = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("🎲 YouTube", callback_data='good')
        item2 = types.InlineKeyboardButton("😊 TikTok", callback_data='bad')
        item3 = types.InlineKeyboardButton("😊 VK", callback_data='bad')
        markup.add(item1, item2, item3)
        
        bot.send_message(message.chat.id, "Вот следующие социальные сети откуда я могу скачивать видео:", reply_markup=markup)
    
    
    bot.send_message(message.chat.id, message.text)
    
    
    
if __name__ == "__main__":
    # Старт бота
    bot.polling(none_stop=True)


# t.me/liliindexsbot - ссылка на бота