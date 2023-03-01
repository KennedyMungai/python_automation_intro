"""A simple python script for sending emails
"""
# EmailBody
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from hacker_news_scaper import now

import os
from dotenv import load_dotenv

load_dotenv()

print('Composing Email....')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = os.getenv("FROM_EMAIL_ADDRESS")
TO = os.getenv("TO_EMAIL_ADDRESS")
PASS = os.getenv("FROM_EMAIL_PASSWORD")

# Creating the message body
msg = MIMEMultipart()
