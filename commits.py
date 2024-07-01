from bulk_update import BulkUpdater as bulk
from configurator import Configurator as config
# from fake import FAKER
import random
import env_checker as envck
import os
from datetime import datetime, timedelta
import subprocess
import logtastic as logg
import data_commit_msg
import helpers

class GitManager:
    def __init__(self):
        self.username = envck.get_var_value("--git_username", "GIT_USERNAME", None, True)
        self.code_pat = envck.get_var_value("--code-pat", "CODE_PAT", None, True)
        self.project_key = envck.get_var_value("--project-key", "PROJECT_KEY", None, True)
        self.repo_location = envck.get_var_value("--repo-location", "REPO_LOCATION", None, True)
        self.clone_url = envck.get_var_value("--clone-url", "CLONE_URL", None, True)
        self.total_commits = envck.get_var_value("--total-commits", "TOTAL_COMMITS", 5)
    
    def get_total_commits(self):
        self.total_commits = envck.get_var_value("--total-commits", "TOTAL_COMMITS", 5)
        logg.er("DEBUG", f'Creating {self.total_commits} commits')
        return self.total_commits
    
    def get_repo_location(self):
        self.repo_location = envck.get_var_value("--repo-location", "REPO_LOCATION", "/harness")
        logg.er("DEBUG", f'Using repo location: {self.repo_location}')
        return self.repo_location

    def get_times(self, ticket, start_time):
        create_date = ticket['fields']['created']
        transition_date = ticket['fields']['statuscategorychangedate']

        timestamp_list = helpers.get_timestamps(create_date, self.total_commits)
        return timestamp_list
    
    def make_code_change(self):
        pass
    

def select_ticket():
    print("DEBUG", "...Selecting ticket...")


def clone_repo():
    print("..Cloning repo")
    

def find_target_files(parent_dir):
    print("...Finding target files...")
    logg.er("DEBUG", f"Using target dir {parent_dir}")
    python_files = []
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def append_to_file(filename, string_to_append):
    print(f"...Appending to file: {filename}...")
    try:
        with open(filename, "a") as file_obj:
            file_obj.write(string_to_append)
            print(f"..Success..")
    except FileNotFoundError:
        print(f'Could not find file "{filename}"')


def make_code_changes(repo_location, code_change_obj):
    print("...Making code change...")
    
    code_change = """
    def test_comman():
        print("Do a thing")
    """
    
    commit_messages = data_commit_msg.get()
    code_change = random.choice(code_change_obj)['code_change']
    # logg.er("DEBUG", f'Got code change {code_change}')
    
    code_file_list = find_target_files(repo_location)
    target_file = random.choice(code_file_list)
    append_to_file(target_file, code_change)
    

def handle_code_changes(repo_location, code_change_obj, timestamp_list):
    print("...Making code change...")
    # code_change_obj = ""
    # commit_messages = data_commit_msg.get()
    
    # checkout branch
    
    
    for x in timestamp_list:
        make_code_changes(repo_location, code_change_obj)
        
        string_command = f'./scripts/git_commit.sh {repo_location} "{x}"'
        subprocess.run(string_command, shell=True)
        

def set_git_creds(repo_location):
    print("...Set git creds...")
    username = envck.get_var_value("--git_username", "GIT_USERNAME", None)
    pat = envck.get_var_value("--code-pat", "CODE_PAT", None)
    
    subprocess.run(f'./scripts/set_git_creds.sh {repo_location} {username} {pat}', shell=True)
    

def set_git_remote(repo_location, clone_url):
    print("...Set git remote...")
    username = envck.get_var_value("--git_username", "GIT_USERNAME", None)
    pat = envck.get_var_value("--code-pat", "CODE_PAT", None)
    
    # https://git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git
    url = clone_url.replace("https://", "https://" + username + ":" + pat + "@")
    logg.er("DEBUG", f'Formatted URL: {url}')
    subprocess.run(f'./scripts/git_cred.sh {repo_location} {clone_url}', shell=True)
    
    
    url = f'https://$PAT@github.com/<username>/<repository>.git'
    

def push_commit_handler(repo_location, branch_name="main"):
    print("...Push commits...")
    logg.er("DEBUG", f'Using branch "{branch_name}"')
    subprocess.run(f'./scripts/push_commits.sh {repo_location} {branch_name}', shell=True)


def mock_selected_ticket():
    return {'expand': 'operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields', 'id': '10072', 'self': 'https://harness-sei.atlassian.net/rest/api/2/issue/10072', 'key': 'FOX-39', 'fields': {'statuscategorychangedate': '2024-06-02T00:21:40.209-0700', 'issuetype': {'self': 'https://harness-sei.atlassian.net/rest/api/2/issuetype/10005', 'id': '10005', 'description': 'Stories track functionality or features expressed as user goals.', 'iconUrl': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium', 'name': 'Story', 'subtask': False, 'avatarId': 10315, 'entityId': 'cd84c884-b6cd-4873-b8c7-afe4dd262b07', 'hierarchyLevel': 0}, 'timespent': None, 'customfield_10030': None, 'project': {'self': 'https://harness-sei.atlassian.net/rest/api/2/project/10001', 'id': '10001', 'key': 'FOX', 'name': 'Fox Team', 'projectTypeKey': 'software', 'simplified': True, 'avatarUrls': {'48x48': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405', '24x24': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small', '16x16': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall', '32x32': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium'}}, 'fixVersions': [], 'aggregatetimespent': None, 'resolution': None, 'customfield_10027': None, 'customfield_10028': None, 'customfield_10029': None, 'resolutiondate': None, 'workratio': -1, 'lastViewed': '2024-06-02T13:28:19.374-0700', 'watches': {'self': 'https://harness-sei.atlassian.net/rest/api/2/issue/FOX-39/watchers', 'watchCount': 1, 'isWatching': True}, 'created': '2024-06-01T23:41:26.894-0700', 'customfield_10020': None, 'customfield_10021': None, 'customfield_10022': None, 'customfield_10023': None, 'priority': {'self': 'https://harness-sei.atlassian.net/rest/api/2/priority/3', 'iconUrl': 'https://harness-sei.atlassian.net/images/icons/priorities/medium.svg', 'name': 'Medium', 'id': '3'}, 'customfield_10024': None, 'customfield_10025': None, 'customfield_10026': None, 'labels': [], 'customfield_10016': None, 'customfield_10017': None, 'customfield_10018': {'hasEpicLinkFieldDependency': False, 'showField': False, 'nonEditableReason': {'reason': 'PLUGIN_LICENSE_ERROR', 'message': 'The Parent Link is only available to Jira Premium users.'}}, 'customfield_10019': '0|i000bj:', 'timeestimate': None, 'aggregatetimeoriginalestimate': None, 'versions': [], 'issuelinks': [], 'assignee': None, 'updated': '2024-06-02T00:21:40.208-0700', 'status': {'self': 'https://harness-sei.atlassian.net/rest/api/2/status/10004', 'description': '', 'iconUrl': 'https://harness-sei.atlassian.net/', 'name': 'In Progress', 'id': '10004', 'statusCategory': {'self': 'https://harness-sei.atlassian.net/rest/api/2/statuscategory/4', 'id': 4, 'key': 'indeterminate', 'colorName': 'yellow', 'name': 'In Progress'}}, 'components': [], 'timeoriginalestimate': None, 'description': 'Buttons on the product listing page have inconsistent spacing, creating a misaligned layout on some screen sizes. (Priority: Low)', 'customfield_10010': None, 'customfield_10014': None, 'customfield_10015': None, 'customfield_10005': None, 'customfield_10006': None, 'customfield_10007': None, 'security': None, 'customfield_10008': None, 'customfield_10009': None, 'aggregatetimeestimate': None, 'summary': 'Fix Visual Bug: Inconsistent Button Spacing on Product Listing Page', 'creator': {'self': 'https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'accountId': '712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'emailAddress': 'wyatt@harness.io', 'avatarUrls': {'48x48': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '24x24': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '16x16': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '32x32': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png'}, 'displayName': 'Wyatt Munson', 'active': True, 'timeZone': 'America/Los_Angeles', 'accountType': 'atlassian'}, 'subtasks': [], 'reporter': {'self': 'https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'accountId': '712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'emailAddress': 'wyatt@harness.io', 'avatarUrls': {'48x48': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '24x24': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '16x16': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '32x32': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png'}, 'displayName': 'Wyatt Munson', 'active': True, 'timeZone': 'America/Los_Angeles', 'accountType': 'atlassian'}, 'aggregateprogress': {'progress': 0, 'total': 0}, 'customfield_10001': None, 'customfield_10002': None, 'customfield_10003': None, 'customfield_10004': None, 'environment': None, 'duedate': None, 'progress': {'progress': 0, 'total': 0}, 'votes': {'self': 'https://harness-sei.atlassian.net/rest/api/2/issue/FOX-39/votes', 'votes': 0, 'hasVoted': False}}}
    

def generate_branch_name(ticket):
    if not ticket: return f'random-branch-{random.randint(1000, 9999)}'
    # print(ticket)
    issue_key = ticket['key']
    print("Issue us", issue_key)
    return f'{ticket["key"]}-generated-branch-{random.randint(300, 800)}'


def handle_change_branch(repo_location, ticket):
    print("...Changing branch...")
    branch_name = generate_branch_name(ticket)
    subprocess.run(f'./scripts/git_checkout.sh {repo_location} {branch_name}', shell=True)
    return branch_name



def commit_workflow():
    print("............Starting commit workflow............")
    bu = bulk()
    co = config()
    conf = co.get_configs()
    # GET PROJECT
    # get JQL query
    # jql = ''
    # jql = co.format_jql_query()
    # jira_project = envck.get_var_value("--project-key", "PROJECT_KEY", None, True)
    # # jql_query = f'project = "{jira_project}" AND status = {conf[jira_project]['ready_for_work_status']} ORDER BY created DESC'
    # tickets = bu.get_tickets(jql)
    
    # # randomly select a ticket to work on
    # selected_ticket = random.choice(tickets)
    selected_ticket = mock_selected_ticket()
    
    
    # GET TOTAL COMMITS and REPO LOCATION 
    
    # GET: total number of commits to make
    total_commits = envck.get_flag_value("--total-commits", 5)
    logg.er("DEBUG", f'Creating {total_commits}')
    
    # GET: repo location path
    repo_location = envck.get_var_value("--repo-location", "REPO_LOCATION", "/harness")
    logg.er("DEBUG", f'Using repo location: {repo_location}')
    
    # GET TIMES
    create_date = selected_ticket['fields']['created']
    transition_date = selected_ticket['fields']['statuscategorychangedate']

    timestamp_list = helpers.get_timestamps(create_date, total_commits)
    # print("Generated timestamps:", timestamp_list)
    
    # CHECKOUT BRANCH
    source_branch = handle_change_branch(repo_location, selected_ticket)
    logg.er("DEBUG", f'Changed to branch {source_branch}')
    
    # # MAKE CODE CHANGE
    code_change_obj = data_commit_msg.get()
    handle_code_changes(repo_location, code_change_obj, timestamp_list)
    
    # CONFIGURE GIT CREDS - SET REMOTE URL
    clone_url = envck.get_var_value("--clone-url", "CLONE_URL")
    set_git_remote(repo_location, clone_url)
    
    # PUSH TO CODE REPO
    push_commit_handler(repo_location, source_branch)
    
    # OPEN PR
    
    # select_ticket()
    
def help_message():
    print("\nUsage: jcreate COMMAND [OPTIONS]")
    print("\nCommands:")
    print("  commit \tCommit workflow")

def commit_maker_handler(args):
    print("............Workflow handler............")
    if len(args) > 2:
        print("Running command ")
        if args[2] == "commit":
            commit_workflow()
        if args[2] in ["-h", "--help", "help"]:
            help_message()
            
        
    else: 
        help_message()