



from TikTokApi import TikTokApi
api = TikTokApi.get_instance()

results = 10

# Поскольку TikTok изменил свой API, вам нужно использовать опцию custom_verifyFp.
# В своем веб-браузере вам нужно будет зайти в TikTok, войти в систему и получить значение s_v_web_id.
trending = api.trending(count=results, custom_verifyFp="")

for tiktok in trending:
    # Prints the id of the tiktok
    print(tiktok['id'])

print(len(trending))