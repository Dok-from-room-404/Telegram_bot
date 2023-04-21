



from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from random import choice
from const import *
from modle.User import USER # NET_ERROR, LINK_ERROR, FORMAT_ERROR
from modle.User.command_bd import *
# from modle.User.file import NET_ERROR, LINK_ERROR


# Экземпляр бота
bot = Bot(TOKEN)
# Диспечер бота. Отсеживает сообщения
dp = Dispatcher(bot)
# Подключаемся к БД
con, cur = connect_bd("db\\user.db")
# maid_bd(con, cur)


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
    await message.answer("Я Lili, могу скачивать видео и аудио из социальный сетей")
    await dowload(message)


@dp.message_handler(commands=['dowload'])
async def dowload(message: types.Message):
    '''Перезапуск функции скачки'''
    message.text = ""
    await wright(message, True)


@dp.message_handler(content_types=["text"])
async def wright(message: types.Message, flag:bool=False):
    '''Необходима для взаимодействия с пользователем'''
    # Класс пользователя. Получаем с БД
    # id - id пользователя
    id = message.from_user.id
    User = get_iser(cur, id)
    if User == None:
        # Если юзера нет в системе
        User = USER()
        append_user(con, cur, id, User)
    
    if flag:
        "Перезапуск функции скачки"
        User.file.reset()
    
    # Флаг первичного запроса данных
    flag = False
    
    if User.sheck_stage_0():
        # Если выбор соц. сети
        if message.text != "":
            "После того как пользователь ввел соц сеть"
            try:
                User.file.append_net(message.text)
                await message.answer("Вы выбрали: {0}".format(message.text))
                flag = True
            # НЕ УДАЛЯТЬ
            # except NET_ERROR:
            #     await message.answer("Выбрана не верная социальная сеть. Выберете из предложенных")
            except Exception as er:
                await message.answer(er)
        else:
            "До того как пользователь ввел соц сеть"
            # resize_keyboard - адаптация под интерфейс
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3) # default - False
            b1, b2, b3 = KeyboardButton('YouTube'), KeyboardButton('TikTok'), KeyboardButton('VK')
            markup.add(b1, b2, b3)
            await message.answer("Из какой социальной сети будем что-либо скачивать:", reply_markup=markup)
            
    if User.sheck_stage_1():
        # Если ввод ссылки
        if flag:
            # Удаляем кнопки
            hideBoard = ReplyKeyboardRemove()
            await message.answer("Введите ссылку: ", reply_markup=hideBoard)
        else:
            try:
                '''После того, как пользователь ввел ссылку'''
                User.file.append_link(message.text)
                await message.answer("Вы ввели следующею ссылку: {0}".format(message.text))
                flag = True
            # НЕ УДАЛЯТЬ
            # except LINK_ERROR:
            #     await message.answer("Введена не допустимая ссылка")
            #     await message.answer("Введите ссылку: ")
            except Exception as er:
                '''Недопустимая ссылка'''
                await message.answer(er)
                await message.answer("Введите ссылку: ")
            
    if User.sheck_stage_2():
        # Если ввод формата файла
        if flag:
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
            for i in User.file.get_format():
                # Добавляем на кнопки форматы
                markup.insert(KeyboardButton(i))
            await message.answer("Выберете необходимый вам формат файла", reply_markup=markup)
            
        else:
            try:
                '''После того, как пользователь ввел формат файла'''
                await message.answer("Вы ввели следующий формат : {0}".format(message.text))
                User.file.append_format(message.text)
                    #await message.answer("Данный формат является аудио дорожкой. Согласны ли вы изменить формат (да/нет)?")
                flag = True
            # НЕ УДАЛЯТЬ
            # except FORMAT_ERROR:
            #     await message.answer("Введен недопустимый формат файла. Выберете из предложенных")
            except Exception as er:
                '''Недопустимый формат файла'''
                await message.answer(er)
    
    if User.sheck_stage_question_format():
        # Согласны ли вы изменить формат
        if flag:
            await message.answer("Данный формат является аудио дорожкой. Согласны ли вы изменить формат (да/нет)?")
        else:
            User.file.check_question_format()
        
    if User.sheck_stage_3():
        # Если ввод типа файла
        if flag:
            types = User.file.found_type()
            if len(types) == 2:
                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
                markup.add(KeyboardButton("Видео")).insert(KeyboardButton("Аудио"))
                await message.answer("Выберете необходимый вам тип файла", reply_markup=markup)
            if len(types) == 1:
                User.file.append_type(*types)
                flag = True
        else:
            try:
                User.file.append_type(message.text)
                flag = True
            # НЕ УДАЛЯТЬ
            # except TYPE_ERROR:
            #     await message.answer("Выбран не верный тип. Выберете из предложенных")
            except Exception as er:
                '''Недопустимый тип файла'''
                await message.answer(er)
                
    if User.sheck_stage_4():
        # Выбор бит рейда у аудио дорожки или выбор разрешения видео
        ...


        
        
        
    # Сохранение изменений в БД
    uppdete_user(con, cur, id, User)


if __name__ == "__main__":
    # Старт бота
    executor.start_polling(dp)
    


# t.me/liliindexsbot - ссылка на бота