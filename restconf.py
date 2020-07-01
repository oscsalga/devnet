import requests
import json
from pprint import pprint


username = "developer"
password = "C1sco12345"
urlBase = "https://ios-xe-mgmt-latest.cisco.com"
port = 9443
url = f"{urlBase}:{port}/restconf/data/native"

headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}


r = requests.get(url, auth=(username, password), headers=headers, verify=False)

rJson = r.json()
pprint(rJson)