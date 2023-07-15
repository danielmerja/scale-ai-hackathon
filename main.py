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

open_ai = openaif(os.environ.get('OPENAI_KEY'))
res = open_ai.user_request("create a Jira task in the MYH project to enable a user to upload an image on their IOS cellphone.")

print(res)
def main():
    app.run()


if __name__ == "__main__":
    main()
