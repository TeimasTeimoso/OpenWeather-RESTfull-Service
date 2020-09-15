import requests, json, logging
import os
import toml
from datetime import datetime

logging.basicConfig(filename="logs/response_log.txt", level="INFO")

api_key = None
base_url = "https://api.openweathermap.org//data/2.5/weather?appid=" 

# add the api_key to the base url
# RETURN: void
def init():
    global api_key, base_url

    api_key = toml.load("config/config.toml")["api"]["key"]
    base_url = base_url + api_key + "&id="

# check if file exists
# RETURN: bool
def in_cache(file_path):
    return os.path.exists(file_path)

# save data on json file
# RETURN: void
def save_in_cache(filepath, response):
    with open(filepath, "w") as outfile:
        json.dump(response, outfile)
        logging.info(f"TIME: {datetime.now()} => Saved in cache {filepath}!")

# fetch the weather given a city_id
# either from cache or openweather api
# RETURN: String (Json)
def get_weather(city_id):
    file_path = f"cache/{city_id}.json"

    # if data exits in cache
    if in_cache(file_path):
        with open(file_path) as result:
            logging.info(f"TIME: {datetime.now()} => Read from cache:{file_path}")
            return json.loads(result.read())

    response = requests.get(base_url+city_id+"&units=metric")
    result = response.json()

    if response.status_code == 200:
        save_in_cache(file_path, result)

    return result

