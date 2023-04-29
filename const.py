import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ['TOKEN']  # Токен бота от BotFather
# t.me/liliindexsbot - ссылка
TEXT_FOR_HELP = '''
Список доступных команд:
\t/help - список доступных команд
\t/start – команда старт
\t/download – команда для скачивания видео из социальных сетей (сбрасывает прошлые настройки для скачки видеороликов)
'''

HELLO_IMAGES = ["data//static//img/lili_hello.png", "data//static//img/lili.png"]
HELLO_VARIATIONS = ["Добро пожаловать,", "Привет,", "Привет, пользователь"]
SOCIALS = ["YouTube", "TikTok"]
BD = "data\\db\\user.db"
YOUTUBE = 'YouTube'
TIKTOK = 'TikTok'
HEADERS = {
    "content-type": "application/octet-stream",
    "X-RapidAPI-Key": os.environ['RAPIDAPI_KEY'],
    "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}
URL = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
