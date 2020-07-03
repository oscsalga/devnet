import requests
import json


urlToken = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"
headers ={"Content-Type": "application/json",
          "Authorization": "Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE="}

r = requests.post(urlToken, headers=headers)

if r.status_code == 200:
    #print(r.json()["Token"])
    headers["x-auth-token"] = r.json()["Token"]

    r = requests.get(url, headers=headers)
    # imprimirlo bien en json
    print(json.dumps(r.json(), indent=2))