import requests

__author__ = 'matthew.farrugia'

class apiUtils:

    @staticmethod
    def getCurrentWeather(apikey, city, countryCode):
        request = 'http://api.openweathermap.org/data/2.5/weather?q=' +city + ',' + countryCode + '&appid=' + apiKey
        requests.get(request)
        return request.content;