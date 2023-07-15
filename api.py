import glob
from flask import Flask, request, jsonify
import logging
from llms.openai import openaif
import os


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
    open_ai = openaif(api_key=os.environ['OPENAI_API_KEY'])
    # Analyze Prompt
    prompt = f"Here are the tasks we have created: {tasks}, and please give us suggestion on a new task.\
        Is it contradictory or dupliate to any previous task we have? If so, please give us the title \
        of the task and the reason why it is contradictory or duplicate."
    return open_ai.user_request(prompt)