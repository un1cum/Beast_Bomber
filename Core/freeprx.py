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

#-------------------------------------(proxies)------------------------------------

import os
import re
import bs4
import sys
import time
import json
import urllib
import socket
import ctypes
import requests
import colorama
import numpy as np
import pandas as pd
from sys import platform
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from unicodedata import normalize
from urllib.request import urlopen as uReq

def validate_ip(ip):
	a = ip.split('.')
	if len(a) != 4:
		return False
	for x in a:
		if not x.isdigit():
			return False
		i = int(x)
		if i < 0 or i > 255:
			return False
	return True

def validate_port(port):
	try:
		if int(port)>=1 and int(port)<=65535:
			return True
		else:
			return False
	except:
		return False

def freeprx():
	res = requests.get('https://hidemy.name/ru/proxy-list', headers={'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'})
	soup = BeautifulSoup(res.text,"lxml")
	
	with open("proxies.txt", "a", encoding="utf-8") as file:
		for child in soup.recursiveChildGenerator():
			if child.name=='td':
				if validate_ip(child.text):
					file.write(child.text)
					file.write(':')
				if validate_port(child.text):
					file.write(child.text)
					file.write('\n')

	res2 = requests.get('https://free-proxy-list.net', headers={'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'})
	soup2 = BeautifulSoup(res2.text,"lxml")

	cnt2=0

	with open("proxies.txt", "a", encoding="utf-8") as file:
		for child in soup2.recursiveChildGenerator():    
			if child.name=='td':
				if cnt2 == 0:
					if not validate_ip(child.text):
						break
					file.write(child.text)
					file.write(':')
				if cnt2 == 1:
					file.write(child.text)
					file.write('\n')

				cnt2 = (cnt2 + 1) % 8