import os
from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

#db variables
mongoHost = "ds015774.mlab.com"
mongoPort = 15774
mongoUser = "root"
mongoPassword = "PanamaPapers123"

#access collection
client = MongoClient("mongodb://root:PanamaPapers123@ds015774.mlab.com:15774/heroku_kjcv89lc")
db = client["heroku_kjcv89lc"]
collection = db["prediction_logs"]

@app.route("/")
def hello():
    return "Hello orld!"

@app.route("/result", methods=["GET"])
def getResult():
    print("hello")
    latestUpdate = collection.find().sort({"id", -1}).limit(1)
    print (latestUpdate.count())
    print ("ello2")
    return latestUpdate

if __name__ == "__main__":
    app.run(port=5001)