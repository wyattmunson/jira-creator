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
    
    for x in timestamp_list:
        make_code_changes(repo_location, code_change_obj)
        
        string_command = f'./git_commit.sh {repo_location} "{x}"'
        subprocess.run(string_command, shell=True)
        

def set_git_creds(repo_location):
    print("...Set git creds...")
    username = envck.get_var_value("--git_username", "GIT_USERNAME", None)
    pat = envck.get_var_value("--code-pat", "CODE_PAT", None)
    
    subprocess.run(f'./scripts/set_git_creds.sh {repo_location} {username} {pat}', shell=True)
    
    # akey = username + ":" + pat
    # code_repo = "https://git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git"
    # clone_url = code_repo.replace("https://", "https://" + akey)
    # print("Using clone url", clone_url)
    

def set_git_remote(repo_location, clone_url):
    print("...Set git remote...")
    username = envck.get_var_value("--git_username", "GIT_USERNAME", None)
    pat = envck.get_var_value("--code-pat", "CODE_PAT", None)
    
    # https://git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git
    url = clone_url.replace("https://", "https://" + username + ":" + pat + "@")
    logg.er("DEBUG", f'Formatted URL: {url}')
    subprocess.run(f'./scripts/git_cred.sh {repo_location} {clone_url}', shell=True)
    
    
    url = f'https://$PAT@github.com/<username>/<repository>.git'
    

def push_commit_handler(repo_location, clone_url):
    print("...Push commits...")
    logg.er("DEBUG", f'Cloning at repo path "{repo_location}" with clone URL "{clone_url}"')
    subprocess.run(f'./scripts/push_commits.sh {repo_location} {clone_url}', shell=True)
    

def handle_push():
    print("...Push handler...")
    # username = envck.get_var_value("--git_username", "GIT_USERNAME", None)
    # pat = envck.get_var_value("--code-pat", "CODE_PAT", None)
    # akey = username + ":" + pat
    # code_repo = "https://git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git"
    # clone_url = code_repo.replace("https://", "https://" + akey)
    # print("Using clone url", clone_url)
    
    # repo_location="/Users/wyatt/code/fake-python"
    
    # subprocess.run(f'./scripts/push_commits.sh {repo_location} {clone_url}', shell=True)
    
def run_command(cmd_string):
    print("...Running command...")
    logg.er("DEBUG", f'Processing command "{cmd_string}"')
    split_list = cmd_string.split(" ")
    logg.er("TRACE", f'Command array: "{split_list}"')
    subprocess.run(split_list, shell=True)


def mock_selected_ticket():
    return {'expand': 'operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields', 'id': '10072', 'self': 'https://harness-sei.atlassian.net/rest/api/2/issue/10072', 'key': 'FOX-39', 'fields': {'statuscategorychangedate': '2024-06-02T00:21:40.209-0700', 'issuetype': {'self': 'https://harness-sei.atlassian.net/rest/api/2/issuetype/10005', 'id': '10005', 'description': 'Stories track functionality or features expressed as user goals.', 'iconUrl': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium', 'name': 'Story', 'subtask': False, 'avatarId': 10315, 'entityId': 'cd84c884-b6cd-4873-b8c7-afe4dd262b07', 'hierarchyLevel': 0}, 'timespent': None, 'customfield_10030': None, 'project': {'self': 'https://harness-sei.atlassian.net/rest/api/2/project/10001', 'id': '10001', 'key': 'FOX', 'name': 'Fox Team', 'projectTypeKey': 'software', 'simplified': True, 'avatarUrls': {'48x48': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405', '24x24': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small', '16x16': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall', '32x32': 'https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium'}}, 'fixVersions': [], 'aggregatetimespent': None, 'resolution': None, 'customfield_10027': None, 'customfield_10028': None, 'customfield_10029': None, 'resolutiondate': None, 'workratio': -1, 'lastViewed': '2024-06-02T13:28:19.374-0700', 'watches': {'self': 'https://harness-sei.atlassian.net/rest/api/2/issue/FOX-39/watchers', 'watchCount': 1, 'isWatching': True}, 'created': '2024-06-01T23:41:26.894-0700', 'customfield_10020': None, 'customfield_10021': None, 'customfield_10022': None, 'customfield_10023': None, 'priority': {'self': 'https://harness-sei.atlassian.net/rest/api/2/priority/3', 'iconUrl': 'https://harness-sei.atlassian.net/images/icons/priorities/medium.svg', 'name': 'Medium', 'id': '3'}, 'customfield_10024': None, 'customfield_10025': None, 'customfield_10026': None, 'labels': [], 'customfield_10016': None, 'customfield_10017': None, 'customfield_10018': {'hasEpicLinkFieldDependency': False, 'showField': False, 'nonEditableReason': {'reason': 'PLUGIN_LICENSE_ERROR', 'message': 'The Parent Link is only available to Jira Premium users.'}}, 'customfield_10019': '0|i000bj:', 'timeestimate': None, 'aggregatetimeoriginalestimate': None, 'versions': [], 'issuelinks': [], 'assignee': None, 'updated': '2024-06-02T00:21:40.208-0700', 'status': {'self': 'https://harness-sei.atlassian.net/rest/api/2/status/10004', 'description': '', 'iconUrl': 'https://harness-sei.atlassian.net/', 'name': 'In Progress', 'id': '10004', 'statusCategory': {'self': 'https://harness-sei.atlassian.net/rest/api/2/statuscategory/4', 'id': 4, 'key': 'indeterminate', 'colorName': 'yellow', 'name': 'In Progress'}}, 'components': [], 'timeoriginalestimate': None, 'description': 'Buttons on the product listing page have inconsistent spacing, creating a misaligned layout on some screen sizes. (Priority: Low)', 'customfield_10010': None, 'customfield_10014': None, 'customfield_10015': None, 'customfield_10005': None, 'customfield_10006': None, 'customfield_10007': None, 'security': None, 'customfield_10008': None, 'customfield_10009': None, 'aggregatetimeestimate': None, 'summary': 'Fix Visual Bug: Inconsistent Button Spacing on Product Listing Page', 'creator': {'self': 'https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'accountId': '712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'emailAddress': 'wyatt@harness.io', 'avatarUrls': {'48x48': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '24x24': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '16x16': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '32x32': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png'}, 'displayName': 'Wyatt Munson', 'active': True, 'timeZone': 'America/Los_Angeles', 'accountType': 'atlassian'}, 'subtasks': [], 'reporter': {'self': 'https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'accountId': '712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897', 'emailAddress': 'wyatt@harness.io', 'avatarUrls': {'48x48': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '24x24': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '16x16': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png', '32x32': 'https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png'}, 'displayName': 'Wyatt Munson', 'active': True, 'timeZone': 'America/Los_Angeles', 'accountType': 'atlassian'}, 'aggregateprogress': {'progress': 0, 'total': 0}, 'customfield_10001': None, 'customfield_10002': None, 'customfield_10003': None, 'customfield_10004': None, 'environment': None, 'duedate': None, 'progress': {'progress': 0, 'total': 0}, 'votes': {'self': 'https://harness-sei.atlassian.net/rest/api/2/issue/FOX-39/votes', 'votes': 0, 'hasVoted': False}}}


def generate_times(time_string):
    print("..Generating times..")
    
    # Convert timestamp to date obj
    start_time = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%f%z")
    logg.er("DEBUG", f'Got start time "{start_time}", Curr time: ""')
    
    # Get current timestamp, add timezone information to data object
    current_timestamp = datetime.now()
    format_string = "%Y-%m-%dT%H:%M:%S.%f"
    ct_string = current_timestamp.strftime(format_string)
    ct_string_with_tz = ct_string + "-0700"
    # print("CT as string with tz", ct_string_with_tz)
    current_timestamp_tz = datetime.strptime(ct_string_with_tz, "%Y-%m-%dT%H:%M:%S.%f%z")
    
    # print(f'Current datetime with tz: {current_timestamp_tz}')
    
    # Get random date between two timestamps
    diff = current_timestamp_tz - start_time
    int_delta = (diff.days * 24 * 60 * 60) + diff.seconds
    random_second = random.randrange(int_delta)
    randy = start_time + timedelta(seconds=random_second)
    # print("INT DELTA", int_delta, "RAND SECOND:", random_second, "RANDY:", randy)
    
    # return timestamp as datetime obj
    return randy
    
    # return timestamp as string
    print("Type of randy", type(randy))
    return randy.strftime("%Y-%m-%dT%H:%M:%S.%f%z")
    

def get_timestamps(start_date, total_commits):
    print("..Getting timestamps..")
    timestamp_list = []
    for x in range(total_commits):
        timestamp_list.append(generate_times(start_date))
    
    def sort_by_datetime(dt):
        return dt
    
    # print("ORIG TIMESTAMP LIST", timestamp_list)
    # sorted_timestamps = timestamp_list.sort()
    sorted_timestamps = sorted(timestamp_list, key=sort_by_datetime)
    
    # CONVERT SORTED LIST TO STRINGS
    sorted_timestamps_as_str = []
    datetime_to_str_regex = "%Y-%m-%dT%H:%M:%S.%f%z"
    for x in sorted_timestamps:
        sorted_timestamps_as_str.append(x.strftime(datetime_to_str_regex))
    
    print("FORMATTED AS STR:", sorted_timestamps_as_str)
    
    return sorted_timestamps_as_str
    
    
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
    
    # print("\n\nSELECTED TICKET:", selected_ticket)
    
    
    
    # GENERATE COMMITS
    
    # GET: total number of commits to make
    total_commits = envck.get_flag_value("--total-commits", 5)
    logg.er("DEBUG", f'Creating {total_commits}')
    
    # GET: repo location path
    repo_location = envck.get_var_value("--repo-location", "REPO_LOCATION", "/harness")
    logg.er("DEBUG", f'Using repo location: {repo_location}')
    
    # get PAT
    pat = envck.get_var_value("--code-pat", "CODE_PAT", )
    
    # GET TIMES
    create_date = selected_ticket['fields']['created']
    transition_date = selected_ticket['fields']['statuscategorychangedate']

    timestamp_list = get_timestamps(create_date, total_commits)
    # print("Generated timestamps:", timestamp_list)
    
    
    
    
    # # MAKE CODE CHANGE
    code_change_obj = data_commit_msg.get()
    handle_code_changes(repo_location, code_change_obj, timestamp_list)
    # make_code_changes(repo_location)
    
    # CODE CREDS
    # set_git_creds(repo_location)
    clone_url = envck.get_var_value("--clone-url", "CLONE_URL", )
    set_git_remote(repo_location, clone_url)
    
    # PUSH 
    push_commit_handler(repo_location, None)
    
    # OPEN PR
    
    # select_ticket()
    
def help_message():
    print("Help")

def commit_maker_handler(args):
    print("............Get transition ids............")
    print("GOT ARGS", args)
    if len(args) > 2:
        print("Running command ")
        command = args[2]
        
        commit_workflow()
    else: 
        help_message()