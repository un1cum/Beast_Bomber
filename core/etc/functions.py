"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                   Beast bomber                                  ║
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
from beast import *
from bs4 import BeautifulSoup
from sys import platform
from colorama import Fore, init
from fake_useragent import UserAgent

init()
proxies_file = os.path.abspath('input/proxies.txt')

def logo_main():
    text = """
╔══╗         ╔╗ ╔══╗      ╔╗       
║╔╗║        ╔╝╚╗║╔╗║      ║║       
║╚╝╚╦══╦══╦═╩╗╔╝║╚╝╚╦══╦╗╔╣╚═╦══╦═╗
║╔═╗║ ═╣╔╗║══╣║ ║╔═╗║╔╗║╚╝║╔╗║ ═╣╔╝
║╚═╝║ ═╣╔╗╠══║╚╗║╚═╝║╚╝║║║║╚╝║ ═╣║ 
╚═══╩══╩╝╚╩══╩═╝╚═══╩══╩╩╩╩══╩══╩╝ 
            By un1cum
  https://t.me/beast_bomberr_bot
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

    with open(os.path.abspath('input/proxies.txt'), 'w+') as f:
        f.seek(0)
        f.close()

    if platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")

    logo_proxies()

    ua = UserAgent()
    user = ua.random

    try:
        res = requests.get('https://free-proxy-list.net', headers={'User-Agent': user})
        soup = BeautifulSoup(res.text, "lxml")
        cnt3 = 0

        with open(os.path.abspath(proxies_file), "a", encoding="utf-8") as file:
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

        with open(os.path.abspath(proxies_file), "a", encoding="utf-8") as file:
            for child in soup.recursiveChildGenerator():
                if child.name == 'td':
                    if validate_ip(child.text):
                        file.write(f"{child.text}:")
                    if validate_port(child.text):
                        file.write(f"{child.text}\n")
    except:
        pass
    urls = ['https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt',
            'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
            'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
            'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt']
    try:
        with open(os.path.abspath(proxies_file), "w", encoding="utf-8") as file:
            for url in urls:
                res = requests.get(url, headers={'User-Agent': user})
                proxy_list = res.text.strip().split('\n')
                for proxy in proxy_list:
                    if validate_ip(proxy.split(':')[0]) and validate_port(proxy.split(':')[1]):
                        file.write(proxy)
                        file.write('\n') 
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

    if lang == "ru":
        print(Fore.LIGHTGREEN_EX + 'Готово')
    else:
        print(Fore.LIGHTGREEN_EX + 'Success')

    time.sleep(1)

