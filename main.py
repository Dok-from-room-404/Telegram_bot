from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from random import choice
from const import *
from modle.Files import *  # NET_ERROR, LINK_ERROR, FORMAT_ERROR
from data.command_bd import *

bot = Bot(TOKEN)
dp = Dispatcher(bot)
con, cur = connect_bd(BD)


# maid_bd(con, cur)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    """Помощь для пользователя """
    await message.reply(TEXT_FOR_HELP, reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    """Приветствие пользователя """
    await message.answer_sticker(open(choice(HELLO_IMAGES), 'rb'))
    # Пишем  приветствие для пользователя
    await message.answer("{hello} {user}!".format(user=message.from_user.first_name,
                                                  hello=choice(HELLO_VARIATIONS)))
    # await bot.send_message(message.chat.id, "Я {bot},
    # могу скачивать видео и аудио".format(bot = bot.get_me().first_name))
    await message.answer("Я Lili, умею скачивать видео с YouTube и TikTok")
    await download(message)


@dp.message_handler(commands=['download'])
async def download(message: types.Message):
    """Перезапуск функции скачки"""
    message.text = ""
    await wright(message, True)


@dp.message_handler(content_types=["text"])
async def wright(message: types.Message, flag: bool = False):
    """Необходима для взаимодействия с пользователем"""
    # Класс пользователя. Получаем с БД
    # id - id пользователя
    id = message.from_user.id
    file = get_user(cur, id)
    if file is None:
        # Если юзера нет в системе
        file = File()
        append_user(con, cur, id, file)

    if flag:
        "Перезапуск функции скачки"
        file.reset()

    # Флаг первичного запроса данных
    flag = False

    if file.stage == 0:
        # Если выбор соц. сети
        if message.text != "":
            "После того как пользователь ввел соц сеть"
            try:
                file.append_net(message.text)
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
            markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
            b1, b2 = KeyboardButton(YOUTUBE), KeyboardButton(TIKTOK)
            markup.add(b1, b2)
            await message.answer("Откуда будем скачивать:", reply_markup=markup)

    if file.stage == 1:
        # Если ввод ссылки
        if flag:
            # Удаляем кнопки
            hideboard = ReplyKeyboardRemove()
            await message.answer(f"Введите ссылку:\n"
                                 f"пример Youtube:https://www.youtube.com/watch?v=********\n"
                                 f"пример TikTok:https://www.tiktok.com/@*******/video/*****",
                                 reply_markup=hideboard, disable_web_page_preview=True)
        else:
            try:
                '''После того, как пользователь ввел ссылку'''
                file.append_link(message.text)
                if file.net == YOUTUBE:
                    try:
                        ans = file.get_youtube_info(message.text)
                        await message.answer(ans, disable_web_page_preview=True)
                    except Exception as e:
                        print(e)
                        await message.answer('Произошла ошибка, введите ссылку еще раз')
                        file.stage_setter(1)
                flag = True
            # НЕ УДАЛЯТЬ
            except LINK_ERROR:
                await message.answer("Введена не допустимая ссылка")
                await message.answer("Введите ссылку: ")
            except Exception as er:
                '''Недопустимая ссылка'''
                await message.answer(er)
                await message.answer("Введите ссылку: ")

    if file.stage == 2:
        # Если ввод формата файла
        if file.net == YOUTUBE:
            if flag:
                try:
                    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
                    for i in file.class_net.format():
                        # Добавляем на кнопки форматы
                        markup.insert(KeyboardButton(i))
                    await message.answer("Выберете необходимый вам формат файла", reply_markup=markup)
                except Exception as e:
                    await message.answer('Произошла неизвестная ошибка, вам придется начать сначала')
                    file.reset()
                    await message.answer('Введите команду \t/download')
            else:
                try:
                    '''После того, как пользователь ввел формат файла'''
                    await message.answer("Вы ввели следующий формат : {0}".format(message.text))
                    file.check_format(message.text)
                    flag = True
                except FORMAT_ERROR:
                    await message.answer("Введен недопустимый формат файла. Выберете из предложенных")
                except Exception as er:
                    '''Недопустимый формат файла'''
                    await message.answer(er)
        elif file.net == TIKTOK:
            if flag:
                # try:
                file.get_tiktok_request()
                ans = file.get_tiktok_info(message.text)
                await message.answer(ans, disable_web_page_preview=True)
                await message.answer_video(file.get_tiktok_video(), caption='Полное видео без водяного знака')
                await message.answer_audio(file.get_tiktok_audio(), caption='Отдельная аудио дорожка')
                file.reset()
            # except Exception as e:
            #    await message.answer('Произошла ошибка')

    if file.stage == "question_format":
        # Согласны ли вы изменить формат
        if file.net == YOUTUBE:
            if flag:
                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
                markup.insert(KeyboardButton("Да"))
                markup.insert(KeyboardButton("Нет"))
                await message.answer("Данный формат является аудио дорожкой. Согласны ли вы изменить формат (Да/Нет)?",
                                     reply_markup=markup)
            else:
                file.check_question_format(message.text)
                flag = True
                if file.stage == 2:
                    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=3)
                    for i in file.class_net.format():
                        # Добавляем на кнопки форматы
                        markup.insert(KeyboardButton(i))
                    await message.answer("Выберете необходимый вам формат файла", reply_markup=markup)

    if file.stage == 3:
        # Если ввод типа файла
        if file.net == YOUTUBE:
            if flag:
                if file.class_net.found_video() and file.class_net.found_audio():
                    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
                    markup.add(KeyboardButton("Видео")).insert(KeyboardButton("Аудио"))
                    await message.answer("Выберете необходимый вам тип файла", reply_markup=markup)
                if file.class_net.found_audio() and not file.class_net.found_video():
                    file.append_type("audio")
                    flag = True
                if file.class_net.found_video() and not file.class_net.found_audio():
                    file.append_type("video")
                    flag = True
            else:
                try:
                    file.append_type(message.text)
                    flag = True
                # НЕ УДАЛЯТЬ
                except TYPE_ERROR:
                    await message.answer("Выбран не верный тип. Выберете из предложенных")
                except Exception as er:
                    '''Недопустимый тип файла'''
                    await message.answer(er)

    if file.stage == 4:
        # Выбор бит рейда у аудио дорожки или выбор разрешения видео
        if file.net == YOUTUBE:
            if flag:
                if file.class_net.found_video():
                    files = file.inform_video()

                elif file.class_net.found_audio():
                    files = file.inform_audio()

                markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
                for i in files:
                    markup.add(KeyboardButton(i))
                await message.answer("Выберете файл по следующим параметрам", reply_markup=markup)
            else:
                try:
                    await message.answer("Загрузка файла. Ожидайте")
                    if file.class_net.found_video():
                        print("found_video")
                        download_file = file.download_audio(message.text)
                    elif file.class_net.found_audio():
                        print("found_audio")
                        download_file = file.download_audio(message.text)

                    await bot.send_document(message.from_user.id, download_file)
                    await message.answer("Загрузка файла закончена\n"
                                         "Нажмите \t/download для продолжения", reply_markup=ReplyKeyboardRemove())
                    message.text = ""
                    file.reset()
                # НЕ УДАЛЯТЬ
                except TYPE_ERROR:
                    await message.answer("Выбран не верный тип. Выберете из предложенных")
                except Exception as er:
                    '''Недопустимый тип файла'''
                    await message.answer(er)
    # Сохранение изменений в БД
    update_user(con, cur, id, file)


if __name__ == "__main__":
    executor.start_polling(dp)

