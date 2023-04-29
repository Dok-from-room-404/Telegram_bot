import os
from dotenv import load_dotenv, find_dotenv
from aiogram import types

load_dotenv(find_dotenv())

TOKEN = os.environ['TOKEN']  # Токен бота от BotFather
# t.me/liliindexsbot - ссылка
TEXT_FOR_HELP = '''
Меня зовут Lili, я умею скачивать видео с ютуба(не больше 50Mb) и TikTok
(Youtube shorts пока не работают)

Список доступных команд:
\t/help - список доступных команд
\t/start – команда старт
\t/download – команда для скачивания видео из социальных сетей (сбрасывает прошлые настройки для скачки видеороликов)
'''

HELLO_IMAGES = ["data//static//img/lili_hello.png", "data//static//img/lili.png"]
HELLO_VARIATIONS = ["Добро пожаловать,", "Привет,", "Привет, пользователь"]
SOCIALS = ["YouTube", "TikTok"]
BD = "user.db"
YOUTUBE = 'YouTube'
TIKTOK = 'TikTok'
HEADERS = {
    "content-type": "application/octet-stream",
    "X-RapidAPI-Key": os.environ['RAPIDAPI_KEY'],
    "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}
URL = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

COMMANDS = [
            types.BotCommand("start", "Start"),
            types.BotCommand("help", "Help"),
            types.BotCommand("download", "Download new"),
        ]
