from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from urllib.request import urlopen
from urllib.parse import urlencode
import json
import random
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'billing/index.html', {'form': form})

# initial={'username': '' + ''.join(random.choice('123456789') for _ in range(5)), 'email': 'afwefewfwe@2fewfwe.com', 'password': 'artart11R%'}

def index2(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            user = form.save(commit=False)
            generated_name = 'b' + ''.join(random.choice('123456789') for _ in range(10))
            generated_name2 = 'angel' + ''.join(random.choice('123456789') for _ in range(5))
            user.username = generated_name
            auth_user = authenticate(username=generated_name, password=form.cleaned_data['password'])
            login(request, auth_user)
            user.save()
            url = 'https://engil.ru:1500/ispmgr'
            params = {
                "authinfo": "root:JKkj3iu3ukjejkdewJKjkdJLKJjkwdjkwjJHJfwjdwjh11",
                "out": "json",
                "func": "user.edit",
                "name": generated_name2,
                "passwd": "LKIK32ioII389(wdw",
                "confirm": "LKIK32ioII389(wdw",
                "sok": "ok"
            }
            res = urlopen(url + '?' + '&'.join(f"{k}={v}" for k, v in params.items()))
            return render(request, 'billing/dashboard.html')
    else:
        form = RegistrationForm()
    return render(request, 'billing/index2.html', {'form': form})

# def index2(request):
#     if request.method == 'POST':
#         print('1')
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             print('2')
#             user = form.save(commit=False)
#             generated_name = 'a' + ''.join(random.choice('123456789') for _ in range(10))
#             generated_name2 = 'angel' + ''.join(random.choice('123456789') for _ in range(5))
#             user.username = generated_name
#             auth_user = authenticate(username=generated_name, password=form.cleaned_data['password1'])
#             login(request, auth_user)
#             user.save()
#             url = 'https://engil.ru:1500/ispmgr'
#             params = {
#                 "authinfo": "root:JKkj3iu3ukjejkdewJKjkdJLKJjkwdjkwjJHJfwjdwjh11",
#                 "out": "json",
#                 "func": "user.edit",
#                 "name": generated_name2,
#                 "passwd": "LKIK32ioII389(wdw",
#                 "confirm": "LKIK32ioII389(wdw",
#                 "sok": "ok"
#             }
#             res = urlopen(url + '?' + '&'.join(f"{k}={v}" for k, v in params.items()))
#             return render(request, 'billing/dashboard.html')
#     else:
#         print('4')
#         form = RegistrationForm(initial={'username': 'angel' + ''.join(random.choice('123456789') for _ in range(5))})
#     return render(request, 'billing/index2.html', {'form': form})

@login_required
def dashboard(request):
    url = 'https://engil.ru:1500/ispmgr'
    owner = request.user.username
    print(owner)
    webdomain_params = {
        "authinfo": "root:JKkj3iu3ukjejkdewJKjkdJLKJjkwdjkwjJHJfwjdwjh11",
        "out": "json",
        "func": "webdomain",
        "owner": 'angel39675'
    }
    webdomain_url_with_params = url + '?' + urlencode(webdomain_params)
    webdomain_response = urlopen(webdomain_url_with_params)
    webdomain_data = json.loads(webdomain_response.read().decode('utf-8'))
    user_domains = [domain for domain in webdomain_data['doc']['elem'] if domain['owner']['$'] == 'angel39675']
    domains = []
    for i in user_domains:
        domains.append(i['docroot']['$'].replace('www/', ''))

    url = 'https://45.81.227.205:1500/ispmgr'
    bd_params = {
        "authinfo": 'root:JKkj3iu3ukjejkdewJKjkdJLKJjkwdjkwjJHJfwjdwjh11',
        'out': 'json',
        'func': 'ftp.user',
        'owner': 'angel39675',
    }
    bd_url_with_params = url + '?' + urlencode(bd_params)
    bd_response = urlopen(bd_url_with_params)
    bd_data = json.loads(bd_response.read().decode('utf-8'))
    print()
    print(bd_data)
    print()
    user_bd = [bd for bd in bd_data['doc']['elem'] if bd['owner']['$'] == 'angel39675']
    bd = []
    # for i in user_bd:
    #     bd.append(i['docroot']['$'].replace('www/', ''))
    print('bd:', bd)

    return render(request, 'billing/dashboard.html', {'bd': bd, 'domains': domains, 'owner': owner})
