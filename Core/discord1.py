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

#--------------------------------------(discord)--------------------------------------

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
from time import sleep
from threading import *
from sys import platform
from asyncio import sleep
from getpass import getpass
from os import name, system
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

def randstr(lenn):
	lib = "abcdefghijklmnopqrstuvwxyz0123456789"
	text = ''
	for i in range(0, lenn):
			text += lib[random.randint(0, len(lib) - 1)]
	return text

def discord(token, target, mes, cnt, prx):
	header = {
		"authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
	}
	if prx == 'yes':
		proxy = []

		with open(f"proxies.txt", "r", encoding="utf-8") as file:
			for line in file:
				proxy.append(line)

		proxy = [line.rstrip() for line in proxy]
		for i in range(cnt):
			try:
				proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
				payload = {'recipient_id': target}
				r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers = header, json = payload, proxies = proxies)
				payload = {
					"content": mes, 
					"tts": False
				}
				j = json.loads(r1.content)
				r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages", headers = header, json = payload, proxies = proxies)
				now = datetime.datetime.now()
				print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[36m {}" .format(i) + "\033[37m {}" .format('|') + "\033[35m {}" .format(target))
			except:
				print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[31m {}" .format(f'FAILED') + "\033[37m {}" .format('|') + "\033[36m {}" .format(i) + "\033[37m {}" .format('|') + "\033[35m {}" .format(target))

	else:
		for i in range(cnt):
			try:
				payload = {'recipient_id': target}
				r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers = header, json = payload)
				payload = {
					"content": mes, 
					"tts": False
				}
				j = json.loads(r1.content)
				r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages", headers = header, json = payload)
				now = datetime.datetime.now()
				print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[32m {}" .format(f'SUCCESS') + "\033[37m {}" .format('|') + "\033[36m {}" .format(i) + "\033[37m {}" .format('|') + "\033[35m {}" .format(target))
			except:
				print("\033[34m{}" .format(now.strftime('%Y-%m-%d / %H:%M:%S')) + "\033[37m {}" .format('|') + "\033[31m {}" .format(f'FAILED') + "\033[37m {}" .format('|') + "\033[36m {}" .format(i) + "\033[37m {}" .format('|') + "\033[35m {}" .format(target))