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


def render_help_main():
    print("HELP TEXT")
    print("bulkcreate          Create many JIRA tickets")

def bulk_create_handler():
    bulk_create.create_ticket_burst()

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