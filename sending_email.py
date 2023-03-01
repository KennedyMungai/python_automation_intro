import os
from dotenv import load_dotenv

load_dotenv()

print('Composing Email....')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM = os.getenv("FROM_EMAIL_ADDRESS")
TO = os.getenv("TO_EMAIL_ADDRESS")
PASS = os.getenv("FROM_EMAIL_PASSWORD")
