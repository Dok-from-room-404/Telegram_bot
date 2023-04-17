



from pytube import YouTube



class File_YouTube:
    '''Данный класс необходим для взаимодействия с YouTube (выкачка файлов)'''
    def __init__(self, link:str) -> None:
        '''Инициализируем класс
        * link - Ссылка на видео'''
        # видео на YouTube (неопределено по формату и качеству)
        self.yt = YouTube(link)
        self.formats = set()
        self.inform = None
        
    def format(self) -> set:
        '''Определяем формат у видео'''
        if len(self.formats) == 0:
            self.formats = set(map(lambda i: i.mime_type.replace(i.type, "")[1:], self.yt.streams))
        return self.formats
    
    def set_format(self, format:str) -> bool:
        '''Устанавливает формат format скачиваемому файлу
            \n* True - выбранный формат не находится в списке допустимых 
            \n* False - выбранный формат находится в списке допустимых'''
        if format not in self.formats:
            return True
        # Отсекаем не нужные форматы
        self.inform = self.yt.streams.filter(file_extension=format)
        return False
    
    def found_vidio(self) -> bool:
        '''Поиск видео в фильтре по формату
            \n* True - выбранный формат не поддерживает видео 
            \n* False - выбранный формат поддерживает видео '''
        for i in self.inform:
            if i.type == "video":
                return False
        return True
    
    def found_audio(self) -> bool:
        '''Поиск аудио в фильтре по формату
            \n* True - выбранный формат не поддерживает аудио 
            \n* False - выбранный формат поддерживает аудио '''
        for i in self.inform:
            if i.type == "audio":
                return False
        return True
    
    def set_type(self, type:str) -> None:
        '''Устанавливает тип type скачиваемому файлу
            \n* True - выбранный формат не находится в списке допустимых 
            \n* False - выбранный формат находится в списке допустимых'''
        self.inform = self.inform.filter(file_extension=format)
        