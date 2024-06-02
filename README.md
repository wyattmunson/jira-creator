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
