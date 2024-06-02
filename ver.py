import json

def load_version():
    with open('version.json') as f:
        d = json.load(f)
        return d

def get_version():
    version = load_version()['version']
    print("jira-creator version is", version)