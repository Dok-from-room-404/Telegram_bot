from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from random import choice
from const import *
from modle.User import USER
from modle.User.file import NET_ERROR, LINK_ERROR
from modle.command_bd import *
import pickle
import os


bot = Bot(TOKEN)
dp = Dispatcher(bot)
con, cur = connect_bd(BD)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    '''Помощь для пользователя '''
    await message.reply(TEXT_FOR_HELP, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    '''Приветствие пользователя'''
    await message.answer_sticker(open(choice(HELLO_IMAGES), 'rb'))
    await message.answer("{hello} {user}!".format(user = message.from_user.first_name, 
                                                               hello = choice(HELLO_VARIATIONS)))
    # await bot.send_message(message.chat.id, "Я {bot}, могу скачивать видео и аудио".format(bot = bot.get_me().first_name))
    await message.answer("Я Lili, могу скачивать видео и аудио из социальный сетей")
    await download(message)


@dp.message_handler(commands=['download'])
async def download(message: types.Message):
    '''Перезапуск функции скачки'''
    message.text = ""
    await wright(message, True)


@dp.message_handler(content_types=["text"])
async def wright(message: types.Message, flag:bool=False):
    '''Необходима для взаимодействия с пользователем'''
    # Класс пользователя. Получаем с БД
    id = message.from_user.id
    inform = get_iser(con, cur, id)
    if inform == None:
        User = USER()
        inf = pickle.dumps(User)
        append_user(con, cur, id, inf)
    else:
        User = pickle.loads(inform[0])
    
    if flag:
        "Перезапуск функции скачки"
        User.reset_file()
    print(User.file.stage)
    
    if User.sheck_stage_0():
        # Если выбор соц. сети
        if message.text != "":
            "После того как пользователь ввел соц сеть"
            try:
                User.append_net(message.text)
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
            b1 = KeyboardButton(YOUTUBE)
            b2 = KeyboardButton('TikTok')
            b3 = KeyboardButton('VK')
            markup.add(b1, b2, b3)
            #markup.add(item1).insert(item2).add(item3)
            await message.answer("Из какой социальной сети будем что-либо скачивать:", reply_markup=markup)

    elif User.sheck_stage_1():
        '''После того как пользователь ввел ссылку. Соц сеть записана в класс'''
        # Если  ввод ссылки
        # https://www.youtube.com/watch?v=M9dvN4S31ts&t=1s
        # https://vk.com/clips 
        # https://www.youtube.com/shorts/96LQhbSIFWI
        try:
            '''После того, как пользователь ввел ссылку'''
            User.append_link(message.text)
            await message.answer("Вы ввели следующею ссылку: {0}".format(message.text))
            # Сохранение изменений в БД (тут из-за рекурсии)
            uppdete_user(con, cur, id, pickle.dumps(User))
            if User.file.net == YOUTUBE:
                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True,
                                             row_width=3)  # default - False
                b1 = KeyboardButton('Video')
                b2 = KeyboardButton('Audio')
                b3 = KeyboardButton('Video+Audio')
                markup.add(b1, b2, b3)
                # markup.add(item1).insert(item2).add(item3)
                await message.answer('В каком формате будем скачивать:', reply_markup=markup)
            
        # НЕ УДАЛЯТЬ
        # except LINK_ERROR:
        #     await message.answer("Введена не допустимая ссылка")
        #     await message.answer("Введите ссылку: ")
        except Exception as er:
            '''До того, как пользователь ввел ссылку'''
            await message.answer(er)
            await message.answer("Введите ссылку: ")
        
    elif User.sheck_stage_2():
        '''После того как пользователь ввел и записал:
            Соц сеть
            класс соц. сети'''
        # Если взаимодействие с классом соц. сети
        if User.file.net == YOUTUBE:
            if message.text in YOUTUBE_FORMATS:
                User.choose_format_youtube(message.text)
                hideBoard = ReplyKeyboardRemove()
                User.file.next_stage()
                await message.answer("Вы выбрали формат: {0}".format(message.text), reply_markup=hideBoard)
                User.download_youtube_file(message.text)
                try:
                    if message.text == 'Video':
                        with open('reply.mp4', 'rb') as f:
                            await message.answer_video(f)
                    elif message.text == 'Audio':
                        with open('reply.mp4', 'rb') as f:
                            await message.answer_audio(f)
                    os.remove('reply.mp4')

                except Exception as e:
                    await message.answer('Произошла ошибка попробуйте снова')
            else:
                await message.answer('Выберите корректный формат')
    elif User.check_stage_3():
        await message.answer('Для продолжения работы введите команду \t/download')
    # Сохранение изменений в БД
    uppdete_user(con, cur, id, pickle.dumps(User))


if __name__ == "__main__":
    executor.start_polling(dp)
