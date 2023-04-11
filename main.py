



from telebot import TeleBot
from const import *


bot = TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def wright(message):
    '''Необходима для написания чего-либо для пользователя'''
    bot.send_message(message.chat.id, message.text)
    
    
# Старт
bot.polling(none_stop=True)


# t.me/liliindexsbot - ссылка на бота