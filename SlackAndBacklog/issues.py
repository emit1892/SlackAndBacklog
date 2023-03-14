import requests
import os
import logging

BASE_URL = 'https://{backlog_space_id}.backlog.com/api/v2/{api}'

api_key = os.environ.get("BACKLOG_TOKEN")
backlog_space_key = os.environ.get("BACKLOG_SPACE_KEY")

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

def get_issues_info(_issue_id_key):
    issue_id_key = _issue_id_key
    api = 'issues'
    url = BASE_URL.format(backlog_space_id=backlog_space_key, api=api)
    
    params = {
        'apiKey': api_key,
        'issueIdOrKey': issue_id_key
    }
    
    response = requests.post(url, params=params)
    issues_info = response.json()
    logging.info(issues_info)
    
    return issues_info