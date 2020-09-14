import json
import os
import requests

connectionString = None

def init() :
    global connectionString
    print("\napi - init\n")

    # Build connectiong string
    connectionString = "https://api.openweathermap.org//data/2.5/weather?id=2267057&units=metric&appid=244df0cbb2bcae2bca2fbe929ae3a613"

def getWeather():
    r = requests.get(connectionString)
    return r.json()

def getInfo() :

    resultJson = getWeather()

    print("Temperature now in " + resultJson['name'] + " is " + str(resultJson['main']['temp']) + " Celsius")
    print("and if you look to the sky you see " + resultJson['weather'][0]['description'] )
