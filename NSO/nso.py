# https://developer.cisco.com/docs/nso/#!cisco-nso-swagger-api-docs
# POSTMAN: http://localhost:8080/restconf/data/tailf-ncs:devices/device=CRD-D/config/tailf-ned-cisco-ios-xr:banner
# /ncs:devices/device{CRD-D}/config/cisco-ios-xr:banner

import requests
import json

credentials = ("admin", "admin")
numeroInterfaz = 10
url = "http://localhost:8080/restconf/data/tailf-ncs:devices/device=CRD-D/config/tailf-ned-cisco-ios-xr:interface/Loopback"
urlAgregar = f"http://localhost:8080/restconf/data/tailf-ncs:devices/device=CRD-D/config/tailf-ned-cisco-ios-xr:interface/Loopback={numeroInterfaz}"

headers = {"Accept": "application/yang-data+json",  ### DEBE DE SER ESTE SI O SI
           "Content-type": "application/yang-data+json",  ### ESTE DEBE DE IR PARA PODER AGREGAR (PUT) ELEMENTOS
           "Authorization": "Basic YWRtaW46YWRtaW4="}  ### AUTHORIZATION PUEDE SER AQUI EN EL REQUEST AUTH=


### PAYLOAD PARA AGREGAR (PUT) ELEMENTOS ###
payload = """
{
  "tailf-ned-cisco-ios-xr:Loopback": [
    {
      "id": 10,
      "description": "testing NSO6",
      "ipv4": {
        "address": {
          "ip": "10.10.10.10",
          "mask": "255.255.255.255"
        }
      }
    }
  ]
}
"""
r = requests.get(url, headers=headers, verify=False)

for x in r.json()["tailf-ned-cisco-ios-xr:Loopback"]:
    print(x)

r = requests.put(urlAgregar, headers=headers, verify=False, data=payload)
print(urlAgregar)
print(r.status_code)