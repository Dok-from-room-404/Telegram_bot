"""
Данная библиотека содержит классы и  константы для работы бота с файлами

Константы:
---------
    * NET - Список доступных соц сетей

Исключения:
----------
    * NET_ERROR - Класс ошибки. Возникает при добавление недопустимой соц. сети
    * LINK_ERROR - Класс ошибки. Возникает при добавление недопустимой ссылки

Классы:
------
    * File - Класс файла который будет обрабатывать бот. Необходим чтобы бот понимал на каком он этапе обработки файла
"""
from .YouTube import *
from .TikTok import *
from .const import NET
from .errors import NET_ERROR, LINK_ERROR, FORMAT_ERROR, TYPE_ERROR


class File(object):
    """Класс файла который будет обрабатывать бот.
       Необходим чтобы бот понимал на каком он этапе обработки файла"""

    def __init__(self) -> None:
        """Инициализация класса с основными атрибутами
           \n* self.__net - Социальная сеть
           \n* self.__class_net - Класс социальной сети (нужен для скачивания)
           \n* self.__stage - Стадия скачивания файла:
           \n\t* 0 -  Выбор соц. сети
           \n\t* 1 -  Ввод ссылки
           \n\t* 2 и более – взаимодействие с классом соц. сети
           """
        self.__net = None
        self.__class_net = None  # Класс социальной сети (нужен для скачивания)
        self.__stage = 0  # Стадия скачивания файла

    @property
    def stage(self):
        """Стадия скачивания файла"""
        return self.__stage

    @property
    def class_net(self):
        """Класс социальной сети"""
        return self.__class_net

    @property
    def net(self):
        """соц. сети"""
        return self.__net

    # stage = 0
    def append_net(self, name_net: str) -> None:
        """Добавление социальной сети"""
        if name_net in NET:
            self.__net = name_net
            self.__stage = 1
        else:
            raise NET_ERROR("Выбрана не верная социальная сеть. Выберете из предложенных")

    # stage = 1
    def append_link(self, link: str):
        """Добавление ссылки и класса социальной сети"""
        # Проверка на правильное начало ссылки
        if not link.startswith("https://www"):
            raise LINK_ERROR("Введена не допустимая ссылка 1")

        if self.__net == "YouTube" and "youtube.com" not in link:
            raise LINK_ERROR("Введена не допустимая ссылка 2")

        elif self.__net == "TikTok" and "tiktok.com" not in link:
            raise LINK_ERROR("Введена не допустимая ссылка 3")
        #try:
        if self.__net == "YouTube":
            self.__class_net = File_YouTube(link)

        elif self.__net == "TikTok":
            self.__class_net = TikTokFile(link)

        self.__stage = 2
        #except:
        #    raise LINK_ERROR("Введена не допустимая ссылка 5")

    # stage = 2
    def check_format(self, format: str):
        """Устанавливает формат format скачиваемому файлу"""
        if self.__net == "YouTube":
            if self.__class_net.set_format(format):
                raise FORMAT_ERROR("Введен недопустимый формат файла")
            if not self.__class_net.found_video():
                self.__stage = "question_format"
            else:
                self.__stage = 3

    # stage = "question_format"
    def check_question_format(self, answer: str):
        """Проверка ответа"""
        if self.__net == "YouTube":
            if answer.lower() == "да":
                self.__stage = 2
            elif answer.lower() == "нет":
                self.__stage = 3
            else:
                raise ValueError("Недопустимое значение")

    # stage = 3
    def found_type(self) -> list:
        """Проверяет наличие аудио и видео типов в выбранном формате"""
        if self.__net == "YouTube":
            listt = []
            if self.__class_net.found_video():
                listt.append("video")
            if self.__class_net.found_audio():
                listt.append("audio")
            return listt

    def append_type(self, type: str) -> None:
        """Устанавливает тип type скачиваемому файлу"""
        if self.__net == "YouTube":
            if type == "Видео": type = "video"
            if type == "Аудио": type = "audio"

            if type not in self.found_type():
                raise TYPE_ERROR("Выбран не верный тип")
            self.__class_net.set_type(type)
            self.__stage = 4

    # stage = 4
    def inform_audio(self) -> dict:
        """Получаем инфу о аудио файлах"""
        self.__class_net.found_audio_file()
        return self.__class_net.files

    def download_audio(self, inform: str):
        """Скачиваем выбранный файл"""
        return self.__class_net.download_audio_file(inform)

    def inform_video(self):
        """Выводим инфу о доступных разрешений видео"""
        self.__class_net.found_video_file()
        return self.__class_net.files

    def get_youtube_info(self, message):
        st = f'Ваша ссылка: {message}\n'
        return st

    def get_tiktok_info(self, message):
        inf = self.__class_net.get_info()
        st = f'Ваша ссылка: {message.text}\n'\
            f'Параметры:\n'\
            f'Автор: {inf[2]}\n'\
            f'Название: {inf[0]}\n'\
            f'Длительность: {inf[1]}\n'
        return st

    def get_tiktok_request(self):
        self.__class_net.get_request()

    def get_tiktok_video(self):
        return self.__class_net.get_video()

    def get_tiktok_audio(self):
        return self.__class_net.get_audio()

    def reset(self) -> None:
        """Сброс настроек класса"""
        self.__net = None
        self.__class_net = None
        self.__stage = 0

    def stage_setter(self, value):
        self.__stage = value
