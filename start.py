"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                   Beast bomber                                  ║
║  Author:                                                                        ║
║  https://github.com/ebankoff                                                    ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2022 ebankoff                           ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import ctypes
import os.path
from sys import platform

try:
	os.system('pip install configparser')
	import configparser
	config_path = os.path.join(sys.path[0], r'core\\config.ini')
	config = configparser.ConfigParser()
	config.read(config_path)
	ans = config.get('config', 'first_setup')
	lang = config.get('config', 'lang')

	if lang == 'ru':
		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW("Подготовка к запуску beast bomber...")
	else:
		if platform == 'win32':
			ctypes.windll.kernel32.SetConsoleTitleW("Preparing to launch the beast bomber...")

	if ans != 'yes':
		try:
			os.system('pip install proxy_checking lxml matplotlib pandas numpy bs4 emoji anticaptchaofficial wheel asyncio requests progress colorama selenium user_agent about-time progressbar beautifulsoup4 selenium_stealth webdriver-manager pycountry pythonping')
			config['config']['first_setup'] = 'yes'
			with open(r'core\\config.ini', 'w') as configfile:
				config.write(configfile)
		except:
			pass
except:
	os.abort()

if platform == 'win32':
	os.system("cls")
else:
	os.system("clear")

import time
import shutil
import colorama
from requests import get
from colorama import Fore
from threading import Thread
from core.sms_spam import sms
from core.dos_attack import dos
from core.email_spam import email
from core.proxy import get_proxies
from core.discord_spam import discord
from core.whatsapp_spam import whatsapp
from core.telegram_spam import telegram

colorama.init()


def pb():
	config_path = os.path.join(sys.path[0], r'core\\config.ini')
	config = configparser.ConfigParser()
	config.read(config_path)
	lang = config.get('config', 'lang')

	tm = 2
	text2 =  Fore.YELLOW + "{}"
	t = time.monotonic()

	if lang == 'ru':
		while time.monotonic() - t < tm:
			print(text2.format('\033[36mЗагрузка...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[31mЗагрузка...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[32mЗагрузка...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[36mЗагрузка...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[33mЗагрузка...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[34mЗагрузка...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[35mЗагрузка...') + '\r', end='')
			time.sleep(.08)

	else:
		while time.monotonic() - t < tm:
			print(text2.format('\033[36mProcessing...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[31mProcessing...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[32mProcessing...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[36mProcessing...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[33mProcessing...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[34mProcessing...') + '\r', end='')
			time.sleep(.08)
			print(text2.format('\033[35mProcessing...') + '\r', end='')
			time.sleep(.08)


def check_internet():
	config_path = os.path.join(sys.path[0], r'core\\config.ini')
	config = configparser.ConfigParser()
	config.read(config_path)
	lang = config.get('config', 'lang')

	try:
		get("http://google.com", timeout=1)

	except:
		if lang == 'ru':
			print(
				Fore.RED + '╔══════════════════════════════════╗',
				Fore.RED + '\n║   Нет соединения с интернетом!   ║',
				Fore.RED + '\n╚══════════════════════════════════╝'
			)

		else:
			print(
				Fore.RED + '╔═════════════════════════════╗',
				Fore.RED + '\n║   No internet connection!   ║',
				Fore.RED + '\n╚═════════════════════════════╝'
			)

		input()
		ex()


def ex():
	config_path = os.path.join(sys.path[0], r'core\\config.ini')
	config = configparser.ConfigParser()
	config.read(config_path)
	lang = config.get('config', 'lang')

	if lang == 'ru':
		param = input(Fore.WHITE + 'Выйти? yes/no: ')
	else:
		param = input(Fore.WHITE + 'Exit? yes/no: ')

	if param == 'yes':
		if platform == 'win32':
			os.system("cls")
		else:
			os.system("clear")

		if lang == 'ru':
			print(Fore.WHITE + 
			'            Спасибо за использование Beast bomber!'
			'\nАвтор будет благодарен, если Вы поставите звезду на GitHub:'
			'\n         https://github.com/ebankoff/BeastBomber'
			'\n'
			'\n              Copyright (C) 2022 ebankoff')
			print("\nНажмите Enter для выхода")
		else:
			print(Fore.WHITE + 
			'               Thanks for using Beast bomber!'
			'\nI would be grateful if you star this repository on GitHub:'
			'\n        https://github.com/ebankoff/BeastBomber'
			'\n'
			'\n              Copyright (C) 2022 ebankoff')
			print("\nPress Enter to exit")

		input()
		os.abort()

	elif param == 'no':
		main()

	else:
		if lang == 'en':
			print(Fore.RED + '━━━━━━━━━━Invalid value━━━━━━━━━━')
		else:
			print(Fore.RED + '━━━━━━━━━━Неверное значение━━━━━━━━━━')
		ex()


def main():
	if platform == 'win32':
		os.system("cls")
	else:
		os.system("clear")

	config_path = os.path.join(sys.path[0], r'core\\config.ini')
	config = configparser.ConfigParser()
	config.read(config_path)
	lang = config.get('config', 'lang')

	print(Fore.RED + 
		'┏━━┓         ┏┓  ┏━━┓      ┏┓'
		'\n┃┏┓┃        ┏┛┗┓ ┃┏┓┃      ┃┃'
		'\n┃┗┛┗┳━━┳━━┳━┻┓┏┛ ┃┗┛┗┳━━┳┓┏┫┗━┳━━┳━┓'
		'\n┃┏━┓┃ ━┫┏┓┃━━┫┃  ┃┏━┓┃┏┓┃┗┛┃┏┓┃ ━┫┏┛'
		'\n┃┗━┛┃ ━┫┏┓┣━━┃┗┓ ┃┗━┛┃┗┛┃┃┃┃┗┛┃ ━┫┃'
		'\n┗━━━┻━━┻┛┗┻━━┻━┛ ┗━━━┻━━┻┻┻┻━━┻━━┻┛'
	)

	if lang == 'ru':
		print(
			Fore.WHITE + '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━',
			Fore.RED + '\nАвтор - https://github.com/ebankoff',
			Fore.RED + f'\nOS: {platform}',
			Fore.RED + f'\nBeast Bomber в telegram: https://t.me/beast_bomberr_bot',
			Fore.WHITE + '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
		)

		print(
			Fore.RED + '\n[' + Fore.WHITE + '0' + Fore.RED + ']' + Fore.WHITE + ' Выход',
			Fore.RED + '\n[' + Fore.WHITE + '1' + Fore.RED + ']' + Fore.WHITE + ' Email спам',
			Fore.RED + '\n[' + Fore.WHITE + '2' + Fore.RED + ']' + Fore.WHITE + ' СМС спам',
			Fore.RED + '\n[' + Fore.WHITE + '3' + Fore.RED + ']' + Fore.WHITE + ' Telegram спам',
			Fore.RED + '\n[' + Fore.WHITE + '4' + Fore.RED + ']' + Fore.WHITE + ' DoS атака',
			Fore.RED + '\n[' + Fore.WHITE + '5' + Fore.RED + ']' + Fore.WHITE + ' WhatsApp спам',
			Fore.RED + '\n[' + Fore.WHITE + '6' + Fore.RED + ']' + Fore.WHITE + ' Discord спам',
			Fore.RED + '\n[' + Fore.WHITE + '7' + Fore.RED + ']' + Fore.WHITE + ' Очистить кэш программы',
			Fore.RED + '\n[' + Fore.WHITE + '8' + Fore.RED + ']' + Fore.WHITE + ' Изменить язык',
			Fore.RED + '\n[' + Fore.WHITE + '9' + Fore.RED + ']' + Fore.WHITE + ' Бесплатные прокси',
			Fore.RED + '\n[' + Fore.WHITE + '10' + Fore.RED + ']' + Fore.WHITE + ' \033[31m♥ Донат \033[31m♥'
		)

	else:
		print(
			Fore.WHITE + '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━',
			Fore.RED + '\nCreated by ebankoff - https://github.com/ebankoff',
			Fore.RED + f'\nOS: {platform}',
			Fore.RED + f'\nBeast Bomber in telegram: https://t.me/beast_bomberr_bot',
			Fore.WHITE + '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
		)

		print(
			Fore.RED + '\n[' + Fore.WHITE + '0' + Fore.RED + ']' + Fore.WHITE + ' Exit',
			Fore.RED + '\n[' + Fore.WHITE + '1' + Fore.RED + ']' + Fore.WHITE + ' Email spam',
			Fore.RED + '\n[' + Fore.WHITE + '2' + Fore.RED + ']' + Fore.WHITE + ' SMS spam',
			Fore.RED + '\n[' + Fore.WHITE + '3' + Fore.RED + ']' + Fore.WHITE + ' Telegram spam',
			Fore.RED + '\n[' + Fore.WHITE + '4' + Fore.RED + ']' + Fore.WHITE + ' DoS attack',
			Fore.RED + '\n[' + Fore.WHITE + '5' + Fore.RED + ']' + Fore.WHITE + ' WhatsApp spam',
			Fore.RED + '\n[' + Fore.WHITE + '6' + Fore.RED + ']' + Fore.WHITE + ' Discord spam',
			Fore.RED + '\n[' + Fore.WHITE + '7' + Fore.RED + ']' + Fore.WHITE + ' Clear program cache',
			Fore.RED + '\n[' + Fore.WHITE + '8' + Fore.RED + ']' + Fore.WHITE + ' Changle language',
			Fore.RED + '\n[' + Fore.WHITE + '9' + Fore.RED + ']' + Fore.WHITE + ' Free proxies',
			Fore.RED + '\n[' + Fore.WHITE + '10' + Fore.RED + ']' + Fore.WHITE + ' \033[31m♥ Donate \033[31m♥'
		)

	try:
		ans = input(Fore.RED + '\n → ' + Fore.CYAN)

		if ans == '0':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")
			ex()

		elif ans == '1':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			check_internet()

			print(Fore.WHITE + 
				'┏━━━┓      ┏┓'
				'\n┃┏━━┛      ┃┃'
				'\n┃┗━━┳┓┏┳━━┳┫┃'
				'\n┃┏━━┫┗┛┃┏┓┣┫┃'
				'\n┃┗━━┫┃┃┃┏┓┃┃┗┓'
				'\n┗━━━┻┻┻┻┛┗┻┻━┛\n')

			try:
				ans4 = ""
				ans5 = ""
				emails = []
				passwords = []

				if lang == 'ru':
					to = input(Fore.WHITE + 'Введите email жертвы: \033[36m')
					amount = int(input(Fore.WHITE + 'Сколько писем отправлять с каждой почты: \033[36m'))
					subj = input(Fore.WHITE + 'Тема письма: \033[36m')
					mes = input(Fore.WHITE + 'Текст письма: \033[36m')
					server = input(Fore.WHITE + 'Выберете сервер email адресов - 1:Gmail 2:Yahoo 3:Outlook 4:Yandex: \033[36m')
				else:
					to = input(Fore.WHITE + 'Enter target email: \033[36m')
					amount = int(input(Fore.WHITE + 'How many send from every address: \033[36m'))
					subj = input(Fore.WHITE + 'Enter subject: \033[36m')
					mes = input(Fore.WHITE + 'Enter message: \033[36m')
					server = input(Fore.WHITE + 'Select emails server - 1:Gmail 2:Yahoo 3:Outlook 4:Yandex: \033[36m')

				with open(r"input/emails.txt", "r", encoding="utf-8") as file:
					for line in file:
						pos = line.find(':')
						ans4 += line[:pos]
						emails.append(ans4)
						ans4 = ""

				with open(r"input/emails.txt", "r", encoding="utf-8") as file:
					for line in file:
						pos = line.find(':')
						ans5 += line[pos + 1:]
						passwords.append(ans5)
						ans5 = ""

				emails = [line.rstrip() for line in emails]
				passwords = [line.rstrip() for line in passwords]

				for i in range(len(emails)):
					th = Thread(target=email, args=(emails[i], passwords[i], to, amount, subj, mes, server,))
					th.start()

				print('\n')

				tm = amount
				text2 =  Fore.YELLOW + "{}"
				t = time.monotonic()

				if lang == 'ru':
					while time.monotonic() - t < tm:
						print(text2.format('\033[36mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[31mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[32mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[36mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[33mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[34mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[35mАтака') + '\r', end='')
						time.sleep(.08)

					print(Fore.WHITE + '\n━━━━━━━━━━Успех━━━━━━━━━━\n')
				else:
					while time.monotonic() - t < tm:
						print(text2.format('\033[36mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[31mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[32mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[36mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[33mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[34mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[35mAttacking') + '\r', end='')
						time.sleep(.08)

					print(Fore.WHITE + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				if lang == 'ru':
					print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')

				else:
					print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '2':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.WHITE + 
				'┏━━━┓┏━┓┏━┓┏━━━┓'
				'\n┃┏━┓┃┃ ┗┛ ┃┃┏━┓┃'
				'\n┃┗━━┫┃┏┓┏┓┃┃┗━━┫'
				'\n┗━━┓┃┃┃┃┃┃┃┗━━┓┃'
				'\n┃┗━┛┃┃┃┃┃┃┃┃┗━┛┃'
				'\n┗━━━┛┗┛┗┛┗┛┗━━━┛'
			)

			print(Fore.WHITE + 
				'\n\033[36m==============================='
				'\n     \033[32mSupported \033[33mcountries'
				'\n          \033[35mRU    \033[35mBY'
				'\n             \033[35mKZ'    
				'\n\033[36m==============================='
			)

			try:
				if lang == 'ru':
					prx = input(Fore.WHITE + "\nПрокси? yes/no: \033[36m").lower()
					captcha = input(Fore.WHITE + "Использовать anticaptcha? yes/no: \033[36m").lower()
					key = ''

					if captcha == 'yes':
						key = input(Fore.WHITE + "Anticaptcha ключ: \033[36m")

					code = input(Fore.WHITE + "Код страны: \033[36m+")

					if code != '380' and code != '44' and code != '7' and code != '1' and code != '375':
						print('Вы ввели неверное значение или эта страна не поддерживается')
						ex()

					number = input(Fore.WHITE + f"Номер телефона: \033[36m{code}")
					tm = int(input(Fore.WHITE + "Время атаки(в секундах): \033[36m"))
					thr = int(input(Fore.WHITE + "Количество потоков: \033[36m"))

				else:
					prx = input(Fore.WHITE + "\nProxy? yes/no: \033[36m").lower()
					captcha = input(Fore.WHITE + "Use anticaptcha? yes/no: \033[36m").lower()
					key = ''

					if captcha == 'yes':
						key = input(Fore.WHITE + "Anticaptcha key: \033[36m")

					code = input(Fore.WHITE + "Target country code: \033[36m+")

					if code != '380' and code != '44' and code != '7' and code != '1' and code != '375':
						print('You entered the wrong value, or the country is not supported')
						ex()

					number = input(Fore.WHITE + f"Target number: \033[36m{code}")
					tm = int(input(Fore.WHITE + "Time attack(in seconds): \033[36m"))
					thr = int(input(Fore.WHITE + "Number of threads: \033[36m"))

				if thr < 0:
					thr = 1

				if lang == 'ru':
					text = "\033[35m[\033[36m{}\033[35m]" + Fore.CYAN + " потоков запущено"

				else:
					text = "\033[35m[\033[36m{}\033[35m]" + Fore.CYAN + " threads started"

				for i in range(thr):
					th = Thread(target=sms, args=(prx, number, tm, code, key,))
					th.start()
					print(text.format(str(i + 1)) + '\r', end='')
					time.sleep(.02)

				print('\n')
				text2 =  Fore.WHITE + "{}"
				t = time.monotonic()

				if lang == 'ru':
					while time.monotonic() - t < tm:
						print(text2.format('\033[36mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[31mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[32mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[36mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[33mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[34mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[35mАтака') + '\r', end='')
						time.sleep(.08)

					print(Fore.WHITE + '\n━━━━━━━━━━Успех━━━━━━━━━━\n')

				else:
					while time.monotonic() - t < tm:
						print(text2.format('\033[36mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[31mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[32mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[36mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[33mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[34mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[35mAttacking') + '\r', end='')
						time.sleep(.08)

					print(Fore.WHITE + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				if lang == 'ru':
					print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')

				else:
					print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '3':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.WHITE + 
				'┏━━━━┓ ┏┓'
				'\n┃┏┓┏┓┃ ┃┃'
				'\n┗┛┃┃┣┻━┫┃┏━━┳━━┳━┳━━┳┓┏┓'
				'\n  ┃┃┃ ━┫┃┃ ━┫┏┓┃┏┫┏┓┃┗┛┃'
				'\n  ┃┃┃ ━┫┗┫ ━┫┗┛┃┃┃┏┓┃┃┃┃'
				'\n  ┗┛┗━━┻━┻━━┻━┓┣┛┗┛┗┻┻┻┛'
				'\n            ┏━┛┃'
				'\n            ┗━━┛'
			)

			try:
				if lang == 'ru':
					prx = input(Fore.WHITE + "\n Прокси? yes/no: \033[36m").lower()
					name = input(Fore.WHITE + "Ник жертвы: \033[36m")
					count = int(input(Fore.WHITE + "Количество сообщений: \033[36m"))
					msg = input(Fore.WHITE + "Текст: \033[36m")
					cn = 0
					print("")
					input(Fore.WHITE + "Нажмите Enter чтобы начать")
					telegram(name, count, msg, cn, prx)

					print(Fore.WHITE + '\n━━━━━━━━━━Успех━━━━━━━━━━\n')

				else:
					prx = input(Fore.WHITE + "\nProxy? yes/no: \033[36m").lower()
					name = input(Fore.WHITE + "Victim name: \033[36m")
					count = int(input(Fore.WHITE + "Number of messages: \033[36m"))
					msg = input(Fore.WHITE + "Message: \033[36m")
					cn = 0
					print("")
					input(Fore.WHITE + "Press Enter to start")
					telegram(name, count, msg, cn, prx)

					print(Fore.WHITE + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				if lang == 'ru':
					print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')

				else:
					print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '4':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.WHITE + 
				'┏━━━┓  ┏━━━┓'
				'\n┗┓┏┓┃  ┃┏━┓┃'
				'\n ┃┃┃┣━━┫┗━━┓'
				'\n ┃┃┃┃┏┓┣━━┓┃'
				'\n┏┛┗┛┃┗┛┃┗━┛┃'
				'\n┗━━━┻━━┻━━━┛'
			)

			try:
				if lang == 'ru':
					prx = input(Fore.WHITE + "\nПрокси? yes/no: \033[36m").lower()
					url = input(Fore.WHITE + "URL: \033[36m")
					tm = int(input(Fore.WHITE + "Время атаки в секундах: \033[36m"))
					threads = int(input(Fore.WHITE + "Потоки: \033[36m"))

					text = "\033[35m[\033[36m{}\033[35m]" + Fore.CYAN + " потоков запущено"

				else:
					prx = input(Fore.WHITE + "\nProxy? yes/no: \033[36m").lower()
					url = input(Fore.WHITE + "URL: \033[36m")
					tm = int(input(Fore.WHITE + "Attack time in seconds: \033[36m"))
					threads = int(input(Fore.WHITE + "Threads: \033[36m"))

					text = "\033[35m[\033[36m{}\033[35m]" + Fore.CYAN + " threads started"

				for i in range(threads):
					th = Thread(target=dos, args=(url, tm, prx,))
					th.start()
					print(text.format(str(i + 1)) + '\r', end='')
					time.sleep(.02)

				print('\n')

				text2 =  Fore.YELLOW + "{}"
				t = time.monotonic()
				if lang == 'ru':
					while time.monotonic() - t < tm:
						print(text2.format('\033[36mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[31mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[32mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[36mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[33mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[34mАтака') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[35mАтака') + '\r', end='')
						time.sleep(.08)

					print(Fore.WHITE + '\n━━━━━━━━━━Успех━━━━━━━━━━\n')

				else:
					while time.monotonic() - t < tm:
						print(text2.format('\033[36mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[31mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[32mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[36mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[33mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[34mAttacking') + '\r', end='')
						time.sleep(.08)
						print(text2.format('\033[35mAttacking') + '\r', end='')
						time.sleep(.08)

					print(Fore.WHITE + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				if lang == 'ru':
					print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')

				else:
					print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '5':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.WHITE +
				'┏┓┏┓┏┳┓    ┏┓   ┏━━━┓'
				'\n┃┃┃┃┃┃┃   ┏┛┗┓  ┃┏━┓┃'
				'\n┃┃┃┃┃┃┗━┳━┻┓┏╋━━┫┃ ┃┣━━┳━━┓'
				'\n┃┗┛┗┛┃┏┓┃┏┓┃┃┃━━┫┗━┛┃┏┓┃┏┓┃'
				'\n┗┓┏┓┏┫┃┃┃┏┓┃┗╋━━┃┏━┓┃┗┛┃┗┛┃'
				'\n ┗┛┗┛┗┛┗┻┛┗┻━┻━━┻┛ ┗┫┏━┫┏━┛'
				'\n                    ┃┃ ┃┃'
				'\n                    ┗┛ ┗┛'
			)

			try:
				if lang == 'ru':
					prx = input(Fore.WHITE + "\nПрокси? yes/no: \033[36m").lower()
					name = input(Fore.WHITE + "Ник жертвы: \033[36m")
					count = int(input(Fore.WHITE + "Количество сообщений: \033[36m"))
					msg = input(Fore.WHITE + "Текст: \033[36m")

				else:
					prx = input(Fore.WHITE + "\nProxy? yes/no: \033[36m").lower()
					name = input(Fore.WHITE + "Victim name: \033[36m")
					count = int(input(Fore.WHITE + "Number of messages: \033[36m"))
					msg = input(Fore.WHITE + "Message: \033[36m")
				cn=0

				print("")
				if lang == 'ru':
					input(Fore.WHITE + "Нажмите Enter чтобы начать")
					whatsapp(name, count, msg, cn, prx)
					print(Fore.WHITE + '\n━━━━━━━━━━Успех━━━━━━━━━━\n')
				else:
					input(Fore.WHITE + "Press Enter to start")
					whatsapp(name, count, msg, cn, prx)
					print(Fore.WHITE + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				if lang == 'ru':
					print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')

				else:
					print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '6':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.WHITE + 
				'┏━━━┓             ┏┓'
				'\n┗┓┏┓┃             ┃┃'
				'\n ┃┃┃┣┳━━┳━━┳━━┳━┳━┛┃'
				'\n ┃┃┃┣┫━━┫┏━┫┏┓┃┏┫┏┓┃'
				'\n┏┛┗┛┃┣━━┃┗━┫┗┛┃┃┃┗┛┃'
				'\n┗━━━┻┻━━┻━━┻━━┻┛┗━━┛'
			)

			try:
				if lang == 'ru':
					prx = input(Fore.WHITE + "\nПрокси? yes/no: \033[36m").lower()
					idd = input(Fore.WHITE + "ID жертвы: \033[36m")
					tkn = input(Fore.WHITE + "Токен аккаунта: \033[36m")
					cnt = int(input(Fore.WHITE + "Количество сообщений: \033[36m"))
					msg = input(Fore.WHITE + "Текст: \033[36m")
					input(Fore.WHITE + "Нажмите Enter чтобы начать")

				else:
					prx = input(Fore.WHITE + "\nProxy? yes/no: \033[36m").lower()
					idd = input(Fore.WHITE + "Target ID: \033[36m")
					tkn = input(Fore.WHITE + "Account token: \033[36m")
					cnt = int(input(Fore.WHITE + "Number of messages: \033[36m"))
					msg = input(Fore.WHITE + "Message: \033[36m")
					input(Fore.WHITE + "\nPress Enter to start")

				discord(tkn, idd, msg, cnt, prx)

				if lang == 'ru':
					print(Fore.WHITE + '\n━━━━━━━━━━Успех━━━━━━━━━━\n')
				else:
					print(Fore.WHITE + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '7':
			try:
				print('')
				pb()
				shutil.rmtree('core\\__pycache__')
				print('')
				if lang == 'ru':
					print(Fore.WHITE + '\n━━━━━━━━━━Успех━━━━━━━━━━\n')
				else:
					print(Fore.WHITE + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				if lang == 'ru':
					print(Fore.RED + '\n━━━━━━━━━━━Кэш пуст━━━━━━━━━━━')
				else:
					print(Fore.RED + '\n━━━━━━━━━━━The program cache is empty━━━━━━━━━━━')

			ex()

		elif ans == '8':
			config_path = os.path.join(sys.path[0], r'core\\config.ini')
			if lang == 'ru':
				read_file=open(config_path,"r")
				ontent=read_file.read()
				config_object= configparser.ConfigParser()
				config_object.read(config_path)
				config_object["config"]["lang"]="en"

				with open(config_path,"w") as file_object:
				    config_object.write(file_object)

			else:
				read_file=open(config_path,"r")
				ontent=read_file.read()
				config_object= configparser.ConfigParser()
				config_object.read(config_path)
				config_object["config"]["lang"]="ru"

				with open(config_path,"w") as file_object:
				    config_object.write(file_object)

			main()

		elif ans == '9':
			try:
				get_proxies()

				if lang == 'ru':
					print(Fore.WHITE + '\n━━━━━━━━━━━Прокси обновлены━━━━━━━━━━━\n')

				else:
					print(Fore.WHITE + '\n━━━━━━━━━━━Proxies updated━━━━━━━━━━━\n')

			except:
				if lang == 'ru':
					print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')

				else:
					print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()


		elif ans == '10':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(
				Fore.WHITE + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━",
				'\n\033[35m▸ \033[36mPayeer: P1063409412',
				'\n\033[35m▸ \033[36mBNB: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1',
				'\n\033[35m▸ \033[36mBitcoin: bc1qxfvstf99kyuc5x5uugxtsh3m6w3a73ruzfav7e',
				'\n\033[35m▸ \033[36mEthereum: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1',
				Fore.WHITE + '\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'
			)

			ex()

		else:
			if lang == 'ru':
				print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')

			else:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')
				
			ex()

	except:
		if lang == 'ru':
			print(Fore.RED + '\n━━━━━━━━━━━Ошибка━━━━━━━━━━━\n')
		else:
			print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')
		ex()

if __name__=='__main__':
	if platform == 'win32':
		ctypes.windll.kernel32.SetConsoleTitleW("Beast bomber 💣")
	pb()
	main()
