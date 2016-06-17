from flask import json
from pymongo import MongoClient
import requests

__author__ = 'matthew.farrugia'

#db variables
mongoHost = "ds015774.mlab.com"
mongoPort = 15774
mongoUser = "root"
mongoPassword = "PanamaPapers123"

#api variables
city = 'Valletta'
countryCode = 'mt'
apiKey = '8eab2eb7bab5914e5a9cf5605ac525e2'

#urls
current_weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' +city + ',' + countryCode + '&appid=' + apiKey
forecast_url = 'http://api.openweathermap.org/data/2.5/forecast?q=' +city + ',' + countryCode + '&appid=' + apiKey

#access collection
client = MongoClient("mongodb://root:PanamaPapers123@ds015774.mlab.com:15774/heroku_kjcv89lc")
db = client["heroku_kjcv89lc"]
collection = db["weather_logs"]

#get data from API
response = requests.get(forecast_url)

#insert data in collection
#insertResult = collection.insert_one(json.loads(response.content))
findResult = collection.find()

totalPrecipitation = 0
isRain = None
firstDateOfRain = None
lastDateOfRain = None

#check total precipitation for the next five days
for document in findResult:
    for forecast in  document["list"]:
        try:
            totalPrecipitation += forecast["rain"]["3h"]
            if totalPrecipitation > 0 and firstDateOfRain is None:
                firstDateOfRain = forecast["dt"]
                isRain = True
            if forecast["rain"]["3h"] > 0:
                lastDateOfRain = forecast["dt"]
        except KeyError:
            continue

json_str = "{washCar : "",
  predictionBasis : {
   daysUntilRain : 3,
   precipitation : 0.6
  },"


    #for key in document.keys():
    #    print document[key]
