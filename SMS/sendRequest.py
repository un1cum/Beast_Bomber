import json
import requests
import SMS.numberTools as numberTools
import SMS.randomData as randomData


def getServices(file='SMS/services.json'):
    with open(file, 'r') as services:
        return json.load(services)["services"]


def getProxys(file='SMS/proxy.json'):
    with open(file, 'r') as proxys:
        return json.load(proxys)["proxy"]


def getDomain(url):
    return url.split('/')[2]


class Service:
    def __init__(self, service):
        self.service = service
        self.proxy = getProxys()
        self.timeout = 10

    def parseData(self, phone):
        payload = None

        try:
            dataType = "data"
            payload = self.service["data"]
        except KeyError:
            pass

        try:
            dataType = "json"
            payload = self.service["json"]
        except KeyError:
            pass
        if not payload:
            payload = json.dumps({"url": self.service["url"]})
            dataType = "url"

        for old, new in {
            "\'": "\"",
            "%phone%": phone,
            "%phone5%": numberTools.transformPhone(phone, 5),
            "%name%": randomData.random_name(),
            "%email%": randomData.random_email(),
            "%password%": randomData.random_password()
        }.items():
            payload = payload.replace(old, new)
        return (json.loads(payload), dataType)

    def sendMessage(self, phone):
        url = self.service["url"]
        payload, dataType = self.parseData(phone)

        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Accept-Encoding": "gzip, deflate, br",
            "User-agent": randomData.random_useragent()
        }

        try:
            customHeaders = self.service["headers"]
        except KeyError:
            pass
        else:
            for key, value in json.loads(customHeaders.replace("\'", "\"")).items():
                headers[key] = value

        okay = " Service (" + getDomain(url) + ") >> Message sent!"
        error = " Service (" + getDomain(url) + ") >> Failed to sent message!"

        try:

            if dataType == "json":
                r = requests.post(url, json=payload, timeout=self.timeout, headers=headers, proxies=self.proxy)
            elif dataType == "data":
                r = requests.post(url, data=payload, timeout=self.timeout, headers=headers, proxies=self.proxy)
            elif dataType == "url":
                r = requests.post(payload["url"], timeout=self.timeout, headers=headers, proxies=self.proxy)

            if r.status_code == 200:
                print("[SUCCESS]" + okay)
            elif r.status_code == 429:
                print("[TOO MANY REQUESTS]" + error)
            else:
                print("[" + str(r.status_code) + "]" + error)

            return r.status_code

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
            print("[CONNECTION TIMED OUT]" + error)
        except (requests.exceptions.ConnectionError):
            print("[CONNECTION ERROR]" + error)
