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
import re
import bs4
import sys
import time
import json
import urllib
import random
import socket
import ctypes
import requests
import colorama
import pycountry
import numpy as np
import pandas as pd
import configparser
from sys import platform
from pythonping import ping
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from unicodedata import normalize
from proxy_checking import ProxyChecker
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


def get_proxies():
	cnt=0
	ip=16
	port=6
	ct=20

	url = 'https://free-proxy-list.net'

	res = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 11; SM-A326B Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'})
	soup = BeautifulSoup(res.text,"lxml")

	cnt=0

	with open(r"proxies.txt", "a", encoding="utf-8") as file:
		for child in soup.recursiveChildGenerator():    
			if child.name=='td':
				if cnt == 0:
					if not validate_ip(child.text):
						break
					file.write(child.text)
					file.write(':')

				if cnt == 1:
					file.write(child.text)
					file.write('\n')

				cnt = (cnt + 1) % 8