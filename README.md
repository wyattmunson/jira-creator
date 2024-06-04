# jira-creator

Randomly create

## Setup

### Required Env Variables

- `JIRA_API_TOKEN` - API token of account
- `JIRA_USERNAME` - Username of the account used when logging in (usually an email address).

## Config

Configuration is located in the `configurator.py` file. Each JIRA project uses different identifiers for issue types and transition ids.

```json
{
    "project_list": ["PROJECT_KEY_1", "PROJECT_KEY_2"],
    "PROJECT_KEY": {
        "bug_id": "10007",
        "story": {
            "id": "10005",
            "points": "customfield_10016",
        },
        "transitions": {
            "To Do": {"id": "11", "name": "To Do", "next": "12"},
            "In Progress": {"id": "12", "name": "In Progress", "next": "31"},
            "Done": {"id": "31", "name": "Done"}
        }
}
```

```python
'PROJECT_KEY': {
  'bug_id': "10007",
  'story': {
      'id': "10005",
      'points': "customfield_10016",
      'transitions': [
          "To Do": {"id": "11", "name": "To Do", "next": "12"},
          {"id": "12", "name": "In Progress", "next": "31"},
          {"id": "31", "name": "Done"}
      ]
  }
```

- `jira_url` - URL of JIRA instance

## Data Sources

- `data_tickets.json` - List of JIRA tickets created with bulkcreate option

## Actions

### `bulkcreate`

Create multiple JIRA tickets.

Creates multiple JIRA tickets in a target project. If a project is not specified, a random project is chosen from `config.project_list`.

```bash
python copier.py bulkcreate
python copier.py bulkcreate --project-key="NORTH"
```

Arguments:

- `--limit` - total number of issues to create (default 5)
- `--project-key` - JIRA project key to create tickets in. Defaults to randomly selecting an element in the `config.project_list`.
- `--issue_type` - Display text name of issue type to use (`story` or `epic`). Default is `story`.

### `bulkupdate`

Select many JIRA tickets and transition status of a random subset.

Select the most recent issues and randomly transitions a subset of ticket to the next status.

```bash
python
```

Notes:

- Each project has a different Id for each transition category.

Arguments

- `--limit` - Total number of tickets to select as candidates to be transitioned.
- `--jql` - JQL expression to use to select tickets.
- `--percentage` - An integer `1` to `100`. Percentage of tickets to move.

### `workflow`

- `workflow move-ticket` - Get ticket in Ready for Dev --> assign to dev if necessary --> transition to In Progress
- `workflow commits` - Get ticket in In Progress -> Create and backdate commits --> Push commits to remote git repo
  - Random chance to not take a JIRA ticket

#### `workflow move-ticket`

Move a JIRA ticket from to do/backlog to In progress state

#### `workflow commits`

Take a Jira issue, create commits, open PR

- Random chance to not move a ticket
- Random chance to not reference Jira Id in commit messages

Arguments:

- `--project-key` - Jira Project to target. If omitted, commits will not be associated with a Jira ticket.
- `--repo-location` - Location of target git repo to make changes to.
- `--total-commits` - Number of commits to make
- `--clone-url` - HTTP clone URL of repo
- `--git-username` - Username in remote git repo SaaS service
- `--code-pat` - Personal Access Token for SaaS git service

| Flag                               | Env Var | Descr                                                                                  |
| ---------------------------------- | ------- | -------------------------------------------------------------------------------------- |
| `--project-key`, `PROJECT_KEY`     | ""      | Jira Project to target. If omitted, commits will not be associated with a Jira ticket. |
| `--repo_location`, `REPO_LOCATION` | ""      | Location of target git repo to make changes to.                                        |
| `--total-commits`, `TOTAL_COMMITS` | ""      | Number of commits to make                                                              |
| `--percent-jira`, `PERCENT_JIRA`   | 95      | Percent chance a Jira ticket will be associated with the commits.                      |

Logic:

1. Grab a Jira issue from the given project. Random chance to not grab a Jira ticket.
1. Get commit times
   1. Get Jira issue start time.
   1. Randomly generate times between Jira create date and current time. Sort times.
   1. Loop through commits and update commit time with timestamp array.
