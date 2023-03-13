import requests
from datetime import datetime
import os

def get_slack_reply(_channel, _thread):
    """
    指定したチャンネル内のスレッドの投稿を取得

    Args:
        _channel (string): チャンネルID
        _thread (string): スレッド情報
    """
    
    TOKEN = os.environ.get("SLACK_TOKEN")
    CHANNEL = _channel
    THEREAD = _thread
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
    
    return response.json()