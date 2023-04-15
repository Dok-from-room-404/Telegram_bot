



from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from random import choice
from const import *

# Экземпляр бота
bot = Bot(TOKEN)
# Диспечер бота. Отсеживает сообщения
dp = Dispatcher(bot)
file = File()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    '''Помощь для пользователя '''
    await message.reply(TEXT_FOR_HELP)




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
    await wright(message)
    
    

    


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
            hideBoard = ReplyKeyboardRemove()
            await message.answer("Введи ссылку: ", reply_markup=hideBoard)
        elif message.text == "TikTok":
            file.set = "TikTok"
            # Удаляем кнопки
            await message.answer("Введи ссылку: ", reply_markup=ReplyKeyboardRemove())
        elif message.text == "VK":
            file.set = "VK"
            # Удаляем кнопки
            await message.answer("Введи ссылку: ", reply_markup=ReplyKeyboardRemove())
        else:
            markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3) # default - False
            b1 = KeyboardButton('YouTube')
            b2 = KeyboardButton('TikTok')
            b3 = KeyboardButton('VK')
            markup.add(b1, b2, b3)
            #markup.add(item1).insert(item2).add(item3)
            await message.answer("Из какой социальной сети будем что-либо скачивать:", reply_markup=markup)
    '''
    elif file.set != None:
        "После того как пользователь ввел соц сеть"
        bot.send_message(message.chat.id, "После того как пользователь ввел соц сеть")
        ...
    
    bot.send_message(message.chat.id, message.text)'''
    
    



    
    
if __name__ == "__main__":
    # Старт бота
    executor.start_polling(dp)#, on_startup=on_startup)
    


# t.me/liliindexsbot - ссылка на бота