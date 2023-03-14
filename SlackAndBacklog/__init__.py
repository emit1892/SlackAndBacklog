import logging
import os
import requests
from SlackAndBacklog import comments
from SlackAndBacklog import issues
import azure.functions as func

BASE_URL = 'https://{backlog_space_id}.backlog.com/api/v2/{api}'
api_key = os.environ.get("BACKLOG_TOKEN")
backlog_space_key = os.environ.get("BACKLOG_SPACE_KEY")

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    # リクエストボディからメンション情報を取得
    slack_req_json = req.get_json()
    logging.info(slack_req_json)
    
    # 投稿するBacklogの課題キー
    issue_id_key = slack_req_json['event']['text'].split(' ')[1]
    logging.info(issue_id_key)

    # slack情報から投稿コメントを作成
    comment = comments.create_comment(slack_req_json)
    
    # slackに投稿
    logging.info(f'課題キー: {issue_id_key}')
    logging.info(f'コメント内容: {comment}')
    
    issues_info = issues.get_issues_info(issue_id_key)
    
    if 'errors' in issues_info:
        return func.HttpResponse(f'{issue_id_key} は存在しません。' ,status_code=200)
    else:
        #comments.add_comment(comment, issue_id_key, api_key, backlog_space_key)
        logging.info(issues_info['issueKey'])
        return func.HttpResponse('' ,status_code=200)