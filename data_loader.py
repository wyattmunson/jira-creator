def get_ticket_desc():
    return [
        {
          "title": "Login Functionality Not Working for New Users",
          "descr": "Users created after May 25th, 2024 are unable to log in. Error message: 'Invalid Credentials.' (Priority: High)"
        },
        {
          "title": "Mobile App Crashing on Product Page Load",
          "descr": "App crashes consistently on Android devices (version 11+) when trying to access the product page. (Priority: High)"
        },
        {
          "title": "Implement Unit Tests for User Registration Flow",
          "descr": "Currently, no unit tests exist for the user registration process. Add unit tests to ensure proper functionality. (Priority: Medium)"
        },
        {
          "title": "Update Documentation for API v2.0 Release",
          "descr": "Update API documentation to reflect changes introduced in version 2.0. (Priority: Medium)"
        },
        {
          "title": "Investigate Performance Issues on Search Functionality",
          "descr": "Search functionality experiencing slow response times for queries with more than 10 keywords. (Priority: Medium)"
        },
        {
          "title": "Implement Feature: User Two-Factor Authentication (2FA)",
          "descr": "Add functionality for users to enable two-factor authentication for their accounts. (Priority: Low)"
        },
        {
          "title": "Fix Broken Link in Admin Dashboard",
          "descr": "Link labeled 'View User Activity' in the admin dashboard is not functioning. (Priority: Low)"
        },
        {
          "title": "Update Error Messages for Payment Processing Failure",
          "descr": "Improve error messages displayed during payment processing failures to provide users with more specific information about the issue. (Priority: Medium)"
        },
        {
          "title": "Investigate Memory Leak in Core Application Service",
          "descr": "Memory usage is increasing steadily over time, potentially indicating a memory leak. (Priority: High)"
        },
        {
          "title": "Design Review: New User Onboarding Process",
          "descr": "Conduct a design review for the proposed new user onboarding process. (Priority: Medium)"
        },
        {
          "title": "Update Code Style Guidelines for Improved Readability",
          "descr": "Review and update code style guidelines to ensure consistency and readability across the codebase.  (Priority: Low)"
        },
        {
          "title": "Implement Automated Testing for Regression Prevention",
          "descr": "Set up automated testing suite to prevent regressions during future deployments. (Priority: Medium)"
        },
        {
          "title": "Fix Visual Bug: Inconsistent Button Spacing on Product Listing Page",
          "descr": "Buttons on the product listing page have inconsistent spacing, creating a misaligned layout on some screen sizes. (Priority: Low)"
        },
        {
          "title": "Investigate Security Vulnerabilities in Third-Party Library",
          "descr": "Recent security reports indicate potential vulnerabilities in a third-party library used in the project. Investigate and take necessary actions. (Priority: High)"
        },
        {
          "title": "Update Database Schema for New Feature Implementation",
          "descr": "Update database schema to accommodate the upcoming Product Reviews feature. (Priority: Medium)"
        },
        {
          "title": "Update CI/CD Pipeline for Faster Deployment (Priority: Medium)",
          "descr": "The current CI/CD pipeline is taking too long to deploy new code changes. Investigate ways to optimize the pipeline for faster deployments."
        },
        {
          "title": "Investigate Compatibility Issues with New Browser Version (Priority: Medium)",
          "descr": "The recent release of a new browser version (e.g., Chrome 110) is causing compatibility issues with our web application. Identify and fix any bugs related to the new browser version."
        },
        {
          "title": "Implement Feature: User Search Functionality (Priority: Medium)",
          "descr": "Implement a search functionality that allows users to search for other users based on various criteria (e.g., username, email address)."
        },
        {
          "title": "Fix Broken Image in Knowledge Base Article (Priority: Low)",
          "descr": "A broken image is present in a knowledge base article, hindering the user experience. Fix the image or replace it with a relevant one."
        },
        {
          "title": "Review Third-Party Library Licenses for Compliance (Priority: Low)",
          "descr": "Review the licenses of all third-party libraries used in the project to ensure compliance with their terms of use."
        },
        {
          "title": "Improve Logging for Debugging Critical System Errors (Priority: Medium)",
          "descr": "Improve logging mechanisms for critical system errors to provide more detailed information for debugging purposes."
        },
        {
          "title": "Conduct Performance Testing for High Traffic Scenarios (Priority: Medium)",
          "descr": "Conduct performance testing to simulate high traffic scenarios and identify any potential bottlenecks in the system."
        },
        {
          "title": "Add Automated Backups for Disaster Recovery (Priority: Medium)",
          "descr": "Implement a system for automated backups to ensure data recovery in case of system failures or disasters."
        },
        {
          "title": "Update External API Integration for Latest Version (Priority: Medium)",
          "descr": "Update the integration with an external API to ensure compatibility with the latest version of the API."
        },
        {
          "title": "Fix Minor UI Bug: Button Hover Effect Not Working (Priority: Low)",
          "descr": "The hover effect for a button is not working as intended. Fix the bug to restore the expected user interaction."
        },
        {
          "title": "Implement A/B Testing for New Landing Page Design (Priority: Medium)",
          "descr": "Implement A/B testing to compare the performance of two different landing page designs and determine which one leads to better user engagement."
        },
        {
          "title": "Improve Documentation for Internal APIs (Priority: Medium)",
          "descr": "Improve the documentation for internal APIs used by developers within the team. Ensure the documentation is clear, concise, and up-to-date."
        },
        {
          "title": "Fix Minor Bug: Incorrect Date Format Displayed on Reports (Priority: Low)",
          "descr": "A minor bug is causing dates to be displayed in the wrong format on reports. Fix the bug to ensure accurate date representation."
        },
        {
          "title": "Update User Onboarding Process for Improved Clarity (Priority: Medium)",
          "descr": "Review and update the user onboarding process to improve clarity and guide new users through the initial setup steps more effectively."
        },
        {
          "title": "Investigate Potential for Data Loss During User Account Deletion (Priority: High)",
          "descr": "Investigate the potential for data loss during the process of deleting a user account. Identify and fix any issues to ensure data integrity."
        },
        {
          "title": "Schedule System Maintenance for Database Upgrade (Priority: Medium)",
          "descr": "Schedule a system maintenance window to perform a database upgrade. Ensure proper communication and minimize downtime for users."
        },
        {
          "title": "Improve Mobile App Responsiveness for Different Devices (Priority: Medium)",
          "descr": "The mobile app layout appears distorted or broken on certain devices. Ensure proper responsiveness of the app across different screen sizes and, device types."
        },
        {
          "title": "Improve User Interface (UI) for Improved User Experience (UX) (Priority: Medium)",
          "descr": "Improve the user interface (UI) to enhance the overall user experience (UX). This could involve refining the visual design, improving layout and navigation, or making interactions more intuitive."
        },
        {
          "title": "Implement Feature: User-Defined Email Notifications (Priority: Medium)",
          "descr": "Implement a feature that allows users to define the types of email notifications they receive from the system (e.g., order updates, account activity alerts)."
        },
        {
          "title": "Update Third-Party Library to Address Security Patch (Priority: High)",
          "descr": "Update a third-party library to the latest version to address a recently identified security patch. Address any breaking changes introduced in the new version."
        },
        {
          "title": "Investigate Spikes in Server Resource Utilization (Priority: Medium)",
          "descr": "Investigate spikes in server resource utilization that could be causing performance issues. Identify the root cause and implement solutions to optimize resource usage."
        },
        {
          "title": "Conduct User Acceptance Testing (UAT) for New Feature Release (Priority: Medium)",
          "descr": "Conduct user acceptance testing (UAT) with a group of representative users to validate the functionality and usability of a new feature before release."
        },
        {
          "title": "Implement Feature: User-Generated Content Moderation Tools (Priority: Medium)",
          "descr": "Implement tools to moderate user-generated content (UGC) on the platform, such as comments or reviews. This could involve filtering inappropriate content or allowing users to report violations."
        },
        {
          "title": "Improve Scalability of System Infrastructure (Priority: Medium)",
          "descr": "Improve the scalability of the system infrastructure to handle increased user traffic or data volume. This might involve adding additional servers or optimizing resource allocation."
        },
        {
          "title": "Conduct Security Audit for Potential Vulnerabilities (Priority: High)",
          "descr": "Conduct a security audit to identify potential vulnerabilities in the system that could be exploited by attackers. Address any high-risk vulnerabilities discovered during the audit."
        },
        {
          "title": "Update Code for Compliance with New Coding Standards (Priority: Medium)",
          "descr": "Update the codebase to comply with new coding standards adopted by the team or industry. This could involve refactoring code, adopting new coding conventions, or using specific code style guidelines."
        },
        {
          "title": "Create Knowledge Base Articles for Common User Issues (Priority: Medium)",
          "descr": "Create knowledge base articles that address common user issues and provide step-by-step instructions for resolving them. These articles can be a valuable self-service resource for users."
        },
        {
          "title": "Update Security Best Practices for User Data Storage (Priority: High)",
          "descr": "Our current practices for user data storage might not be aligned with the latest security best practices. Review and update data storage methods to ensure user data is protected."
        },
        {
          "title": "Update Code Coverage Metrics for Improved Test Suite Efficiency (Priority: Medium)",
          "descr": "Review the code coverage metrics of the current test suite. Look for areas with low coverage and add additional tests to improve overall test efficiency."
        },
        {
          "title": "Conduct Code Review for Recently Merged Feature Branch (Priority: Medium)",
          "descr": "A recently merged feature branch might contain bugs or unintended changes. Conduct a code review to identify any issues and ensure the code meets quality standards."
        }
        ]

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