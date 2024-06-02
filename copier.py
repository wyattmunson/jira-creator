import env_checker
import bulk_create
import bulk_update
import sys
import ver
from base64 import b64encode

def render_help_main():
    print("JIRA CREATOR")
    print("\nUsage: jcreate COMMAND")
    print("\nCommon commands:")
    print("bulkcreate          Create many JIRA tickets")
    print("bulkupdate          Update many JIRA tickets")
    
    print("\nTesting Commands:")
    print("get-transitions     Get issue ids for a given project id")
    
    print("\nFor more help, go to https://github.com/wyattmunson/jira-creator")

def bulk_create_handler():
    bulk_create.create_ticket_burst()

def bulk_update_handler():
    bulk_update.bulk_update_orchestrator()

def get_transition_handler():
    bulk_update.get_transition_id_orchestrator()


def get_version_handler():
    ver.get_version()


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
        if command == "get-transitions":
            get_transition_handler()
        if command in ["version", "--version", "-v"]:
            get_version_handler()
    else:
        render_help_main()