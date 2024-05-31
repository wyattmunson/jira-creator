import json

def get_ticket_desc():
    with open('data_tickets.json') as f:
        d = json.load(f)
        return d

def get_tickets():
    return {
    "expand": "schema,names",
    "startAt": 0,
    "maxResults": 50,
    "total": 18,
    "issues": [
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10000",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10000",
            "key": "FOX-1",
            "fields": {
                "statuscategorychangedate": "2024-05-30T13:09:01.670-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-1/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2024-05-30T13:09:01.376-0700",
                "customfield_10020": [
                    {
                        "id": 1,
                        "name": "FOX Sprint 1",
                        "state": "active",
                        "boardId": 2,
                        "goal": "",
                        "startDate": "2024-05-31T02:01:59.024Z",
                        "endDate": "2024-06-14T02:01:53.000Z"
                    }
                ],
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|hzzzzz:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T13:09:02.120-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "Create framework for FE application",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-1/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10001",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10001",
            "key": "FOX-2",
            "fields": {
                "statuscategorychangedate": "2024-05-30T13:09:09.578-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": "2024-05-30T14:58:33.378-0700",
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-2/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T13:09:09.341-0700",
                "customfield_10020": [
                    {
                        "id": 1,
                        "name": "FOX Sprint 1",
                        "state": "active",
                        "boardId": 2,
                        "goal": "",
                        "startDate": "2024-05-31T02:01:59.024Z",
                        "endDate": "2024-06-14T02:01:53.000Z"
                    }
                ],
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "customfield_10026": None,
                "labels": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i00007:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T13:09:09.819-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "Create FE design mocks",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-2/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10003",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10003",
            "key": "FOX-3",
            "fields": {
                "statuscategorychangedate": "2024-05-30T15:00:40.474-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": None,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-3/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T15:00:40.132-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "customfield_10026": None,
                "labels": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0000n:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T15:00:40.192-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "Sample create ticket",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-3/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10004",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10004",
            "key": "FOX-4",
            "fields": {
                "statuscategorychangedate": "2024-05-30T15:20:55.136-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": "2024-05-30T16:39:21.296-0700",
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-4/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T15:20:54.864-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "customfield_10026": None,
                "labels": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0000v:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T15:20:54.911-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "[\"Create route 53 domain\", \"Fix redirect on failed login\", \"Grab a beer\", \"Let residents out of Vault 101\", \"Add Harness FF to main site\"][Math.floor(Math.random() * arr.length)]",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-4/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10005",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10005",
            "key": "FOX-5",
            "fields": {
                "statuscategorychangedate": "2024-05-30T15:25:53.744-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-5/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2024-05-30T15:25:53.542-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i00013:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T15:25:53.580-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "[\"Create route 53 domain\", \"Fix redirect on failed login\", \"Grab a beer\", \"Let residents out of Vault 101\", \"Add Harness FF to main site\"]None",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-5/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10006",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10006",
            "key": "FOX-6",
            "fields": {
                "statuscategorychangedate": "2024-05-30T15:26:59.375-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": None,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-6/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T15:26:59.136-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "customfield_10026": None,
                "labels": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0001b:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T15:26:59.179-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "[\"Create route 53 domain\", \"Fix redirect on failed login\", \"Grab a beer\", \"Let residents out of Vault 101\", \"Add Harness FF to main site\"][Math.floor(Math.random() * arr.length)]",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-6/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10007",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10007",
            "key": "FOX-7",
            "fields": {
                "statuscategorychangedate": "2024-05-30T15:31:27.211-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-7/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2024-05-30T15:31:26.890-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "customfield_10026": None,
                "labels": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0001j:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T15:31:26.953-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "[\"Create route 53 domain\", \"Fix redirect on failed login\", \"Grab a beer\", \"Let residents out of Vault 101\", \"Add Harness FF to main site\"][<+Math.floor(Math.random() * 11)]",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-7/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10008",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10008",
            "key": "FOX-8",
            "fields": {
                "statuscategorychangedate": "2024-05-30T15:32:03.666-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-8/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2024-05-30T15:32:03.421-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0001r:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T15:32:03.458-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": None,
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "[\"Create route 53 domain\", \"Fix redirect on failed login\", \"Grab a beer\", \"Let residents out of Vault 101\", \"Add Harness FF to main site\"][None]",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-8/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10009",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10009",
            "key": "FOX-9",
            "fields": {
                "statuscategorychangedate": "2024-05-30T16:38:39.543-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": "2024-05-30T17:36:13.575-0700",
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-9/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T16:38:39.151-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "customfield_10026": None,
                "labels": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0001z:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T16:38:39.337-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Your story description here (optional)",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "Made by API call",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-9/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10010",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10010",
            "key": "FOX-10",
            "fields": {
                "statuscategorychangedate": "2024-05-30T16:39:32.052-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": "2024-05-30T16:55:28.069-0700",
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-10/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T16:39:31.795-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i00027:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T16:39:31.866-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Your story description here (optional)",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "Made by API call",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-10/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10011",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10011",
            "key": "FOX-11",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:46:27.135-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-11/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": "2024-05-30T18:54:38.142-0700",
                "created": "2024-05-30T16:54:36.058-0700",
                "customfield_10020": [
                    {
                        "id": 1,
                        "name": "FOX Sprint 1",
                        "state": "active",
                        "boardId": 2,
                        "goal": "",
                        "startDate": "2024-05-31T02:01:59.024Z",
                        "endDate": "2024-06-14T02:01:53.000Z"
                    }
                ],
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [
                    "Test",
                    "sampleLabel"
                ],
                "customfield_10026": None,
                "customfield_10016": 4848.0,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0002f:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:46:27.135-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10004",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "In Progress",
                    "id": "10004",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/4",
                        "id": 4,
                        "key": "indeterminate",
                        "colorName": "yellow",
                        "name": "In Progress"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Your story description here (optional)",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "Created by python script",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-11/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10012",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10012",
            "key": "FOX-12",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:37:53.288-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": None,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-12/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T18:37:52.996-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0002n:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:37:53.061-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Implement A/B testing to compare the performance of two different landing page designs and determine which one leads to better user engagement.",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "Implement A/B Testing for New Landing Page Design (Priority: Medium)",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-12/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10013",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10013",
            "key": "FOX-13",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:46:14.961-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": "2024-05-30T18:41:44.250-0700",
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-13/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T18:37:54.239-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0002v:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:46:14.960-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10004",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "In Progress",
                    "id": "10004",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/4",
                        "id": 4,
                        "key": "indeterminate",
                        "colorName": "yellow",
                        "name": "In Progress"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Investigate spikes in server resource utilization that could be causing performance issues. Identify the root cause and implement solutions to optimize resource usage.",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "Investigate Spikes in Server Resource Utilization (Priority: Medium)",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-13/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10014",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10014",
            "key": "FOX-14",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:37:55.666-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": None,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-14/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T18:37:55.441-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i00033:",
                "aggregatetimeoriginalestimate": None,
                "timeestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:37:55.505-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Search functionality experiencing slow response times for queries with more than 10 keywords. (Priority: Medium)",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "Investigate Performance Issues on Search Functionality",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-14/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10015",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10015",
            "key": "FOX-15",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:54:50.730-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-15/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2024-05-30T18:37:56.557-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0003b:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:54:50.728-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10004",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "In Progress",
                    "id": "10004",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/4",
                        "id": 4,
                        "key": "indeterminate",
                        "colorName": "yellow",
                        "name": "In Progress"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Improve logging mechanisms for critical system errors to provide more detailed information for debugging purposes.",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "Improve Logging for Debugging Critical System Errors (Priority: Medium)",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-15/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10016",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10016",
            "key": "FOX-16",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:37:57.936-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-16/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2024-05-30T18:37:57.699-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "customfield_10023": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0003j:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:37:57.770-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Review and update code style guidelines to ensure consistency and readability across the codebase.  (Priority: Low)",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "Update Code Style Guidelines for Improved Readability",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-16/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10017",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10017",
            "key": "FOX-17",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:41:32.873-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-17/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "lastViewed": None,
                "created": "2024-05-30T18:41:32.662-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "customfield_10026": None,
                "labels": [],
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0003r:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:41:32.720-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Search functionality experiencing slow response times for queries with more than 10 keywords. (Priority: Medium)",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "customfield_10007": None,
                "security": None,
                "customfield_10008": None,
                "aggregatetimeestimate": None,
                "customfield_10009": None,
                "summary": "Investigate Performance Issues on Search Functionality",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-17/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        },
        {
            "expand": "operations,versionedRepresentations,editmeta,changelog,customfield_10010.requestTypePractice,renderedFields",
            "id": "10018",
            "self": "https://harness-sei.atlassian.net/rest/api/2/issue/10018",
            "key": "FOX-18",
            "fields": {
                "statuscategorychangedate": "2024-05-30T18:41:33.981-0700",
                "issuetype": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issuetype/10005",
                    "id": "10005",
                    "description": "Stories track functionality or features expressed as user goals.",
                    "iconUrl": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10315?size=medium",
                    "name": "Story",
                    "subtask": False,
                    "avatarId": 10315,
                    "entityId": "cd84c884-b6cd-4873-b8c7-afe4dd262b07",
                    "hierarchyLevel": 0
                },
                "timespent": None,
                "customfield_10030": None,
                "project": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/project/10001",
                    "id": "10001",
                    "key": "FOX",
                    "name": "Fox Team",
                    "projectTypeKey": "software",
                    "simplified": True,
                    "avatarUrls": {
                        "48x48": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405",
                        "24x24": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=small",
                        "16x16": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=xsmall",
                        "32x32": "https://harness-sei.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10405?size=medium"
                    }
                },
                "fixVersions": [],
                "aggregatetimespent": None,
                "resolution": None,
                "customfield_10027": None,
                "customfield_10028": None,
                "customfield_10029": None,
                "resolutiondate": None,
                "workratio": -1,
                "lastViewed": "2024-05-30T19:28:53.689-0700",
                "watches": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-18/watchers",
                    "watchCount": 1,
                    "isWatching": True
                },
                "created": "2024-05-30T18:41:33.765-0700",
                "customfield_10020": None,
                "customfield_10021": None,
                "customfield_10022": None,
                "priority": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/priority/3",
                    "iconUrl": "https://harness-sei.atlassian.net/images/icons/priorities/medium.svg",
                    "name": "Medium",
                    "id": "3"
                },
                "customfield_10023": None,
                "customfield_10024": None,
                "customfield_10025": None,
                "labels": [],
                "customfield_10026": None,
                "customfield_10016": None,
                "customfield_10017": None,
                "customfield_10018": {
                    "hasEpicLinkFieldDependency": False,
                    "showField": False,
                    "nonEditableReason": {
                        "reason": "PLUGIN_LICENSE_ERROR",
                        "message": "The Parent Link is only available to Jira Premium users."
                    }
                },
                "customfield_10019": "0|i0003z:",
                "timeestimate": None,
                "aggregatetimeoriginalestimate": None,
                "versions": [],
                "issuelinks": [],
                "assignee": None,
                "updated": "2024-05-30T18:41:33.820-0700",
                "status": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/status/10003",
                    "description": "",
                    "iconUrl": "https://harness-sei.atlassian.net/",
                    "name": "To Do",
                    "id": "10003",
                    "statusCategory": {
                        "self": "https://harness-sei.atlassian.net/rest/api/2/statuscategory/2",
                        "id": 2,
                        "key": "new",
                        "colorName": "blue-gray",
                        "name": "To Do"
                    }
                },
                "components": [],
                "timeoriginalestimate": None,
                "description": "Buttons on the product listing page have inconsistent spacing, creating a misaligned layout on some screen sizes. (Priority: Low)",
                "customfield_10010": None,
                "customfield_10014": None,
                "customfield_10015": None,
                "customfield_10005": None,
                "customfield_10006": None,
                "security": None,
                "customfield_10007": None,
                "customfield_10008": None,
                "customfield_10009": None,
                "aggregatetimeestimate": None,
                "summary": "Fix Visual Bug: Inconsistent Button Spacing on Product Listing Page",
                "creator": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "subtasks": [],
                "reporter": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/user?accountId=712020%3A1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "accountId": "712020:1d5dd3c0-e762-4ab6-bf15-e1a5153e9897",
                    "emailAddress": "wyatt@harness.io",
                    "avatarUrls": {
                        "48x48": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "24x24": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "16x16": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png",
                        "32x32": "https://secure.gravatar.com/avatar/c6c429f0cce03fcfc529413e70a79734?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FWM-5.png"
                    },
                    "displayName": "Wyatt Munson",
                    "active": True,
                    "timeZone": "America/Los_Angeles",
                    "accountType": "atlassian"
                },
                "aggregateprogress": {
                    "progress": 0,
                    "total": 0
                },
                "customfield_10001": None,
                "customfield_10002": None,
                "customfield_10003": None,
                "customfield_10004": None,
                "environment": None,
                "duedate": None,
                "progress": {
                    "progress": 0,
                    "total": 0
                },
                "votes": {
                    "self": "https://harness-sei.atlassian.net/rest/api/2/issue/FOX-18/votes",
                    "votes": 0,
                    "hasVoted": False
                }
            }
        }
    ]
}