class Configurator:
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
              'subtask_id': "10011",
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
          }
      }
    
    def get_configs(self):
        return self.project_configs
    
    def get_project_list(self):
        return self.project_list