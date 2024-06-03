from base64 import b64encode
import requests
import env_checker
import logtastic as logg

def assemble_header():
    username = env_checker.get_env_var("JIRA_USERNAME")
    password = env_checker.get_env_var("JIRA_API_TOKEN")
    auth_str = b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")

    return {
        "Authorization": f"Basic {auth_str}",
        "Content-Type": "application/json"
    }

def make_post_call(url, payload):
    headers = assemble_header()

    try:
        logg.er("DEBUG", f"JSON payload: \n{payload}")
        response = requests.post(url, headers=headers, json=payload)
        print("API status code:", response.status_code)
        
    
        if response.status_code in [200, 201]:
            print("Api call successful.")
            return response.json()
        elif response.status_code in [204]:
            print("API call success - updated")
            return None
        else:
            print("Successful error:", response.text)
    except requests.exceptions.RequestException as e:
        print(e)
        return None

    # else:
    #     print(f"Error creating story: {response.status_code}")
    #     return None


def make_get_call(url, params=None):
    headers = assemble_header()

    response = requests.get(url, headers=headers, params=params)

    if response.status_code in [200, 201]:
        print("Api call successful.")
        return response.json()
    else:
        print(f"Error creating story: {response.status_code}")
        return None

def get_issues(jql=None, max_results=50):
    url = "https://harness-sei.atlassian.net/rest/api/2/search"
    q_params = {
        'maxResults': max_results,
    }
    if jql: q_params['jql'] = jql
    

    res = make_get_call(url, q_params)
    return res
    # response = requests.get(url, headers=headers)


def get_transitions(issue_key):
    url = f"https://harness-sei.atlassian.net/rest/api/2/issue/{issue_key}/transitions"
    res = make_get_call(url)
    return res

def do_transition(issue_key, transition_id):
    url = f"https://harness-sei.atlassian.net/rest/api/2/issue/{issue_key}/transitions"
    payload = { 'transition': { 'id': transition_id }}
    # print("Using URL", url)

    res = make_post_call(url, payload)
    return res