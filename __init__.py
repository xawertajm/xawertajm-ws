import requests

__author__ = 'matthew.farrugia'

city = 'Valletta'
countryCode = 'mt'
apiKey = '8eab2eb7bab5914e5a9cf5605ac525e2'
request = 'http://api.openweathermap.org/data/2.5/weather?q=' +city + ',' + countryCode + '&appid=' + apiKey

r = requests.get(request)

print r.json();
print r.content;