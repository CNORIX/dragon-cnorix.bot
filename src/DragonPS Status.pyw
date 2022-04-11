import requests
import time

while True:
    requests.get('http://ps.fhgdps.com/dragonpsgdps/mods/statuspageping.php')
    print('completed get')
    time.sleep(2)
    requests.post('http://ps.fhgdps.com/dragonpsgdps/mods/statuspageping.php')
    print('completed post')
    time.sleep(2)