



'''Тупая болванка'''
from pytube import YouTube



class File_YouTube:
    def __init__(self, link) -> None:
        # yt = YouTube('https://www.youtube.com/shorts/96LQhbSIFWI')
        self.yt = YouTube(link)