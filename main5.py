import json
from urllib.request import urlopen
from urllib.parse import urlencode
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://45.81.227.205:1500/ispmgr'
owner = 'angel52528'
webdomain_params = {
    "authinfo": "root:LKIeefiiuUife7738^&^8738322387^&^&7282737878%^^&@aswjk2s@2WdD",
    "out": "json",
    "func": "webdomain",
    "owner": owner
}
webdomain_url_with_params = url + '?' + urlencode(webdomain_params)
webdomain_response = urlopen(webdomain_url_with_params)
webdomain_data = json.loads(webdomain_response.read().decode('utf-8'))
user_domains = [domain for domain in webdomain_data['doc']['elem'] if domain['owner']['$'] == owner]
domains = []
for i in user_domains:
    domains.append(i['docroot']['$'].replace('www/', ''))