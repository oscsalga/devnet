# curl -X GET "https://webexapis.com/v1/rooms"
# -H "Authorization: Bearer "
# -H "Accept: application/json"

import requests
import json

url = "https://webexapis.com/v1/rooms"
clave = ""
token = f"Bearer {clave}"
headers = {"Accept": "application/json",
           "Authorization": token}

r = requests.get(url, headers=headers).json()

# print(r.status_code) # IMPRIME 200 SI ESTÁ BIEN
#p rint(r.ok) # IMPRIME True SI ESTÁ BIEN

for x in range(0, len(r["items"])):
    print(r["items"][x]["title"])

