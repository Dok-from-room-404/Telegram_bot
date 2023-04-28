



import requests
from tqdm import tqdm
import os.path






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

    print(f'[+] Название канала получено: "{channel_name}"')
    return channel_name


def get_video_download(vid_id, channel_name):
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

    print(f'[+] Получаю название и ссылку на видео...')
    response = requests.get(f'https://downloader.freemake.com/api/videoinfo/{vid_id}', headers=headers).json()
    #for i in response:
        #print(i, response[i])
    video_title = str(response['metaInfo']['title']) # Имя видео
    print(video_title)
    url = response['qualities']#[0]#['url']
    for i in url:
        #print(i['url'])
        print(i["qualityInfo"])

    
    '''if response['qualities'][0]['qualityInfo']['itag'] == 22:
        video_title = str(response['metaInfo']['title'])
        for m in ["?", '"', "'", "/", ":", "#", "|", ",", " | "]:
            video_title = video_title.replace(m, "")
        url = response['qualities'][0]['url']
        print(f'[+] Название и ссылка получены. Начинаю загрузку: "{video_title}"...')
        if not os.path.isdir(f'{channel_name}'):
            os.mkdir(f'{channel_name}')
            print(f'[+] Создаю папку для сохранения видео...\n')
        else:
            print(f'[+] Папка для сохранения существует...\n')
        req = requests.get(url=url, headers=headers, stream=True)
        total = int(req.headers.get('content-length', 0))
        with open(f'{os.path.join(channel_name, f"{video_title}.mp4")}', 'wb') as file, tqdm(
                desc=f"{video_title[0:int(len(video_title) / 2)]}...",
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in req.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
        print(f'\n[+] Видео сохранено в папку: "{channel_name}".\n[+] Загрузка завершена.\n')
    else:
        user_change = input('\n[+] Нет видео в качестве 720р...\n[+] Загрузить в доступном качестве?:\n'
                            '\t[1]: Да\n\t[2]: Нет\n\t>>> ')
        if user_change == "1":
            video_title = str(response['metaInfo']['title'])
            for m in ["?", '"', "'", "/", ":", "#", "|", ",", " | "]:
                video_title = video_title.replace(m, "")
            url = response['qualities'][0]['url']
            print(f'[+] Название и ссылка получены. Начинаю загрузку: "{video_title}"...')
            if not os.path.isdir(f'{channel_name}'):
                os.mkdir(f'{channel_name}')
                print(f'[+] Создаю папку для сохранения видео...\n')
            else:
                print(f'[+] Папка для сохранения существует...\n')
            req = requests.get(url=url, headers=headers, stream=True)
            total = int(req.headers.get('content-length', 0))
            with open(f'{os.path.join(channel_name, f"{video_title}.mp4")}', 'wb') as file, tqdm(
                    desc=f"{video_title[0:int(len(video_title) / 2)]}...",
                    total=total,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
            ) as bar:
                for data in req.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)
            print(f'\n[+] Видео сохранено в папку: "{channel_name}".\n[+] Загрузка завершена.\n')'''



# vid_id = input('\t[+] Введите ссылку на видео\n\t>>> ')
vid_id = "https://www.youtube.com/watch?v=p_eDvYKKyK0"
#vid_id = 'https://www.youtube.com/watch?v=riYIJaBOQOc'
#vid_id = 'https://www.youtube.com/watch?v=l9K1YvvcX4Y'

vid_id = vid_id.split("=")[-1]



channel_name = get_channel_name(vid_id)
get_video_download(vid_id, channel_name)


#response = requests.get(f'https://downloader.freemake.com/api/videoinfo/9ksTBr3HpFU').json()
#for i in response:
    #print(i, response[i])

#print(yt.streams.filter(file_extension='mp4')) 
#stream = yt.streams.get_by_itag(140) #выбираем по тегу, в каком формате будем скачивать.
#print(stream)
#stream.download() #загружаем видео.




'''

{'isDash': False, 'url': 
    'https://rr2---sn-5hneknek.googlevideo.com/videoplayback?expire=1682683382&ei=lmFLZJHaHNq11gL_lLygCQ&ip=185.192.1.122&id=o-AOdV5x8l8yNXaKgZsCPwQufY2wy6KHZKV0-fTsbpQYSp&itag=140&source=youtube&requiressl=yes&mh=2W&mm=31,26&mn=sn-5hneknek,sn-4g5e6nsr&ms=au,onr&mv=u&mvi=2&pl=22&vprv=1&mime=audio/mp4&ns=37TiiuEam24Tp9c9Ho3feJAN&gir=yes&clen=15380993&dur=950.299&lmt=1682264472665118&mt=1682660847&fvip=4&keepalive=yes&fexp=24007246&c=WEB&txp=5532434&n=m6qXugzmGwwxU0fmvvo&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ns,gir,clen,dur,lmt&sig=AOq0QJ8wRAIgbUGbBYTBppq9fkUfqjPY2DIii_XGgVOgabOVYmrzVVoCIFdOSeoqLuNM6gHza9ISuXp4Ni9O-6iHHdBrFqJeu3yO&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgDxIQ1AUaDMRLh-45R6PGH8z1yGgb74Hbvz9ow8BtYqgCIQDgCJqwdaNi2BFobdVIEQVx__i8vQVHrsQ-O2uJLbMuzQ==&avi=K1A%2FHwERIiwAVF9GU25XdyYrIj0cP31HSFQmDVNZV0E1FigaFRwsBwECFkYZahB9ESg%2BJS0xCSY2MDMwZHNrTQEnIzssPwIpNCkUE0ZDRkolGwYGBAcpAwMeDw97S0pQJhAHGzpRf11BQSdBFnNeEXxQKCwyJxUgIDU3InVldXEJOicjLzkELis6NTtSRldBJAscHwoELBYAEAIMSVpeSQERHxQLGRJAVk5AU2EUB3EuV1tHRylhRycfFQxGQ2ZaPRcaAgQZPUdeVD44AQAEC2JEX0dVQHo5Rlo5RhIHCgFmQ1lAVkERRzkKVFIbAwQFYUVRREdYbzUIFxwFQVheWiQLOgIEADgWRkxHK2gTHhEGGw0TCj0jAwsjFwhqX1ZWKFBTRklWFDEHGRAKV0NLEWpQJzpHWG81FhkdHQELEFskBhlMSlt8XVFYVF0RHwMdYUBbTF1EfVVLVElGblBKfjkcDTUKASMRFg9HXgFjZxF8UCoDFwYoCxAiDAlGQkZSPQJLTEdFe11WQFNVFAkAEXxQLA4RBiwGEBkXMFpBVxFqUAMFChoECzQXAgEBTA%3D%3D&from_cache=True', 
    'urls': ['https://rr2---sn-5hneknek.googlevideo.com/videoplayback?expire=1682683382&ei=lmFLZJHaHNq11gL_lLygCQ&ip=185.192.1.122&id=o-AOdV5x8l8yNXaKgZsCPwQufY2wy6KHZKV0-fTsbpQYSp&itag=140&source=youtube&requiressl=yes&mh=2W&mm=31,26&mn=sn-5hneknek,sn-4g5e6nsr&ms=au,onr&mv=u&mvi=2&pl=22&vprv=1&mime=audio/mp4&ns=37TiiuEam24Tp9c9Ho3feJAN&gir=yes&clen=15380993&dur=950.299&lmt=1682264472665118&mt=1682660847&fvip=4&keepalive=yes&fexp=24007246&c=WEB&txp=5532434&n=m6qXugzmGwwxU0fmvvo&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ns,gir,clen,dur,lmt&sig=AOq0QJ8wRAIgbUGbBYTBppq9fkUfqjPY2DIii_XGgVOgabOVYmrzVVoCIFdOSeoqLuNM6gHza9ISuXp4Ni9O-6iHHdBrFqJeu3yO&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgDxIQ1AUaDMRLh-45R6PGH8z1yGgb74Hbvz9ow8BtYqgCIQDgCJqwdaNi2BFobdVIEQVx__i8vQVHrsQ-O2uJLbMuzQ==&avi=K1A%2FHwERIiwAVF9GU25XdyYrIj0cP31HSFQmDVNZV0E1FigaFRwsBwECFkYZahB9ESg%2BJS0xCSY2MDMwZHNrTQEnIzssPwIpNCkUE0ZDRkolGwYGBAcpAwMeDw97S0pQJhAHGzpRf11BQSdBFnNeEXxQKCwyJxUgIDU3InVldXEJOicjLzkELis6NTtSRldBJAscHwoELBYAEAIMSVpeSQERHxQLGRJAVk5AU2EUB3EuV1tHRylhRycfFQxGQ2ZaPRcaAgQZPUdeVD44AQAEC2JEX0dVQHo5Rlo5RhIHCgFmQ1lAVkERRzkKVFIbAwQFYUVRREdYbzUIFxwFQVheWiQLOgIEADgWRkxHK2gTHhEGGw0TCj0jAwsjFwhqX1ZWKFBTRklWFDEHGRAKV0NLEWpQJzpHWG81FhkdHQELEFskBhlMSlt8XVFYVF0RHwMdYUBbTF1EfVVLVElGblBKfjkcDTUKASMRFg9HXgFjZxF8UCoDFwYoCxAiDAlGQkZSPQJLTEdFe11WQFNVFAkAEXxQLA4RBiwGEBkXMFpBVxFqUAMFChoECzQXAgEBTA%3D%3D&from_cache=True'], 
    'length': 15380993, 'qualityInfo': {'itag': 140, 'format': 'M4a', 'qualityLabel': '', 'type': 3, 'audioBitrate': 128}}
- аудио

 {'isDash': False, 
 'url': 'https://redirector-cf.freemake.com/download/https://rr2---sn-5hneknek.googlevideo.com/videoplayback?expire=1682683382&ei=lmFLZJHaHNq11gL_lLygCQ&ip=185.192.1.122&id=o-AOdV5x8l8yNXaKgZsCPwQufY2wy6KHZKV0-fTsbpQYSp&itag=18&source=youtube&requiressl=yes&mh=2W&mm=31,26&mn=sn-5hneknek,sn-4g5e6nsr&ms=au,onr&mv=u&mvi=2&pl=22&vprv=1&mime=video/mp4&ns=A-wHG1gDLpRLfvtpxKaOz-sN&gir=yes&clen=53337792&ratebypass=yes&dur=950.299&lmt=1682264569243064&mt=1682660847&fvip=4&fexp=24007246&c=WEB&txp=5538434&n=FyQYwnbNIiHsz4CeAo4&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ns,gir,clen,ratebypass,dur,lmt&sig=AOq0QJ8wRAIgIcYPLtFXCE9LPuh4kfDDFeWMRRT-Q5Bxjda0n2hiZkYCIDZgRt245tOffe-TykfRFBeZKwdSbVJrPekzx7fYThew&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgDxIQ1AUaDMRLh-45R6PGH8z1yGgb74Hbvz9ow8BtYqgCIQDgCJqwdaNi2BFobdVIEQVx__i8vQVHrsQ-O2uJLbMuzQ==&avi=K1A%2FHwERIiwAVF9GU25XdyYrIj0cP31HSFQmDVNZV0E1FigaFRwsBwECFkYZahB9ESg%2BJS0xCSY2MDMwZHNrTQEnIzssPwIpNCkUE0ZDRkolGwYGBAcpAwMeDw97S0pQJhAHGzpRf11BQSdBFnNeEXxQKCwyJxUgIDU3InVldXEJOicjLzkELis6NTtSRldBJAscHwoELBYAEAIMSVpeSQERHxQLGRJAVk5AU2EUB3EuV1tHRylhRycfFQxGQ2ZaPRcaAgQZPUdeVD44AQAEC2JEX0dVQHo5Rlo5RhIHCgFmQ1lAVkERRzkKVFIbAwQFYUVRREdYbzUIFxwFQVheWiQLOgIEADgWRkxHK2gTHhEGGw0TCj0jAwsjFwhqX1ZWKFBTRklWFDEHGRAKV0NLEWpQJzpHWG81FhkdHQELEFskBhlMSlt8XVFYVF0RHwMdYUBbTF1EfVVLVElGblBKfjkcDTUKASMRFg9HXgFjZxF8UCoDFwYoCxAiDAlGQkZSPQJLTEdFe11WQFNVFAkAEXxQLA4RBiwGEBkXMFpBVxFqUAMFChoECzQXAgEBTA%3D%3D&from_cache=True',
 'urls': ['https://redirector-cf.freemake.com/download/https://rr2---sn-5hneknek.googlevideo.com/videoplayback?expire=1682683382&ei=lmFLZJHaHNq11gL_lLygCQ&ip=185.192.1.122&id=o-AOdV5x8l8yNXaKgZsCPwQufY2wy6KHZKV0-fTsbpQYSp&itag=18&source=youtube&requiressl=yes&mh=2W&mm=31,26&mn=sn-5hneknek,sn-4g5e6nsr&ms=au,onr&mv=u&mvi=2&pl=22&vprv=1&mime=video/mp4&ns=A-wHG1gDLpRLfvtpxKaOz-sN&gir=yes&clen=53337792&ratebypass=yes&dur=950.299&lmt=1682264569243064&mt=1682660847&fvip=4&fexp=24007246&c=WEB&txp=5538434&n=FyQYwnbNIiHsz4CeAo4&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ns,gir,clen,ratebypass,dur,lmt&sig=AOq0QJ8wRAIgIcYPLtFXCE9LPuh4kfDDFeWMRRT-Q5Bxjda0n2hiZkYCIDZgRt245tOffe-TykfRFBeZKwdSbVJrPekzx7fYThew&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgDxIQ1AUaDMRLh-45R6PGH8z1yGgb74Hbvz9ow8BtYqgCIQDgCJqwdaNi2BFobdVIEQVx__i8vQVHrsQ-O2uJLbMuzQ==&avi=K1A%2FHwERIiwAVF9GU25XdyYrIj0cP31HSFQmDVNZV0E1FigaFRwsBwECFkYZahB9ESg%2BJS0xCSY2MDMwZHNrTQEnIzssPwIpNCkUE0ZDRkolGwYGBAcpAwMeDw97S0pQJhAHGzpRf11BQSdBFnNeEXxQKCwyJxUgIDU3InVldXEJOicjLzkELis6NTtSRldBJAscHwoELBYAEAIMSVpeSQERHxQLGRJAVk5AU2EUB3EuV1tHRylhRycfFQxGQ2ZaPRcaAgQZPUdeVD44AQAEC2JEX0dVQHo5Rlo5RhIHCgFmQ1lAVkERRzkKVFIbAwQFYUVRREdYbzUIFxwFQVheWiQLOgIEADgWRkxHK2gTHhEGGw0TCj0jAwsjFwhqX1ZWKFBTRklWFDEHGRAKV0NLEWpQJzpHWG81FhkdHQELEFskBhlMSlt8XVFYVF0RHwMdYUBbTF1EfVVLVElGblBKfjkcDTUKASMRFg9HXgFjZxF8UCoDFwYoCxAiDAlGQkZSPQJLTEdFe11WQFNVFAkAEXxQLA4RBiwGEBkXMFpBVxFqUAMFChoECzQXAgEBTA%3D%3D&from_cache=True'], 
 'length': 53337792, 'qualityInfo': {'itag': 18, 'format': 'Mp4', 'qualityLabel': '360p', 'type': 2, 'audioBitrate': 96}}
- видео + аудио 
 
 {'isDash': False, 
 'url': 'https://rr2---sn-5hneknek.googlevideo.com/videoplayback?expire=1682683382&ei=lmFLZJHaHNq11gL_lLygCQ&ip=185.192.1.122&id=o-AOdV5x8l8yNXaKgZsCPwQufY2wy6KHZKV0-fTsbpQYSp&itag=22&source=youtube&requiressl=yes&mh=2W&mm=31,26&mn=sn-5hneknek,sn-4g5e6nsr&ms=au,onr&mv=u&mvi=2&pl=22&vprv=1&mime=video/mp4&ns=A-wHG1gDLpRLfvtpxKaOz-sN&cnr=14&ratebypass=yes&dur=950.299&lmt=1682267530537739&mt=1682660847&fvip=4&fexp=24007246&c=WEB&txp=5532434&n=FyQYwnbNIiHsz4CeAo4&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ns,cnr,ratebypass,dur,lmt&sig=AOq0QJ8wRgIhAPlgjyDzNrnqi5vNLqYus9Of_LPYW0A8dwLdF-TaH5zGAiEAxLjtiQ13SSQRwEGaGQSf7_X0gt4rj4Rk6rBvnOHuKZE=&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgDxIQ1AUaDMRLh-45R6PGH8z1yGgb74Hbvz9ow8BtYqgCIQDgCJqwdaNi2BFobdVIEQVx__i8vQVHrsQ-O2uJLbMuzQ==&avi=K1A%2FHwERIiwAVF9GU25XdyYrIj0cP31HSFQmDVNZV0E1FigaFRwsBwECFkYZahB9ESg%2BJS0xCSY2MDMwZHNrTQEnIzssPwIpNCkUE0ZDRkolGwYGBAcpAwMeDw97S0pQJhAHGzpRf11BQSdBFnNeEXxQKCwyJxUgIDU3InVldXEJOicjLzkELis6NTtSRldBJAscHwoELBYAEAIMSVpeSQERHxQLGRJAVk5AU2EUB3EuV1tHRylhRycfFQxGQ2ZaPRcaAgQZPUdeVD44AQAEC2JEX0dVQHo5Rlo5RhIHCgFmQ1lAVkERRzkKVFIbAwQFYUVRREdYbzUIFxwFQVheWiQLOgIEADgWRkxHK2gTHhEGGw0TCj0jAwsjFwhqX1ZWKFBTRklWFDEHGRAKV0NLEWpQJzpHWG81FhkdHQELEFskBhlMSlt8XVFYVF0RHwMdYUBbTF1EfVVLVElGblBKfjkcDTUKASMRFg9HXgFjZxF8UCoDFwYoCxAiDAlGQkZSPQJLTEdFe11WQFNVFAkAEXxQLA4RBiwGEBkXMFpBVxFqUAMFChoECzQXAgEBTA%3D%3D&from_cache=True',
 'urls': ['https://rr2---sn-5hneknek.googlevideo.com/videoplayback?expire=1682683382&ei=lmFLZJHaHNq11gL_lLygCQ&ip=185.192.1.122&id=o-AOdV5x8l8yNXaKgZsCPwQufY2wy6KHZKV0-fTsbpQYSp&itag=22&source=youtube&requiressl=yes&mh=2W&mm=31,26&mn=sn-5hneknek,sn-4g5e6nsr&ms=au,onr&mv=u&mvi=2&pl=22&vprv=1&mime=video/mp4&ns=A-wHG1gDLpRLfvtpxKaOz-sN&cnr=14&ratebypass=yes&dur=950.299&lmt=1682267530537739&mt=1682660847&fvip=4&fexp=24007246&c=WEB&txp=5532434&n=FyQYwnbNIiHsz4CeAo4&sparams=expire,ei,ip,id,itag,source,requiressl,vprv,mime,ns,cnr,ratebypass,dur,lmt&sig=AOq0QJ8wRgIhAPlgjyDzNrnqi5vNLqYus9Of_LPYW0A8dwLdF-TaH5zGAiEAxLjtiQ13SSQRwEGaGQSf7_X0gt4rj4Rk6rBvnOHuKZE=&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgDxIQ1AUaDMRLh-45R6PGH8z1yGgb74Hbvz9ow8BtYqgCIQDgCJqwdaNi2BFobdVIEQVx__i8vQVHrsQ-O2uJLbMuzQ==&avi=K1A%2FHwERIiwAVF9GU25XdyYrIj0cP31HSFQmDVNZV0E1FigaFRwsBwECFkYZahB9ESg%2BJS0xCSY2MDMwZHNrTQEnIzssPwIpNCkUE0ZDRkolGwYGBAcpAwMeDw97S0pQJhAHGzpRf11BQSdBFnNeEXxQKCwyJxUgIDU3InVldXEJOicjLzkELis6NTtSRldBJAscHwoELBYAEAIMSVpeSQERHxQLGRJAVk5AU2EUB3EuV1tHRylhRycfFQxGQ2ZaPRcaAgQZPUdeVD44AQAEC2JEX0dVQHo5Rlo5RhIHCgFmQ1lAVkERRzkKVFIbAwQFYUVRREdYbzUIFxwFQVheWiQLOgIEADgWRkxHK2gTHhEGGw0TCj0jAwsjFwhqX1ZWKFBTRklWFDEHGRAKV0NLEWpQJzpHWG81FhkdHQELEFskBhlMSlt8XVFYVF0RHwMdYUBbTF1EfVVLVElGblBKfjkcDTUKASMRFg9HXgFjZxF8UCoDFwYoCxAiDAlGQkZSPQJLTEdFe11WQFNVFAkAEXxQLA4RBiwGEBkXMFpBVxFqUAMFChoECzQXAgEBTA%3D%3D&from_cache=True'], 
 'length': 108461606, 'qualityInfo': {'itag': 22, 'format': 'Mp4', 'qualityLabel': '720p', 'type': 2, 'audioBitrate': 192}}
- видео + аудио 
'''