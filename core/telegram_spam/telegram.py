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
import urllib3
from sys import platform
from pythonping import ping
from datetime import datetime
from opentele.td import TDesktop
from threading import Thread, Lock
from fake_useragent import UserAgent
from colorama import Fore, Style, Back, init
from opentele.api import UseCurrentSession, CreateNewSession
from core.etc.functions import logo_telegram, get_lang, get_proxies, get_telegram_accounts

urllib3.disable_warnings()
init()


class TelegramAttack:
    def __init__(self):
        self.r = '0'
        self.r2 = '0'
        self.todo = 0
        self.started = 0
        self.lock = Lock()
        self.lang = get_lang()
        self.accounts = get_telegram_accounts()

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

    async def telegram_thread(self, users, message):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            for account in self.accounts:
                try:
                    tdata = os.path.join(os.path.abspath('input/telegram_accounts/' + account), 'tdata')
                    exist = False
                    for file in os.listdir(os.path.abspath(tdata)):
                        if file.endswith(".session"):
                            exist = True
                    if exist is True:
                        tdesk = TDesktop(tdata)
                        client = await tdesk.ToTelethon(session=f"{tdata}.session", flag=UseCurrentSession)
                    else:
                        tdesk = TDesktop(tdata)
                        client = await tdesk.ToTelethon(session=f"{tdata}.session", flag=CreateNewSession)

                    for user in users:
                        await client.connect()
                        try:
                            await client.send_message(user, message)
                            self.r = str(int(self.r) + 1)
                            self.stat()
                        except:
                            self.r2 = str(int(self.r2) + 1)
                            self.stat()
                        await client.disconnect()
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()

    def run_thread(self, time_a, users, message,):
        t = time.monotonic()
        while time.monotonic() - t < time_a:
            asyncio.run(self.telegram_thread(users, message,))

    def start_telegram(self):
        if platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        logo_telegram()

        if self.lang == 'ru':
            text = "\nUsername(ы) для атаки > "
            text2 = """
╔═════════════════════════════════════════════════╗
║Если вы собираетесь указать несоклько юзернеймов,║ 
║      то делайте это в следующем вормате:        ║
║              username, username                 ║
║                                                 ║
║          Формат юзернейма: @username            ║
╚═════════════════════════════════════════════════╝
            """
        else:
            text = "\nUsername(s) for the attack > "
            text2 = """
╔═════════════════════════════════════════════════╗
║If you are going to enter more than one username,║
║        do it in the following format:           ║
║             username, username                  ║
║                                                 ║
║          Username format: @username             ║
╚═════════════════════════════════════════════════╝
                    """

        print(fade.water(text2))

        usernames = input(Fore.YELLOW + Style.BRIGHT + text + Fore.GREEN)
        usernames = usernames.replace(' ', '')
        usernames = usernames.split(',')

        if self.lang == 'ru':
            text1 = 'Потоки > '
            text2 = 'Время атаки (в сек.) > '
            text3 = 'поток запущен'
            text4 = "Сообщение для отправки > "
        else:
            text1 = 'Threads > '
            text2 = 'Time attack (in sec.) > '
            text3 = 'thread started'
            text4 = "Message to send > "

        self.todo = int(input(Fore.YELLOW + Style.BRIGHT + text1 + Fore.GREEN))
        time_attack = int(input(Fore.YELLOW + Style.BRIGHT + text2 + Fore.GREEN))
        message = input(Fore.YELLOW + Style.BRIGHT + text4 + Fore.GREEN)

        th = None

        for count in range(self.todo):
            th = Thread(target=self.run_thread, args=(time_attack, usernames, message,))
            th.start()
            self.started += 1
            print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                  Fore.YELLOW + Style.BRIGHT + text3)

        time.sleep(1)

        th.join()
