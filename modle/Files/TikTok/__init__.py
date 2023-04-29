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
