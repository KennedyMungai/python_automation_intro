
# EmailBody
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# WebScraping
from bs4 import BeautifulSoup

# HTTP requests
import requests
# System Date and Time Manipulation
import datetime


now = datetime.datetime.now()

# Email content placeholder
content = ''

# Extracting Hacker News Stories


def extract_news(url):
    print('Extracting content from hacker news')
