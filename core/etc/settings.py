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
import time
import ctypes
from sys import platform
from colorama import Fore, Style, Back, init
from core.etc.functions import get_lang, logo_settings, settings_menu_en, settings_menu_ru, update_proxies, change_language

init()


class Settings:
    def __init__(self):
        self.lang = get_lang()

    def settings_main(self):
        if platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        logo_settings()

        if self.lang == 'ru':
            settings_menu_ru()
        else:
            settings_menu_en()

        option = input(Fore.MAGENTA + ' > ' + Fore.GREEN)

        if option == '0':
            from beast import BeastBomber
            beast = BeastBomber()
            beast.main()

        elif option == '1':
            update_proxies()

            if self.lang == 'ru':
                text = '\nГотово'
            else:
                text = '\nDone'

            print(Fore.GREEN + text)
            time.sleep(2)
            self.settings_main()

        elif option == '2':
            change_language()
            self.lang = get_lang()
            self.settings_main()

        elif option == '3':
            try:
                os.remove(os.path.abspath('__pycache__'))
            except:
                pass
            try:
                os.remove(os.path.abspath('core/ddos_attack/__pycache__'))
            except:
                pass
            try:
                os.remove(os.path.abspath('core/discord_spam/__pycache__'))
            except:
                pass
            try:
                os.remove(os.path.abspath('core/email_spam/__pycache__'))
            except:
                pass
            try:
                os.remove(os.path.abspath('core/etc/__pycache__'))
            except:
                pass
            try:
                os.remove(os.path.abspath('core/sms_spam/__pycache__'))
            except:
                pass
            try:
                os.remove(os.path.abspath('core/telegram_spam/__pycache__'))
            except:
                pass

            if self.lang == 'ru':
                text = '\nГотово'
            else:
                text = '\nDone'

            print(Fore.GREEN + text)
            time.sleep(2)
            self.settings_main()

        else:
            from beast import BeastBomber
            beast = BeastBomber()
            beast.ex()
