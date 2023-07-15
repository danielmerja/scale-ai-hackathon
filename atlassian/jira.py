import os
from jira import JIRA
from typing import Dict, List

#Research:
#    http://pythonjira.com/create-a-jira-ticket-with-python/
#    https://datageeks.medium.com/automate-your-jira-tasks-in-python-bbbcb3145a95

class Jira(object):
    def __init__(self): 
            jira_email = os.environ.get("JIRA_EMAIL")
            jira_api_token = os.environ.get("JIRA_API_TOKEN")
            jira_server = os.environ.get("JIRA_SERVER")
            options =  {'server': jira_server}
            self.jira_connection = JIRA(options, basic_auth=(jira_email, jira_api_token))


    def createIssue(self, projectId: str, summary: str, description: str, issuetype: str):

        #issue_dict = {
        #    'project': {'key': 'PJH'},
        #    'summary': 'Testing issue from Python Jira Handbook',
        #    'description': 'Detailed ticket description.',
        #    'issuetype': {'name': 'Bug'},
        #}


        issue_dict = {
            'project': {'key': projectId},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issuetype},
        }

        new_issue = self.jira_connection.create_issue(fields=issue_dict)
        return new_issue

    def searchIssuesByProjectName(self, projectName: str) -> List:
        retList = []
        for issue in self.jira_connection(kql_str='project = ' + projectName):
            retList.append({ issue.key, issue.fields.summary, issue.fields.reporter.displayName})
        return retList

    def searchIssueByUniqueId(self, Id: str) -> List:
        issue = self.jira_connection.issue(Id)
        return {issue.key, issue.fields.summary, issue.fields.reporter.displayName}
