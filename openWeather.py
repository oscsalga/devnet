import requests
import json
import time

urlOpen = "http://api.openweathermap.org/data/2.5/weather?id=3529947&units=metric&APPID=60dc4a5a9cbaec2de2279f548a35b806"




while True:
    respuesta = requests.get(urlOpen).json()

    name = json.dumps(respuesta, indent=2)
    print(respuesta["main"]["temp"])
    time.sleep(2)

