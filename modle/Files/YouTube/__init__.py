from io import BytesIO

import requests
from tqdm import tqdm


def get_channel_name(vid_id):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.141 Safari/537.36',
        'accept': '*/*',
    }

    params = {
        'key': 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        'prettyPrint': 'false',
    }

    json_data = {
        'videoId': vid_id,
        'context': {
            'client': {
                'hl': 'ru',
                'gl': 'RU',
                'remoteHost': '31.173.242.98',
                'deviceMake': '',
                'deviceModel': '',
                'visitorData': 'CgtrdUNhZ3U2VGNEOCiDndSTBg%3D%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/98.0.4758.141 Safari/537.36,gzip(gfe)',
                'clientName': 'WEB',
                'clientVersion': '2.20220502.01.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': 'https://www.youtube.com/watch?v=4MPWVKFaLD8',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CIOd1JMGELiLrgUQmN79EhCUj64FEOqQrgUQw_KtBRCY6q0FELfLrQUQ8IKuBRC7ka4FENSDrgUQ6JCu'
                                      'BRCw7q0FEK_yrQUQgub9EhCR-PwSENi-rQU%3D',
                },
                'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                'timeZone': 'Asia/Omsk',
                'browserName': 'Chrome',
                'browserVersion': '98.0.4758.141',
                'screenWidthPoints': 1137,
                'screenHeightPoints': 870,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': 360,
                'connectionType': 'CONN_CELLULAR_4G',
                'memoryTotalKbytes': '8000000',
                'mainAppWebInfo': {
                    'graftUrl': 'https://www.youtube.com/watch?v=4MPWVKFaLD8',
                    'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                    'isWebNativeShareAvailable': True,
                },
                'playerType': 'UNIPLAYER',
                'tvAppInfo': {
                    'livingRoomAppMode': 'LIVING_ROOM_APP_MODE_UNSPECIFIED',
                },
                'clientScreen': 'WATCH_FULL_SCREEN',
            },
            'user': {
                'lockedSafetyMode': False,
            },
            'request': {
                'useSsl': True,
                'internalExperimentFlags': [],
                'consistencyTokenJars': [],
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1651838604229',
                    },
                    {
                        'key': 'flash',
                        'value': '0',
                    },
                    {
                        'key': 'frm',
                        'value': '0',
                    },
                    {
                        'key': 'u_tz',
                        'value': '360',
                    },
                    {
                        'key': 'u_his',
                        'value': '5',
                    },
                    {
                        'key': 'u_h',
                        'value': '1080',
                    },
                    {
                        'key': 'u_w',
                        'value': '1920',
                    },
                    {
                        'key': 'u_ah',
                        'value': '1032',
                    },
                    {
                        'key': 'u_aw',
                        'value': '1920',
                    },
                    {
                        'key': 'u_cd',
                        'value': '24',
                    },
                    {
                        'key': 'bc',
                        'value': '31',
                    },
                    {
                        'key': 'bih',
                        'value': '870',
                    },
                    {
                        'key': 'biw',
                        'value': '1121',
                    },
                    {
                        'key': 'brdim',
                        'value': '43,12,43,12,1920,0,1708,991,1137,870',
                    },
                    {
                        'key': 'vis',
                        'value': '1',
                    },
                    {
                        'key': 'wgl',
                        'value': 'true',
                    },
                    {
                        'key': 'ca_type',
                        'value': 'image',
                    },
                ],
            },
        },
        'playbackContext': {
            'contentPlaybackContext': {
                'html5Preference': 'HTML5_PREF_WANTS',
                'lactMilliseconds': '2979',
                'referer': 'https://www.youtube.com/watch?v=4MPWVKFaLD8',
                'signatureTimestamp': 19117,
                'autonavState': 'STATE_OFF',
                'autoCaptionsDefaultOn': False,
                'mdxContext': {},
                'playerWidthPixels': 647,
                'playerHeightPixels': 364,
            },
        },
        'cpn': 'pwy4NMkpT8PY63hl',
        'captionParams': {
            'deviceCaptionsOn': True,
        },
        'attestationRequest': {
            'omitBotguardData': True,
        },
    }

    channel_name = str(requests.post('https://www.youtube.com/youtubei/v1/player', params=params, headers=headers,
                                     json=json_data).json()['videoDetails']['author'])

    # print(f'[+] Название канала получено: "{channel_name}"')
    return channel_name


def get_response(vid_id):
    headers = {
        'authority': 'downloader.freemake.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Yandex";v="22"',
        'dnt': '1',
        'x-cf-country': 'RU',
        'sec-ch-ua-mobile': '?0',
        'x-user-platform': 'Win32',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'x-user-browser': 'YaBrowser',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36',
        'x-analytics-header': 'UA-18256617-1',
        'x-request-attempt': '1',
        'x-user-id': '94119398-e27a-3e13-be17-bbe7fbc25874',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.freemake.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.freemake.com/ru/free_video_downloader/',
        'accept-language': 'ru,en;q=0.9,uk;q=0.8',
    }

    response = requests.get(f'https://downloader.freemake.com/api/videoinfo/{vid_id}', headers=headers).json()
    return response


class File_YouTube:
    """Данный класс необходим для взаимодействия с YouTube (выкачка файлов)"""

    def __init__(self, link) -> None:
        """Инициализируем класс"""
        # видео на YouTube (неопределено по формату и качеству)
        # self.yt = YouTube(link)
        vid_id = link.split("=")[-1]

        self.channel_name = get_channel_name(vid_id)
        self.response = get_response(vid_id)

        # https://www.youtube.com/watch?v=9ksTBr3HpFU

        # print(response)
        self.formats = set()
        self.inform = []
        self.files = {}
        self.name_format = ""

    def get_info(self):
        return None, None, None

    def format(self) -> set:
        """Определяем формат у видео"""
        if len(self.formats) == 0:
            self.formats = set()
            print("pp")
            url = self.response['qualities']  # [0]#['url']
            for i in url:
                # print(i['url'])
                print(i["qualityInfo"]['format'])
                self.formats.add(i["qualityInfo"]['format'])
        return self.formats

    def set_format(self, format: str) -> bool:
        """Устанавливает формат format скачиваемому файлу
            \n* True - выбранный формат не находится в списке допустимых
            \n* False - выбранный формат находится в списке допустимых"""
        if format not in self.formats:
            return True
        # Отсекаем не нужные форматы
        url = self.response['qualities']
        for i in url:
            if i["qualityInfo"]['format'] == format:
                self.inform.append(i)

        self.name_format = format
        return False

    def found_video(self) -> bool:
        """Поиск видео в фильтре по формату
            \n* False - выбранный формат не поддерживает видео
            \n* True - выбранный формат поддерживает видео """
        for i in self.inform:
            if i["qualityInfo"]['qualityLabel'] != '':
                return True
        return False

    def found_audio(self) -> bool:
        """Поиск аудио в фильтре по формату
            \n* False - выбранный формат не поддерживает аудио
            \n* True - выбранный формат поддерживает аудио """
        for i in self.inform:
            if i["qualityInfo"]['audioBitrate'] != '':
                return True
        return False

    def set_type(self, type: str) -> None:
        """Устанавливает тип type скачиваемому файлу
            \n* True - выбранный формат не находится в списке допустимых
            \n* False - выбранный формат находится в списке допустимых"""
        print("seter")
        for i in self.inform:
            print(i)
        print(type)
        spp = []
        if type == "audio":
            par = 'audioBitrate'
        if type == "video":
            par = 'qualityLabel'

        for i in self.inform:
            if i["qualityInfo"][par] != '':
                spp.append(i)
        for i in spp:
            print(i["qualityInfo"])
        print(self.inform)
        self.inform = spp
        print(self.inform)
        print("pass_seter")

    def found_audio_file(self) -> None:
        """Находим возможные варианты аудио с параметрами (битрейт – (abr),
            формат сжатия аудио – (audio_codec))"""
        # self.files = {}
        for i in self.inform:
            print(i)
            st = "Битрейт: {audioBitrate}".format(audioBitrate=i["qualityInfo"]["audioBitrate"])
            self.files[st] = int(i['qualityInfo']["itag"])

    def download_audio_file(self, inform):
        print("download_audio_file")
        headers = {
            'authority': 'downloader.freemake.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Yandex";v="22"',
            'dnt': '1',
            'x-cf-country': 'RU',
            'sec-ch-ua-mobile': '?0',
            'x-user-platform': 'Win32',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'x-user-browser': 'YaBrowser',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/98.0.4758.141 YaBrowser/22.3.3.852 Yowser/2.5 Safari/537.36',
            'x-analytics-header': 'UA-18256617-1',
            'x-request-attempt': '1',
            'x-user-id': '94119398-e27a-3e13-be17-bbe7fbc25874',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://www.freemake.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.freemake.com/ru/free_video_downloader/',
            'accept-language': 'ru,en;q=0.9,uk;q=0.8',
        }

        print(self.files)
        id = self.files[inform]
        print(id)
        for i in self.inform:
            if i['qualityInfo']["itag"] == id:
                stream = i
                break
        name = str(self.response['metaInfo']['title'])
        url = stream['url']
        req = requests.get(url=url, headers=headers, stream=True)
        total = int(req.headers.get('content-length', 0))
        print(url)

        byte_io = BytesIO()
        # stream.stream_to_buffer(byte_io)

        # total = int(req.headers.get('content-length', 0))

        print("Запись")
        with tqdm(desc=f"{name[0:int(len(name) / 2)]}...",
                  total=total, unit='iB',
                  unit_scale=True, unit_divisor=1024, ) as bar:
            for data in req.iter_content(chunk_size=1024):
                size = byte_io.write(data)
                bar.update(size)

        print("Запись окончена")
        byte_io.name = "{name}.{format}".format(name=name, format=self.name_format)
        byte_io.seek(0)
        return byte_io

    def found_video_file(self) -> None:
        '''Находим возможные варианты аудио с параметрами (битрейт – (abr),
            формат сжатия аудио – (audio_codec))'''
        # self.files = {}
        for i in self.inform:
            print(i["qualityInfo"])
            codec = i["qualityInfo"]["audioBitrate"]
            if codec == '':
                st = ''' Разрешение видео {res}, Наличие аудио: {progressive} , Битрейт: {audioBitrate}'''.format(
                    res=i["qualityInfo"]["qualityLabel"],
                    progressive="Нет",
                    audioBitrate="Нет")
            else:
                st = '''Разрешение видео {res}, Наличие аудио: {progressive} , Битрейт: {audioBitrate}'''.format(
                    res=i["qualityInfo"]["qualityLabel"],
                    progressive="Есть",
                    audioBitrate=codec)
            self.files[st] = int(i['qualityInfo']["itag"])
