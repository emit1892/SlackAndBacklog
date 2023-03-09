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
    
    issue_id_key = 'EMPROJECT-1'
    comment = '''
        test
        テスト
        # test
    '''
    comments.add_comment(comment, issue_id_key, api_key, backlog_space_key)
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
