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
