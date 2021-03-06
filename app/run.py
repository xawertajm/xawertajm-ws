import datetime
import requests
import json
import os
import time
from flask import Flask, jsonify
from pymongo import MongoClient
from bson.json_util import dumps

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

#api variables
city = 'Valletta'
countryCode = 'mt'
apiKey = '8eab2eb7bab5914e5a9cf5605ac525e2'

#urls
current_weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' +city + ',' + countryCode + '&appid=' + apiKey
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?q=' +city + ',' + countryCode + '&appid=' + apiKey

@app.route("/result", methods=["GET"])
def getLatestPrediction():
    result = collection.find().sort("id", -1).limit(1)
    timestamp = int(result[1]['id'])
    if isUpdated(timestamp):
        return jsonify(dumps(result))
    else:
        newPredictions = updatePredictions()
        return jsonify(dumps(newPredictions))

def daysTilRain(firstDayOfRain):
    timeNow = time.time()
    todayDate = datetime.datetime.fromtimestamp(timeNow)
    daysToRain = (firstDayOfRain - todayDate).days  # whole days
    return daysToRain

# returns true if predictions were updated over the last hour
def isUpdated(timestamp):
    timestampNow = time.time()
    if timestampNow-timestamp <3600:
        return True
    else:
        return False

def updatePredictions():
    # get data from API
    response = requests.get(forecast_url)

    isRain = None
    firstDateOfRain = None
    lastDateOfRain = None
    totalPrecipitation = 0

    # check total precipitation for the next five days
    weekForecasts = json.loads(response.content)
    for forecast in weekForecasts["list"]:
        try:
            totalPrecipitation += forecast["rain"]["3h"]
            if totalPrecipitation > 0 and firstDateOfRain is None:
                firstDateOfRain = datetime.datetime.fromtimestamp(forecast["dt"])
                daysUntilRain = daysTilRain(firstDateOfRain)
                isRain = False if daysUntilRain < 3 else True
        except KeyError:
            continue

    id = int(time.time()).__str__()
    prediction = '{"id" : "' + id + '","washCar" : "' + isRain.__str__() + '", "predictionBasis" : { "daysUntilRain" : "' + daysUntilRain.__str__() + '", "precipitation" : "' + totalPrecipitation.__str__() + 'ml" }}'
    prediction_json = json.loads(prediction)

    # insert data in collection
    collection.insert_one(prediction_json)

    return prediction_json