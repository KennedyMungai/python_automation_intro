"""A simple python script for sending emails
"""
# EmailBody
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from hacker_news_scaper import now, content

import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

print('Composing Email....')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = os.getenv("FROM_EMAIL_ADDRESS")
TO = os.getenv("TO_EMAIL_ADDRESSES")
PASS = os.getenv("FROM_EMAIL_PASSWORD")

# Creating the message body
msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories from Hacker News' + ' ' + \
    str(now.day) + ' - ' + str(now.month) + ' - ' + str(now.year)
msg['From'] = FROM
msg['TO'] = TO
msg.attach(MIMEText(content, 'html'))

print("Initiating Server...")

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(0)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent...')

server.quit()
