import logging
import os
import requests
from SlackAndBacklog import comments
import azure.functions as func

BASE_URL = 'https://{backlog_space_id}.backlog.com/api/v2/{api}'
api_key = os.environ.get("BACKLOG_TOKEN")
backlog_space_key = os.environ.get("BACKLOG_SPACE_KEY")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info(req)
    issue_id_key = 'EMPROJECT-1'
    comment = '''
        test
        テスト
        # test
    '''
    #comments.add_comment(comment, issue_id_key, api_key, backlog_space_key)    
    url = req.url
    logging.info(url)
    
    str_req_body = req.get_body().decode('utf-8')
    list_req_body = str_req_body.split("&")
    
    dic_req_body = {}
    for req_body in list_req_body:
        key_value_req_body = req_body.split("=")
        dic_req_body[key_value_req_body[0]] = key_value_req_body[1]
    
    logging.info(dic_req_body)
    
    channel_id = dic_req_body['channel_id']
    if not channel_id:
        return func.HttpResponse(f"channel_idが取得できませんでした。")
    else:
        return func.HttpResponse(
             f"{channel_id}, This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
