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

#------------------------------------(whatsapp)------------------------------------

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