import requests
import asyncio

url = "webhook_url" # HAHAHHA, I JOINED TO OLD AND UNACTIVE DISCORD SERVER AND I FIND MY WEBHOOK LINK WITH THIS WORDS:

# 🦦 Hey, this webhook's URL was found here: https://github.com/DragonFire1230/dragonfire-source-code-archive/blob/00c72e06f15b63803a5558210af3f965fb3b6118/src/WebHookSpammer.py
# Be more careful in the future, and make sure to not accidentally upload your webhook's URL publicly!

# THIS WAS VERY FUNNY :)))

while True:
    msg = input('Msg> ')

    data = {
        "username" : "Компьютер 2.0",
        "avatar_url": "https://cdn.discordapp.com/avatars/897820066731663381/a_9cca75b36c86a52dc1514ab78c37bfd1.gif?size=96",
        "content" : msg
    }

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))
