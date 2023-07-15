import glob
from flask import Flask, request, jsonify
import logging
from llms.openai import openaif
import os
from dotenv import load_dotenv


app = Flask(__name__) 
load_dotenv()
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
    tasks = collect_tasks()
    answer = ask_ai(tasks)
    return {"reply": "Message Received!" + message}


@app.route("/sendpage", methods=["POST", "GET"])
def sendpage():
    doc = request.json["message"]
    url = doc['url']
    title = doc['title']
    body = doc['body']

    return {"reply": "Analysis Complete!"}


def collect_tasks():
    return 'string of tasks'

def ask_ai(tasks):
    open_ai = openaif(api_key=os.getenv('OPENAI_API_KEY'))
    # Analyze Prompt
    prompt = f"Here are the tasks we have created: {tasks}, and please give us suggestion on a new task.\
        Is it contradictory or dupliate to any previous task we have? If so, please give us the title \
        of the task and the reason why it is contradictory or duplicate."
    return open_ai.user_request(prompt)

# For testing
if __name__ == "__main__":
    print(ask_ai("I am developing mobile application for generating stories with images. I have two version \
           of application in parallel, one for android and one for iOS assume I have completed the \
           following task 1 Story Input Screen - iOS with description As a parent I want the app to \
           have a page story input So That I could provide description for the heros and setting and \
           acceptance criteria Given: that I install iOS app And: long in When: initiate new story \
           Then: I should see the screen Story Input with the following fields character name character \
           appearacne charted gimmick And: I should see dropdown for setting with the following options\
            ancient greece nordic gods pantheon Hans Christian Andersen faritale universe And: I should\
            see the buttons \"Back\" - always active, takes user to the home screen \"Continue\" - \
                disabled by default, becomes active wwhen a setting is selected and at least one \
           character field is filled up Notes: a character and a setting must be requirted I should \
           be able to add more than one character \
> assume I have completed the following task 2 Story Input Screen - Android with description As a \
           parent I want the app to have a page story input So That I could provide description \
            for the heros and setting and acceptance criteria Given: that I install Android app And:\
            long in When: initiate new story Then: I should see the screen Story Input with the \
           following fields character name character appearacne charted gimmick And: I should see \
           dropdown for setting with the following options ancient greece nordic gods pantheon Hans \
           Christian Andersen faritale universe And: I should see the buttons Back - always active, \
           takes user to the home screen Continue - disabled by default, becomes active wwhen a \
           setting is selected and at least one character field is filled up Notes: a character and \
           a setting must be requirted I should be able to add more than one character"))