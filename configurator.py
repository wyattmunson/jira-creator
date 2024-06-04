import env_checker
import logtastic as logg

class Configurator:
    def __init__(self):
      print("...Initializing: Config...")
      self.up = True
      self.project_list = ["FOX"]
      # self.project_list = ["FOX", "NORTH", "RED"]
      self.jira_api_url = "https://harness-sei.atlassian.net/rest/api/2/"
      self.project_configs = {
          'kaban_types': ["story, bug, epic, task, subtask"],
          'FOX': {
              'bug_id': "10007",
              'story_id': "10005",
              'transition_list': {
                   "To Do": {"id": "11", "name": "To Do", "next": "In Progress"},
                   "In Progress": {"id": "21", "name": "In Progress", "next": "Testing"},
                   "Testing": {"id": "2", "name": "Testing", "next": "Done"},
                   "Done": {"id": "31", "name": "Done"}
               },
              'story': {
                  'id': "10005",
                  'points': "customfield_10016",
                  'sprint': "customfield_10020",
                  'transitions': [
                      {"id": "11", "name": "To Do"},
                      {"id": "12", "name": "In Progress"},
                      {"id": "2", "name": "Testing"},
                      {"id": "31", "name": "Done"}
                  ],
                  'transition_list': {
                        "To Do": {"id": "11", "name": "To Do", "next": "In Progress"},
                        "In Progress": {"id": "21", "name": "In Progress", "next": "Testing"},
                        "Testing": {"id": "2", "name": "Testing", "next": "Done"},
                        "Done": {"id": "31", "name": "Done"}
                    }
              },
              'epic_id': "10008",
              'task_id': "10006",
              'subtask_id': "10009",
              'ready_for_work_status': "Selected for Development",
          },
          'NORTH': {
              'ready_for_work_status': "Selected for Development",
              'bug': {'id': "10012"},
              'story': {'id': "10004", 'transition_list': {
                  "Backlog": {"id": "14", "name": "Backlog", "next": "Selected for Development"},
                  "Selected for Development": { 'id': "21", 'name': "Selected for Development", 'next': "In Progress"},
                  "In Progress": { "id": "31", "name": "In Progress", "next": "QA"},
                  "QA": { "id": "51", "name": "QA", "next": "QA"},
                  "PM Approval": { "id": "61", "name": "PM Approval", "next": "Done"},
                  "Done": { "id": "41", "name": "Done"},
              }},
              'epic': {'id': "10000"},
              'task': {'id': "10010"},
              'subtask': {'id': "10011"},
              'transition_list': {
                  "Backlog": {"id": "14", "name": "Backlog", "next": "Selected for Development"},
                  "Selected for Development": { 'id': "21", 'name': "Selected for Development", 'next': "In Progress"},
                  "In Progress": { "id": "31", "name": "In Progress", "next": "QA"},
                  "QA": { "id": "51", "name": "QA", "next": "QA"},
                  "PM Approval": { "id": "61", "name": "PM Approval", "next": "Done"},
                  "Done": { "id": "41", "name": "Done"},
              }
          }
      }
    
    def get_configs(self):
        return self.project_configs
    
    def get_project_list(self):
        return self.project_list
    
    def get_api_url(self):
        return self.jira_api_url
    
    def format_jql_query(self):
        input_jql = env_checker.find_flag("--jql")
        project_key = env_checker.find_flag("--project-key")
        logg.er("DEBUG", f'Got project key: {project_key}')
        
        if not input_jql:
            logg.er("DEBUG", f'Project key not supplied')
            return f'project = "{project_key}" AND status != "Done" ORDER BY created DESC'
        else:
            logg.er("DEBUG", f'JQL provided via flag: {input_jql}')
            return input_jql