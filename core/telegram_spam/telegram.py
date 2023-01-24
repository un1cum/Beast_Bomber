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
from threading import Thread
from opentele.td import TDesktop
from opentele.api import UseCurrentSession

accounts = os.listdir(os.path.abspath('input/telegram_accounts'))


async def telegram_attack(target, time_a, mes):
    t = time.monotonic()

    while time.monotonic() - t < time_a:
        for user in accounts:
            acc = os.path.abspath('input/telegram_accounts/' + user + '/tdata')
            tempmas = os.listdir(os.path.abspath('input/telegram_accounts/' + user))

            if acc[-8:] == '.session':
                acc = acc.replace('.session', '')

            if acc[-18:] == '.session - journal':
                acc = acc.replace('.session - journal', '')

            if f'{acc}.session' not in tempmas:
                tdesk = TDesktop(acc)
                client = await tdesk.ToTelethon(f"{acc}.session", UseCurrentSession)
            else:
                tdesk = TDesktop(acc)
                client = await tdesk.ToTelethon(session=f"{acc}.session", flag=UseCurrentSession)

            try:
                await client.connect()
                await client.send_message(target, mes)
                await client.disconnect()
            except:
                pass
