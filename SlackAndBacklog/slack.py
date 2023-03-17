import requests
import os

def get_slack_reply(_channel, _thread):
    """
    指定したチャンネル内のスレッドの投稿を取得

    Args:
        _channel (str): チャンネルID
        _thread (str): スレッド情報
    """
    
    TOKEN = os.environ.get("SLACK_TOKEN")
    BASE_TOKEN = 'Bearer {TOKEN}'
    
    url = 'https://slack.com/api/conversations.replies'

    headers = {
        "Authorization": BASE_TOKEN.format(TOKEN=TOKEN)
    }

    params = {
        "channel": _channel,
        "ts": _thread
    }

    response = requests.get(url, headers=headers, params=params)
    
    return response.json()