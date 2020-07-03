import requests
import json
import time

clave = ""
urlOpen = f"http://api.openweathermap.org/data/2.5/weather?id=3529947&units=metric&APPID={clave}"

while True:
    respuesta = requests.get(urlOpen).json()

    name = json.dumps(respuesta, indent=2)
    print("Temperatura real: " + str(respuesta["main"]["temp"]))
    print("Feels like:: " + str(respuesta["main"]["feels_like"]) + "\n")
    time.sleep(2)

