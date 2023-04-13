



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
        
        bot.send_message(message.chat.id, "Вот следующие социальные сети откуда я могу что-либо скачивать:", reply_markup=markup)
    
    
    bot.send_message(message.chat.id, message.text)
    
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
            # # show alert
            # bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #     text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
    except:
        ...
    
    
    
if __name__ == "__main__":
    # Старт бота
    bot.polling(none_stop=True)


# t.me/liliindexsbot - ссылка на бота