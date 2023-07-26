import json
import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://45.81.227.205:1500/ispmgr'

params = {
    "authinfo": "root:LKIeefiiuUife7738^&^8738322387^&^&7282737878%^^&@aswjk2s@2WdD",
    "out": "json",
    'func': 'webdomain'
}

response = requests.get(url, params=params)
data = response.json()

print(data)
