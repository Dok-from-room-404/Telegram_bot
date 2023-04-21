



from pytube import YouTube
from io import BytesIO



class File_YouTube:
    '''Данный класс необходим для взаимодействия с YouTube (выкачка файлов)'''
    def __init__(self, link) -> None:
        '''Инициализируем класс'''
        # видео на YouTube (неопределено по формату и качеству)
        self.yt = YouTube(link)
        self.formats = set()
        self.inform = None
        self.files = {}
        self.name_format = ""
        
    # def append_link(self, link:str) -> None:
    #     '''Добавляем ссылку'''
    #     self.yt = YouTube(link)
        
        
    def format(self) -> set:
        '''Определяем формат у видео'''
        if len(self.formats) == 0:
            print(self.yt.streams)
            self.formats = set()
            for i in self.yt.streams:
                self.formats.add(i.mime_type.replace(i.type, "")[1:])
            #self.formats = set(map(lambda i: i.mime_type.replace(i.type, "")[1:], self.yt.streams))
        return self.formats
    
    def set_format(self, format:str) -> bool:
        '''Устанавливает формат format скачиваемому файлу
            \n* True - выбранный формат не находится в списке допустимых 
            \n* False - выбранный формат находится в списке допустимых'''
        if format not in self.formats:
            return True
        # Отсекаем не нужные форматы
        self.inform = self.yt.streams.filter(file_extension=format)
        self.name_format = format
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
        self.inform = self.inform.filter(type=type)
        
    def found_audio_file(self) -> None:
        '''Находим возможные варианты аудио с параметрами (битрейт – (abr),
            формат сжатия аудио – (audio_codec))'''
        for i in self.inform:
            print(i)
            st = "Битрейт: {abr}, Формат сжатия аудио: {audio_codec}".format(abr = i.abr, audio_codec = i.audio_codec)
            self.files[st] = int(i.itag)
            
    def dowload_audio_file(self, inform):
        id = self.files[inform]
        stream = self.inform.get_by_itag(id)
        byte_io = BytesIO()
        stream.stream_to_buffer(byte_io)
        
        byte_io.name = "{name}.{format}".format(name = stream.title, format = self.name_format)
        byte_io.seek(0)
        return byte_io
        
        