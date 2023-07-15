from api import app
from dotenv import load_dotenv
from atlassian.jira import Jira


load_dotenv()

# Create Jira Instance, select issue, and add a new issue.
a = Jira()
test =  a.searchIssueByUniqueId('MYH-9')
issues =  a.searchIssuesByProjectName('MyHero')
#new_issue = a.createIssue('MYH', 'A test from Sean''s python code', 'hopefully success','Bug')




def main():
    app.run()


if __name__ == "__main__":
    main()
