



'''
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
'''
from modle.YouTube import *
from .const import NET
from .errors import NET_ERROR, LINK_ERROR, FORMAT_ERROR, TYPE_ERROR




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
        if name_net in NET:
            self.__net = name_net
            self.__stage = 1
        else:
            raise NET_ERROR("Выбрана не верная социальная сеть. Выберете из предложенных")
        
    def append_link(self, link:str):
        '''Добавление ссылки и класса социальной сети'''
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
            self.__stage = 2
        except:
            raise LINK_ERROR("Введена не допустимая ссылка 5")
        
    def get_format(self) -> set:
        '''Возвращает возможные форматы файлов'''
        return self.__class_net.format()
    
    def append_format(self, format:str):
        '''Устанавливает формат format скачиваемому файлу'''
            #\n* True - выбранный формат не поддерживает видео 
            #\n* False - выбранный формат поддерживает видео'''
        if self.__class_net.set_format(format):
            raise FORMAT_ERROR("Введен недопустимый формат файла")
        if self.__class_net.found_vidio():
            self.__stage = "question_format"
            #return True
        else:
            self.__stage = 3
            #return False
        
    def check_question_format(self, answer:str):
        '''Проверка ответа'''
        if answer.lower() != "да":
            self.__stage = 2
        elif answer.lower() != "нет":
            return
        else:
            raise ValueError("Недопустимое значение")
        
    def found_type(self) -> list:
        '''Проверяет наличие аудио и видео типов в выбранном формате'''
        list = []
        if not self.__class_net.found_vidio():
            list.append("vidio")
        if not self.__class_net.found_audio():
            list.append("audio")
        return list
    
    def append_type(self, type:str) -> None:
        '''Устанавливает тип type скачиваемому файлу'''
        if type == "Видео":
            type = "vidio"
        if type == "Аудио":
            type = "audio" 
        if type not in self.found_type():
            raise TYPE_ERROR("Выбран не верный тип")
        self.__class_net.set_type(type)
        self.__stage = 4


    def reset(self) -> None:
        '''Сброс настроек класса'''
        self.__net = None
        self.__class_net = None
        self.__stage = 0