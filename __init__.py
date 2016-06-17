import json
import time
import datetime
from pymongo import MongoClient
import requests

__author__ = 'matthew.farrugia'

def daysTilRain(firstDayOfRain):

    timeNow = time.time()
    todayDate = datetime.datetime.fromtimestamp(timeNow)
    daysToRain = (firstDayOfRain - todayDate).days  # whole days
    return daysToRain


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
collection = db["prediction_logs"]

#get data from API
response = requests.get(forecast_url)

totalPrecipitation = 0
isRain = None
firstDateOfRain = None
lastDateOfRain = None

#check total precipitation for the next five days
weekForecasts = json.loads(response.content)
for forecast in weekForecasts["list"]:
    try:
        totalPrecipitation += forecast["rain"]["3h"]
        if totalPrecipitation > 0 and firstDateOfRain is None:
            firstDateOfRain = datetime.datetime.fromtimestamp(forecast["dt"])
            daysUntilRain = daysTilRain(firstDateOfRain)
            isRain = False if daysUntilRain<3 else True
#        if forecast["rain"]["3h"] > 0:
#           lastDateOfRain = datetime.datetime.fromtimestamp(forecast["dt"]).strftime('%Y-%m-%d %H:%M:%S')
    except KeyError:
        continue

result = '{"washCar" : "'+isRain.__str__()+'", "predictionBasis" : { "daysUntilRain" : "'+daysUntilRain.__str__()+'", "precipitation" : "'+totalPrecipitation.__str__()+'ml" }}'
result_json = json.loads(result)

#insert data in collection
collection.insert_one(result_json)