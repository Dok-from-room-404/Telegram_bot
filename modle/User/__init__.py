



'''
Данная библиотека позволяет работать и с пользователями
'''

from .Files import File
from .Files import NET_ERROR, LINK_ERROR
from .command_bd import *


class USER:
    '''Класс пользователя'''
    def __init__(self) -> None:
        '''Инициализация класса пользователя с основными атрибутами:
        \n* self.file - класс файла который будет обрабатывать бот. Необходим чтобы бот понимал на каком он этапе обработки файла'''
        # Класс файла который будет обрабатывать бот. Необходим чтобы бот понимал на каком он этапе обработки файла
        self.file = File()
        

    def sheck_stage_0(self) -> bool: 
        '''Проверка на стадию 0 (Выбор соц. сети):
        \t* True - текущая стадия 0
        \t* False - текущая стадия 0'''
        print("state 0")
        return self.file.stage == 0 # not self.file.check_net() and 
    
    def sheck_stage_1(self) -> bool: 
        '''Проверка на стадию 1 (Ввод ссылки):
        \t* True - текущая стадия 1
        \t* False - текущая стадия 1'''
        print("state 1")
        return self.file.stage == 1 # self.file.check_net() and self.file.stage == 1
    
    def sheck_stage_2(self) -> bool: 
        '''Проверка на стадию 2 (Ввод формата файла):
        \t* True - текущая стадия 2
        \t* False - текущая стадия 2'''
        print("state 2")
        return self.file.stage == 2 # self.file.check_class_net() and self.file.stage == 2
    
    def sheck_stage_question_format(self) -> bool: 
        '''Проверка на стадию question_format (Данный формат является аудио дорожкой. Согласны ли вы изменить формат (да/нет)?):
        \t* True - текущая стадия question_format
        \t* False - текущая стадия question_format'''
        print("state question_format")
        return self.file.stage == "question_format"
    
    def sheck_stage_3(self) -> bool: 
        '''Проверка на стадию 3 (Ввод типа файла (видео/аудио)):
        \t* True - текущая стадия 3
        \t* False - текущая стадия 3'''
        print("state 3")
        return self.file.stage == 3  
        
