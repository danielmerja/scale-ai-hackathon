import os
from api import app
from dotenv import load_dotenv
from atlassian.jira import Jira
from llms.openai import openaif

load_dotenv()

# Create Jira Instance, select issue, and add a new issue.
#a = Jira()
#test =  a.searchIssueByUniqueId('MYH-9')
#issues =  a.searchIssuesByProjectName('MyHero')
#new_issue = a.createIssue('MYH', 'A test from Sean''s python code', 'hopefully success','Bug')

jira_query = """
Preamble: You are an expert project manager tasked with meticulously outlining projects for engineers to work on.

A new project manager has created a project with the following tasks:
"""


jira_query += """
    Please provide analysis and guidance as to what the project manager may want to scrutinize in terms of additional items that may need to be created
""" 

def main():
    app.run()


if __name__ == "__main__":
    main()
