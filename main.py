import os
from api import app
from dotenv import load_dotenv
from atlassian.jira import Jira
from llms.openai import openaif


load_dotenv()

# Create Jira Instance, select issue, and add a new issue.
a = Jira()
test =  a.searchIssueByUniqueId('MYH-9')
issues =  a.searchIssuesByProjectName('MyHero')
#new_issue = a.createIssue('MYH', 'A test from Sean''s python code', 'hopefully success','Bug')

jira_query = """
I am developing mobile application for generating stories with images. 
I have two version of application in parallel, one for android and one for iOS
Following are the tasks I have, some of which I have finished.

"""

for issue in issues:
    jira_query += str(issue) + "\n"

jira_query += """
    Please give us suggestion on tasks I have created but not finished. \
    Are they contradictory or dupliate to any previous tasks we have? If so, please give us the title \
    of the task and the reason why it is contradictory or duplicate. \
    Also, is there task or subtask I am missing? If so, please tell me the summary of one new task I should have made."
""" 

apikey = os.environ.get("OPENAI_KEY")
chat = openaif(apikey)
response = chat.user_request(jira_query)

print(response)



def main():
    app.run()


# if __name__ == "__main__":
#     main()
