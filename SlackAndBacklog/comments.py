import requests
import os

BASE_URL = 'https://{backlog_space_id}.backlog.com/api/v2/{api}'

api_key = os.environ.get("BACKLOG_TOKEN")
backlog_space_key = os.environ.get("BACKLOG_SPACE_KEY")

def add_comment(_comment, _issue_id_key):
    api = f'issues/{_issue_id_key}/comments'
    url = BASE_URL.format(backlog_space_id=backlog_space_key, api=api)
    
    params = {
        'apiKey': api_key
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

# issue_id_key = 'EMPROJECT-1'
# comment = '''
#     test
#     テスト
#     # test
# '''

# response = add_comment(comment, issue_id_key)