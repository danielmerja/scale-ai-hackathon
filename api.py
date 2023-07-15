import os
import glob
from flask import Flask, request, jsonify
import logging
from atlassian.jira import Jira
from llms.openai import openaif

app = Flask(__name__) 

#@app.route("/", defaults={"path": "index.html"})
#@app.route("/<path:path>")
#def static_file(path):
#    path1 = app.instance_path
#    return app.send_static_file(path)


# message / reply format
@app.route("/sendchat", methods=["POST", "GET"])
def chat():
    message = request.json["message"]
    return {"reply": "Message Received!" + message}


# message / reply format
@app.route("/analyze", methods=["POST", "GET"])
def analyze():
    a = Jira()
    issues =  a.searchIssuesByProjectName('MyHero')
    answer = ask_ai(issues)
    return {"reply": answer}


@app.route("/sendpage", methods=["POST", "GET"])
def sendpage():
    doc = request.json["message"]
    url = doc['url']
    title = doc['title']
    body = doc['body']

    return {"reply": "Analysis Complete!"}


def ask_ai(tasks):
    api_key=os.environ.get('OPENAI_KEY')
    open_ai = openaif(api_key)
    # Analyze Prompt
    project = "I am developing mobile application for generating stories with images. I have two version of application in parallel, one for android and one for iOS. "
    prompt = f"I am working on a project: {project}. Here are the tasks we have created: {tasks}, and please give us suggestion on a new task.\
        Is it contradictory or dupliate to any previous task we have? If so, please give us the title \
        of the task and the reason why it is contradictory or duplicate. \
        Also, is there task or subtask I am missing? If so, please tell me the summary of one new task I should have made."
    return open_ai.user_request(prompt)
