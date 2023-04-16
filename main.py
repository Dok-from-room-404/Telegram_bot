



from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from random import choice
from const import *
from modle.User import File, NET_ERROR, LINK_ERROR



# Экземпляр бота
bot = Bot(TOKEN)
# Диспечер бота. Отсеживает сообщения
dp = Dispatcher(bot)
# Класс файла который будет обрабатывать бот. Необходим чтобы бот понимал на каком он этапе обработки файла
file = File()


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    '''Помощь для пользователя '''
    await message.reply(TEXT_FOR_HELP, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
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
    await message.answer("Я могу скачивать видео и аудио из социальный сетей")
    file.reset()
    message.text = ""
    await wright(message)


@dp.message_handler(commands=['dowload'])
async def dowload(message: types.Message):
    '''Перезапуск функции скачки'''
    file.reset()
    await wright(message)


@dp.message_handler(content_types=["text"])
async def wright(message: types.Message):
    '''Необходима для взаимодействия с пользователем'''
    # message - то что написал пользователь
    # print(message.text)
    if not file.check_net() and file.stage == 0:
        # Выбор соц. сети
        if message.text != "":
            "После того как пользователь ввел соц сеть"
            try:
                file.append_net(message.text)
                await message.answer("Вы выбрали: {0}".format(message.text))
                # Удаляем кнопки
                hideBoard = ReplyKeyboardRemove()
                await message.answer("Введите ссылку: ", reply_markup=hideBoard)
            # НЕ УДАЛЯТЬ
            # except NET_ERROR:
            #     await message.answer("Выбрана не верная социальная сеть. Выберете из предложенных")
            except Exception as er:
                await message.answer(er)
        else:
            "До того как пользователь ввел соц сеть"
            # resize_keyboard - адаптация под интерфейс
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3) # default - False
            b1 = KeyboardButton('YouTube')
            b2 = KeyboardButton('TikTok')
            b3 = KeyboardButton('VK')
            markup.add(b1, b2, b3)
            #markup.add(item1).insert(item2).add(item3)
            await message.answer("Из какой социальной сети будем что-либо скачивать:", reply_markup=markup)
            
    elif file.check_net() and file.stage == 1:
        '''После того как пользователь ввел ссылку. Соц сеть записана в класс'''
        # Ввод ссылки
        # print(message.text)
        # https://www.youtube.com/watch?v=M9dvN4S31ts&t=1s
        # https://vk.com/clips 
        # https://www.youtube.com/shorts/96LQhbSIFWI
        try:
            file.append_link(message.text)
            await message.answer("Вы ввели следующею ссылку: {0}".format(message.text))
        # НЕ УДАЛЯТЬ
        # except LINK_ERROR:
        #     await message.answer("Введена не допустимая ссылка")
        #     await message.answer("Введите ссылку: ")
        except Exception as er:
            await message.answer(er)
            await message.answer("Введите ссылку: ")
        
    elif file.check_class_net() and file.stage == 2:
        '''После того как пользователь ввел и записал:
            Соц сеть
            класс соц. сети'''
        # взаимодействие с классом соц. сети
        print("juvhoerihroih")

        
    
    '''bot.send_message(message.chat.id, message.text)'''
    
    



    
    
if __name__ == "__main__":
    # Старт бота
    executor.start_polling(dp)
    


# t.me/liliindexsbot - ссылка на бота