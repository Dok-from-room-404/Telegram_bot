



from .file import File


class USER:
    '''Класс пользователя'''
    def __init__(self) -> None:
        '''Инициализация класса пользователя с основными атрибутами:
        \n* self.file - ласс файла который будет обрабатывать бот. Необходим чтобы бот понимал на каком он этапе обработки файла'''
        # Класс файла который будет обрабатывать бот. Необходим чтобы бот понимал на каком он этапе обработки файла
        self.file = File()
        
    def append_net(self, net:str):
        '''Добавление социальной сети'''
        self.file.append_net(net)
        
    def append_link(self, link:str):
        '''Добавление ссылки и класса социальной сети'''
        self.file.append_link(link)

    def sheck_stage_0(self) -> bool: 
        '''Проверка на стадию 0 (Выбор соц. сети):
        \t* True - текущая стадия 0
        \t* False - текущая стадия 0'''
        return not self.file.check_net() and self.file.stage == 0
    
    def sheck_stage_1(self) -> bool: 
        '''Проверка на стадию 1 (Ввод ссылки):
        \t* True - текущая стадия 1
        \t* False - текущая стадия 1'''
        return self.file.check_net() and self.file.stage == 1
    
    def sheck_stage_2(self) -> bool: 
        '''Проверка на стадию 2 (взаимодействие с классом соц. сети):
        \t* True - текущая стадия 2
        \t* False - текущая стадия 2'''
        print("state 2")
        return self.file.check_class_net() and self.file.stage == 2
        
        
    def reset_file(self) -> None:
        '''Сброс настроек класса файла'''
        self.file.reset()