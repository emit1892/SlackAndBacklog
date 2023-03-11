import logging
import os
import requests
from SlackAndBacklog import comments
import azure.functions as func

BASE_URL = 'https://{backlog_space_id}.backlog.com/api/v2/{api}'
api_key = os.environ.get("BACKLOG_TOKEN")
backlog_space_key = os.environ.get("BACKLOG_SPACE_KEY")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(str(req.get_body()))
    
    req_body = req.get_json()
    # slack_info_list = req.get_body().split("&")
    
    # slack_info_dict = {}
    # for key_value in slack_info_list:
    #     key_value = key_value.split("=")
    #     slack_info_dict[key_value[0]] = key_value[1]
    
    return func.HttpResponse(req_body.get('challenge') ,status_code=200)
    # slack情報から投稿コメントを作成
    slack_info = req.get_body().decode('utf-8')
    comment = comments.create_comment(slack_info)
    
    # slash commandのテキストから投稿対象の課題番号を取得
    issue_id_key = slack_info['text']
    logging.info(issue_id_key)
    
    #comments.add_comment(comment, issue_id_key, api_key, backlog_space_key)
    
    # if not channel_id:
    #     return func.HttpResponse(f"channel_idが取得できませんでした。")
    # else:
    #     return func.HttpResponse(
    #         f"{channel_id}, This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #         status_code=200
    #     )

    
