import random
import time
import env_checker
import api
import data_loader
import logtastic as logg
from configurator import Configurator

class BulkUpdater:
    def __init__(self) -> None:
        self.tickets = []
        self.transition_ids = []
        self.project_key = env_checker.find_var("PROJECT_KEY", "--project-key")
    
    def startup(self):
        print("Starting up...")
        if not self.project_key:
            self.project_key = random.choice(["FOX"])
            print("Project key not specified, randomly selected:", self.project_key)

    def get_tickets(self, jql_query):
        print("Getting tickets...")
        # TODO: Update API to have dev mode to load mocks
        # ticket_list = data_loader.get_tickets()
        ticket_list = api.get_issues(jql_query)
        self.tickets = ticket_list['issues']
    
    def get_transition_ids(self, issue_key=env_checker.find_flag("--issue-key")):
        # get the first ticket (all issues types in same project use common transition ids)
        if not issue_key:
            sample_ticket = self.tickets[0]
            issue_key = sample_ticket['key']

        transition_ids = api.get_transitions(issue_key)
        self.transition_ids = transition_ids['transitions']
        print(self.transition_ids)


    def process_transitions(self, transition_list):
        # percentage = int(env_checker.find_flag("--percentage"))
        # if not percentage: percentage = 100
        percentage = env_checker.find_flag("--percentage")
        if not percentage: 
            percentage = 100
        else:
            percentage = int(percentage)

        for item in self.tickets:
            status = item['fields']['status']['name']
            issue_key = item['key']
            print(f"\nStatus for {issue_key} is {status}")

            # randomly decide if it should be moved
            roll = random.randint(1, 100)
            if roll >= percentage and status != "Done":
                print(f"Transitioning {issue_key}...")
                next_stage = transition_list[status]['next']
                transition_id = transition_list[next_stage]['id']
                print(f"Next status ID for {issue_key} is", transition_id)

                api.do_transition(issue_key, transition_id)

            else:
                logg.logger("Skipping ticket", issue_key)
            
            # Add sleep to avoid rate-limit issues
            time.sleep(0.2)
    
    def get_project_key(self):
        return self.project_key
    

    def get_issues(self, jql=None):
        jql = ""


def get_jql_query(jira_project):
    input_jql = env_checker.find_flag("--jql")
    if not input_jql:
        return f'project = "{jira_project}" AND status != "Done" ORDER BY created DESC'
        # return f'project = "{jira_project}" AND status = "To Do" ORDER BY created DESC'
    else:
        return input_jql

def get_transition_id_orchestrator():
    print("............Get transition ids............")
    updater = BulkUpdater()
    updater.get_transition_ids()
    

def bulk_update_orchestrator():
    print("............Bulk update............")
    updater = BulkUpdater()
    updater.startup()
    config = Configurator()
    transition_list = config.get_configs()

    # Get target project (or select random one)
    jira_project = updater.get_project_key()
    print("Using JIRA project", jira_project)

    # jql_query = f'project = "{jira_project}" AND status = "To Do" ORDER BY created DESC'
    jql_query = get_jql_query(jira_project)
    
    # 1. Get all-ish tickets and update a random subet
    # TODO: add a way to easy target only to do tickets or update all, ect. 
    ticket_list = updater.get_tickets(jql_query)
    # transitions_ids = updater.get_transition_ids()
    updater.process_transitions(transition_list[jira_project]['transition_list'])
    