from pytube import YouTube


class File_YouTube():
    def __init__(self, link) -> None:
        # yt = YouTube('https://www.youtube.com/shorts/96LQhbSIFWI')
        self.yt = YouTube(link)

    def choose_format(self, form):
        if form == 'Video':
            self.stream = self.yt.streams.get_by_itag(self.yt.streams.filter(mime_type='video/mp4',
                                                                             res='1080p').first().itag)
        elif form == 'Audio':
            self.stream = self.yt.streams.get_by_itag(self.yt.streams.filter(type='audio',
                                                                             mime_type='audio/mp4').first().itag)
        else:
            self.stream = self.yt.streams.get_by_itag(self.yt.streams.filter(progressive=True, res='720p').first().itag)

    def download_video(self):
        self.stream.download(filename='reply.mp4')

    def download_audio(self):
        self.stream.download(filename='reply.mp4')

    def download_both(self):
        self.stream.download(filename='reply.mp4')

