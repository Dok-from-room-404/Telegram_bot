



from pytube import YouTube
# https://www.youtube.com/shorts/96LQhbSIFWI
yt = YouTube('https://www.youtube.com/shorts/96LQhbSIFWI') #ссылка на видео.
# yt.stream показывает какое видео ты можешь скачать 
# (mp4(720) + audio или только mp4(1080) без звука). 
# Сейчас стоит фильтр по mp4.
# print(type(yt.streams))
for i in yt.streams.filter(type="audio"):
    print(i)


#print(yt.streams.filter(file_extension='mp4')) 
stream = yt.streams.get_by_itag(140) #выбираем по тегу, в каком формате будем скачивать.
#print(stream)
stream.download() #загружаем видео.