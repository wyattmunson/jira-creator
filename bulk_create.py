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

def create_ticket_burst(tickets=data_loader.get_ticket_desc(), limit=5, project_key=env_checker.find_var("PROJECT_KEY", "--project-key")):
    conf = Configurator()

    # if project_key not specified, check env var
    if not project_key:
        project_list = conf.get_project_list()
        project_key = random.choice(project_list)
        print("Project key not set. Selecting random key:", project_key)
    
    # get configs: issue id
    configs = conf.get_configs()
    issue_type = "story"
    issue_id = configs[project_key][issue_type]['id']
    
    print("Project key is", project_key)
    print("Creating a burst of tickets...")

    # create issues
    for x in range(limit):
        message = random.choice(tickets)
        payload = assemble_payload(project_key, issue_id, summary=message['title'], description=message['descr'])
        print("Got a message", message)
        print(payload)
        url = "https://harness-sei.atlassian.net/rest/api/2/issue"
        # tester = input("AAA")
        api.make_post_call(url, payload)
        time.sleep(0.5)


def bulk_create_orchestrator():
    print("............Bulk create............")
