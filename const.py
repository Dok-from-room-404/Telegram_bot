"""
Данный модуль содержит константы для работы бота

Константы:
---------
    * TOKEN - Токен бота от BotFather
    * TEXT_FOR_HELP - Список доступных команд
"""

TOKEN = "6218093072:AAHR9dUmAo24AcMOmWIl-QIGe3Ln2btGQuA"  # Токен бота от BotFather
# t.me/liliindexsbot - ссылка
TEXT_FOR_HELP = '''
Список доступных команд:
\t/help - список доступных команд
\t/start – команда старт
\t/download – команда для скачивания видео из социальных сетей (сбрасывает прошлые настройки для скачки видеороликов)
'''

HELLO_IMAGES = ["static//img/lili_hello.png", "static//img/lili.png"]
HELLO_VARIATIONS = ["Добро пожаловать,", "Привет,", "Привет, пользователь"]
SOCIALS = ["YouTube", "TikTok", "VK"]
BD = "db\\user.db"
YOUTUBE = 'YouTube'
HEADERS = {
    "content-type": "application/octet-stream",
    "X-RapidAPI-Key": "f5624db1d4msh20fca6f65d29e20p1cfb25jsn4ade0d2c525a",
    "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
}
URL = "https://tiktok-video-no-watermark2.p.rapidapi.com/"