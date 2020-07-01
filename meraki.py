import requests
import json

url = "https://dashboard.meraki.com/api/v0/organizations/566327653141842188/networks"


headers = {
  'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0' # DEBEMOS CREAR ESA VARIABLE CON EL API TOKEN
}

response = requests.request("GET", url, headers=headers)

# IMPRIMIMOS LA SALIDA EN FORMATO JSON
print(json.dumps(response.json(), indent=2))

