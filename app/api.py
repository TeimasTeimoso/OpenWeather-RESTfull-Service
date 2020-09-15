import json
import os
import requests
import toml
# local import

api_key = None
base_url = "https://api.openweathermap.org//data/2.5/weather?appid=" # id=2267057&units=metric&appid=244df0cbb2bcae2bca2fbe929ae3a613

# add the api_key to the base url
# RETURN: void
def init():
    global api_key, base_url

    api_key = toml.load("config/config.toml")["api"]["key"]
    base_url += api_key + "&id="

# check if file exists
# RETURN: bool
def in_cache(file_path):
    return os.path.exists(file_path)

# save data on json file
# RETURN: void
def save_in_cache(city_id, response):
    with open(f"cache/{city_id}.json", "w") as outfile:
        json.dump(response, outfile)

# fetch the weather given a city_id
# either from cache or openweather api
# RETURN: String (Json)
def get_weather(city_id):
    file_path = f"cache/{city_id}.json"

    # if data exits in cache
    if in_cache(file_path):
        with open(file_path) as result:
            return result.read()

    response = requests.get(base_url+city_id)
    result = response.json()

    if response.status_code == 200:
        save_in_cache(city_id, result)

    return result

init()

print(api_key)
print(base_url)

print(get_weather(str(3448433)))

