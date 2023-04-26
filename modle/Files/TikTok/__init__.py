import requests
from const import HEADERS, URL


class TikTokFile:
	def __init__(self, link):
		self.link = link
		self.querystring = {'url': link, 'hd': '0'}
		self.response = None

	def get_request(self):
		self.response = requests.get(URL, headers=HEADERS, params=self.querystring).json()
		print(self.response)

	def get_video(self):
		return self.response['data']['play']

	def get_audio(self):
		return self.response['data']['music']

	def get_info(self):
		return self.response['data']['title'], self.response['data']['duration'], self.response['data']['author']['nickname']


a = {'code': 0, 'msg': 'success', 'processed_time': 0.1889,
 'data': {'aweme_id': 'v12044gd0000cafum43c77u65l2kj0jg',
		  'id': '7106658991907802411', 'region': 'US',
		  'title': 'which biome style are you? 🛶🐠🕯🏔 #Minecraft',
		  'cover': 'https://p19-sign.tiktokcdn-us.com/obj/tos-useast5-p-0068-tx/4f940b4be2814fc6993f7807ecefcd16_1654647989?x-expires=1682586000&x-signature=8DmVgM6OB0fuhMO1ptMYoSfxK%2FA%3D&s=AWEME_DETAIL&se=false&sh=&sc=dynamic_cover&l=202304260906048BF2C7D29E545805E06A', 'origin_cover': 'https://p16-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/8d1f933115514abbab4e3ce6a4d2b836_1654647988~tplv-tiktokx-360p.jpeg?x-expires=1682586000&x-signature=qL8vfL179na1YN7G6OSWaE4WCFg%3D&s=AWEME_DETAIL&se=false&sh=&sc=feed_cover&l=202304260906048BF2C7D29E545805E06A', 'duration': 22, 'play': 'https://v16m-default.akamaized.net/29d5971de359f23b26b644587d290b5b/64493df3/video/tos/maliva/tos-maliva-ve-0068c799-us/4c875ae630294556bd3dd3810fd55c56/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=1366&bt=683&cs=0&ds=6&ft=iJOG.y7oZzv0PD1M9j9Xg9wk.-MrBEeC~&mime_type=video_mp4&qs=0&rc=aTU6NWQ5Z2lmaWU4N2hkOEBpajNubzk6Zjd4ZDMzZzczNEAvYl8wMzQxNV8xNDZjLjFiYSNnZy8ycjQwamNgLS1kMS9zcw%3D%3D&l=202304260906048BF2C7D29E545805E06A&btag=80000', 'wmplay': 'https://v16m-default.akamaized.net/19876dfc9f9d071c5787e28f29cb5be5/64493df3/video/tos/maliva/tos-maliva-ve-0068c799-us/02cb5475032c4631bf85b05d0822b05f/?a=0&ch=0&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=1418&bt=709&cs=0&ds=3&ft=iJOG.y7oZzv0PD1M9j9Xg9wk.-MrBEeC~&mime_type=video_mp4&qs=0&rc=OGg7NzY3OzVmZ2g6OGQ2OUBpajNubzk6Zjd4ZDMzZzczNEBiNjQwMl8uXi4xMjAvNTEvYSNnZy8ycjQwamNgLS1kMS9zcw%3D%3D&l=202304260906048BF2C7D29E545805E06A&btag=80000', 'size': 1957413, 'wm_size': 2383250, 'music': 'https://sf16-ies-music-va.tiktokcdn.com/obj/ies-music-ttp-dup-us/7106658973058599722.mp3', 'music_info': {'id': '7106658961021225774', 'title': 'original sound - tiktok', 'play': 'https://sf16-ies-music-va.tiktokcdn.com/obj/ies-music-ttp-dup-us/7106658973058599722.mp3', 'cover': 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/1971e99be0d67160f34f39fb1d66a0e5~c5_1080x1080.jpeg?x-expires=1682586000&x-signature=8aJ6zPGSKoqrhOjaouVjNLm3tWU%3D', 'author': 'TikTok', 'original': True, 'duration': 22, 'album': ''}, 'play_count': 633171, 'digg_count': 21057, 'comment_count': 1288, 'share_count': 195, 'download_count': 95, 'create_time': 1654647988, 'author': {'id': '107955', 'unique_id': 'tiktok', 'nickname': 'TikTok', 'avatar': 'https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/1971e99be0d67160f34f39fb1d66a0e5~c5_300x300.jpeg?x-expires=1682586000&x-signature=SNuu9ZIqvAzXc0C%2BBDelHXotOCc%3D'}}}
