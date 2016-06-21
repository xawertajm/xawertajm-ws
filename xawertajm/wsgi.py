import os
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

#db variables

mongoHost = "ds015774.mlab.com"
mongoPort = 15774
mongoUser = "root"
mongoPassword = "PanamaPapers123"
mongoDb = "heroku_kjcv89lc"

#access collection
client = MongoClient("mongodb://root:PanamaPapers123@ds015774.mlab.com:15774/heroku_kjcv89lc")
db = client[mongoDb]
collection = db["prediction_logs"]


@app.route("/")
def hello():
    return "Welcome to XAWERTAJM-WS!"

@app.route("/result", methods=["GET"])
def getResult():
    latestUpdate = collection.find().sort({"id", -1}).limit(1)
    return latestUpdate