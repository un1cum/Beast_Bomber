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
import platform
from sys import platform
from os import name, system
from os.path import exists, isfile

if platform == 'win32':
	ctypes.windll.kernel32.SetConsoleTitleW("Preparing to launch the beast bomber...")

try:
	os.system('pip install configparser')
	import configparser
	ans = ""
	config_path = os.path.join(sys.path[0], r'core/config.ini')
	config = configparser.ConfigParser()
	config.read(config_path)
	ans = config.get('config', 'first_setup')
	if ans != 'yes':
		try:
			os.system('pip install lxml && pip install matplotlib && pip install pandas && pip install numpy && pip install bs4 && pip install emoji && pip install wheel && pip install asyncio && pip install requests && pip install progress && pip install colorama && pip install selenium && pip install user_agent && pip install about-time && pip install progressbar && pip install beautifulsoup4 && pip install selenium_stealth && pip install webdriver-manager')
			config['config']['first_setup'] = 'yes'
			with open(r'core/config.ini', 'w') as configfile:
				config.write(configfile)
		except:
			pass
except:
	pass

if platform == 'win32':
	os.system("cls")
else:
	os.system("clear")

import time
import shutil
import colorama
from threading import Thread
from core.sms_spam import sms
from requests import get, post
from core.dos_attack import dos
from core.freeprx import freeprx
from core.email_spam import email
from core.discord_spam import discord
from core.whatsapp_spam import whatsapp
from core.telegram_spam import telegram
from colorama import Fore, Back, Style, init

colorama.init()


def pb():
	tm = 2
	text2 =  Fore.YELLOW + Style.BRIGHT + "{}"
	t = time.monotonic()
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
	try:
		get("http://google.com", timeout=1)

	except:
		print(
			Fore.RED + '╔═════════════════════════════╗',
			Fore.RED + '\n║   No internet connection!   ║',
			Fore.RED + '\n╚═════════════════════════════╝'
		)

		input()
		ex()


def ex():
	param = input(Fore.YELLOW + Style.BRIGHT + 'Exit? yes/no: ')

	if param == 'yes':
		if platform == 'win32':
			os.system("cls")
		else:
			os.system("clear")

		print(Fore.CYAN + 
		'               Thanks for using Beast bomber!'
		'\nI would be grateful if you star on this repository on GitHub:'
		'\n           https://github.com/ebankoff/BeastBomber'
		'\n    You can support me by sending any amount to my Qiwi:'	
		'\n                  qiwi.com/n/HERAMANT'	
		'\n'
		'\n              Copyright (C) 2022 ebankoff')
		print("\nPress Enter to exit")
		input()
		os.abort()

	elif param == 'no':
		main()

	else:
		print(Fore.RED + '━━━━━━━━━━Invalid value━━━━━━━━━━')
		ex()


def main():
	if platform == 'win32':
		os.system("cls")
	else:
		os.system("clear")

	print(Fore.CYAN + 
		'┏━━┓         ┏┓  ┏━━┓      ┏┓'
		'\n┃┏┓┃        ┏┛┗┓ ┃┏┓┃      ┃┃'
		'\n┃┗┛┗┳━━┳━━┳━┻┓┏┛ ┃┗┛┗┳━━┳┓┏┫┗━┳━━┳━┓'
		'\n┃┏━┓┃ ━┫┏┓┃━━┫┃  ┃┏━┓┃┏┓┃┗┛┃┏┓┃ ━┫┏┛'
		'\n┃┗━┛┃ ━┫┏┓┣━━┃┗┓ ┃┗━┛┃┗┛┃┃┃┃┗┛┃ ━┫┃'
		'\n┗━━━┻━━┻┛┗┻━━┻━┛ ┗━━━┻━━┻┻┻┻━━┻━━┻┛'
	)

	print(
		Fore.CYAN + '\n=================================================',
		Fore.YELLOW + '\nCreated by ebankoff - https://github.com/ebankoff',
		Fore.YELLOW + f'\nOS: {platform}',
		Fore.CYAN + '\n================================================='
	)

	print(
		Fore.MAGENTA + '\n[' + Fore.GREEN + '0' + Fore.MAGENTA + ']' + Fore.RED + ' Exit',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '1' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' Email spam',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '2' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' SMS spam',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '3' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' Telegram spam',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '4' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' DoS attack',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '5' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' WhatsApp spam',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '6' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' Discord spam',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '7' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' Get free proxies',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '8' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' Clear program cache',
		Fore.MAGENTA + '\n[' + Fore.GREEN + '9' + Fore.MAGENTA + ']' + Fore.YELLOW + Style.BRIGHT + ' \033[31m♥ Donate \033[31m♥'
	)

	try:
		ans = input(Fore.MAGENTA + '\n → ' + Fore.CYAN)

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

			try:
				ans4 = ""
				ans5 = ""
				emails = []
				passwords = []

				to = str(input(Fore.YELLOW + Style.BRIGHT + 'Enter target email: \033[36m'))
				amount = int(input(Fore.YELLOW + Style.BRIGHT + 'How many send from every address: \033[36m'))
				subj = str(input(Fore.YELLOW + Style.BRIGHT + 'Enter subject: \033[36m'))
				mes = str(input(Fore.YELLOW + Style.BRIGHT + 'Enter message: \033[36m'))
				server = input(Fore.YELLOW + Style.BRIGHT + 'Select emails server - 1:Gmail 2:Yahoo 3:Outlook 4:Yandex: \033[36m')

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
				text2 =  Fore.YELLOW + Style.BRIGHT + "{}"
				t = time.monotonic()

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

				print(Fore.GREEN + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '2':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT + 
				'┏━━━┓┏━┓┏━┓┏━━━┓'
				'\n┃┏━┓┃┃ ┗┛ ┃┃┏━┓┃'
				'\n┃┗━━┫┃┏┓┏┓┃┃┗━━┫'
				'\n┗━━┓┃┃┃┃┃┃┃┗━━┓┃'
				'\n┃┗━┛┃┃┃┃┃┃┃┃┗━┛┃'
				'\n┗━━━┛┗┛┗┛┗┛┗━━━┛'
			)

			print(Fore.YELLOW + Style.BRIGHT + 
				'\n\033[36m==============================='
				'\n     \033[32mSupported \033[33mcountries'
				'\n          \033[35mRU    \033[35mBY'
				'\n          \033[35mKZ    \033[35mUA'
				'\n          \033[35mUS    \033[35mUK'
				'\n\033[36m==============================='
			)

			try:
				prx = input(Fore.YELLOW + Style.BRIGHT + "\nProxy? yes/no: \033[36m").lower()
				code = input(Fore.YELLOW + Style.BRIGHT + "Target country code: \033[36m+")

				if code != '380' and code != '44' and code != '7' and code != '1' and code != '375':
					print('You entered the wrong value, or the country is not supported')
					ex()

				number = code + input(Fore.YELLOW + Style.BRIGHT + f"Target number: \033[36m{code}")
				tm = int(input(Fore.YELLOW + Style.BRIGHT + "Time attack(in seconds): \033[36m"))
				thr = int(input(Fore.YELLOW + Style.BRIGHT + "Number of threads: \033[36m"))

				if thr < 0:
					thr = 1

				text = "\033[35m[\033[36m{}\033[35m]" + Fore.CYAN + " threads started"
				for i in range(thr):
					th = Thread(target=sms, args=(prx, number, tm, code,))
					th.start()
					print(text.format(str(i + 1)) + '\r', end='')
					time.sleep(.02)

				print('\n')
				text2 =  Fore.YELLOW + Style.BRIGHT + "{}"
				t = time.monotonic()
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

				print(Fore.GREEN + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '3':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT + 
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
				prx = input(Fore.YELLOW + Style.BRIGHT + "\nProxy? yes/no: \033[36m").lower()
				name = input(Fore.YELLOW + Style.BRIGHT + "Victim name: \033[36m")
				count = int(input(Fore.YELLOW + Style.BRIGHT + "Number of messages: \033[36m"))
				msg = input(Fore.YELLOW + Style.BRIGHT + "Message: \033[36m")
				cn = 0
				print("")
				input(Fore.YELLOW + Style.BRIGHT + "Press Enter to start")
				telegram(name, count, msg, cn, prx)

				print(Fore.GREEN + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '4':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT + 
				'┏━━━┓  ┏━━━┓'
				'\n┗┓┏┓┃  ┃┏━┓┃'
				'\n ┃┃┃┣━━┫┗━━┓'
				'\n ┃┃┃┃┏┓┣━━┓┃'
				'\n┏┛┗┛┃┗┛┃┗━┛┃'
				'\n┗━━━┻━━┻━━━┛'
			)

			try:
				prx = input(Fore.YELLOW + Style.BRIGHT + "\nProxy? yes/no: \033[36m").lower()
				url = input(Fore.YELLOW + Style.BRIGHT + "URL:n\033[36m")
				tm = int(input(Fore.YELLOW + Style.BRIGHT + "Attack time in seconds: \033[36m"))
				threads = int(input(Fore.YELLOW + Style.BRIGHT + "Threads: \033[36m"))

				text = "\033[35m[\033[36m{}\033[35m]" + Fore.CYAN + " threads started"

				for i in range(threads):
					th = Thread(target=dos, args=(url, tm, prx,))
					th.start()
					print(text.format(str(i + 1)) + '\r', end='')
					time.sleep(.02)

				print('\n')

				text2 =  Fore.YELLOW + Style.BRIGHT + "{}"
				t = time.monotonic()
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
				
				print(Fore.GREEN + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '5':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT +
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
				prx = input(Fore.YELLOW + Style.BRIGHT + "\nProxy? yes/no: \033[36m").lower()
				name = input(Fore.YELLOW + Style.BRIGHT + "Victim name: \033[36m")
				count = int(input(Fore.YELLOW + Style.BRIGHT + "Number of messages: \033[36m"))
				msg = input(Fore.YELLOW + Style.BRIGHT + "Message: \033[36m")
				cn=0

				print("")
				input(Fore.YELLOW + Style.BRIGHT + "Press Enter to start")
				whatsapp(name, count, msg, cn, prx)

				print(Fore.GREEN + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '6':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT + 
				'┏━━━┓             ┏┓'
				'\n┗┓┏┓┃             ┃┃'
				'\n ┃┃┃┣┳━━┳━━┳━━┳━┳━┛┃'
				'\n ┃┃┃┣┫━━┫┏━┫┏┓┃┏┫┏┓┃'
				'\n┏┛┗┛┃┣━━┃┗━┫┗┛┃┃┃┗┛┃'
				'\n┗━━━┻┻━━┻━━┻━━┻┛┗━━┛'
			)

			try:
				prx = input(Fore.YELLOW + Style.BRIGHT + "\nProxy? yes/no: \033[36m").lower()
				idd = input(Fore.YELLOW + Style.BRIGHT + "Target ID: \033[36m")
				tkn = input(Fore.YELLOW + Style.BRIGHT + "Account token: \033[36m")
				cnt = int(input(Fore.YELLOW + Style.BRIGHT + "Number of messages: \033[36m"))
				msg = input(Fore.YELLOW + Style.BRIGHT + "Message: \033[36m")
				input(Fore.YELLOW + Style.BRIGHT + "\nPress Enter to start")
				discord(tkn, idd, msg, cnt, prx)
				
				print(Fore.GREEN + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '7':
			try:
				print('')
				pb()
				freeprx()
				print('')
				print(Fore.GREEN + '\n━━━━━━━━━━━Proxies saved━━━━━━━━━━━')
				print('')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')

			ex()

		elif ans == '8':
			try:
				print('')
				pb()
				shutil.rmtree('core/__pycache__')
				print('')
				print(Fore.GREEN + '\n━━━━━━━━━━Success━━━━━━━━━━\n')

			except:
				print(Fore.RED + '\n━━━━━━━━━━━The program cache is already empty━━━━━━━━━━━')

			ex()

		elif ans == '9':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(
				Fore.YELLOW + Style.BRIGHT + "===========================================================",
				'\n\033[35m▸ \033[36mPayeer: P1063409412',
				'\n\033[35m▸ \033[36mQiwi: https://qiwi.com/n/HERAMANT',
				'\n\033[35m▸ \033[36mBNB: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1',
				'\n\033[35m▸ \033[36mBitcoin: bc1qxfvstf99kyuc5x5uugxtsh3m6w3a73ruzfav7e',
				'\n\033[35m▸ \033[36mEthereum: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1',
				Fore.YELLOW + Style.BRIGHT + '\n===========================================================\n'
			)

			ex()

		else:
			print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')
			ex()

	except:
		print(Fore.RED + '\n━━━━━━━━━━━Error━━━━━━━━━━━\n')
		ex()

if __name__=='__main__':
	if platform == 'win32':
		ctypes.windll.kernel32.SetConsoleTitleW("Beast bomber 💣")
	pb()
	main()