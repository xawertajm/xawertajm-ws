from flask import json
from pymongo import MongoClient
import requests

__author__ = 'matthew.farrugia'

#db variables
mongoHost = "ds015774.mlab.com"
mongoPort = 15774
mongoReadPreference = 1
mongoUser = "root"
mongoPassword = "PanamaPapers123"

#api variables
city = 'Valletta'
countryCode = 'mt'
apiKey = '8eab2eb7bab5914e5a9cf5605ac525e2'
url = 'http://api.openweathermap.org/data/2.5/weather?q=' +city + ',' + countryCode + '&appid=' + apiKey
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?q=' +city + ',' + countryCode + '&appid=' + apiKey

client = MongoClient(
        "mongodb://root:PanamaPapers123@ds015774.mlab.com:15774/heroku_kjcv89lc"
        #host=mongoHost,
        #port=mongoPort
        #read_preference=mongoReadPreference
    )

db = client["heroku_kjcv89lc"]
collection = db["weather_logs"]
response = requests.get(forecast_url)
insertResult = collection.insert_one(json.loads(response.content))

print insertResult;