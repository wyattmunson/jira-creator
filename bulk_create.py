import api
import env_checker
import random
import time
import data_loader
# from copier import Copier
from configurator import Configurator

def assemble_payload(project_key, issue_id, summary="Created by script", description="Story description"):
    payload = {
        "fields": {
          "project": {
            "key": project_key  
          },
          "summary": summary,
          "issuetype": {
            "id": issue_id  
          },
          "description": description,
          "assignee": {
            "name": "username_of_assignee"  
          }
        }
      }
    
    return payload

def create_ticket_burst(tickets=data_loader.get_ticket_desc(), 
                        limit=env_checker.find_flag("--limit") or 5, 
                        project_key=env_checker.find_var("PROJECT_KEY", "--project-key"),
                        issue_type=env_checker.find_flag("--issue-type")):
    conf = Configurator()
    configs = conf.get_configs()
    
    limit = int(limit)

    # if project_key not specified, randomly select one
    if not project_key:
        project_list = conf.get_project_list()
        project_key = random.choice(project_list)
        print("Project key not set. Selecting random key:", project_key)
    
    # get issue id from issue type
    if not issue_type:
        issue_type = "story"
        print(f"Issue type not set, defaulting to {issue_type}")
    issue_id = configs[project_key][issue_type]['id']
    
    print(f"Project key: {project_key}, Issue type: {issue_type}, Issue Id: {issue_id}. Creating burst of tickets...")

    # create issues
    for x in range(limit):
        message = random.choice(tickets)
        payload = assemble_payload(project_key, issue_id, summary=message['title'], description=message['descr'])

        print("Issue payload:", payload)
        url = conf.get_api_url() + "issue"
        api.make_post_call(url, payload)
        time.sleep(0.5)


def bulk_create_orchestrator():
    print("............Bulk create............")
