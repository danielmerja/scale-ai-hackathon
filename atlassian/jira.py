import os
from jira import JIRA
from typing import Dict, List

#Research:
#    http://pythonjira.com/create-a-jira-ticket-with-python/
#    https://datageeks.medium.com/automate-your-jira-tasks-in-python-bbbcb3145a95

class JiraBase(object):
        def __init__(self): 
            jira_workspace_email = os.environ.get("JIRA_WORKSPACE_EMAIL")
            jira_api_token = os.environ.get("JIRA_API_TOKEN")
            jira_server = os.environ.get("JIRA_SERVER")
            self.jira_connection = JIRA(
            basic_auth=(jira_workspace_email, jira_api_token),
            server=jira_server)


class Jira(JiraBase):
    def __init__(self):
        JiraBase.__init__(self)


    def createIssue(self, projectId: str, summary: str, description: str, issuetype: str) -> JIRA.new_issue:

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
