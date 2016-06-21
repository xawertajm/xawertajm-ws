import os
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

#db variables
mongoHost = os.environ.get("MONGO_HOST")
mongoPort = os.environ.get("MONGO_PORT")
mongoUser = os.environ.get("USERNAME")
mongoPassword = os.environ.get("PASSWORD")
mongoDb = os.environ.get("DATABASE_NAME")

#access collection
client = MongoClient("mongodb://"+mongoUser+":"+mongoPassword+"@"+mongoHost+":"+mongoPort+"/"+db)
db = client[mongoDb]
collection = db["prediction_logs"]

"""
@app.route("/")
def hello():
    return "Hello orld!"
"""

@app.route("/result", methods=["GET"])
def getResult():
    latestUpdate = collection.find().sort({"id", -1}).limit(1)
    return latestUpdate