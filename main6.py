import json
import random
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://45.81.227.205:1500/ispmgr'

name = 'angel' + ''.join(random.choice('123456789') for _ in range(5))

params = {
    "authinfo": "root:LKIeefiiuUife7738^87383223877282737878%^^aswjk2s2WdD",
    "out": "json",
    "func": "user.edit",
    "name": name,
    "passwd": "LKIK32ioII389(wdw",
    "confirm": "LKIK32ioII389(wdw",
    "sok": "ok"
}

res = urlopen(url + '?' + '&'.join(f"{k}={v}" for k, v in params.items()))
data = json.loads(res.read().decode('utf-8'))

print(data)