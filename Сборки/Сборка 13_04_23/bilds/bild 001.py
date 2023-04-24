



from pytube import YouTube
import pytube.query
from pytube.cli import on_progress
# https://www.youtube.com/shorts/96LQhbSIFWI
yt = YouTube('https://www.youtube.com/watch?v=4n3zXfkAVZg') #ссылка на видео.
# yt.stream показывает какое видео ты можешь скачать 
# (mp4(720) + audio или только mp4(1080) без звука). 
# Сейчас стоит фильтр по mp4.
# print(type(yt.streams))
for i in yt.streams.filter(file_extension="mp4"):
    print(i)
    i: pytube.query.StreamQuery
    print(i.audio_codec)


#print(yt.streams.filter(file_extension='mp4')) 
#stream = yt.streams.get_by_itag(140) #выбираем по тегу, в каком формате будем скачивать.
#print(stream)
#stream.download() #загружаем видео.