'''
Данный модуль содержит классы и  константы для работы бота с файлами
    
Исключения:
----------
    * NET_ERROR - Класс ошибки. Возникает при добавление недопустимой соц. сети
    * LINK_ERROR - Класс ошибки. Возникает при добавление недопустимой ссылки
    
Классы:
------
    * File - Класс файла который будет обрабатывать бот. Необходим чтобы бот понимал на каком он этапе обработки файла
'''
from modle.YouTube import *
from const import *


class NET_ERROR(Exception):
    '''Класс ошибки. Возникает при добавление недопустимой соц. сети'''
    def __init__(self, inform="") -> None:
        self.inform = inform

    def __str__(self):
        print('calling str')
        if self.inform:
            return 'NET_ERROR: {0} '.format(self.inform)
        else:
            return 'NET_ERROR'


class LINK_ERROR(Exception):
    '''Класс ошибки. Возникает при добавление недопустимой ссылки'''
    def __init__(self, inform="") -> None:
        self.inform = inform

    def __str__(self):
        print('calling str')
        if self.inform:
            return 'LINK_ERROR: {0} '.format(self.inform)
        else:
            return 'LINK_ERROR'


class File(object):
    '''Класс файла который будет обрабатывать бот. 
       Необходим чтобы бот понимал на каком он этапе обработки файла'''

    def __init__(self) -> None:
        '''Инициализация класса с основными атрибутами
           \n* self.__net - Социальная сеть
           \n* self.__class_net - Класс социальной сети (нужен для скачивания)
           \n* self.__stage - Стадия скачивания файла:
           \n\t* 0 -  Выбор соц. сети
           \n\t* 1 -  Ввод ссылки
           \n\t* 2 и более – взаимодействие с классом соц. сети
           '''
        self.__net = None # Социальная сеть
        self.__class_net = None # Класс социальной сети (нужен для скачивания)
        self.__stage = 0 # Стадия скачивания файла
        
    @property
    def net(self):
        '''Социальная сеть'''
        return self.__net
    
    @property
    def stage(self):
        '''Стадия скачивания файла'''
        return self.__stage
        
    def check_net(self) -> bool:
        '''Проверка на наличие социальной сети:
           \n* True - есть социальная сеть
           \n* False - нету социальной сети'''
        return self.__net != None
    
    def check_class_net(self) -> bool:
        '''Проверка на наличие класса социальной сети:
           \n* True - есть класс
           \n* False - нету класса'''
        return self.__class_net != None
    
    def append_net(self, name_net:str) -> None:
        '''Добавление социальной сети'''
        if name_net in SOCIALS:
            self.__net = name_net
            self.__stage = 1
        else:
            raise NET_ERROR("Выбрана не верная социальная сеть. Выберете из предложенных")
        
    def append_link(self, link:str):
        '''Добавление ссылки и класса социальной сети'''
        # Проверка на правильное начало ссылки
        if not link.startswith("https://www") and not link.startswith("https://"):
            raise LINK_ERROR("Введена не допустимая ссылка 1")

        try:
            if self.__net == "YouTube":
                if "youtube.com" in link or 'youtu.be' in link:
                    self.__class_net = File_YouTube(link)
                else:
                    raise LINK_ERROR("Введена не допустимая ссылка 2")
                
            elif self.__net == "TikTok":
                ...
                
            elif self.__net == "VK":
                ...
            self.__stage = 2
        except:
            raise LINK_ERROR("Введена не допустимая ссылка 5")

    def append_youtube_form(self, form:str):
        self.__class_net.choose_format(form)

    def download_youtube_file(self, form):
        if form == 'Video':
            self.__class_net.download_video()
        elif form == 'Audio':
            self.__class_net.download_audio()

    def next_stage(self):
        self.__stage += 1

    def reset(self) -> None:
        '''Сброс настроек класса'''
        self.__net = None
        self.__class_net = None
        self.__stage = 0