



'''
Данный модуль содержит классы и  константы для работы бота с файлами

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
'''
from modle.YouTube import *


# Список доступных соц сетей
NET = ["YouTube", "TikTok", "VK"]


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
        '''Инициализация класса с основными атрибутами'''
        self.__net = None # Социальная сеть
        self.__class_net = None # Класс социальной сети (нужен для скачивания)
        
    def have_net(self) -> bool:
        '''Проверка на наличие социальной сети:
           \n* True - есть социальная сеть
           \n* False - нету социальной сети'''
        return self.__net != None
    
    def append_net(self, name_net:str) -> None:
        '''Добавление социальной сети'''
        if name_net in NET:
            self.__net = name_net
        else:
            raise NET_ERROR("Выбрана не верная социальная сеть. Выберете из предложенных")
        
    def append_link(self, link:str):
        '''Добавление ссылки'''
        # Проверка на правильное начало ссылки
        if not link.startswith("https://www") and not (self.__net == "VK" and link.startswith("https://")):
            raise LINK_ERROR("Введена не допустимая ссылка 1")
        
        if self.__net == "YouTube" and "youtube.com" not in link:
            raise LINK_ERROR("Введена не допустимая ссылка 2")
        
        elif self.__net == "TikTok" and "tiktok.com" not in link:
            raise LINK_ERROR("Введена не допустимая ссылка 3")
        
        elif self.__net == "VK" and "vk.com" not in link:
            raise LINK_ERROR("Введена не допустимая ссылка 4")
        try:
            if self.__net == "YouTube":
                self.__class_net = File_YouTube(link)
                
            elif self.__net == "TikTok":
                ...
                
            elif self.__net == "VK":
                ...
        except:
            raise LINK_ERROR("Введена не допустимая ссылка 5")
        
        
    

    def reset(self) -> None:
        '''Сброс настроек класса'''
        self.__net = None
        self.__class_net = None