from bulk_update import BulkUpdater as bulk
from configurator import Configurator as config
import random
import env_checker as envck
import os
from datetime import datetime
import subprocess

def select_ticket():
    print("DEBUG", "...Selecting ticket...")


def clone_repo():
    print("..Cloning repo")
    

def find_target_files(parent_dir):
    print("...Finding target files...")
    python_files = []
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def append_to_file(filename, string_to_append):
    try:
        with open(filename, "a") as file_obj:
            file_obj.write(string_to_append)
            print(f"Appended {string_to_append}")
    except FileNotFoundError:
        print(f'Could not find file "{filename}"')

def make_code_changes(repo_location):
    print("...Making code change...")
    
    code_change = """
    def test_comman():
        print("Do a thing")
    """
    
    code_file_list = find_target_files(repo_location)
    target_file = random.choice(code_file_list)
    append_to_file(target_file, code_change)
    
    
def run_command(cmd_string):
    print("...Running command...")
    split_list = cmd_string.split(" ")
    subprocess.run(split_list)

def commit_workflow():
    print("............Starting commit workflow............")
    bu = bulk()
    conf = config()
    # get JQL query
    # jql = ''
    # jql = conf.format_jql_query()
    # tickets = bu.get_tickets(jql)
    
    # # randomly select a ticket to work on
    # selected_ticket = random.choice(tickets)
    
    # GENERATE COMMITS
    
    # get commits to make
    total_commits = envck.get_flag_value("--total-commits", 5)
    
    # clone git repo
    repo_location = envck.get_var_value("--repo-location", "REPO_LOCATION", "/harness")
    
    # get PAT
    pat = envck.get_var_value("--code-pat", "CODE_PAT", )
    
    # MAKE CODE CHANGE
    make_code_changes(repo_location)
    
    # COMMIT CHANGES
    cmd_move_to_repo = f"cd {repo_location}"
    run_command(cmd_move_to_repo)
    git_add_cmd = f"git add ."
    run_command(git_add_cmd)
    git_commit_cmd = f'git commit -m "generated_commit_message"'
    run_command(git_commit_cmd)
    
    
    # AMMEND COMMITS
    current_date=datetime.now()
    formatted_timestamp = current_date.strftime("")
    
    command = "git commit --amend --date="<DATE>" --no-edit"
    
    # PUSH COMMITS
    
    # OPEN PR
    
    # select_ticket()
    
def help_message():
    print("Help")

def commit_maker_handler(args):
    print("............Get transition ids............")
    print("GOT ARGS", args)
    if len(args) > 2:
        print("Running command ")
        commit_workflow()
    else: 
        help_message()