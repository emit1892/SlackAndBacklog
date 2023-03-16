import requests
import logging
from SlackAndBacklog import slack
import azure.functions as func
import json

BASE_URL = 'https://{backlog_space_id}.backlog.com/api/v2/{api}'

def add_comment(_comment, _issue_id_key, _api_key, _backlog_space_key):
    """
    Backlogにコメントを追加する

    Args:
        _comment (str): コメント
        _issue_id_key (str): 課題番号
        _api_key (str): apikey
        _backlog_space_key (str): プロジェクトキー

    Returns:
        登録結果
    """
    api = f'issues/{_issue_id_key}/comments'
    url = BASE_URL.format(backlog_space_id=_backlog_space_key, api=api)
    
    params = {
        'apiKey': _api_key
    }
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    payload = {
        'content': _comment
    }
    
    response = requests.post(url, params=params, headers=headers, data=payload)
    response.raise_for_status()
    
    return response

def create_comment(_slack_req_json):
    """
    Slack情報からBacklog用コメントを作成する

    Args:
        _slack_req_json (str): Slack情報

    Returns: 
        Backlog用コメント
    """
    
    slack_req_json = _slack_req_json
    channel_id = slack_req_json['event']['channel'] 
    ts = slack_req_json['event']['ts']
    thread_ts = slack_req_json['event']['thread_ts']
    
    slack_reply_json = slack.get_slack_reply(channel_id, thread_ts)
    logging.info(slack_reply_json)
    
    comment = 'Slackから登録\r\n'
    
    for slack_comment in slack_reply_json['messages']:
        # @Slack and Backlogの投稿は除外
        if not f'@U04SCK3SJG3' in slack_comment['text']:
            comment += slack_comment['text']
            comment += '\r\n***********\r\n'
        
    return comment
