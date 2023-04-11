



from telebot import TeleBot
from const import *


bot = TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def wright(message):
    bot.send_message(message.chat.id, message.text)
    
    
# Старт
bot.polling(none_stop=True)