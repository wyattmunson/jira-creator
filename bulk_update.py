import random
import time
import env_checker
import api
import data_loader
import logtastic as logg

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
        # ticket_list = data_loader.get_tickets()
        ticket_list = api.get_issues(jql_query)
        # ticket_list = api.get_issues('project = "FOX" AND status = "To Do" ORDER BY created DESC')
        self.tickets = ticket_list['issues']
    
    def get_transition_ids(self):
        # get the first ticket (transition ids are subset of issue)
        sample_ticket = self.tickets[0]
        sample_ticket_key = sample_ticket['key']

        transition_ids = api.get_transitions(sample_ticket_key)
        self.transition_ids = transition_ids['transitions']
        print(self.transition_ids)


    def process_transitions(self):
        transition_list = {
            "To Do": {"id": "11", "name": "To Do", "next": "In Progress"},
            "In Progress": {"id": "21", "name": "In Progress", "next": "Testing"},
            "Testing": {"id": "2", "name": "Testing", "next": "Done"},
            "Done": {"id": "31", "name": "Done"}
        }

        for item in self.tickets:
            status = item['fields']['status']['name']
            issue_key = item['key']
            print(f"\nStatus for {issue_key} is {status}")

            # randomly decide if it should be moved
            roll = random.randint(0, 9)
            if roll >= 5 and status != "Done":
                print("Taking action...")
                next_stage = transition_list[status]['next']
                transition_id = transition_list[next_stage]['id']
                print("Next ID is", transition_id)

                api.do_transition(issue_key, transition_id)

            else:
                logg.logger("Skipping ticket", issue_key)
            
            # Add sleep to avoid rate-limit issues
            time.sleep(0.2)
    
    def get_project_key(self):
        return self.project_key
    

    def get_issues(self, jql=None):
        jql = ""


def bulk_update_orchestrator():
    print("Prepping bulk update...")
    updater = BulkUpdater()
    updater.startup()

    # Get target project (or select random one)
    jira_project = updater.get_project_key()
    print("Using JIRA project", jira_project)

    jql_query = f'project = "{jira_project}" AND status = "To Do" ORDER BY created DESC'
    # 1. Get all-ish tickets and update a random subet
    # TODO: add a way to easy target only to do tickets or update all, ect. 
    ticket_list = updater.get_tickets(jql_query)
    # transitions_ids = updater.get_transition_ids()
    updater.process_transitions()
    