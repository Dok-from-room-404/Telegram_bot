



from aiogram import Bot, Dispatcher, executor, types
from random import choice
from const import *

# Экземпляр бота
bot = Bot(TOKEN)
# Диспечер бота. Отсеживает сообщения
dp = Dispatcher(bot)
file = File()


@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    '''Приветствие пользователя '''
    # Список стикеров для приветствия пользователя
    sp = ["static//img/lili_hello.png", "static//img/lili.png"]
    # Стикер приветствия
    await message.answer_sticker(open(choice(sp), 'rb'))
    # Список приветствий для пользователя
    sp = ["Добро пожаловать,", "Привет,", "Привет, пользователь"]
    # Пишем  приветствие для пользователя
    await message.answer("{hello} {user}!".format(user = message.from_user.first_name, 
                                                               hello = choice(sp)))
                     
    # await bot.send_message(message.chat.id, "Я {bot}, могу скачивать видео и аудио".format(bot = bot.get_me().first_name))
    await message.answer("Я могу скачивать видео и аудио")
    # wright(message)


@dp.message_handler(content_types=["text"])
async def wright(message):
    '''Необходима для взаимодействия с пользователем'''
    # message - то что написал пользователь
    # Пишем то, что написал пользователь
    if file.set == None:
        "До того как пользователь ввел соц сеть"
        if message.text == "YouTube":
            file.set = "YouTube"
            # Удаляем кнопки
            hideBoard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "Введи ссылку: ", reply_markup=hideBoard)
        elif message.text == "TikTok":
            file.set = "TikTok"
            # Удаляем кнопки
            hideBoard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "Введи ссылку: ", reply_markup=hideBoard)
        elif message.text == "VK":
            file.set = "VK"
            # Удаляем кнопки
            hideBoard = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, "Введи ссылку: ", reply_markup=hideBoard)
        else:
            markup = types.ReplyKeyboardMarkup(row_width=1)
            item1 = types.KeyboardButton("YouTube")
            item2 = types.KeyboardButton("TikTok")
            item3 = types.KeyboardButton("VK")
            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id, "Из какой социальной сети будем что-либо скачивать:", parse_mode='html', reply_markup=markup)
    elif file.set != None:
        "После того как пользователь ввел соц сеть"
        bot.send_message(message.chat.id, "После того как пользователь ввел соц сеть")
        ...
    
    bot.send_message(message.chat.id, message.text)
    
    

    
    
if __name__ == "__main__":
    # Старт бота
    executor.start_polling(dp)#, on_startup=on_startup)
    


# t.me/liliindexsbot - ссылка на бота