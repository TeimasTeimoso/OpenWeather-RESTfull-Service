
# BOOTSTRAP-PY #

  

Boostrap development project for container based Sensefinity Cloud services built in Python.

### ASSESSMENT EXERCISE ###

**After reading** the goal of the exercise, **check below explanations** on how to deal with the development environment.

Please, any questions get in touch with us by email.

Current working project gets Lisbon weather directly from an **OpenWeather** URL and write it on the log screen, as you can see running docker-compose.
The goal is, with a **REST solution**, to **receive a code** from any **city**, **check** if the requested code **is already in Cache** key value system with weather information, if exists use it from "cache", **if not get from OpenWeather once again**.

You can **see how to get cities ID's** for your tests as explained here [Part 3: Get your OpenWeatherMap City ID](https://www.dmopress.com/openweathermap-howto/)

 1. **Create a JSON RESTfull service**, that **accept a GET request with a city ID** (you can use any PORT you want as example here we suggest 5656), **e.g.** São Paulo Brazil weather could be requested with URL [GET Method] http://localhost:5656/weather/city/3448433  (**3448433** number is dynamic, your code will return based on this code number)
 2. After receiving the request **check if it already exists in a cache** solution, for this exercise can be a folder with text, or json files which name is the ID, and the content the weather, see the example in *app/cache/* folder.. 
 3. At the file system cache feature, **if it exists in the files cache folder, use the one already there**, **if** it does **not** exist **go** directly **to OpenWeather** and get the new info
 4. return the reques in JSON format for the user request after **saving it in the cache folder** for the next requests.
 5. **Important to note**, **don't worry for the time files are in the cache folder, they can be there forever :)**. 

> This assessment will evaluate how you structure code, types,
> variables, nomenclatures, move data across functions and how far you go to have a reliable code in place.


### How do I get set up? ###

    git clone git@gitlab.com:sensefinity-world/bootstrap-py.git

rename the folder to your project name

    mv bootstrap-py the-new-name

move in to the folder

    cd the-new-name

checkout assessment branch (should have been sent by email)

    git checkout assessment-level-date
    
and remove the .git folder

    rm -fr .git

  

Now the project have no connection with the original repository. Further on to have it in a new repository create a new project at an online repositories manager e.g. Gitlab, Github,... with your own account, and push your solution there, after finishing send us the URL of where you pushed your work to by email.
  

### Executing

  
To run the solution, go into app/ folder and execute

    python do.py

  
### Helping links

[Install Python 3 in Windows 10](https://phoenixnap.com/kb/how-to-install-python-3-windows)

[How install requests module in Python 3 on Windows 10/8/7](https://www.youtube.com/watch?v=HdJywzSCGbc)

[Read and Write files in Python](https://realpython.com/read-write-files-python/)

[Simple Python REST API ](https://github.com/RahulYadav119/PYTHON-REST-API-Without-Framework-/blob/master/final.py)

> Note that for assessment only GET Method is needed, no need for POST, DELETE or PUT, you can ignore this ones

