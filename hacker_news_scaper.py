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
    """A function that holds web scraping logic

    Args:
        url (string): The location of the website
    """
    print('Extracting content from hacker news')

    cnt = ''
    cnt += ('<b>Hacker News Top Stories: </b>\n' + '<br>' + '-'*50+'<br>')

    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')

    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'yalign': ''})):
        cnt += ((str(i+1) + ' :: ' + tag.text + '\n' + '<br />')
                ) if tag.next != 'More' else ''

    return cnt


cnt = extract_news('https://news.ycombinator.com/')
