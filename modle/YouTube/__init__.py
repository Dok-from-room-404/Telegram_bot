



from pytube import YouTube



class File_YouTube:
    '''Данный класс необходим для взаимодействия с YouTube (выкачка файлов)'''
    def __init__(self, link:str) -> None:
        '''Инициализируем класс
        * link - Ссылка на видео'''
        # видео на YouTube (неопределено по формату и качеству)
        self.yt = YouTube(link)
        self.formats = set()
        
    def format(self) -> set:
        '''Определяем формат у видео'''
        self.formats = set(map(lambda i: i.mime_type.replace(i.type, "")[1:], self.yt.streams))
        return self.formats