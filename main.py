import json
from urllib.request import urlopen
from urllib.parse import urlencode

url = 'https://engil.ru:1500/ispmgr'
owner = 'angel42528'
webdomain_params = {
    "authinfo": "root:JKkj3iu3ukjejkdewJKjkdJLKJjkwdjkwjJHJfwjdwjh11",
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

print(domains)