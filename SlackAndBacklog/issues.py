import requests
import os

BASE_URL = 'https://{backlog_space_id}.backlog.com/api/v2/{api}'

api_key = os.environ.get("BACKLOG_TOKEN")
backlog_space_key = 'emit1892'

def add_issue(_project_key, _issue_type_id, _priority_id, _summary, _description):
    api = 'issues'
    url = BASE_URL.format(backlog_space_id=backlog_space_key, api=api)
    
    params = {
        'apiKey': api_key
    }
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    payload = {
        'projectId': _project_key,
        'issueTypeId': _issue_type_id,
        'priorityId': _priority_id,
        'summary': _summary,
        'description': _description
    }
    
    response = requests.post(url, params=params, headers=headers, data=payload)
    print(response.status_code)
    response.raise_for_status()
    
    return response

project_id = 375344
issue_type_id = 1891580
priority_id = 3
summary = 'test'
description = '''
    test
    テスト
    # test
'''

response = add_issue(project_id, issue_type_id, priority_id, summary, description)