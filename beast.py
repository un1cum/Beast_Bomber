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
import asyncio
import ctypes
import os
import sys
import fade
import json
import socket
import time
import telethon
from sys import platform
from colorama import Fore, init
from core.sms_spam.sms import *
from core.email_spam.email import *
from core.discord_spam.discord import *
from core.ddos_attack.ddos import *
from core.etc.functions import *
from core.telegram_spam.telegram import *

init()


def ports():
    ip = socket.gethostbyname(socket.gethostname())
    av_ports = []

    for port in range(65535):
        try:
            serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            serv.bind((ip, port))
        except:
            av_ports.append(port)

        serv.close()

    return av_ports


class BeastBomber:
    def __init__(self):
        self.js_file = ''

        with open(os.path.abspath('core/config.json'), 'r') as file:
            for line in file:
                self.js_file += str(line)

        self.js_file = json.loads(self.js_file)
        self.lang = self.js_file["language"]

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
        https://github.com/ebankoff/BeastBomber
              Copyright (C) 2023 un1cum
                """
            else:
                text = """
            Thanks for using Beast bomber!
The author would appreciate it if you would put a star on 
              this repository on GitHub:
       https://github.com/ebankoff/BeastBomber
              Copyright (C) 2023 un1cum
                """

            print(fade.purplepink(text))

            os.abort()

        elif option == 'no':
            BeastBomber().main()

        else:
            self.ex()

    def options(self):
        self.lang = self.js_file["language"]

        if platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        logo_settings()

        if self.lang == 'ru':
            settings_menu_ru()
        else:
            settings_menu_en()

        option = input(Fore.LIGHTMAGENTA_EX + ' >> ')

        if option == '0':
            self.main()

        elif option == '1':
            update_proxies()
            self.options()

        elif option == '2':
            if self.lang == "ru":
                self.js_file["language"] = "en"
                with open(os.path.abspath('core/config.json'), 'w') as file:
                    json.dump(self.js_file, ensure_ascii=False, indent=4, fp=file)

            else:
                self.js_file["language"] = "ru"
                with open(os.path.abspath('core/config.json'), 'w') as file:
                    json.dump(self.js_file, ensure_ascii=False, indent=4, fp=file)

            self.options()

        elif option == '3':
            try:
                os.remove('__pycache__')
            except:
                pass

            if platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")

            if self.lang == "ru":
                print(Fore.LIGHTGREEN_EX + 'Готово')
            else:
                print(Fore.LIGHTGREEN_EX + 'Success')

            time.sleep(1)
            self.options()

    def main(self):
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
            option = input(Fore.LIGHTMAGENTA_EX + ' >> ')

            if option == '0':
                self.ex()

            elif option == '1':
                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")
                logo_sms()
                if self.lang == "ru":
                    print(Fore.LIGHTCYAN_EX + 'Напишите exit для отмены\n')

                    phone = input(Fore.LIGHTMAGENTA_EX + 'Номер телефона в формате: 7xxxxxxxxxx > ')
                    if phone == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Количество потоков (стандарт - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Время атаки в секундах (стандарт 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    proxy = input(Fore.LIGHTMAGENTA_EX + 'Использовать прокси? yes/no > ')
                    if proxy == '' or proxy != 'yes' and proxy != 'no':
                        proxy = 'no'

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Начать? yes/no > ')
                else:
                    print(Fore.LIGHTCYAN_EX + 'Write exit to cancel\n')

                    phone = input(Fore.LIGHTMAGENTA_EX + 'Phone number in the format: 7xxxxxxxxxx > ')
                    if phone == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Number of threads (standard - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Attack time in seconds (standard 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    proxy = input(Fore.LIGHTMAGENTA_EX + 'Use proxy? yes/no > ')
                    if proxy == '' or proxy != 'yes' and proxy != 'no':
                        proxy = 'no'

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Start? yes/no > ')

                if qsn == "yes":
                    text_e = f"""
    ╔══════════[Attack info]══════════╗
        Threads: {str(threads)}        
        Time: {str(time_a)}            
        Target: {phone}      
        Proxy: {proxy}               
    ╚═════════════════════════════════╝"""

                    if proxy == 'yes':
                        proxy_r = 'да'
                    else:
                        proxy_r = 'нет'

                    text_r = f"""
    ╔═════════[Инфо об атаке]═════════╗
        Потоки: {str(threads)}        
        Время: {str(time_a)}          
        Цель: {phone}    
        Прокси: {proxy_r}             
    ╚═════════════════════════════════╝"""

                    if self.lang == "ru":
                        print(fade.fire(text_r))
                    else:
                        print(fade.fire(text_e))

                    start_sms(phone, threads, time_a, proxy)

                    text = "{}"
                    t = time.monotonic()
                    pb = ''

                    while time.monotonic() - t < time_a:
                        sp = ''
                        if len(pb) == 20:
                            pb = ''
                        pb += '█'
                        for _ in range(20 - len(pb)):
                            sp += ' '
                        print(text.format(Fore.LIGHTMAGENTA_EX + '[' + pb + sp + ']') + '\r', end='')
                        time.sleep(0.5)

                    if platform == 'win32':
                        os.system("cls")
                    else:
                        os.system("clear")

                    logo_sms()

                    if self.lang == "ru":
                        print(Fore.LIGHTGREEN_EX + '\nГотово!')
                    else:
                        print(Fore.LIGHTGREEN_EX + '\nFinished!')

                    self.ex()
                else:
                    self.main()

            elif option == '2':
                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_email()

                if self.lang == "ru":
                    print(Fore.LIGHTCYAN_EX + 'Напишите exit для отмены\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'Почта для атаки > ')
                    if target == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Количество потоков (стандарт - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Время атаки в секундах (стандарт 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    message = input(Fore.LIGHTMAGENTA_EX + 'Сообщение для отправки > ')
                    if message == "exit":
                        self.main()

                    subj = input(Fore.LIGHTMAGENTA_EX + 'Тема сообщения > ')
                    if subj == "exit":
                        self.main()

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Начать? yes/no > ')

                else:
                    print(Fore.LIGHTCYAN_EX + 'Write exit to cancel\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'Email for attack > ')
                    if target == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Number of threads (standard - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Attack time in seconds (standard 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    message = input(Fore.LIGHTMAGENTA_EX + 'Message to send > ')
                    if message == "exit":
                        self.main()

                    subj = input(Fore.LIGHTMAGENTA_EX + 'Subject > ')
                    if subj == "exit":
                        self.main()

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Start? yes/no > ')

                if qsn == "yes":
                    text_e = f"""
    ╔══════════[Attack info]══════════╗
        Threads: {str(threads)}        
        Time: {str(time_a)}            
        Target: {target}                
    ╚═════════════════════════════════╝"""
                    text_r = f"""
    ╔═════════[Инфо об атаке]═════════╗
        Потоки: {str(threads)}        
        Время: {str(time_a)}          
        Цель: {target}                 
    ╚═════════════════════════════════╝"""

                    if self.lang == "ru":
                        print(fade.fire(text_r))

                    else:
                        print(fade.fire(text_e))

                    email_start(threads, time_a, target, message, subj)

                    text = "{}"
                    t = time.monotonic()
                    pb = ''

                    while time.monotonic() - t < time_a:
                        sp = ''
                        if len(pb) == 20:
                            pb = ''
                        pb += '█'
                        for _ in range(20 - len(pb)):
                            sp += ' '
                        print(text.format(Fore.LIGHTMAGENTA_EX + '[' + pb + sp + ']') + '\r', end='')
                        time.sleep(0.5)

                    if platform == 'win32':
                        os.system("cls")
                    else:
                        os.system("clear")

                    logo_email()

                    if self.lang == "ru":
                        print(Fore.LIGHTGREEN_EX + '\nГотово!')
                    else:
                        print(Fore.LIGHTGREEN_EX + '\nFinished!')

                else:
                    self.main()

            elif option == '3':
                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_telegram()

                if self.lang == "ru":
                    print(Fore.LIGHTCYAN_EX + 'Напишите exit для отмены\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'Username для атаки в формате: @username > ')
                    if target == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Время атаки в секундах (стандарт 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    message = input(Fore.LIGHTMAGENTA_EX + 'Сообщение для отправки > ')
                    if message == "exit":
                        self.main()

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Начать? yes/no > ')

                else:
                    print(Fore.LIGHTCYAN_EX + 'Write exit to cancel\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'Username for the attack in the format: @username > ')
                    if target == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Attack time in seconds (standard 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    message = input(Fore.LIGHTMAGENTA_EX + 'Message to send > ')
                    if message == "exit":
                        self.main()

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Start? yes/no > ')

                if qsn == "yes":
                    text_e = f"""
    ╔══════════[Attack info]══════════╗
        Time: {str(time_a)}            
        Target: {target}                
    ╚═════════════════════════════════╝"""
                    text_r = f"""
    ╔═════════[Инфо об атаке]═════════╗
        Время: {str(time_a)}          
        Цель: {target}                 
    ╚═════════════════════════════════╝"""

                    if self.lang == "ru":
                        print(fade.fire(text_r))
                    else:
                        print(fade.fire(text_e))

                    asyncio.get_event_loop().run_until_complete(telegram_attack(target, time_a, message))

                    text = "{}"
                    t = time.monotonic()
                    pb = ''

                    while time.monotonic() - t < time_a:
                        sp = ''
                        if len(pb) == 20:
                            pb = ''
                        pb += '█'
                        for _ in range(20 - len(pb)):
                            sp += ' '
                        print(text.format(Fore.LIGHTMAGENTA_EX + '[' + pb + sp + ']') + '\r', end='')
                        time.sleep(0.5)

                    if platform == 'win32':
                        os.system("cls")
                    else:
                        os.system("clear")

                    logo_telegram()

                    if self.lang == "ru":
                        print(Fore.LIGHTGREEN_EX + '\nГотово!')
                    else:
                        print(Fore.LIGHTGREEN_EX + '\nFinished!')

                else:
                    self.main()

            elif option == '4':
                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_discord()

                if self.lang == "ru":
                    print(Fore.LIGHTCYAN_EX + 'Напишите exit для отмены\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'ID для атаки > ')
                    if target == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Количество потоков (стандарт - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Время атаки в секундах (стандарт 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    message = input(Fore.LIGHTMAGENTA_EX + 'Сообщение для отправки > ')
                    if message == "exit":
                        self.main()

                    proxy = input(Fore.LIGHTMAGENTA_EX + 'Использовать прокси? yes/no > ')
                    if proxy == '' or proxy != 'yes' and proxy != 'no':
                        proxy = 'no'

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Начать? yes/no > ')

                else:
                    print(Fore.LIGHTCYAN_EX + 'Write exit to cancel\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'ID for attack > ')
                    if target == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Number of threads (standard - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Attack time in seconds (standard 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    message = input(Fore.LIGHTMAGENTA_EX + 'Message to send > ')
                    if message == "exit":
                        self.main()

                    proxy = input(Fore.LIGHTMAGENTA_EX + 'Use proxy? yes/no > ')
                    if proxy == '' or proxy != 'yes' and proxy != 'no':
                        proxy = 'no'

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Start? yes/no > ')

                if qsn == "yes":
                    text_e = f"""
    ╔══════════[Attack info]══════════╗
        Threads: {str(threads)}        
        Time: {str(time_a)}            
        Target: {target}                
    ╚═════════════════════════════════╝"""
                    text_r = f"""
    ╔═════════[Инфо об атаке]═════════╗
        Потоки: {str(threads)}        
        Время: {str(time_a)}          
        Цель: {target}                 
    ╚═════════════════════════════════╝"""

                    if self.lang == "ru":
                        print(fade.fire(text_r))

                    else:
                        print(fade.fire(text_e))

                    start_discord(threads, time_a, message, target, proxy)

                    text = "{}"
                    t = time.monotonic()
                    pb = ''

                    while time.monotonic() - t < time_a:
                        sp = ''
                        if len(pb) == 20:
                            pb = ''
                        pb += '█'
                        for _ in range(20 - len(pb)):
                            sp += ' '
                        print(text.format(Fore.LIGHTMAGENTA_EX + '[' + pb + sp + ']') + '\r', end='')
                        time.sleep(0.5)

                    if platform == 'win32':
                        os.system("cls")
                    else:
                        os.system("clear")

                    logo_telegram()

                    if self.lang == "ru":
                        print(Fore.LIGHTGREEN_EX + '\nГотово!')
                    else:
                        print(Fore.LIGHTGREEN_EX + '\nFinished!')

                else:
                    self.main()

            elif option == '5':
                if platform == 'win32':
                    os.system("cls")
                else:
                    os.system("clear")

                logo_ddos()

                av_ports = ports()

                if self.lang == "ru":
                    print(Fore.LIGHTCYAN_EX + 'Напишите exit для отмены\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'Url или ip для атаки > ')
                    if target == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Количество потоков (стандарт - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Время атаки в секундах (стандарт 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Начать? yes/no > ')

                else:
                    print(Fore.LIGHTCYAN_EX + 'Write exit to cancel\n')

                    target = input(Fore.LIGHTMAGENTA_EX + 'Url or ip to attack > ')
                    if target == "exit":
                        self.main()

                    threads = input(Fore.LIGHTMAGENTA_EX + 'Number of threads (standard - 4) > ')
                    if threads == '' or int(threads) <= 0:
                        threads = 4
                    else:
                        threads = int(threads)
                    if threads == "exit":
                        self.main()

                    time_a = input(Fore.LIGHTMAGENTA_EX + 'Attack time in seconds (standard 60) > ')
                    if time_a == '' or int(time_a) <= 0:
                        time_a = 60
                    else:
                        time_a = int(time_a)
                    if time_a == "exit":
                        self.main()

                    qsn = input(Fore.LIGHTMAGENTA_EX + 'Start? yes/no > ')

                if qsn == "yes":
                    text_e = f"""
╔══════════[Attack info]══════════╗
    Threads: {str(threads)}        
    Time: {str(time_a)}            
    Target: {target}                
╚═════════════════════════════════╝"""
                    text_r = f"""
╔═════════[Инфо об атаке]═════════╗
    Потоки: {str(threads)}        
    Время: {str(time_a)}          
    Цель: {target}                 
╚═════════════════════════════════╝"""

                    if self.lang == "ru":
                        print(fade.fire(text_r))

                    else:
                        print(fade.fire(text_e))

                    start_ddos(threads, time_a, target, av_ports)

                    text = "{}"
                    t = time.monotonic()
                    pb = ''

                    while time.monotonic() - t < time_a:
                        sp = ''
                        if len(pb) == 20:
                            pb = ''
                        pb += '█'
                        for _ in range(20 - len(pb)):
                            sp += ' '
                        print(text.format(Fore.LIGHTMAGENTA_EX + '[' + pb + sp + ']') + '\r', end='')
                        time.sleep(0.5)

                    if platform == 'win32':
                        os.system("cls")
                    else:
                        os.system("clear")

                    logo_ddos()

                    if self.lang == "ru":
                        print(Fore.LIGHTGREEN_EX + '\nГотово!')
                    else:
                        print(Fore.LIGHTGREEN_EX + '\nFinished!')

                else:
                    self.main()

            elif option == '6':
                self.options()

            else:
                if self.lang == "ru":
                    print(Fore.RED + '\nНеверное значение')
                else:
                    print(Fore.RED + '\nInvalid value')
                self.ex()

        except:
            if self.lang == "ru":
                print(Fore.RED + '\nОшибка. Проверьте правильность введенного значения.')
            else:
                print(Fore.RED + '\nError. Check that the value you entered is correct.')
            self.ex()


if __name__ == "__main__":
    if platform == 'win32':
        ctypes.windll.kernel32.SetConsoleTitleW("Beast bomber 💣")
    BeastBomber().main()
