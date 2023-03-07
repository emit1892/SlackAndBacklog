import requests
from datetime import datetime
import os

TOKEN = os.environ.get("SLACK_TOKEN")
CHANNEL = 'C04SBRJBY3D'
THEREAD = '1678096378.742129'
BASE_TOKEN = 'Bearer {TOKEN}'

url = 'https://slack.com/api/conversations.replies'

headers = {
    "Authorization":  BASE_TOKEN.format(TOKEN=TOKEN)
}

params = {
    "channel": CHANNEL,
    "ts": THEREAD,
    "limit": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())