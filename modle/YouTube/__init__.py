



'''Тупая болванка'''
from pytube import YouTube



class File_YouTube:
    '''Данный класс необходим для взаимодействия с YouTube (выкачка файлов)'''
    def __init__(self, link:str) -> None:
        '''Инициализируем класс
        * link - Ссылка на видео'''
        # видео на YouTube (неопределено по формату и качеству)
        self.yt = YouTube(link)
        
    def format(self):
        '''Определяем формат у видео'''
        formats = set()
        for i in self.yt.streams:
            formats.add(i.mime_type.replace(i.type, "")[1:])
        print(formats)