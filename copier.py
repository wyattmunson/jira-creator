import api
import env_checker
import data_loader
import bulk_create
import bulk_update
import sys
import json
import random
import time
from base64 import b64encode

class Copier:
    def __init__(self):
      self.up = True
      self.project_list = ["FOX"]
      # self.project_list = ["FOX", "NORTH", "RED"]
      self.project_configs = {
          'kaban_types': ["story, bug, epic, task, subtask"],
          'FOX': {
              'bug_id': "10007",
              'story_id': "10005",
              'story': {
                  'id': "10005",
                  'points': "customfield_10016",
                  'sprint': "customfield_10020",
                  'transitions': [
                      {"id": "11", "name": "To Do"},
                      {"id": "12", "name": "In Progress"},
                      {"id": "2", "name": "Testing"},
                      {"id": "31", "name": "Done"}
                  ]
              },
              'epic_id': "10008",
              'task_id': "10006",
              'subtask_id': "10009"
              
          },
          'NORTH': {
              'bug_id': "10012",
              'story_id': "10004",
              'epic_id': "10000",
              'task_id': "10010",
              'subtask_id': "10011"
          }
      }
    
    def get_configs(self):
        return self.project_configs
    
    def get_project_list(self):
        return self.project_list


payload = {
  "fields": {
    "project": {
      "key": "FOX"  
    },
    "summary": "Created by python script",
    "issuetype": {
      "id": "10005"  
    },
    "description": "Your story description here (optional)",
    "assignee": {
      "name": "username_of_assignee"  
    }
  }
}

# api.make_post_call(payload)



data_tickets = data_loader.get_ticket_desc()
# print(data_tickets[0])

def render_help_main():
    print("HELP TEXT")
    print("bulkcreate          Create many JIRA tickets")

def bulk_create_handler():
    bulk_create.create_ticket_burst(data_tickets)

def bulk_update_handler():
    bulk_update.bulk_update_orchestrator()

if __name__ == "__main__":
    print("Initial startup...")

    # Check required env variables
    required_vars_list = ["JIRA_API_TOKEN", "JIRA_USERNAME"]
    env_checker.check_env_vars(required_vars_list)

    if len(sys.argv) > 1:
        command = sys.argv[1]
        print("Running command", command)
        if command in ["-h", "--help", "help"]:
            render_help_main()
        if command == "bulkcreate":
            bulk_create_handler()
        if command == "bulkupdate":
            bulk_update_handler()
    else:
        print("No args passed...")
        render_help_main()