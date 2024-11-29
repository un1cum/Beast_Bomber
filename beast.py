"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                   Beast bomber                                  ║
║  Author:                                                                        ║
║  https://github.com/un1ucm                                                      ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                            Copyright (C) 2024 un1ucm                            ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""
import os
import fade
import ctypes
from sys import platform
from core.sms_spam.sms import SMSAttack
from colorama import Fore, Style, Back, init
from core.ddos_attack.ddos import DDoSAttack
from core.discord_spam.discord import DiscordSpam
from core.email_spam.email_attack import EmailAttack
from core.telegram_spam.telegram import TelegramAttack
from core.etc.settings import Settings
from core.etc.functions import get_lang, logo_main, menu_ru, menu_en, logo_sms, logo_ddos, logo_email, logo_discord, logo_telegram

init()


class BeastBomber:
    def __init__(self):
        self.js_file = ''
        self.lang = get_lang()
        self.settings = Settings()
        self.sms_attack = SMSAttack()
        self.ddos_attack = DDoSAttack()
        self.email_attack = EmailAttack()
        self.discord_attack = DiscordSpam()
        self.telegram_attack = TelegramAttack()

    def ex(self):
        if self.lang == 'ru':
            option = input(Fore.LIGHTCYAN_EX + '\n\nВыйти? yes/no: ')
        else:
            option = input(Fore.LIGHTCYAN_EX + '\n\nExit? yes/no: ')

        if option == 'yes':
            if platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")

            if self.lang == 'ru':
                text = """
        Спасибо за использование Beast bomber!
Автор будет благодарен, если Вы поставите звезду на GitHub:
        https://github.com/un1ucm/Beast_Bomber
              Copyright (C) 2024 un1ucm"""
            else:
                text = """
            Thanks for using Beast bomber!
The author would appreciate it if you would put a star on 
              this repository on GitHub:
        https://github.com/un1ucm/Beast_Bomber
              Copyright (C) 2024 un1ucm"""

            print(fade.purplepink(text))
            os.abort()

        elif option == 'no':
            BeastBomber().main()

        else:
            self.ex()

    def main(self):
        if platform == 'win32':
            ctypes.windll.kernel32.SetConsoleTitleW("Beast Bomber 💣")

        if platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        logo_main()

        if self.lang == "ru":
            menu_ru()
        else:
            menu_en()

        try:
            option = input(Fore.MAGENTA + ' > ' + Fore.GREEN)

            if option == '0':
                self.ex()

            elif option == '1':
                self.sms_attack.start_sms()

                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_sms()

                if self.lang == "ru":
                    print(Fore.GREEN + '\nГотово')
                else:
                    print(Fore.GREEN + '\nDone')

                self.ex()

            elif option == '2':
                self.email_attack.email_start()

                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_email()

                if self.lang == "ru":
                    print(Fore.GREEN + '\nГотово')
                else:
                    print(Fore.GREEN + '\nDone')

                self.ex()

            elif option == '3':
                self.telegram_attack.start_telegram()

                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_telegram()

                if self.lang == "ru":
                    print(Fore.GREEN + '\nГотово')
                else:
                    print(Fore.GREEN + '\nDone')

                self.ex()

            elif option == '4':
                self.discord_attack.start_discord()

                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_discord()

                if self.lang == "ru":
                    print(Fore.GREEN + '\nГотово')
                else:
                    print(Fore.GREEN + '\nDone')

                self.ex()

            elif option == '5':
                self.ddos_attack.start_ddos()

                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_ddos()

                if self.lang == "ru":
                    print(Fore.GREEN + '\nГотово')
                else:
                    print(Fore.GREEN + '\nDone')

                self.ex()

            elif option == '6':
                self.settings.settings_main()

            else:
                self.ex()

        except:
            if self.lang == "ru":
                print(Fore.RED + '\nВо время работы бомбера произошла ошибка, проверьте корректность введенных данных.')
            else:
                print(Fore.RED + '\nAn error occurred during bomber working, check the correctness of the entered data.')

            self.ex()


if __name__ == "__main__":
    BeastBomber().main()
