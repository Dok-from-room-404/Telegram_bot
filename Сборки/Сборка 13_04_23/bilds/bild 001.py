



from pytube import YouTube
import pytube.query
from pytube.cli import on_progress
# https://www.youtube.com/shorts/96LQhbSIFWI
yt = YouTube('https://www.youtube.com/watch?v=rMzt3CBS4EY') #ссылка на видео.
# yt.stream показывает какое видео ты можешь скачать 
# (mp4(720) + audio или только mp4(1080) без звука). 
# Сейчас стоит фильтр по mp4.

for i in yt.streams.filter(file_extension="mp4"):
    print(i)
print(yt.streaming_data)
print(yt.author)
print(yt.views)
print(yt.metadata)
print(yt.publish_date)
print(yt.title)




#print(yt.streams.filter(file_extension='mp4')) 
#stream = yt.streams.get_by_itag(140) #выбираем по тегу, в каком формате будем скачивать.
#print(stream)
#stream.download() #загружаем видео.