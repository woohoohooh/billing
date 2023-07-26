import json
from urllib.request import urlopen
from urllib.parse import urlencode

url = 'https://engil.ru:1500/ispmgr'

params = {
    "authinfo": "root:JKkj3iu3ukjejkdewJKjk",
    "out": "json",
    "func": "user.edit",
    "name": "sgenerajjj72",
    "passwd": "LKIK32i389(wdw2",
    "confirm": "LKIK32i389(wdw2",
    "sok": "ok"
}

res = urlopen(url + '?' + '&'.join(f"{k}={v}" for k, v in params.items()))
data = json.loads(res.read().decode('utf-8'))

print(data)
