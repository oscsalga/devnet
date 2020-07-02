import requests
import json

urlBase = "https://swapi.dev/api/"
url = "planets/1"


respuesta = requests.get(f"{urlBase}{url}").json()


name = json.dumps(respuesta, indent=2)

print(respuesta["residents"][3])