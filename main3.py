from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://engil.ru:1500/ispmgr'

params = {
    'authinfo': 'root:LKIeefiiuUife7738^&^8738322387^&^&7282737878%^^&@aswjk2s@2WdD',
    'out': 'json',
    'func': 'webdomain',
    'elid': 'angel69542'
}
res = urlopen(url + '?' + '&'.join(f"{k}={v}" for k, v in params.items()))

print(res)

# Обработка списка доменов
for domain in res:
    print(domain)
