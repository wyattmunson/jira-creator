import api
import env_checker
import random
import time
from copier import Copier

def assemble_payload(project_key, summary="Created by script", description="Story description"):
    payload = {
        "fields": {
          "project": {
            "key": project_key  
          },
          "summary": summary,
          "issuetype": {
            "id": "10005"  
          },
          "description": description,
          "assignee": {
            "name": "username_of_assignee"  
          }
        }
      }
    
    return payload

def create_ticket_burst(tickets=[], limit=5, project_key=env_checker.get_env_var("PROJECT_KEY")):
    copier = Copier()
    # tickets = copier
    # SELECT PROJECT
    # This can be randomly selected for now

    # if project_key not specified, check env var
    if not project_key:
        project_list = copier.get_project_list()
        project_key = random.choice(project_list)
        print("Selecting random project key:", project_key)
    
    print("Project key is", project_key)
    print("Creating a burst of tickets...")
    for x in range(limit):
        message = random.choice(tickets)
        payload = assemble_payload(project_key, summary=message['title'], description=message['descr'])
        print("Got a message", message)
        print(payload)
        url = "https://harness-sei.atlassian.net/rest/api/2/issue"
        api.make_post_call(url, payload)
        time.sleep(0.5)
