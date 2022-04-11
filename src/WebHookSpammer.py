import requests
import asyncio

url = "https://discord.com/api/webhooks/942441163493896262/5el6z0brswx99Rp2x3cVr745Eeq-fN3HiPVDKYmhXfxD4hdVZHc1Vtx0j952_RaG_iih"

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