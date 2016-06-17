import requests

__author__ = 'matthew.farrugia'

class apiUtils:

    @staticmethod
    def getCurrentWeather(apiKey, city, countryCode):
        request = 'http://api.openweathermap.org/data/2.5/weather?q=' +city + ',' + countryCode + '&appid=' + apiKey
        response = requests.get(request)
        return response.content;
