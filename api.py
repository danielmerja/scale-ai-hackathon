import glob
from flask import Flask, request, jsonify
import logging


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


@app.route("/sendpage", methods=["POST", "GET"])
def sendpage():
    doc = request.json["message"]
    url = doc['url']
    title = doc['title']
    body = doc['body']

    return {"reply": "Analysis Complete!"}
