import requests

from bs4 import BeautifulSoup

import re

import sys


# Exception Handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit('Error: Please enter the TED Talk URL')

r = requests.get(url)

print('Download about to start')

soup = BeautifulSoup(r.content, features='lxml')

for val in soup.findAll("script"):
    if (re.search("talkPage.init", str(val))) is not None:
        result = str(val)
