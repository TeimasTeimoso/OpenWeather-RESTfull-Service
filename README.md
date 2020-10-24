# OpenWeather-RESTfull-Service

## Default values
By default the server is running on **port 5656**. It can be changed in _config/config.toml_ as well as the API key.

## Running
Inside de _/app_ folder run _python3 do.py_ to start the server.
To fetch data you can use either the browser, postman, or terminal (using _curl_), querying, by default, _http://localhost:5656/weather/city/2268406_, in which the last path element is _city_id_.
