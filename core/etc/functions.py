"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                   Beast Bomber                                  ║
║  Author:                                                                        ║
║  https://github.com/un1cum                                                      ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                            Copyright (C) 2023 un1cum                            ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""
import os
import fade
import re
import json
import ipaddress
import requests
import time
import random
from bs4 import BeautifulSoup
from sys import platform
from colorama import Fore, init
from fake_useragent import UserAgent

init()


def logo_main():
    text = """
╔══╗         ╔╗ ╔══╗      ╔╗       
║╔╗║        ╔╝╚╗║╔╗║      ║║       
║╚╝╚╦══╦══╦═╩╗╔╝║╚╝╚╦══╦╗╔╣╚═╦══╦═╗
║╔═╗║ ═╣╔╗║══╣║ ║╔═╗║╔╗║╚╝║╔╗║ ═╣╔╝
║╚═╝║ ═╣╔╗╠══║╚╗║╚═╝║╚╝║║║║╚╝║ ═╣║ 
╚═══╩══╩╝╚╩══╩═╝╚═══╩══╩╩╩╩══╩══╩╝ 
            By un1cum
  https://t.me/beast_bomber_team
    """
    print(fade.water(text))


def logo_sms():
    text = """
╔═══╦═╗╔═╦═══╗             
║╔═╗║ ╚╝ ║╔═╗║             
║╚══╣╔╗╔╗║╚══╗╔══╦══╦══╦╗╔╗
╚══╗║║║║║╠══╗║║══╣╔╗║╔╗║╚╝║
║╚═╝║║║║║║╚═╝║╠══║╚╝║╔╗║║║║
╚═══╩╝╚╝╚╩═══╝╚══╣╔═╩╝╚╩╩╩╝
                 ║║        
                 ╚╝        
    """
    print(fade.greenblue(text))


def logo_discord():
    text = """
╔═══╗             ╔╗             
╚╗╔╗║             ║║             
 ║║║╠╦══╦══╦══╦═╦═╝║╔══╦══╦══╦╗╔╗
 ║║║╠╣══╣╔═╣╔╗║╔╣╔╗║║══╣╔╗║╔╗║╚╝║
╔╝╚╝║╠══║╚═╣╚╝║║║╚╝║╠══║╚╝║╔╗║║║║
╚═══╩╩══╩══╩══╩╝╚══╝╚══╣╔═╩╝╚╩╩╩╝
                       ║║        
                       ╚╝        
    """
    print(fade.fire(text))


def logo_email():
    text = """
╔═══╗      ╔╗              
║╔══╝      ║║              
║╚══╦╗╔╦══╦╣║ ╔══╦══╦══╦╗╔╗
║╔══╣╚╝║╔╗╠╣║ ║══╣╔╗║╔╗║╚╝║
║╚══╣║║║╔╗║║╚╗╠══║╚╝║╔╗║║║║
╚═══╩╩╩╩╝╚╩╩═╝╚══╣╔═╩╝╚╩╩╩╝
                 ║║        
                 ╚╝        
    """
    print(fade.purplepink(text))


def logo_ddos():
    text = """
╔═══╦═══╗  ╔═══╗
╚╗╔╗╠╗╔╗║  ║╔═╗║
 ║║║║║║║╠══╣╚══╗
 ║║║║║║║║╔╗╠══╗║
╔╝╚╝╠╝╚╝║╚╝║╚═╝║
╚═══╩═══╩══╩═══╝
    """
    print(fade.brazil(text))


def logo_telegram():
    text = """
╔════╗ ╔╗
║╔╗╔╗║ ║║
╚╝║║╠╩═╣║╔══╦══╦═╦══╦╗╔╗╔══╦══╦══╦╗╔╗
  ║║║ ═╣║║ ═╣╔╗║╔╣╔╗║╚╝║║══╣╔╗║╔╗║╚╝║
  ║║║ ═╣╚╣ ═╣╚╝║║║╔╗║║║║╠══║╚╝║╔╗║║║║
  ╚╝╚══╩═╩══╩═╗╠╝╚╝╚╩╩╩╝╚══╣╔═╩╝╚╩╩╩╝
            ╔═╝║           ║║
            ╚══╝           ╚╝
    """
    print(fade.greenblue(text))


def logo_settings():
    text = """
╔═══╗  ╔╗ ╔╗           
║╔═╗║ ╔╝╚╦╝╚╗          
║╚══╦═╩╗╔╩╗╔╬╦═╗╔══╦══╗
╚══╗║ ═╣║ ║║╠╣╔╗╣╔╗║══╣
║╚═╝║ ═╣╚╗║╚╣║║║║╚╝╠══║
╚═══╩══╩═╝╚═╩╩╝╚╩═╗╠══╝
                ╔═╝║   
                ╚══╝   
    """
    print(fade.greenblue(text))


def logo_proxies():
    text = """
╔╗ ╔╗    ╔╗  ╔╗
║║ ║║    ║║ ╔╝╚╗
║║ ║╠══╦═╝╠═╩╗╔╬╦═╗╔══╗╔══╦═╦══╦╗╔╦╦══╦══╗
║║ ║║╔╗║╔╗║╔╗║║╠╣╔╗╣╔╗║║╔╗║╔╣╔╗╠╬╬╬╣ ═╣══╣
║╚═╝║╚╝║╚╝║╔╗║╚╣║║║║╚╝║║╚╝║║║╚╝╠╬╬╣║ ═╬══║
╚═══╣╔═╩══╩╝╚╩═╩╩╝╚╩═╗║║╔═╩╝╚══╩╝╚╩╩══╩══╝
    ║║             ╔═╝║║║
    ╚╝             ╚══╝╚╝
    """
    print(fade.pinkred(text))


def menu_en():
    text = """[0] Exit          
[1] SMS spam      
[2] Email spam   
[3] Telegram spam
[4] Discord spam 
[5] DDoS attack  
[6] Settings      
    """
    print(fade.purplepink(text))


def menu_ru():
    text = """[0] Выход        
[1] СМС спам     
[2] Email спам   
[3] Telegram спам
[4] Discord спам 
[5] DDoS атака
[6] Настройки    
    """
    print(fade.purplepink(text))


def settings_menu_ru():
    text = """[0] Назад        
[1] Обновить прокси    
[2] Сменить язык
[3] Очистить кэш
        """
    print(fade.purplepink(text))


def settings_menu_en():
    text = """[0] Back        
[1] Update proxies    
[2] Change language
[3] Clear cache
        """
    print(fade.purplepink(text))


def validate_ip(ip):
    try:
        parts = list(map(int, ip.split('.')))
        return len(parts) == 4 and all(0 <= p <= 255 for p in parts)
    except ValueError:
        return False


def validate_port(port):
    return str(port).isdigit() and 1 <= int(port) <= 65535


def update_proxies():
    with open(os.path.abspath('core/config.json'), 'r') as file:
        js_file = json.load(file)

    lang = js_file["language"]
    urls = ['https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt']

    with open(os.path.abspath('input/proxies.txt'), 'w+') as f:
        f.seek(0)
        f.close()

    ua = UserAgent(verify_ssl=False)
    user = ua.random

    try:
        res = requests.get('https://free-proxy-list.net', headers={'User-Agent': user})
        soup = BeautifulSoup(res.text, "lxml")
        cnt3 = 0

        with open(os.path.abspath('input/proxies.txt'), "a", encoding="utf-8") as file:
            for child in soup.recursiveChildGenerator():
                if child.name == 'td':
                    if cnt3 == 0:
                        if not validate_ip(child.text):
                            break
                        file.write(f"{child.text}:")
                    if cnt3 == 1:
                        file.write(f"{child.text}\n")

                    cnt3 = (cnt3 + 1) % 8
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

    try:
        res = requests.get('https://hidemy.name/ru/proxy-list', headers={'User-Agent': user})
        soup = BeautifulSoup(res.text, "lxml")

        with open(os.path.abspath('input/proxies.txt'), "a", encoding="utf-8") as file:
            for child in soup.recursiveChildGenerator():
                if child.name == 'td':
                    if validate_ip(child.text):
                        file.write(f"{child.text}:")
                    if validate_port(child.text):
                        file.write(f"{child.text}\n")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

    try:
        with open(os.path.abspath('input/proxies.txt'), "w", encoding="utf-8") as file:
            for url in urls:
                res = requests.get(url, headers={'User-Agent': user})
                proxy_list = res.text.strip().split('\n')
                for proxy in proxy_list:
                    if validate_ip(proxy.split(':')[0]) and validate_port(proxy.split(':')[1]):
                        file.write(proxy)
                        file.write('\n')
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")


def get_lang():
    try:
        js_file = ''
        with open(os.path.abspath('core/config.json'), 'r') as file:
            for line in file:
                js_file += str(line)

        return json.loads(js_file)["language"]
    except:
        return 'en'


def get_proxies():
    proxies = []
    lang = get_lang()

    try:
        with open(os.path.abspath('input/proxies.txt'), 'r') as file:
            for line in file:
                proxies.append(line.replace('\n', ''))
    except:
        if lang == 'ru':
            print(Fore.RED + '\nОшибка при попытке открыть файл input/proxies.txt')
        else:
            print(Fore.RED + '\nError when trying to open a file input/proxies.txt')

    return proxies


def generate_email():
    lib = 'qwertyuiopasdfhgjklzxcvbnm'
    lib2 = ['@gmail.com', '@hotmail.com', '@yahoo.com', '@yandex.ru']
    email = ''.join(random.choice(lib) for _ in range(random.randint(10, 25))) + random.choice(lib2)
    return email


def randstr(str_len):
    lib = '1234567890qwertyuiopasdfghjklzxcvbnm'
    text = ''.join(random.choices(lib, k=str_len))
    return text


def get_discord_tokens():
    tokens = []
    lang = get_lang()

    try:
        with open(os.path.abspath('input/discord_tokens.txt'), 'r') as file:
            for line in file:
                tokens.append(line.replace('\n', ''))
    except:
        if lang == 'ru':
            print(Fore.RED + '\nОшибка при попытке открыть файл input/discord_tokens.txt')
        else:
            print(Fore.RED + '\nError when trying to open a file input/discord_tokens.txt')

    return tokens


def get_telegram_accounts():
    lang = get_lang()
    accounts = []

    try:
        accounts = os.listdir(os.path.abspath('input/telegram_accounts'))
    except:
        if lang == 'ru':
            print(Fore.RED + '\nОшибка при попытке получить Telegram аккаунты из input/telegram_accounts')
        else:
            print(Fore.RED + '\nError when trying to retrieve Telegram accounts from input/telegram_accounts')

    return accounts


def get_email_accounts():
    emails = []
    lang = get_lang()

    try:
        with open(os.path.abspath('input/email_accounts.txt'), 'r') as file:
            for line in file:
                emails.append(line.replace('\n', ''))
    except:
        if lang == 'ru':
            print(Fore.RED + '\nОшибка при попытке открыть файл input/email_accounts.txt')
        else:
            print(Fore.RED + '\nError when trying to open a file input/email_accounts.txt')

    return emails


def change_language():
    lang = get_lang()
    js_file = os.path.abspath('core/config.json')
    with open(os.path.abspath(js_file)) as file:
        js = json.load(file)

    if lang == "ru":
        js["language"] = "en"
        with open(os.path.abspath('core/config.json'), 'w') as file:
            json.dump(js, ensure_ascii=False, indent=4, fp=file)

    else:
        js["language"] = "ru"
        with open(os.path.abspath('core/config.json'), 'w') as file:
            json.dump(js, ensure_ascii=False, indent=4, fp=file)
